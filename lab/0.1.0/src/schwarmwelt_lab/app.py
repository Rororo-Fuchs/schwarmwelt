from __future__ import annotations

from pathlib import Path

from .ui import MainWindow


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    scenario_directory = root / "scenarios"
    app = MainWindow(scenario_directory)
    app.mainloop()
