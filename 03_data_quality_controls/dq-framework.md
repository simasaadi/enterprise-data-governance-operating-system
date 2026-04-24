# Data Quality Framework

## Purpose
This framework defines how data quality is governed, measured, monitored, and escalated across critical data assets, reports, and operational datasets.

## Objective
The objective is to ensure data is fit for operational, analytical, reporting, compliance, and executive use through structured controls, explicit thresholds, named ownership, and traceable remediation.

## Core principles
- data quality must be defined in business terms, not only technical terms
- controls must be tied to risk and business impact
- recurring issues must trigger structured remediation
- exceptions must be visible and traceable
- thresholds must be approved, not assumed
- quality monitoring should support prevention as well as detection

## Quality dimensions
This operating model uses the following dimensions:

| Dimension | Definition | Example question |
|---|---|---|
| Completeness | Required data is present | Are critical fields populated? |
| Validity | Values conform to expected format or rule | Does the value match allowed patterns or code sets? |
| Accuracy | Data reflects the real-world condition or approved source logic | Does the recorded value match the trusted source or business rule? |
| Consistency | Data is aligned across systems, reports, or fields | Do key values match across related systems? |
| Timeliness | Data is current enough for intended use | Was the dataset refreshed within the agreed window? |
| Uniqueness | Records that should be unique are not duplicated | Are customer IDs or transaction IDs duplicated? |
| Integrity | Relationships between records are preserved | Do child records reference valid parent records? |

## Control model

### Preventive controls
Used to stop issues before they enter or spread through the process.
Examples:
- required-field validation
- controlled reference lists
- form logic and input constraints
- role-based edit restrictions

### Detective controls
Used to identify errors after entry, movement, or transformation.
Examples:
- exception reports
- reconciliation checks
- duplicate detection
- threshold monitoring
- variance and reasonableness review

### Corrective controls
Used to resolve defects and restore confidence in downstream use.
Examples:
- issue remediation workflow
- data correction procedure
- root cause review
- control redesign after repeated failure

## Control lifecycle
1. Define critical data elements and business rules
2. Assign control owner and accountable owner
3. Define threshold or expected result
4. Run control on a defined cadence
5. Record result and exceptions
6. Triage issues
7. Remediate and document root cause
8. Monitor trends and repeat failures
9. Escalate when thresholds are repeatedly breached

## Roles in the data quality model

| Role | Responsibility |
|---|---|
| Data Owner | Approves thresholds, tolerances, and major remediation priorities |
| Data Steward | Coordinates monitoring, issue intake, follow-up, and reporting |
| Control Owner | Executes the quality control and evidences the result |
| Analyst / SME | Investigates exceptions and supports validation |
| Governance Lead | Monitors cross-domain trends and recurring structural issues |

## Control evidence
At minimum, each quality control should have:
- control name
- business purpose
- asset or dataset covered
- dimension addressed
- rule logic
- threshold
- cadence
- control owner
- accountable owner
- evidence location
- exception handling path

## Escalation triggers
Escalation should occur when:
- a control repeatedly fails across review periods
- a material report or executive output is affected
- no accountable owner can resolve the issue
- a defect affects multiple systems or teams
- a threshold is no longer realistic or no longer protective
- manual workarounds create unmanaged risk

## Minimum KPIs for quality governance
- percent of critical controls executed on time
- percent of threshold breaches resolved within target time
- number of repeated exceptions by asset
- number of unresolved high-risk issues
- trend in completeness, validity, and reconciliation pass rates
- number of reports released with open material data-quality conditions

## Maturity indicators
A stronger quality environment usually shows:
- approved thresholds rather than informal expectations
- named control owners
- recurring evidence production
- trend monitoring
- consistent issue logging
- structured escalation for repeat failures
- linkage between defects and root cause action
