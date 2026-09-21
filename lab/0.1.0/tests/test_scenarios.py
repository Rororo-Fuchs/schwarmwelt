from __future__ import annotations

from pathlib import Path
import unittest

from schwarmwelt_lab.core.config import SimulationConfig
from schwarmwelt_lab.core.engine import SimulationEngine

ROOT = Path(__file__).resolve().parents[1]


class ScenarioSmokeTests(unittest.TestCase):
    def test_all_scenarios_run(self) -> None:
        for path in sorted((ROOT / "scenarios").glob("*.json")):
            with self.subTest(path=path.name):
                config = SimulationConfig.load(path)
                config.agents = 16
                config.pulses = 3
                engine = SimulationEngine(config)
                engine.step(3)
                self.assertEqual(engine.tick, 3)
                self.assertEqual(len(engine.agents), 16)


if __name__ == "__main__":
    unittest.main()
