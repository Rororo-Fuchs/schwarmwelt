from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from schwarmwelt_lab.core.config import SimulationConfig
from schwarmwelt_lab.core.engine import SimulationEngine
from schwarmwelt_lab.core.plugins import load_plugin_directory
from schwarmwelt_lab.core.recording import SnapshotRecorder


def main() -> None:
    parser = argparse.ArgumentParser(description="Schwarmwelt ohne Oberfläche ausführen")
    parser.add_argument("scenario", nargs="?", default="scenarios/ritual_baseline.json")
    parser.add_argument("--ticks", type=int, default=1000)
    parser.add_argument("--seed", type=int)
    parser.add_argument("--record", type=Path, help="Snapshots als .jsonl.gz speichern")
    parser.add_argument("--record-interval", type=int, default=10)
    args = parser.parse_args()

    scenario = (ROOT / args.scenario).resolve() if not Path(args.scenario).is_absolute() else Path(args.scenario)
    load_plugin_directory(ROOT / "plugins")
    config = SimulationConfig.load(scenario)
    if args.seed is not None:
        config.seed = args.seed
    engine = SimulationEngine(config)
    recorder = SnapshotRecorder(config.to_dict(), args.record_interval) if args.record else None
    if recorder:
        recorder.capture(engine.snapshot(False))

    for _ in range(args.ticks):
        engine.step(1)
        if recorder:
            recorder.capture(engine.snapshot(False))

    if recorder and args.record:
        recorder.save(args.record)

    result = {
        "scenario": config.title,
        "seed": config.seed,
        "ticks": engine.tick,
        "digest": engine.deterministic_digest(),
        "metrics": engine.metrics(),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
