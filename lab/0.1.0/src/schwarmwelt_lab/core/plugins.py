from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

_LOADED: set[Path] = set()


def load_plugin_directory(directory: str | Path) -> list[str]:
    root = Path(directory).resolve()
    if not root.exists():
        return []
    loaded: list[str] = []
    for path in sorted(root.glob("*.py")):
        if path.name.startswith("_") or path in _LOADED:
            continue
        module_name = f"schwarmwelt_external_{path.stem}_{abs(hash(path))}"
        spec = importlib.util.spec_from_file_location(module_name, path)
        if spec is None or spec.loader is None:
            raise ImportError(f"Plugin kann nicht geladen werden: {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        _LOADED.add(path)
        loaded.append(path.name)
    return loaded
