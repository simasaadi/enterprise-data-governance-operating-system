# Metadata Model

## Purpose
This model defines the minimum metadata structure required to govern critical data assets, reports, datasets, tables, fields, extracts, and governed business terms.

## Objective
The objective is to ensure that important data assets are understandable, traceable, owned, and usable without relying on informal memory or person-dependent explanation.

## Why metadata matters
Weak metadata environments usually create:
- unclear ownership
- inconsistent definitions
- report logic that cannot be traced
- high dependency on specific individuals
- repeated clarification requests
- slow onboarding for new analysts or stewards
- hidden downstream impacts when changes are made

A stronger metadata model reduces ambiguity and supports governance, operations, reporting, and change management.

## Metadata layers

| Layer | Description | Typical examples |
|---|---|---|
| Business metadata | Describes meaning, ownership, purpose, and use | business term, KPI definition, owner, steward |
| Technical metadata | Describes system and structural characteristics | schema, table, column, datatype, refresh pattern |
| Operational metadata | Describes how the asset is used and maintained | refresh frequency, SLA, certification status, issue status |
| Governance metadata | Describes governance and control conditions | classification, criticality, access model, quality rule linkage |
| Lineage metadata | Describes upstream/downstream movement and dependencies | source system, transformation step, downstream report |

## Minimum metadata fields for governed assets

| Field | Description |
|---|---|
| Asset ID | Unique identifier for the governed asset |
| Asset Name | Plain-language name of the asset |
| Asset Type | Report, dataset, table, field set, glossary term, extract, dashboard |
| Business Description | What the asset means and why it exists |
| Domain | Business domain or subject area |
| Data Owner | Accountable owner |
| Data Steward | Stewarding role |
| Source System | Primary source or origin |
| Refresh Frequency | Daily, weekly, monthly, event-based, ad hoc |
| Criticality Tier | Tier 1, Tier 2, Tier 3 or equivalent |
| Classification | Public, internal, confidential, restricted, etc. |
| Key Consumers | Primary users or downstream teams |
| Quality Rule Linkage | Related controls or threshold references |
| Approved Definition Reference | Link to approved term, logic, or business rule |
| Lineage Summary | Short description of upstream and downstream flow |
| Last Reviewed Date | Most recent governance review date |

## Minimum metadata fields for glossary terms

| Field | Description |
|---|---|
| Term ID | Unique term identifier |
| Term Name | Approved business term |
| Definition | Approved plain-language definition |
| Domain | Business domain |
| Owner | Decision authority for the term |
| Steward | Metadata coordinator |
| Synonyms | Related or alternative terms |
| Non-Approved Terms | Terms that should not be used |
| Calculation Rule | Where relevant, the approved logic basis |
| Source Reference | Policy, report rule, procedure, or standard |
| Effective Date | Start date of approval |
| Review Date | Next review date |

## Metadata quality expectations
Good metadata should be:
- current
- approved where needed
- understandable to non-technical and technical users
- linked to ownership
- linked to controls where material
- sufficiently structured for reuse

Weak metadata is usually:
- incomplete
- copied from technical systems without business context
- inconsistent across reports
- hard to search
- not reviewed after change

## Metadata maintenance rules
- all critical assets should have an owner and steward
- approved terms should not have competing unofficial definitions
- material assets should identify upstream source and downstream use
- metadata changes linked to report logic or business meaning should be reviewed
- metadata for high-risk assets should be reviewed on a defined cadence

## Governance use cases supported by this model
- onboarding new analysts and stewards
- supporting business glossary and data dictionary maintenance
- identifying downstream impacts before change
- supporting issue triage and escalation
- supporting access review and classification decisions
- improving trust in shared reporting and analytics outputs
