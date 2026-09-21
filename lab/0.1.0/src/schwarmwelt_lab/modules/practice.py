from __future__ import annotations

import math
from random import Random

from ..core.interfaces import PracticeModule
from ..core.registry import register
from ..core.types import AgentState, LearningEpisode


def _softmax(logits: list[float]) -> list[float]:
    maximum = max(logits)
    weights = [math.exp(value - maximum) for value in logits]
    total = sum(weights)
    return [weight / total for weight in weights]


def _sample(probabilities: list[float], rng: Random) -> int:
    draw = rng.random()
    acc = 0.0
    for index, probability in enumerate(probabilities):
        acc += probability
        if draw <= acc:
            return index
    return len(probabilities) - 1


@register("practice", "compact_ritual")
class CompactRitualPractice(PracticeModule):
    def __init__(
        self,
        learning_rate: float = 0.4,
        policy_scale: float = 0.05,
        imitation_strength: float = 1.0,
        use_estimate: bool = True,
        use_previous_symbol: bool = True,
    ) -> None:
        self.learning_rate = learning_rate
        self.policy_scale = policy_scale
        self.imitation_strength = imitation_strength
        self.use_estimate = use_estimate
        self.use_previous_symbol = use_previous_symbol
        self.states = 4
        self.symbols = 5

    def initialize(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None:
        self.states = states
        self.symbols = symbols
        agent.data["ritual_logits"] = {
            (state, previous): [rng.gauss(0.0, self.policy_scale) for _ in range(symbols)]
            for state in range(states + 1)
            for previous in range(symbols + 1)
        }
        agent.data["episode_baseline"] = 0.0

    def choose(
        self,
        agent: AgentState,
        estimated_state: int,
        previous_partner_symbol: int,
        memory_bias: list[float],
        rng: Random,
        symbols: int,
    ) -> int:
        state_key = estimated_state if self.use_estimate else self.states
        previous_key = previous_partner_symbol if self.use_previous_symbol else self.symbols
        logits = agent.data["ritual_logits"][(state_key, previous_key)]
        combined = [logits[index] + memory_bias[index] for index in range(symbols)]
        return _sample(_softmax(combined), rng)

    def learn_episode(
        self,
        agent: AgentState,
        episode: LearningEpisode,
        rng: Random,
        symbols: int,
    ) -> None:
        own_return = episode.intrinsic_return
        baseline = float(agent.data.get("episode_baseline", 0.0))
        advantage = max(-1.0, min(1.0, own_return - baseline))
        agent.data["episode_baseline"] = 0.995 * baseline + 0.005 * own_return
        logits_map = agent.data["ritual_logits"]
        for pulse_index, pulse in enumerate(episode.pulses, start=1):
            estimate = pulse.estimated_state
            previous_partner = pulse.previous_partner_symbol
            own_action = pulse.own_symbol
            partner_action = pulse.partner_symbol
            state_key = estimate if self.use_estimate else self.states
            previous_key = previous_partner if self.use_previous_symbol else self.symbols
            logits = logits_map[(state_key, previous_key)]
            probabilities = _softmax(logits)
            discount = 0.9 ** (len(episode.pulses) - 1 - pulse_index)
            rate = self.learning_rate * advantage * discount * (0.25 + 0.75 * agent.valence_b)
            for symbol in range(symbols):
                own_target = 1.0 if symbol == own_action else 0.0
                partner_target = 1.0 if symbol == partner_action else 0.0
                target = (1.0 - self.imitation_strength) * own_target + self.imitation_strength * partner_target
                logits[symbol] += rate * (target - probabilities[symbol])

    def reset(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None:
        self.initialize(agent, rng, states, symbols)
