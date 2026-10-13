from core.engine import calculate_inventory, validate_record

def record(**changes):
    data = {"record_id":"R1","source_category":"boiler","pollutant":"CO2",
            "activity_value":10,"activity_unit":"tonne_fuel","emission_factor":2,
            "factor_unit":"tonne_CO2_per_tonne_fuel","reporting_period":"2026-Q1"}
    data.update(changes)
    return data

def test_valid_record():
    assert validate_record(record()) == []

def test_missing_required_field():
    item = record()
    del item["pollutant"]
    assert "Missing required field: pollutant" in validate_record(item)

def test_empty_unit_invalid():
    assert any("activity_unit" in e for e in validate_record(record(activity_unit="")))

def test_negative_activity_invalid():
    assert any("activity_value" in e for e in validate_record(record(activity_value=-1)))

def test_calculation_formula():
    result = calculate_inventory([record()])
    assert result["calculated_records"][0]["estimated_emissions"] == 20

def test_invalid_records_excluded():
    result = calculate_inventory([record(), record(record_id="bad", activity_value=-5)])
    assert len(result["calculated_records"]) == 1
    assert len(result["invalid_records"]) == 1

def test_summary_by_pollutant_and_category():
    result = calculate_inventory([record(), record(record_id="R2", activity_value=5)])
    assert result["summary"][0]["estimated_total"] == 30

def test_report_never_certifies_compliance():
    assert calculate_inventory([record()])["regulatory_compliance_certified"] is False
