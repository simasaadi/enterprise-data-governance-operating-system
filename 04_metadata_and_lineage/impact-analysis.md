# Impact Analysis

## Purpose
This document defines how to assess the downstream impact of changes to governed data assets, definitions, rules, lineage paths, access structures, and reporting logic.

## Objective
The objective is to reduce uncontrolled change by making affected assets, users, controls, and decisions visible before implementation.

## Why impact analysis matters
Without structured impact analysis, organizations often experience:
- KPI changes without stakeholder awareness
- report breaks after upstream modifications
- inconsistent logic across teams
- access side effects after structural change
- increased remediation workload after release
- loss of trust in shared reporting

## When impact analysis is required
Impact analysis should be completed when a change affects:
- a critical data element
- an approved business definition
- calculation logic for a KPI or management metric
- source-to-target mapping
- classification or access treatment
- a shared dataset, report, or dashboard
- refresh timing or SLA for a critical asset
- lineage dependencies across systems or teams

## Core impact questions
1. What is changing?
2. Which assets are directly affected?
3. Which downstream reports, dashboards, extracts, or consumers are affected?
4. Does the change alter business meaning, not just technical structure?
5. Are controls, thresholds, or reconciliations affected?
6. Does access logic or classification need review?
7. Is communication, training, or re-certification required?
8. Is phased rollout or temporary dual-running needed?

## Impact categories

| Category | What to assess |
|---|---|
| Business meaning | Definition changes, KPI interpretation, policy alignment |
| Data structure | Field addition/removal, datatype change, mapping change |
| Reporting | Dashboards, scheduled outputs, extracts, scorecards |
| Quality controls | Rules, thresholds, certification logic, reconciliation checks |
| Access and privacy | Permission logic, classification, sharing conditions |
| Process and workflow | Manual workarounds, timing shifts, operational handoffs |
| Stakeholders | Teams, owners, stewards, analysts, decision-makers |
| Documentation | Glossary, dictionary, SOPs, user notes, templates |

## Minimum impact analysis record
Each material change should capture:
- change ID
- description of change
- rationale
- affected source asset
- affected downstream assets
- impacted teams or roles
- affected controls
- affected definitions or calculations
- access/privacy review needed
- communication required
- approval path
- effective date
- post-change validation plan

## Impact severity guide

| Severity | Meaning | Expected response |
|---|---|---|
| Low | Local change with limited downstream effect | Document and implement in routine workflow |
| Medium | Change affects one or more shared assets | Notify stakeholders and validate outputs |
| High | Change affects critical reporting, controls, or multiple teams | Formal review and approval required |
| Critical | Enterprise, executive, financial, regulatory, or public-facing impact | Escalate and require controlled rollout |

## Minimum validation actions after change
- confirm metadata has been updated
- validate downstream outputs
- re-run affected controls
- review access implications
- confirm stakeholders were notified
- document the final implemented state

## Governance rule
No material change should be treated as complete until:
- downstream impacts were assessed
- affected owners and stewards were identified
- required communication occurred
- post-change validation evidence exists
