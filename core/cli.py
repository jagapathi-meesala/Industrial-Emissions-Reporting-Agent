"""Command-line interface for emissions inventory calculations."""
import json
import sys
from pathlib import Path
from .engine import calculate_inventory

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 -m core.cli <records.json>")
        return 2
    try:
        records = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        return 1
    if not isinstance(records, list):
        print(json.dumps({"error": "Input JSON must be a list of records."}, indent=2))
        return 1
    print(json.dumps(calculate_inventory(records), indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
