from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from schwarmwelt_lab.core.config import SimulationConfig
from schwarmwelt_lab.core.engine import SimulationEngine
from schwarmwelt_lab.core.plugins import load_plugin_directory


def parse_int_list(value: str) -> list[int]:
    return [int(part.strip()) for part in value.split(",") if part.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Szenario-/Seed-Matrix ausführen")
    parser.add_argument(
        "--scenarios",
        default="ritual_baseline,social_memory_trace,sequence_imitation_control,no_sequence_control,full_mixing_control",
        help="Kommagetrennte Dateinamen ohne .json",
    )
    parser.add_argument("--seeds", default="20,21,22")
    parser.add_argument("--ticks", type=int, default=1000)
    parser.add_argument("--output", type=Path, default=ROOT / "matrix_results.csv")
    args = parser.parse_args()

    load_plugin_directory(ROOT / "plugins")
    scenario_names = [item.strip() for item in args.scenarios.split(",") if item.strip()]
    seeds = parse_int_list(args.seeds)
    rows: list[dict[str, object]] = []

    for scenario_name in scenario_names:
        path = ROOT / "scenarios" / f"{scenario_name}.json"
        for seed in seeds:
            config = SimulationConfig.load(path)
            config.seed = seed
            engine = SimulationEngine(config)
            engine.step(args.ticks)
            metrics = engine.metrics()
            memory = metrics["memory"]
            row = {
                "scenario": scenario_name,
                "seed": seed,
                "ticks": args.ticks,
                "digest": engine.deterministic_digest(),
                "encounters": metrics["encounters"],
                "turnovers": metrics["turnovers"],
                "mean_valence_a": metrics["mean_valence_a"],
                "mean_valence_b": metrics["mean_valence_b"],
                "memory_type": memory.get("type"),
                "memory_entries": memory.get("entries", 0),
                "memory_strength": memory.get("strength", 0.0),
                "visible_sequence_types": len(metrics["frequent_sequences"]),
            }
            rows.append(row)
            print(f"{scenario_name} / seed {seed} abgeschlossen")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Ergebnis: {args.output}")


if __name__ == "__main__":
    main()
