# Access Request Workflow

## Purpose
This workflow defines how access requests should be initiated, reviewed, approved, fulfilled, and periodically re-evaluated.

## Objective
The objective is to reduce informal access granting, improve traceability, and ensure that access decisions are aligned to business need, role, and classification level.

## Workflow stages

| Stage | Description | Primary role |
|---|---|---|
| Request initiation | Requester provides access need, role, asset, and duration | Requester |
| Completeness review | Request is checked for clarity and required fields | Data Steward / Coordinator |
| Business review | Business need and minimum necessary access are assessed | Data Owner / Approver |
| Risk review | Sensitive, exceptional, or external cases are assessed | Privacy / Security / Governance as needed |
| Decision | Approve, reject, conditionally approve, or route for escalation | Decision owner |
| Fulfilment | Technical provisioning or sharing action is completed | System Owner / Admin |
| Confirmation | Requester and steward confirm fulfilment state | Fulfilment role / Steward |
| Periodic review | Access remains justified or is removed | Owner / Steward / Manager |

## Minimum request information
Each request should capture:
- requester name
- requester role and unit
- asset or system requested
- classification level
- requested access type
- business reason
- minimum necessary assessment
- requested start date
- end date or review date if temporary
- downstream sharing intent
- decision owner
- decision and rationale
- fulfilment status

## Decision options
- Approved
- Approved with conditions
- Rejected
- Escalated for review
- Pending additional information

## Example approval conditions
- access limited to a subset of fields
- read-only access only
- temporary duration
- no onward sharing
- use restricted to named business purpose
- supervisor confirmation required
- additional privacy or security review before release

## Escalation triggers
Escalation should occur when:
- the request involves restricted data
- the business reason is unclear or weak
- the requester asks for broad or sweeping access
- temporary access becomes recurring without review
- cross-team or external sharing is requested
- the approver is unclear
- the request conflicts with minimum-necessary principles

## Periodic review expectations
Access should be reviewed when:
- roles change
- employment or assignment ends
- project-based access expires
- classification changes
- repeated exceptions indicate access creep
- an asset becomes more sensitive or broadly shared

## Governance rule
No material access decision should rely only on an undocumented verbal or email approval where the asset is sensitive, shared, restricted, or exception-based.
