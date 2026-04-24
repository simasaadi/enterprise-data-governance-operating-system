# Change Impact Assessment

## Purpose
This template defines how to assess the operational, reporting, governance, access, and downstream effects of a material change before implementation.

## When to use
Use this template for changes affecting:
- critical data elements
- business definitions or KPI logic
- source-to-target mappings
- access rules or classification
- shared reports, dashboards, or extracts
- control logic or thresholds
- workflow timing or handoffs

## Change summary
- Change ID:
- Change title:
- Requested by:
- Change owner:
- Proposed implementation date:
- Related issue or request ID:
- Affected domain:

## Description of change
Describe:
- what is changing
- why it is changing
- whether this is corrective, enhancement, or structural

## Change type
Choose one or more:
- business rule change
- data structure change
- mapping or transformation change
- access / sharing change
- metadata / definition change
- reporting logic change
- workflow / process change
- control or threshold change

## Affected assets
List:
- source systems
- datasets
- reports
- dashboards
- extracts
- logs
- metadata artifacts

## Impact assessment questions

### Business meaning
- Does this change alter interpretation of a KPI, metric, status, or term?
- Does it create any risk of inconsistent definitions across teams?

### Reporting and analytics
- Which reports, dashboards, or recurring outputs are affected?
- Will historical comparability change?

### Controls and quality
- Which controls, thresholds, or reconciliations are affected?
- Will validation logic need revision?

### Access and privacy
- Does classification need review?
- Does the change alter who should have access?

### Stakeholders
- Which teams, managers, analysts, or stewards must be informed?
- Does any training or user guidance need updating?

### Implementation risk
- Is phased rollout needed?
- Is rollback possible?
- Is temporary dual-running required?

## Impact severity

| Level | Meaning | Expected response |
|---|---|---|
| Low | Local, limited downstream effect | Routine implementation |
| Medium | Affects one or more shared outputs | Stakeholder notification and validation |
| High | Affects critical reports, controls, or multiple teams | Formal review and approval |
| Critical | Enterprise, executive, financial, legal, or public-facing impact | Controlled rollout and escalation |

## Required approvals
- Data Owner:
- Data Steward:
- Governance Lead:
- Privacy / Security review if needed:
- Technical / System Owner:
- Executive / Council if needed:

## Validation plan
Before closure, confirm:
- metadata updated
- affected controls updated
- downstream outputs validated
- access implications reviewed
- stakeholders notified
- final implemented state documented

## Decision
- Approved
- Approved with conditions
- Rejected
- Escalated

## Conditions / notes
Document any restrictions, dependencies, or follow-up requirements.
