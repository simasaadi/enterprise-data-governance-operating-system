# Governance Structure

## Structure overview

| Layer | Primary role | Core responsibility |
|---|---|---|
| Executive oversight | Executive sponsor / governance council | Strategic direction, prioritization, escalation resolution |
| Domain accountability | Data owner | Decision authority for domain rules, quality, access, and use |
| Operational stewardship | Data steward | Day-to-day coordination of definitions, controls, issues, and metadata |
| Control execution | Analysts / SMEs / control owners | Execute controls, validate outputs, document issues, support remediation |
| Platform and enablement | System owners / technical teams | Support access, technical controls, lineage inputs, and implementation |

## Governance council
The council provides:
- direction on priorities
- resolution of cross-domain conflicts
- review of high-risk issues
- endorsement of major governance standards
- visibility into KPI and maturity performance

## Data owners
Data owners are accountable for:
- approving critical definitions and business rules
- agreeing quality thresholds
- approving access for sensitive or material assets
- resolving escalated issues where business judgment is required
- supporting remediation when recurring control failures appear

## Data stewards
Data stewards are responsible for:
- maintaining core metadata and definitions
- coordinating issue intake and triage
- monitoring quality indicators
- supporting access workflow completeness
- maintaining traceability for operational governance artifacts

## Escalation logic
Escalation is required when:
- ownership is unclear
- business units disagree on meaning or use
- thresholds are repeatedly breached
- access requests involve high sensitivity or exceptions
- changes create downstream reporting or operational risk

## Meeting cadence

| Forum | Frequency | Purpose |
|---|---|---|
| Governance council | Monthly | Oversight, decisions, escalations, KPI review |
| Domain stewardship forum | Bi-weekly | Metadata, quality, issue review, change visibility |
| Working session | As needed | Design or resolve specific governance items |
| Executive review | Quarterly | Maturity, risks, and implementation status |

## Decision categories

| Decision type | Primary decision maker | Consulted |
|---|---|---|
| Business definition | Data owner | Steward, SMEs, reporting leads |
| Quality threshold | Data owner | Steward, analyst, operational lead |
| Access exception | Data owner / delegated approver | Privacy, security, steward |
| Cross-domain conflict | Governance council | Relevant owners and stewards |
| Material change approval | Owner or council depending on impact | Steward, technical lead, impacted consumers |
