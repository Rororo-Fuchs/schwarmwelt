from __future__ import annotations

from abc import ABC, abstractmethod
from random import Random
from typing import Any

from .types import AgentState, LearningEpisode, ObservableContext


class ValenceModule(ABC):
    @abstractmethod
    def initialize(self, agent: AgentState, rng: Random) -> None: ...

    @abstractmethod
    def endogenous_step(self, agent: AgentState, rng: Random) -> None: ...

    @abstractmethod
    def state_bin(self, agent: AgentState) -> int: ...

    @abstractmethod
    def decoy_state_bin(self, agent: AgentState) -> int: ...

    @abstractmethod
    def social_response(self, agent: AgentState, estimated_state: int) -> float: ...


class GeographyModule(ABC):
    @abstractmethod
    def initialize(self, agent: AgentState, rng: Random, zone_count: int) -> None: ...

    @abstractmethod
    def move(self, agent: AgentState, rng: Random, zone_count: int) -> None: ...


class EmissionModule(ABC):
    @abstractmethod
    def initialize(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None: ...

    @abstractmethod
    def emit(self, agent: AgentState, true_state: int, rng: Random, symbols: int) -> int: ...

    @abstractmethod
    def reset(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None: ...


class InferenceModule(ABC):
    @abstractmethod
    def initialize_population(self, agents: list[AgentState], states: int, symbols: int, rng: Random) -> None: ...

    @abstractmethod
    def observe(
        self,
        observer: AgentState,
        target: AgentState,
        symbol: int,
        rng: Random,
        learn: bool = True,
    ) -> tuple[int, list[float]]: ...

    @abstractmethod
    def reset_agent(self, agent: AgentState, agents: list[AgentState], rng: Random) -> None: ...

    @abstractmethod
    def belief(self, observer_id: int, target_id: int) -> list[float]: ...


class PracticeModule(ABC):
    @abstractmethod
    def initialize(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None: ...

    @abstractmethod
    def choose(
        self,
        agent: AgentState,
        estimated_state: int,
        previous_partner_symbol: int,
        memory_bias: list[float],
        rng: Random,
        symbols: int,
    ) -> int: ...

    @abstractmethod
    def learn_episode(
        self,
        agent: AgentState,
        episode: LearningEpisode,
        rng: Random,
        symbols: int,
    ) -> None: ...

    @abstractmethod
    def reset(self, agent: AgentState, rng: Random, states: int, symbols: int) -> None: ...


class SocialMemoryModule(ABC):
    """Erhält ausschließlich ObservableContext bzw. sichtbare Episodenbestandteile."""

    @abstractmethod
    def initialize(self, zone_count: int, symbols: int, states: int) -> None: ...

    @abstractmethod
    def tick(self, tick: int) -> None: ...

    @abstractmethod
    def action_bias(self, zone: int, estimated_state: int, previous_partner_symbol: int) -> list[float]: ...

    @abstractmethod
    def observe(self, context: ObservableContext, chosen_symbol: int) -> None: ...

    @abstractmethod
    def summary(self) -> dict[str, Any]: ...
