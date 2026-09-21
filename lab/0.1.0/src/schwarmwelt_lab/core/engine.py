from __future__ import annotations

from collections import Counter, deque
from dataclasses import asdict
import hashlib
import json
import math
from random import Random
from typing import Any

from .config import SimulationConfig
from .events import EventBuffer
from .registry import build
from .types import (
    AgentState,
    EpisodeRecord,
    LearningEpisode,
    LearningPulse,
    ObservableContext,
    PublicEvent,
    PulseRecord,
)
from .. import modules as _registered_modules  # noqa: F401


SYMBOL_GLYPHS = ("△", "○", "⬡", "◇", "✦", "□", "▽", "✧", "⬢", "◌")


class SimulationEngine:
    """Schrittweiser, deterministischer Simulationskern ohne UI-Abhängigkeit."""

    def __init__(self, config: SimulationConfig) -> None:
        self.config = config
        self.rng = Random(config.seed)
        self.tick = 0
        self.events = EventBuffer(config.recent_event_limit)
        self.recent_pulses: deque[PulseRecord] = deque(maxlen=48)
        self.recent_episodes: deque[EpisodeRecord] = deque(maxlen=300)
        self.total_encounters = 0
        self.total_turnovers = 0
        self._build_modules()
        self.agents = self._initialize_agents()
        self.inference.initialize_population(self.agents, config.states, config.symbols, self.rng)
        self.memory.initialize(config.zones, config.symbols, config.states)
        self.events.append(PublicEvent(0, "reset", f"Lauf gestartet: {config.title}"))

    def _build_modules(self) -> None:
        defaults: dict[str, dict[str, Any]] = {
            "valence": {"name": "intrinsic_2d", "params": {}},
            "geography": {
                "name": "porous_zones",
                "params": {"permeability": self.config.permeability},
            },
            "emission": {"name": "random_state_asymmetry", "params": {}},
            "inference": {"name": "pair_hmm", "params": {}},
            "practice": {"name": "compact_ritual", "params": {}},
            "memory": {"name": "none", "params": {}},
        }
        specs = {**defaults, **self.config.modules}
        self.valence = build("valence", specs["valence"])
        self.geography = build("geography", specs["geography"])
        self.emission = build("emission", specs["emission"])
        self.inference = build("inference", specs["inference"])
        self.practice = build("practice", specs["practice"])
        self.memory = build("memory", specs["memory"])

    def _initialize_agents(self) -> list[AgentState]:
        agents: list[AgentState] = []
        for agent_id in range(self.config.agents):
            agent = AgentState(
                id=agent_id,
                zone=agent_id % self.config.zones,
                x=0.5,
                y=0.5,
                heading=0.0,
                valence_a=0.0,
                valence_b=0.5,
                velocity_a=0.0,
                velocity_b=0.0,
                decoy_a=0.0,
                decoy_b=0.5,
                decoy_velocity_a=0.0,
                decoy_velocity_b=0.0,
            )
            self.valence.initialize(agent, self.rng)
            self.geography.initialize(agent, self.rng, self.config.zones)
            self.emission.initialize(agent, self.rng, self.config.states, self.config.symbols)
            self.practice.initialize(agent, self.rng, self.config.states, self.config.symbols)
            agents.append(agent)
        self.rng.shuffle(agents)
        agents.sort(key=lambda agent: agent.id)
        return agents

    def reset(self, seed: int | None = None) -> None:
        if seed is not None:
            self.config.seed = seed
        self.__init__(self.config)

    def step(self, count: int = 1) -> None:
        for _ in range(max(0, count)):
            self._step_once()

    def _step_once(self) -> None:
        self.tick += 1
        self.memory.tick(self.tick)
        for agent in self.agents:
            self.valence.endogenous_step(agent, self.rng)
            self.geography.move(agent, self.rng, self.config.zones)

        zone_members: dict[int, list[AgentState]] = {zone: [] for zone in range(self.config.zones)}
        for agent in self.agents:
            zone_members[agent.zone].append(agent)
        for members in zone_members.values():
            self.rng.shuffle(members)
            for index in range(0, len(members) - 1, 2):
                self._run_encounter(members[index], members[index + 1])

        if self.config.turnover_interval > 0 and self.tick % self.config.turnover_interval == 0:
            self._turnover()

    def _run_encounter(self, left: AgentState, right: AgentState) -> None:
        pulses: list[PulseRecord] = []
        left_learning: list[LearningPulse] = []
        right_learning: list[LearningPulse] = []
        start_token = self.config.symbols
        previous_left = start_token
        previous_right = start_token
        frozen_left_estimate = self.config.states
        frozen_right_estimate = self.config.states
        left_return = 0.0
        right_return = 0.0

        for pulse_index in range(self.config.pulses):
            left_true = self.valence.state_bin(left)
            right_true = self.valence.state_bin(right)
            left_decoy = self.valence.decoy_state_bin(left)
            right_decoy = self.valence.decoy_state_bin(right)

            if pulse_index == 0:
                left_symbol = self.emission.emit(left, left_true, self.rng, self.config.symbols)
                right_symbol = self.emission.emit(right, right_true, self.rng, self.config.symbols)
            else:
                left_bias = self.memory.action_bias(left.zone, frozen_left_estimate, previous_right)
                right_bias = self.memory.action_bias(right.zone, frozen_right_estimate, previous_left)
                left_symbol = self.practice.choose(
                    left,
                    frozen_left_estimate,
                    previous_right,
                    left_bias,
                    self.rng,
                    self.config.symbols,
                )
                right_symbol = self.practice.choose(
                    right,
                    frozen_right_estimate,
                    previous_left,
                    right_bias,
                    self.rng,
                    self.config.symbols,
                )

            current_left_estimate, _ = self.inference.observe(left, right, right_symbol, self.rng, learn=True)
            current_right_estimate, _ = self.inference.observe(right, left, left_symbol, self.rng, learn=True)
            if pulse_index == 0:
                frozen_left_estimate = current_left_estimate
                frozen_right_estimate = current_right_estimate

            left_delta = self.valence.social_response(left, current_left_estimate)
            right_delta = self.valence.social_response(right, current_right_estimate)
            left_return += left_delta
            right_return += right_delta
            left.last_symbol = left_symbol
            right.last_symbol = right_symbol

            record = PulseRecord(
                tick=self.tick,
                pulse=pulse_index,
                left_id=left.id,
                right_id=right.id,
                left_symbol=left_symbol,
                right_symbol=right_symbol,
                left_estimate=frozen_left_estimate,
                right_estimate=frozen_right_estimate,
                left_delta=left_delta,
                right_delta=right_delta,
                left_true_state=left_true,
                right_true_state=right_true,
                left_decoy_state=left_decoy,
                right_decoy_state=right_decoy,
                left_prev_symbol=previous_left,
                right_prev_symbol=previous_right,
            )
            pulses.append(record)
            self.recent_pulses.append(record)

            if pulse_index > 0:
                left_learning.append(
                    LearningPulse(
                        pulse=pulse_index,
                        own_symbol=left_symbol,
                        partner_symbol=right_symbol,
                        estimated_state=frozen_left_estimate,
                        previous_partner_symbol=previous_right,
                    )
                )
                right_learning.append(
                    LearningPulse(
                        pulse=pulse_index,
                        own_symbol=right_symbol,
                        partner_symbol=left_symbol,
                        estimated_state=frozen_right_estimate,
                        previous_partner_symbol=previous_left,
                    )
                )

                self.memory.observe(
                    ObservableContext(
                        observer_id=left.id,
                        target_id=right.id,
                        zone=left.zone,
                        tick=self.tick,
                        pulse=pulse_index,
                        estimated_state=frozen_left_estimate,
                        previous_partner_symbol=previous_right,
                        previous_own_symbol=previous_left,
                        observed_partner_symbol=right_symbol,
                        own_valence_delta=left_delta,
                    ),
                    left_symbol,
                )
                self.memory.observe(
                    ObservableContext(
                        observer_id=right.id,
                        target_id=left.id,
                        zone=right.zone,
                        tick=self.tick,
                        pulse=pulse_index,
                        estimated_state=frozen_right_estimate,
                        previous_partner_symbol=previous_left,
                        previous_own_symbol=previous_right,
                        observed_partner_symbol=left_symbol,
                        own_valence_delta=right_delta,
                    ),
                    right_symbol,
                )

            previous_left = left_symbol
            previous_right = right_symbol

        scale = max(1, self.config.pulses)
        episode = EpisodeRecord(
            tick=self.tick,
            left_id=left.id,
            right_id=right.id,
            zone=left.zone,
            pulses=pulses,
            left_return=left_return / scale,
            right_return=right_return / scale,
        )
        self.practice.learn_episode(
            left,
            LearningEpisode(left_learning, episode.left_return),
            self.rng,
            self.config.symbols,
        )
        self.practice.learn_episode(
            right,
            LearningEpisode(right_learning, episode.right_return),
            self.rng,
            self.config.symbols,
        )
        self.recent_episodes.append(episode)
        self.total_encounters += 1
        sequence = " ".join(self.symbol_glyph(p.left_symbol) + self.symbol_glyph(p.right_symbol) for p in pulses)
        self.events.append(
            PublicEvent(
                self.tick,
                "encounter",
                f"A{left.id} ↔ A{right.id}: {sequence}",
                {"left": left.id, "right": right.id, "zone": left.zone},
            )
        )

    def _turnover(self) -> None:
        count = max(1, round(self.config.agents * self.config.turnover_fraction))
        replaced = self.rng.sample(self.agents, count)
        for agent in replaced:
            agent.newcomer = True
            agent.age = 0
            self.valence.initialize(agent, self.rng)
            self.geography.initialize(agent, self.rng, self.config.zones)
            self.emission.reset(agent, self.rng, self.config.states, self.config.symbols)
            self.practice.reset(agent, self.rng, self.config.states, self.config.symbols)
            self.inference.reset_agent(agent, self.agents, self.rng)
        self.total_turnovers += 1
        ids = ", ".join(str(agent.id) for agent in replaced)
        self.events.append(PublicEvent(self.tick, "turnover", f"Turnover: neue Agenten {ids}"))

    def symbol_glyph(self, symbol: int) -> str:
        if symbol < 0:
            return "·"
        return SYMBOL_GLYPHS[symbol % len(SYMBOL_GLYPHS)]

    def _visible_sequence_counts(self) -> dict[str, int]:
        counter: Counter[str] = Counter()
        for episode in self.recent_episodes:
            left_sequence = "".join(self.symbol_glyph(p.left_symbol) for p in episode.pulses)
            right_sequence = "".join(self.symbol_glyph(p.right_symbol) for p in episode.pulses)
            counter[f"Z{episode.zone + 1}:{left_sequence}"] += 1
            counter[f"Z{episode.zone + 1}:{right_sequence}"] += 1
        return dict(counter.most_common(8))

    def metrics(self) -> dict[str, Any]:
        mean_a = sum(agent.valence_a for agent in self.agents) / len(self.agents)
        mean_b = sum(agent.valence_b for agent in self.agents) / len(self.agents)
        return {
            "tick": self.tick,
            "encounters": self.total_encounters,
            "turnovers": self.total_turnovers,
            "mean_valence_a": round(mean_a, 4),
            "mean_valence_b": round(mean_b, 4),
            "memory": self.memory.summary(),
            "frequent_sequences": self._visible_sequence_counts(),
        }

    def snapshot(self, diagnostic: bool = False) -> dict[str, Any]:
        agents: list[dict[str, Any]] = []
        for agent in self.agents:
            item: dict[str, Any] = {
                "id": agent.id,
                "zone": agent.zone,
                "x": round(agent.x, 6),
                "y": round(agent.y, 6),
                "last_symbol": agent.last_symbol,
                "newcomer": agent.newcomer,
                "age": agent.age,
            }
            if diagnostic:
                item.update(
                    {
                        "valence_a": round(agent.valence_a, 6),
                        "valence_b": round(agent.valence_b, 6),
                        "true_state": self.valence.state_bin(agent),
                        "decoy_state": self.valence.decoy_state_bin(agent),
                    }
                )
            agents.append(item)

        latest_pairs: dict[tuple[int, int], PulseRecord] = {}
        for pulse in self.recent_pulses:
            if pulse.tick == self.tick:
                latest_pairs[(min(pulse.left_id, pulse.right_id), max(pulse.left_id, pulse.right_id))] = pulse
        visible_pulses = list(latest_pairs.values())[-14:]
        pulses = [
            {
                "tick": pulse.tick,
                "pulse": pulse.pulse,
                "left": pulse.left_id,
                "right": pulse.right_id,
                "left_symbol": pulse.left_symbol,
                "right_symbol": pulse.right_symbol,
                "left_estimate": pulse.left_estimate if diagnostic else None,
                "right_estimate": pulse.right_estimate if diagnostic else None,
            }
            for pulse in visible_pulses
        ]
        return {
            "tick": self.tick,
            "title": self.config.title,
            "diagnostic": diagnostic,
            "agents": agents,
            "recent_pulses": pulses,
            "events": [asdict(event) for event in self.events.recent(30)],
            "metrics": self.metrics(),
            "symbols": [self.symbol_glyph(index) for index in range(self.config.symbols)],
        }

    def agent_details(self, agent_id: int, diagnostic: bool = False) -> dict[str, Any]:
        agent = self.agents[agent_id]
        details: dict[str, Any] = {
            "id": agent.id,
            "zone": agent.zone,
            "position": [round(agent.x, 4), round(agent.y, 4)],
            "last_symbol": self.symbol_glyph(agent.last_symbol),
            "newcomer": agent.newcomer,
            "age": agent.age,
        }
        partners = sorted(
            (
                (other.id, self.inference.belief(agent.id, other.id))
                for other in self.agents
                if other.id != agent.id
            ),
            key=lambda pair: max(pair[1]),
            reverse=True,
        )[:5]
        details["most_decisive_beliefs"] = [
            {"target": target, "belief": [round(value, 3) for value in belief]}
            for target, belief in partners
        ]
        if diagnostic:
            details.update(
                {
                    "valence_a": round(agent.valence_a, 5),
                    "valence_b": round(agent.valence_b, 5),
                    "true_state": self.valence.state_bin(agent),
                    "decoy_state": self.valence.decoy_state_bin(agent),
                }
            )
        return details

    def deterministic_digest(self) -> str:
        payload = {
            "tick": self.tick,
            "agents": [
                (
                    agent.id,
                    agent.zone,
                    round(agent.x, 8),
                    round(agent.y, 8),
                    round(agent.valence_a, 8),
                    round(agent.valence_b, 8),
                    agent.last_symbol,
                )
                for agent in self.agents
            ],
            "metrics": self.metrics(),
        }
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()
