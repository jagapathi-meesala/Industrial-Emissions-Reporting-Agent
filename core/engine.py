"""Validation and transparent calculations for emissions inventory records."""
from typing import Any

REQUIRED = ("record_id", "source_category", "pollutant", "activity_value",
            "activity_unit", "emission_factor", "factor_unit", "reporting_period")

def validate_record(record: dict[str, Any]) -> list[str]:
    errors = []
    for key in REQUIRED:
        if key not in record:
            errors.append(f"Missing required field: {key}")
    for key in ("record_id", "source_category", "pollutant", "activity_unit", "factor_unit", "reporting_period"):
        if key in record and (not isinstance(record[key], str) or not record[key].strip()):
            errors.append(f"{key} must be a non-empty string")
    for key in ("activity_value", "emission_factor"):
        if key in record and (not isinstance(record[key], (int, float)) or isinstance(record[key], bool) or record[key] < 0):
            errors.append(f"{key} must be a non-negative number")
    return errors

def calculate_inventory(records: list[dict[str, Any]]) -> dict[str, Any]:
    calculated, invalid = [], []
    totals = {}
    for record in records:
        errors = validate_record(record)
        if errors:
            invalid.append({"record_id": record.get("record_id"), "validation_errors": errors})
            continue
        value = round(record["activity_value"] * record["emission_factor"], 8)
        item = {
            "record_id": record["record_id"],
            "source_category": record["source_category"],
            "pollutant": record["pollutant"],
            "reporting_period": record["reporting_period"],
            "estimated_emissions": value,
            "result_unit": f"({record['activity_unit']}) × ({record['factor_unit']})",
            "formula": "activity_value × emission_factor",
            "status": "estimate; confirm unit compatibility and factor validity"
        }
        calculated.append(item)
        key = (record["pollutant"], record["source_category"], record["reporting_period"])
        totals[key] = totals.get(key, 0.0) + value
    summary = [
        {"pollutant": k[0], "source_category": k[1], "reporting_period": k[2], "estimated_total": round(v, 8)}
        for k, v in sorted(totals.items())
    ]
    return {
        "calculated_records": calculated,
        "invalid_records": invalid,
        "summary": summary,
        "assumptions": [
            "No automatic unit conversion is performed.",
            "Activity and emission-factor units must be compatible.",
            "Calculated values are estimates from user-supplied inputs."
        ],
        "regulatory_compliance_certified": False
    }
