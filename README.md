# Industrial Emissions Reporting Agent

A local, explainable agent for validating supplied industrial activity/emissions records, calculating inventory totals from provided factors, and preparing review-ready summaries.

## Features
- Validates records, units, periods, and numeric activity values.
- Calculates estimated emissions using `activity_value × emission_factor`, after requiring compatible units as stated in the input.
- Summarizes totals by pollutant and source category.
- Retains input provenance and flags missing factors or units.
- Generates a JSON report with assumptions and limitations.

## Run
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m pytest -q
python3 verification/readiness_audit.py
python3 -m core.cli examples/emissions_records.json
```
If installed, run `opengap validate` from this directory.

## Important limitations
This tool performs arithmetic on supplied values; it does not measure emissions, validate factors against a regulator's approved list, or certify compliance. Ensure factor units match activity units and obtain qualified environmental/compliance review before filing.
