from __future__ import annotations

from pathlib import Path
from typing import Any

from .config import SimulationConfig
from .engine import SimulationEngine
from .recording import Replay, SnapshotRecorder
from .plugins import load_plugin_directory


class LabController:
    def __init__(self, scenario_path: str | Path) -> None:
        self.scenario_path = Path(scenario_path)
        self.project_root = self.scenario_path.resolve().parent.parent
        load_plugin_directory(self.project_root / "plugins")
        self.config = SimulationConfig.load(self.scenario_path)
        self.engine = SimulationEngine(self.config)
        self.replay: Replay | None = None
        self.recorder: SnapshotRecorder | None = None
        self.diagnostic = False

    @property
    def is_replay(self) -> bool:
        return self.replay is not None

    def load_scenario(self, scenario_path: str | Path, seed: int | None = None) -> None:
        self.scenario_path = Path(scenario_path)
        self.project_root = self.scenario_path.resolve().parent.parent
        load_plugin_directory(self.project_root / "plugins")
        self.config = SimulationConfig.load(self.scenario_path)
        if seed is not None:
            self.config.seed = seed
        self.engine = SimulationEngine(self.config)
        self.replay = None
        self.recorder = None

    def reset(self, seed: int | None = None) -> None:
        if self.replay is not None:
            self.replay.reset()
            return
        if seed is not None:
            self.config.seed = seed
        self.engine = SimulationEngine(self.config)
        self.recorder = None

    def step(self, count: int = 1) -> dict[str, Any]:
        if self.replay is not None:
            return self.replay.step(count)
        self.engine.step(count)
        snapshot = self.engine.snapshot(self.diagnostic)
        if self.recorder is not None:
            self.recorder.capture(snapshot)
        return snapshot

    def snapshot(self) -> dict[str, Any]:
        if self.replay is not None:
            return self.replay.current()
        return self.engine.snapshot(self.diagnostic)

    def toggle_recording(self, enabled: bool, interval: int = 1) -> None:
        if enabled:
            self.recorder = SnapshotRecorder(self.config.to_dict(), interval)
            self.recorder.capture(self.snapshot())
        else:
            self.recorder = None

    def save_recording(self, path: str | Path) -> None:
        if self.recorder is None:
            raise RuntimeError("Keine Aufzeichnung aktiv.")
        self.recorder.save(path)

    def load_replay(self, path: str | Path) -> None:
        self.replay = Replay.load(path)
        self.recorder = None

    def agent_details(self, agent_id: int) -> dict[str, Any]:
        if self.replay is not None:
            snapshot = self.replay.current()
            for agent in snapshot.get("agents", []):
                if agent.get("id") == agent_id:
                    return agent
            return {"id": agent_id}
        return self.engine.agent_details(agent_id, self.diagnostic)
