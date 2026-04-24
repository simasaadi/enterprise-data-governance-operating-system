# Data Owner and Data Steward Model

## Purpose
This model distinguishes accountability from operational stewardship so governance activities are assigned to the right level.

## Why this matters
A common governance failure is role confusion:
- analysts make business decisions they do not own
- managers assume stewardship is happening but it is not structured
- access approvals happen without clear business authority
- issue follow-up depends on individual memory rather than assigned responsibility

This model separates decision authority, coordination responsibility, and control execution.

## Role definitions

### Data owner
The data owner is accountable for business decisions related to a data domain, report, or critical data asset.

Typical accountabilities:
- approve critical business definitions
- approve quality thresholds and tolerances
- approve sensitive or exceptional access
- sponsor remediation for major data issues
- resolve domain-level disputes
- endorse material changes affecting downstream business use

### Data steward
The data steward coordinates day-to-day governance operations for the domain.

Typical responsibilities:
- maintain glossary and metadata records
- coordinate data quality checks and issue follow-up
- track exceptions, actions, and unresolved items
- support access workflow completeness
- maintain traceability across governance artifacts
- support change communication and downstream visibility

### Control owner
A control owner executes or oversees a specific governance control.

Examples:
- reconciliation owner
- certification owner
- access review owner
- issue log owner
- threshold monitoring owner

### System owner
The system owner supports the platform or application layer.

Typical responsibilities:
- maintain system configuration
- support technical access provisioning
- advise on platform constraints
- provide technical lineage inputs
- support implementation of approved changes

### Governance lead
The governance lead designs, coordinates, and monitors the governance system at a cross-domain level.

Typical responsibilities:
- maintain governance standards
- facilitate governance forums
- resolve role ambiguity
- track operating maturity
- support escalations and implementation planning

## Accountability model

| Activity | Data Owner | Data Steward | Control Owner | System Owner | Governance Lead |
|---|---|---|---|---|---|
| Approve business definitions | A | R | C | I | C |
| Maintain glossary and metadata | C | A/R | I | C | C |
| Approve quality thresholds | A | R | C | I | C |
| Execute recurring control checks | I | C | A/R | C | I |
| Triage governance issues | C | A/R | R | C | C |
| Approve sensitive access | A | R | I | C | C |
| Provision technical access | I | C | I | A/R | I |
| Assess material change impacts | A | R | C | C | C |
| Escalate unresolved cross-domain issues | C | R | I | I | A |

## Design principle
The owner decides.  
The steward coordinates.  
The control owner executes.  
The system owner enables.  
The governance lead stabilizes the model across domains.

## Failure modes this model is designed to prevent
- everyone is consulted but nobody is accountable
- the steward becomes an informal owner without authority
- access decisions are made without business sign-off
- controls exist but have no named executor
- recurring issues remain unowned across teams

## Minimum evidence of role clarity
A mature role model should make it easy to identify:
- who approves
- who maintains
- who executes
- who escalates
- who is consulted
- who is informed
