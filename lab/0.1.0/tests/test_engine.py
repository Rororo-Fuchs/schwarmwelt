from __future__ import annotations

from dataclasses import fields
from pathlib import Path
import tempfile
import unittest

from schwarmwelt_lab.core.config import SimulationConfig
from schwarmwelt_lab.core.engine import SimulationEngine
from schwarmwelt_lab.core.recording import Replay, SnapshotRecorder
from schwarmwelt_lab.core.types import ObservableContext

ROOT = Path(__file__).resolve().parents[1]


class EngineTests(unittest.TestCase):
    def load(self, name: str) -> SimulationConfig:
        return SimulationConfig.load(ROOT / "scenarios" / name)

    def test_determinism(self) -> None:
        cfg1 = self.load("ritual_baseline.json")
        cfg2 = self.load("ritual_baseline.json")
        first = SimulationEngine(cfg1)
        second = SimulationEngine(cfg2)
        first.step(30)
        second.step(30)
        self.assertEqual(first.deterministic_digest(), second.deterministic_digest())

    def test_surface_snapshot_hides_hidden_state(self) -> None:
        engine = SimulationEngine(self.load("ritual_baseline.json"))
        engine.step(1)
        surface = engine.snapshot(False)
        diagnostic = engine.snapshot(True)
        self.assertNotIn("true_state", surface["agents"][0])
        self.assertNotIn("valence_a", surface["agents"][0])
        self.assertIn("true_state", diagnostic["agents"][0])
        self.assertIn("decoy_state", diagnostic["agents"][0])

    def test_memory_module_swappable_by_config(self) -> None:
        engine = SimulationEngine(self.load("social_memory_trace.json"))
        engine.step(20)
        summary = engine.metrics()["memory"]
        self.assertEqual(summary["type"], "distributed_trace")
        self.assertGreaterEqual(summary["entries"], 0)

    def test_observable_context_excludes_ground_truth(self) -> None:
        names = {field.name for field in fields(ObservableContext)}
        self.assertNotIn("true_state", names)
        self.assertNotIn("partner_valence", names)
        self.assertIn("estimated_state", names)
        self.assertIn("own_valence_delta", names)

    def test_recording_roundtrip(self) -> None:
        engine = SimulationEngine(self.load("ritual_baseline.json"))
        recorder = SnapshotRecorder(engine.config.to_dict())
        for _ in range(4):
            engine.step(1)
            recorder.capture(engine.snapshot(False))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "run.jsonl.gz"
            recorder.save(path)
            replay = Replay.load(path)
            self.assertEqual(replay.current()["tick"], 1)
            self.assertEqual(replay.step(3)["tick"], 4)

    def test_turnover_resets_agent_without_crashing(self) -> None:
        config = self.load("ritual_baseline.json")
        config.turnover_interval = 3
        engine = SimulationEngine(config)
        engine.step(3)
        self.assertEqual(engine.total_turnovers, 1)
        self.assertTrue(any(agent.newcomer for agent in engine.agents))


if __name__ == "__main__":
    unittest.main()
