# Data Quality Thresholds

## Purpose
This document defines how thresholds are set, interpreted, and escalated for critical data quality controls.

## Why thresholds matter
Without approved thresholds, organizations often rely on vague statements such as "this looks fine" or "the numbers seem close enough." Thresholds create explicit quality expectations and make exception handling more disciplined.

## Threshold design principles
- thresholds should reflect business impact, not arbitrary perfection
- stricter thresholds are expected for critical fields and executive reporting
- warning and breach levels should be distinguished
- thresholds should be reviewed when operating conditions change
- repeated breaches should trigger root cause review, not only short-term fixes

## Threshold model

| Level | Meaning | Typical action |
|---|---|---|
| Target | Expected operating condition | Continue monitoring |
| Warning | Early deterioration or minor exception | Review and assess risk |
| Breach | Threshold not met | Open issue, investigate, and assess escalation |
| Material Breach | Serious failure affecting reporting, operations, or risk | Escalate immediately |

## Suggested starting thresholds

| Control Area | Metric | Warning Level | Breach Level | Typical Owner |
|---|---|---|---|---|
| Critical field completeness | Required fields populated | < 99.0% | < 98.0% | Data Owner |
| Primary key uniqueness | Duplicate keys | > 0 | > 0 | Data Owner |
| Reference-code validity | Valid code set alignment | < 99.5% | < 99.0% | Data Owner |
| Refresh timeliness | Delay from SLA cutoff | > 30 min | > 2 hrs | Data Owner / System Owner |
| Cross-system reconciliation | Count/amount variance | > 0.2% | > 0.5% | Data Owner |
| Manual adjustment traceability | Fully documented adjustments | < 100% | < 99.0% | Data Owner |
| Executive report certification | Controls completed before release | < 100% | < 100% | Data Owner |
| Recurring issue recurrence | Repeat occurrence window | 1 repeat | 2+ repeats in 90 days | Governance Lead |

## Threshold-setting method
Thresholds should be set using:
1. criticality of the data asset
2. downstream decision impact
3. regulatory or reputational risk
4. operational tolerance for errors or delay
5. control maturity and automation level
6. historical baseline performance

## Example tiering model

| Asset Tier | Example | Threshold posture |
|---|---|---|
| Tier 1 | Executive reporting, regulatory, financial close, public reporting | Very strict |
| Tier 2 | Management reporting, operational KPIs, shared analytical marts | Strict |
| Tier 3 | Internal working datasets, lower-risk reference views | Moderate |

## Breach handling expectations
When a breach occurs:
- capture the exception
- assess whether output use should be paused, conditioned, or allowed with caveat
- assign an owner
- define target resolution date
- determine whether escalation is needed
- document root cause if repeat or material

## When thresholds should be reviewed
Thresholds should be revisited when:
- a new data source or system is introduced
- a major change affects calculation or process logic
- operating volumes materially change
- repeated breaches suggest the threshold is unrealistic or the control is too weak
- leadership reclassifies the asset as higher or lower risk

## Governance rule
Thresholds are not valid unless:
- the accountable owner is identified
- the business rationale is clear
- the breach response path is defined
- the review cadence is defined
