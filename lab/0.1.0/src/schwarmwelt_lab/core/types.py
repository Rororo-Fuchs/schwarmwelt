from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentState:
    id: int
    zone: int
    x: float
    y: float
    heading: float
    valence_a: float
    valence_b: float
    velocity_a: float
    velocity_b: float
    decoy_a: float
    decoy_b: float
    decoy_velocity_a: float
    decoy_velocity_b: float
    last_symbol: int = -1
    newcomer: bool = False
    age: int = 0
    data: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ObservableContext:
    """Information an Lern-/Gedächtnismodule ohne Ground Truth des Gegenübers."""

    observer_id: int
    target_id: int
    zone: int
    tick: int
    pulse: int
    estimated_state: int
    previous_partner_symbol: int
    previous_own_symbol: int
    observed_partner_symbol: int
    own_valence_delta: float


@dataclass
class PulseRecord:
    tick: int
    pulse: int
    left_id: int
    right_id: int
    left_symbol: int
    right_symbol: int
    left_estimate: int
    right_estimate: int
    left_delta: float
    right_delta: float
    left_true_state: int
    right_true_state: int
    left_decoy_state: int
    right_decoy_state: int
    left_prev_symbol: int
    right_prev_symbol: int


@dataclass
class LearningPulse:
    pulse: int
    own_symbol: int
    partner_symbol: int
    estimated_state: int
    previous_partner_symbol: int


@dataclass
class LearningEpisode:
    pulses: list[LearningPulse]
    intrinsic_return: float


@dataclass
class EpisodeRecord:
    tick: int
    left_id: int
    right_id: int
    zone: int
    pulses: list[PulseRecord]
    left_return: float
    right_return: float


@dataclass
class PublicEvent:
    tick: int
    kind: str
    text: str
    payload: dict[str, Any] = field(default_factory=dict)
