# Minimum Necessary Access Policy

## Purpose
This policy establishes the principle that users should only receive the minimum level of data access needed to perform their approved business responsibilities.

## Objective
The objective is to reduce unnecessary exposure, control sprawl, and unmanaged downstream risk while still enabling operational and analytical work.

## Policy statement
Access should be:
- role-based where possible
- limited to legitimate business need
- proportionate to the sensitivity of the asset
- limited in scope, duration, and action rights where appropriate
- reviewed when roles, systems, or uses change

## Minimum-necessary principles
1. Access should match the task, not personal convenience
2. Full-dataset access should not be the default
3. Broad export rights require stronger scrutiny
4. Temporary access should expire or be reviewed
5. Derived outputs should not become a workaround for uncontrolled sharing
6. Sensitive fields may require narrower access than the broader dataset

## Access dimensions to limit
- system or dataset scope
- field or attribute scope
- row or subject scope
- read versus edit rights
- export/download rights
- temporary versus ongoing duration
- internal versus external sharing rights

## Examples

| Scenario | Better design |
|---|---|
| Analyst needs one KPI view | Read-only access to certified reporting layer, not source tables |
| Manager needs one region | Region-filtered access rather than all-region access |
| Short-term project request | Time-bound access with review date |
| Sensitive extract needed for one task | Controlled extract with approved purpose and no onward sharing |

## Warning signs of over-access
- users hold access because they might need it later
- roles receive the same broad access regardless of task
- legacy access is never reviewed
- extracts are shared to avoid formal access approval
- no one can explain why a user still has access

## Governance expectations
Requests should show:
- business purpose
- why narrower access is insufficient
- whether temporary access is appropriate
- whether sensitive fields can be masked or excluded
- review date where applicable

## Exception handling
Exceptions to minimum necessary access should:
- be documented
- identify the decision owner
- state the rationale
- state expiry or review conditions
- be logged for later review
