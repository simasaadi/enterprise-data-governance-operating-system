# Data Classification Model

## Purpose
This model defines how governed data assets should be classified based on sensitivity, exposure risk, operational impact, and handling requirements.

## Objective
The objective is to ensure that data handling, access decisions, sharing conditions, and control expectations are proportionate to business and privacy risk.

## Why classification matters
Without a working classification model, organizations often face:
- inconsistent access decisions
- over-permissioned users
- unclear handling expectations
- informal external sharing
- weak review of sensitive extracts
- confusion about what requires higher approval

A classification model creates a common basis for access, storage, sharing, and review decisions.

## Classification levels

| Classification | Description | Typical handling expectation |
|---|---|---|
| Public | Information approved for public release | Broad access and standard publication controls |
| Internal | Business information intended for internal organizational use | Access limited to legitimate internal business need |
| Confidential | Sensitive internal information with material business, operational, financial, or privacy implications | Restricted access, tighter sharing review, traceable decisions |
| Restricted | Highly sensitive information with elevated privacy, legal, regulatory, safety, or executive risk | Need-to-know access only, strong approval and monitoring requirements |

## Classification factors
Classification should consider:
- presence of personal or confidential information
- operational sensitivity
- financial or legal exposure
- executive or public reporting implications
- reputational impact if mishandled
- downstream sharing risk
- whether the asset combines multiple sensitive fields

## Minimum handling expectations by level

| Area | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Access approval | Standard | Business need | Owner approval | Owner plus elevated review where required |
| Sharing | Broad | Internal only unless approved | Controlled internal and approved external only | Highly limited and exception-based |
| Storage | Standard | Standard managed storage | Controlled managed storage | Restricted managed storage only |
| Review | Routine | Periodic | More frequent | Formal and risk-based |
| Logging / traceability | Basic | Standard | Required for material cases | Strongly expected |

## Governance rules
- each governed asset should have an assigned classification
- classification should not be inferred informally where the asset is shared, sensitive, or business-critical
- a higher classification should be used when uncertainty remains
- classification changes should trigger access and sharing review
- sensitive extracts and derived files should inherit or exceed source sensitivity where appropriate

## Typical examples

| Asset type | Likely classification |
|---|---|
| Public dashboard approved for publication | Public |
| Internal performance report | Internal |
| Financial close workbook | Confidential |
| Sensitive access log or personal information extract | Restricted |

## Review triggers
Classification should be reviewed when:
- a new field is added
- new downstream sharing is proposed
- an asset becomes executive-facing or external-facing
- multiple datasets are combined
- privacy or legal interpretation changes
- the asset is re-used for a different purpose

## Minimum metadata linkage
Each classified asset should ideally identify:
- classification level
- owner
- steward
- approved use
- sharing conditions
- review date
- related access workflow or policy reference
