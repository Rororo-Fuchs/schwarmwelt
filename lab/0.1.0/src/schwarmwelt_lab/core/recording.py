from __future__ import annotations

import gzip
import json
from pathlib import Path
from typing import Any


class SnapshotRecorder:
    def __init__(self, config: dict[str, Any], interval: int = 1) -> None:
        self.config = config
        self.interval = max(1, interval)
        self.snapshots: list[dict[str, Any]] = []

    def capture(self, snapshot: dict[str, Any]) -> None:
        if snapshot["tick"] % self.interval == 0:
            self.snapshots.append(snapshot)

    def save(self, path: str | Path) -> None:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        with gzip.open(target, "wt", encoding="utf-8") as handle:
            handle.write(json.dumps({"type": "header", "config": self.config}, ensure_ascii=False) + "\n")
            for snapshot in self.snapshots:
                handle.write(json.dumps({"type": "snapshot", "data": snapshot}, ensure_ascii=False) + "\n")


class Replay:
    def __init__(self, config: dict[str, Any], snapshots: list[dict[str, Any]]) -> None:
        self.config = config
        self.snapshots = snapshots
        self.index = 0

    @classmethod
    def load(cls, path: str | Path) -> "Replay":
        config: dict[str, Any] = {}
        snapshots: list[dict[str, Any]] = []
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            for line in handle:
                item = json.loads(line)
                if item.get("type") == "header":
                    config = item.get("config", {})
                elif item.get("type") == "snapshot":
                    snapshots.append(item["data"])
        if not snapshots:
            raise ValueError("Die Aufzeichnung enthält keine Snapshots.")
        return cls(config, snapshots)

    def step(self, count: int = 1) -> dict[str, Any]:
        self.index = min(len(self.snapshots) - 1, self.index + max(0, count))
        return self.current()

    def current(self) -> dict[str, Any]:
        return self.snapshots[self.index]

    def reset(self) -> dict[str, Any]:
        self.index = 0
        return self.current()
