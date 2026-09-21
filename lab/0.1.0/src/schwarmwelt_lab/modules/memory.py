from __future__ import annotations

from collections import defaultdict
from typing import Any

from ..core.interfaces import SocialMemoryModule
from ..core.registry import register
from ..core.types import ObservableContext


@register("memory", "none")
class NoSocialMemory(SocialMemoryModule):
    def initialize(self, zone_count: int, symbols: int, states: int) -> None:
        self.symbols = symbols

    def tick(self, tick: int) -> None:
        return None

    def action_bias(self, zone: int, estimated_state: int, previous_partner_symbol: int) -> list[float]:
        return [0.0] * self.symbols

    def observe(self, context: ObservableContext, chosen_symbol: int) -> None:
        return None

    def summary(self) -> dict[str, Any]:
        return {"type": "none", "entries": 0}


@register("memory", "distributed_trace")
class DistributedTraceMemory(SocialMemoryModule):
    """Experimentelles, verteiltes Sozialgedächtnis ohne Ground Truth.

    Gespeichert werden nur lokal beobachtbare Kontext-Folge-Verknüpfungen:
    private Zustandshypothese, sichtbares Partnersymbol, gewählte Handlung und
    eigene intrinsische Reaktion. Der Speicher ist zonal, vergänglich und
    besitzt keine globale Richtigkeitsinstanz.
    """

    def __init__(
        self,
        decay: float = 0.998,
        write_threshold: float = 0.004,
        read_strength: float = 0.65,
        write_strength: float = 1.0,
        maximum_weight: float = 6.0,
    ) -> None:
        self.decay = decay
        self.write_threshold = write_threshold
        self.read_strength = read_strength
        self.write_strength = write_strength
        self.maximum_weight = maximum_weight
        self.symbols = 5
        self.traces: dict[tuple[int, int, int], list[float]] = {}
        self.last_tick = 0

    def initialize(self, zone_count: int, symbols: int, states: int) -> None:
        self.zone_count = zone_count
        self.symbols = symbols
        self.states = states
        self.traces.clear()
        self.last_tick = 0

    def tick(self, tick: int) -> None:
        if tick <= self.last_tick:
            return
        steps = tick - self.last_tick
        factor = self.decay ** steps
        delete: list[tuple[int, int, int]] = []
        for key, values in self.traces.items():
            for index in range(len(values)):
                values[index] *= factor
            if max(abs(value) for value in values) < 1e-4:
                delete.append(key)
        for key in delete:
            del self.traces[key]
        self.last_tick = tick

    def action_bias(self, zone: int, estimated_state: int, previous_partner_symbol: int) -> list[float]:
        values = self.traces.get((zone, estimated_state, previous_partner_symbol))
        if values is None:
            return [0.0] * self.symbols
        return [self.read_strength * value for value in values]

    def observe(self, context: ObservableContext, chosen_symbol: int) -> None:
        if abs(context.own_valence_delta) < self.write_threshold:
            return
        key = (context.zone, context.estimated_state, context.previous_partner_symbol)
        values = self.traces.setdefault(key, [0.0] * self.symbols)
        sign = 1.0 if context.own_valence_delta > 0 else -1.0
        magnitude = min(1.0, abs(context.own_valence_delta) / max(self.write_threshold, 1e-9))
        values[chosen_symbol] = max(
            -self.maximum_weight,
            min(self.maximum_weight, values[chosen_symbol] + sign * magnitude * self.write_strength),
        )

    def summary(self) -> dict[str, Any]:
        total_strength = sum(sum(abs(value) for value in values) for values in self.traces.values())
        return {
            "type": "distributed_trace",
            "entries": len(self.traces),
            "strength": round(total_strength, 4),
        }
