# Explainability

## Inputs
The agent accepts records containing `record_id`, `source_category`, `pollutant`, `activity_value`, `activity_unit`, `emission_factor`, `factor_unit`, and `reporting_period`. Optional notes and source references are retained when supplied.

## Decision
For records with complete numeric values and explicit unit descriptions, estimated emissions are calculated as `activity_value × emission_factor`. The output labels the result as an estimate and carries through the stated units and reporting period. It does not perform automatic dimensional conversion.

## Limits
The agent cannot verify whether measurements or emission factors are accurate, approved, or appropriate for a specific facility or jurisdiction. It does not determine legal compliance. Unit compatibility must be confirmed by the user or reviewer.

## Tool: validate-emissions-record
### Inputs and Data Sources
One supplied industrial emissions activity record.
### Decision and Reasoning
Checks required keys, non-empty identifiers/units/periods, and numeric non-negative activity and factor values.
### Outputs and Evidence
Returns validity and field-level validation errors.
### Limits and Constraints
Cannot independently verify source records or unit compatibility.
### Failure Handling
Invalid records are returned with explicit errors and excluded from calculations.
### Human Review
Confirm units, source evidence, and reporting-period coverage.

## Tool: calculate-emissions-inventory
### Inputs and Data Sources
A list of supplied records with activity values and emission factors.
### Decision and Reasoning
Calculates each valid record using the documented multiplication formula, without unit conversion.
### Outputs and Evidence
Returns per-record estimates and pollutant/category totals, with source IDs.
### Limits and Constraints
The calculation is only meaningful when activity and factor units are compatible.
### Failure Handling
Invalid records are excluded and listed separately.
### Human Review
Check factors against approved methods and confirm units before using totals in formal reports.

## Tool: prepare-emissions-report
### Inputs and Data Sources
Calculated inventory result and supplied reporting period.
### Decision and Reasoning
Formats totals, excluded records, assumptions, and limitations into a structured report.
### Outputs and Evidence
Returns a JSON report suitable for reviewer handoff.
### Limits and Constraints
Does not complete official forms or certify regulatory compliance.
### Failure Handling
Missing or malformed input produces explicit errors.
### Human Review
Environmental and compliance staff must approve the final report and any jurisdiction-specific disclosures.
