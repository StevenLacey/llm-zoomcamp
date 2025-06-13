import json
from pathlib import Path
from typing import Any

def load_json(path: Path) -> Any:
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return None

def save_json(path: Path, data: Any):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def append_json_record(path: Path, record: dict):
    data = load_json(path) or []
    data.append(record)
    save_json(path, data)