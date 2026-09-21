from __future__ import annotations

import math
from random import Random

from ..core.interfaces import EmissionModule
from ..core.registry import register
from ..core.types import AgentState


def _sample_softmax(logits: list[float], rng: Random) -> int:
    maximum = max(logits)
    weights = [math.exp(value - maximum) for value in logits]
    total = sum(weights)
    draw = rng.random() * total
    acc = 0.0
    for index, weight in enumerate(weights):
        acc += weight
        if draw <= acc:
            return index
    return len(weights) - 1


@register("emission", "random_state_asymmetry")
class RandomStateAsymmetry(EmissionModule):
    def __init__(self, scale: float = 0.8, state_expression: bool = True) -> None:
        self.scale = scale
        self.state_expression = state_expression

    def initialize(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None:
        agent.data["emission_logits"] = [
            [rng.gauss(0.0, self.scale) for _ in range(symbols)]
            for _ in range(states)
        ]

    def emit(self, agent: AgentState, true_state: int, rng: Random, symbols: int) -> int:
        logits = agent.data["emission_logits"]
        if self.state_expression:
            row = logits[true_state]
        else:
            row = [sum(logits[state][symbol] for state in range(len(logits))) / len(logits) for symbol in range(symbols)]
        return _sample_softmax(row, rng)

    def reset(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None:
        self.initialize(agent, rng, states, symbols)
