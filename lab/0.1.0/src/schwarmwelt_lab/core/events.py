from __future__ import annotations

from collections import deque
from typing import Iterable

from .types import PublicEvent


class EventBuffer:
    def __init__(self, limit: int = 120) -> None:
        self._events: deque[PublicEvent] = deque(maxlen=limit)

    def append(self, event: PublicEvent) -> None:
        self._events.append(event)

    def recent(self, limit: int | None = None) -> list[PublicEvent]:
        events = list(self._events)
        return events if limit is None else events[-limit:]

    def clear(self) -> None:
        self._events.clear()

    def __iter__(self) -> Iterable[PublicEvent]:
        return iter(self._events)
