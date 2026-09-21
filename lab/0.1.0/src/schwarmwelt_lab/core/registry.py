from __future__ import annotations

from collections.abc import Callable
from typing import Any

_REGISTRY: dict[str, dict[str, type]] = {
    "valence": {},
    "geography": {},
    "emission": {},
    "inference": {},
    "practice": {},
    "memory": {},
}


def register(kind: str, name: str) -> Callable[[type], type]:
    if kind not in _REGISTRY:
        raise KeyError(f"Unbekannter Modultyp: {kind}")

    def decorator(cls: type) -> type:
        if name in _REGISTRY[kind]:
            raise KeyError(f"Modul doppelt registriert: {kind}/{name}")
        _REGISTRY[kind][name] = cls
        return cls

    return decorator


def build(kind: str, spec: dict[str, Any]) -> Any:
    name = spec.get("name")
    params = spec.get("params", {})
    try:
        cls = _REGISTRY[kind][name]
    except KeyError as exc:
        known = ", ".join(sorted(_REGISTRY.get(kind, {}))) or "keine"
        raise ValueError(f"Unbekanntes Modul {kind}/{name}; bekannt: {known}") from exc
    return cls(**params)


def registered() -> dict[str, list[str]]:
    return {kind: sorted(items) for kind, items in _REGISTRY.items()}
