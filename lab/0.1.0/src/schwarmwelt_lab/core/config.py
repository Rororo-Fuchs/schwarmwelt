from __future__ import annotations

from dataclasses import dataclass, field
import json
from pathlib import Path
from typing import Any


@dataclass
class SimulationConfig:
    title: str = "Schwarmwelt"
    description: str = ""
    seed: int = 1
    agents: int = 48
    zones: int = 4
    symbols: int = 5
    states: int = 4
    pulses: int = 8
    permeability: float = 0.005
    turnover_interval: int = 1200
    turnover_fraction: float = 0.125
    recent_event_limit: int = 120
    modules: dict[str, dict[str, Any]] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "SimulationConfig":
        known = {
            key: raw[key]
            for key in cls.__dataclass_fields__
            if key in raw
        }
        return cls(**known)

    @classmethod
    def load(cls, path: str | Path) -> "SimulationConfig":
        with Path(path).open("r", encoding="utf-8") as handle:
            config = cls.from_dict(json.load(handle))
        config.validate()
        return config

    def validate(self) -> None:
        if self.agents < 2:
            raise ValueError("agents muss mindestens 2 sein")
        if self.zones < 1:
            raise ValueError("zones muss mindestens 1 sein")
        if self.symbols < 2:
            raise ValueError("symbols muss mindestens 2 sein")
        if self.states < 2:
            raise ValueError("states muss mindestens 2 sein")
        if self.pulses < 1:
            raise ValueError("pulses muss mindestens 1 sein")
        if not 0.0 <= self.permeability <= 1.0:
            raise ValueError("permeability muss zwischen 0 und 1 liegen")
        if not 0.0 <= self.turnover_fraction <= 1.0:
            raise ValueError("turnover_fraction muss zwischen 0 und 1 liegen")
        for kind, spec in self.modules.items():
            if not isinstance(spec, dict) or not isinstance(spec.get("name"), str):
                raise ValueError(f"Ungültige Modulspezifikation für {kind}")
            if "params" in spec and not isinstance(spec["params"], dict):
                raise ValueError(f"params für {kind} muss ein Objekt sein")

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "seed": self.seed,
            "agents": self.agents,
            "zones": self.zones,
            "symbols": self.symbols,
            "states": self.states,
            "pulses": self.pulses,
            "permeability": self.permeability,
            "turnover_interval": self.turnover_interval,
            "turnover_fraction": self.turnover_fraction,
            "recent_event_limit": self.recent_event_limit,
            "modules": self.modules,
            "metadata": self.metadata,
        }
