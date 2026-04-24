# Data Quality Issue Management Workflow

## Purpose
This workflow defines how data quality issues are captured, triaged, assigned, resolved, and closed.

## Objective
The objective is to prevent defects from being handled through scattered email chains, undocumented fixes, or untracked manual workarounds.

## Workflow stages

| Stage | Description | Primary role |
|---|---|---|
| Intake | Issue is logged with enough detail to assess it | Data Steward / Analyst |
| Triage | Issue is classified by severity, impact, and scope | Data Steward |
| Assignment | Owner and supporting roles are named | Data Owner / Steward |
| Investigation | Root cause and affected outputs are assessed | Analyst / SME / Control Owner |
| Containment | Temporary risk reduction action is taken if needed | Data Owner / Steward |
| Remediation | Corrective action is implemented | Control Owner / System Owner / Analyst |
| Validation | Fix is checked and evidence is captured | Data Steward / Analyst |
| Closure | Issue is formally closed with notes and dates | Data Steward / Data Owner |
| Monitoring | Recurrence and trend are reviewed | Governance Lead / Steward |

## Minimum issue log fields
Each issue record should capture:
- issue ID
- date identified
- reported by
- affected asset, report, or system
- issue summary
- quality dimension affected
- severity
- business impact
- whether output use is restricted
- assigned owner
- target resolution date
- root cause category
- remediation action
- validation status
- closure date
- recurrence flag

## Severity model

| Severity | Meaning | Typical response |
|---|---|---|
| Low | Limited impact, low-risk local issue | Track and resolve in routine workflow |
| Medium | Operational inconvenience or moderate reporting impact | Assign owner and monitor closely |
| High | Material operational, management, or shared reporting impact | Escalate to owner/manager |
| Critical | Executive, regulatory, financial, or enterprise-wide risk | Immediate escalation |

## Triage questions
- What asset or output is affected?
- Is the issue local or cross-system?
- Is current output use still acceptable?
- Does the issue affect a critical field, KPI, or approved definition?
- Has this happened before?
- Is a manual workaround currently hiding the problem?

## Output-use decision guidance

| Condition | Recommended action |
|---|---|
| Minor issue with low business impact | Continue use with tracking |
| Moderate issue with understood limitation | Continue with caveat or note |
| Material issue affecting key decision-making | Pause release or escalate approval |
| Critical unresolved defect | Stop release until decision owner direction is received |

## Root cause categories
Suggested categories:
- source data entry issue
- business rule ambiguity
- transformation logic defect
- mapping or reference-table issue
- reconciliation failure
- timing or refresh failure
- manual handling error
- access or workflow breakdown
- documentation gap
- ownership gap

## Repeat issue rule
If a material issue recurs:
- log it as recurrence-linked
- perform root cause review
- assess whether the control design is inadequate
- consider escalation to governance lead or council

## Closure rule
An issue should only be closed when:
- remediation action is complete
- output risk has been reassessed
- validation evidence exists
- owner agreement is documented
- follow-up monitoring is defined where needed
