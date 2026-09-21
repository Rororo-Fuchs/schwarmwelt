from __future__ import annotations

import math
from random import Random

from ..core.interfaces import ValenceModule
from ..core.registry import register
from ..core.types import AgentState


def _reflect(value: float, lower: float, upper: float) -> float:
    span = upper - lower
    shifted = (value - lower) % (2.0 * span)
    if shifted > span:
        shifted = 2.0 * span - shifted
    return lower + shifted


@register("valence", "intrinsic_2d")
class IntrinsicValence2D(ValenceModule):
    def __init__(
        self,
        endogenous_noise_a: float = 0.003,
        endogenous_noise_b: float = 0.002,
        inertia: float = 0.985,
        social_scale: float = 0.035,
        attraction_ratio: float = 0.9,
        boundary_start: float = 0.8,
    ) -> None:
        self.noise_a = endogenous_noise_a
        self.noise_b = endogenous_noise_b
        self.inertia = inertia
        self.social_scale = social_scale
        self.attraction_ratio = attraction_ratio
        self.boundary_start = boundary_start
        self.centers = ((0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75))

    def initialize(self, agent: AgentState, rng: Random) -> None:
        agent.valence_a = rng.uniform(-0.65, 0.65)
        agent.valence_b = rng.uniform(0.15, 0.85)
        agent.velocity_a = rng.gauss(0.0, 0.008)
        agent.velocity_b = rng.gauss(0.0, 0.005)
        agent.decoy_a = rng.uniform(-0.65, 0.65)
        agent.decoy_b = rng.uniform(0.15, 0.85)
        agent.decoy_velocity_a = rng.gauss(0.0, 0.008)
        agent.decoy_velocity_b = rng.gauss(0.0, 0.005)
        agent.data["valence_baseline"] = 0.5

    def _boundary_push(self, value: float, velocity: float, lo: float, hi: float) -> float:
        width = (hi - lo) * (1.0 - self.boundary_start) / 2.0
        if value < lo + width:
            velocity += 0.002 * ((lo + width) - value) / max(width, 1e-9)
        elif value > hi - width:
            velocity -= 0.002 * (value - (hi - width)) / max(width, 1e-9)
        return velocity

    def endogenous_step(self, agent: AgentState, rng: Random) -> None:
        agent.velocity_a = self.inertia * agent.velocity_a + rng.gauss(0.0, self.noise_a)
        agent.velocity_b = self.inertia * agent.velocity_b + rng.gauss(0.0, self.noise_b)
        agent.velocity_a = self._boundary_push(agent.valence_a, agent.velocity_a, -1.0, 1.0)
        agent.velocity_b = self._boundary_push(agent.valence_b, agent.velocity_b, 0.0, 1.0)
        agent.valence_a = _reflect(agent.valence_a + agent.velocity_a, -1.0, 1.0)
        agent.valence_b = _reflect(agent.valence_b + agent.velocity_b, 0.0, 1.0)

        agent.decoy_velocity_a = self.inertia * agent.decoy_velocity_a + rng.gauss(0.0, self.noise_a)
        agent.decoy_velocity_b = self.inertia * agent.decoy_velocity_b + rng.gauss(0.0, self.noise_b)
        agent.decoy_a = _reflect(agent.decoy_a + agent.decoy_velocity_a, -1.0, 1.0)
        agent.decoy_b = _reflect(agent.decoy_b + agent.decoy_velocity_b, 0.0, 1.0)
        agent.age += 1

    def state_bin(self, agent: AgentState) -> int:
        return (2 if agent.valence_a >= 0.0 else 0) + (1 if agent.valence_b >= 0.5 else 0)

    def decoy_state_bin(self, agent: AgentState) -> int:
        return (2 if agent.decoy_a >= 0.0 else 0) + (1 if agent.decoy_b >= 0.5 else 0)

    def social_response(self, agent: AgentState, estimated_state: int) -> float:
        estimated_state = max(0, min(3, estimated_state))
        own_x = (agent.valence_a + 1.0) / 2.0
        own_y = agent.valence_b
        center_x, center_y = self.centers[estimated_state]
        distance = math.dist((own_x, own_y), (center_x, center_y)) / math.sqrt(2.0)
        fit = self.attraction_ratio * (1.0 - distance) + (1.0 - self.attraction_ratio) * distance
        baseline = float(agent.data.get("valence_baseline", 0.5))
        relative = fit - baseline
        delta = self.social_scale * math.tanh(4.0 * relative)
        agent.data["valence_baseline"] = 0.997 * baseline + 0.003 * fit
        agent.valence_a = _reflect(agent.valence_a + delta, -1.0, 1.0)
        agent.valence_b = _reflect(
            agent.valence_b + 0.002 * abs(delta) / max(self.social_scale, 1e-9),
            0.0,
            1.0,
        )
        return delta
