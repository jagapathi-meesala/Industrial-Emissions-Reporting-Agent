from pathlib import Path
required = [
"agent.yaml","SOUL.md","README.md","RULES.md","DUTIES.md","AGENTS.md","EXPLAINABILITY.md",
"requirements.txt",".env.example",".gitignore","pytest.ini","core/__init__.py","core/engine.py","core/cli.py",
"tools/validate-emissions-record.yaml","tools/calculate-emissions-inventory.yaml","tools/prepare-emissions-report.yaml",
"skills/emissions-data-validation/SKILL.md","skills/emissions-calculation/SKILL.md","skills/report-preparation/SKILL.md",
"tests/test_engine.py","examples/emissions_records.json"
]
missing = [name for name in required if not Path(name).is_file()]
if missing:
    print("FAIL: missing required files: " + ", ".join(missing))
    raise SystemExit(1)
print(f"PASS: all {len(required)}/{len(required)} required files present")
