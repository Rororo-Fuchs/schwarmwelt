from __future__ import annotations

import math
from random import Random

from ..core.interfaces import GeographyModule
from ..core.registry import register
from ..core.types import AgentState


@register("geography", "porous_zones")
class PorousZones(GeographyModule):
    def __init__(self, permeability: float = 0.005, base_speed: float = 0.012, turn_noise: float = 0.35) -> None:
        self.permeability = permeability
        self.base_speed = base_speed
        self.turn_noise = turn_noise

    def initialize(self, agent: AgentState, rng: Random, zone_count: int) -> None:
        agent.x = rng.random()
        agent.y = rng.random()
        agent.heading = rng.random() * math.tau

    def move(self, agent: AgentState, rng: Random, zone_count: int) -> None:
        # Valenz beeinflusst Bewegungsart, nie Zielrichtung.
        persistence = 0.2 + 0.7 * max(0.0, min(1.0, (agent.valence_a + 1.0) / 2.0))
        agent.heading += rng.gauss(0.0, self.turn_noise * (1.1 - persistence))
        speed = self.base_speed * (0.55 + agent.valence_b)
        nx = agent.x + math.cos(agent.heading) * speed
        ny = agent.y + math.sin(agent.heading) * speed

        crossed_x = nx < 0.0 or nx >= 1.0
        crossed_y = ny < 0.0 or ny >= 1.0
        if not crossed_x and not crossed_y:
            agent.x, agent.y = nx, ny
            return

        if rng.random() < self.permeability:
            row = agent.zone // 2
            col = agent.zone % 2
            if crossed_x:
                col = 1 - col
                nx %= 1.0
            if crossed_y:
                row = 1 - row
                ny %= 1.0
            agent.zone = (row * 2 + col) % max(zone_count, 1)
            agent.x, agent.y = nx % 1.0, ny % 1.0
        else:
            if crossed_x:
                agent.heading = math.pi - agent.heading
                nx = min(0.999, max(0.001, agent.x - math.cos(agent.heading) * speed))
            if crossed_y:
                agent.heading = -agent.heading
                ny = min(0.999, max(0.001, agent.y - math.sin(agent.heading) * speed))
            agent.x, agent.y = nx, ny
