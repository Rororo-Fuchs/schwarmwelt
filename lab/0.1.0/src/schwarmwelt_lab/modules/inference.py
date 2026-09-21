from __future__ import annotations

import math
from random import Random

from ..core.interfaces import InferenceModule
from ..core.registry import register
from ..core.types import AgentState


def _normalize(values: list[float]) -> list[float]:
    total = sum(values)
    if total <= 1e-15:
        return [1.0 / len(values)] * len(values)
    return [value / total for value in values]


@register("inference", "pair_hmm")
class PairHMMInference(InferenceModule):
    def __init__(self, learning_rate: float = 0.08, stickiness: float = 0.72, pseudocount: float = 1.0, initialization_scale: float = 0.12) -> None:
        self.learning_rate = learning_rate
        self.stickiness = stickiness
        self.pseudocount = pseudocount
        self.initialization_scale = initialization_scale
        self.states = 4
        self.symbols = 5
        self.beliefs: dict[tuple[int, int], list[float]] = {}
        self.emission_counts: dict[int, list[list[float]]] = {}

    def initialize_population(self, agents: list[AgentState], states: int, symbols: int, rng: Random) -> None:
        self.states = states
        self.symbols = symbols
        self.beliefs.clear()
        self.emission_counts = {
            agent.id: [
                [max(0.05, self.pseudocount + rng.gauss(0.0, self.initialization_scale)) for _ in range(symbols)]
                for _ in range(states)
            ]
            for agent in agents
        }
        uniform = [1.0 / states] * states
        for observer in agents:
            for target in agents:
                self.beliefs[(observer.id, target.id)] = uniform.copy()

    def _emission_probability(self, observer_id: int, state: int, symbol: int) -> float:
        row = self.emission_counts[observer_id][state]
        return row[symbol] / sum(row)

    def observe(
        self,
        observer: AgentState,
        target: AgentState,
        symbol: int,
        rng: Random,
        learn: bool = True,
    ) -> tuple[int, list[float]]:
        previous = self.beliefs[(observer.id, target.id)]
        predicted = []
        for state in range(self.states):
            stay = previous[state] * self.stickiness
            move = (sum(previous) - previous[state]) * (1.0 - self.stickiness) / max(1, self.states - 1)
            predicted.append(stay + move)
        posterior = _normalize([
            predicted[state] * self._emission_probability(observer.id, state, symbol)
            for state in range(self.states)
        ])
        self.beliefs[(observer.id, target.id)] = posterior
        if learn:
            for state, responsibility in enumerate(posterior):
                self.emission_counts[observer.id][state][symbol] += self.learning_rate * responsibility
        estimate = max(range(self.states), key=lambda state: posterior[state])
        return estimate, posterior.copy()

    def reset_agent(self, agent: AgentState, agents: list[AgentState], rng: Random) -> None:
        self.emission_counts[agent.id] = [
            [max(0.05, self.pseudocount + rng.gauss(0.0, self.initialization_scale)) for _ in range(self.symbols)]
            for _ in range(self.states)
        ]
        uniform = [1.0 / self.states] * self.states
        for other in agents:
            self.beliefs[(agent.id, other.id)] = uniform.copy()
            self.beliefs[(other.id, agent.id)] = uniform.copy()

    def belief(self, observer_id: int, target_id: int) -> list[float]:
        return self.beliefs[(observer_id, target_id)].copy()
