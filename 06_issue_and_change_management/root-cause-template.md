# Root Cause Analysis Template

## Purpose
This template provides a structured way to analyze material data, reporting, access, process, or control issues so remediation addresses the underlying cause rather than only the immediate symptom.

## When to use
Use this template when:
- a high-risk or repeated issue occurs
- a control fails more than once
- an executive or shared reporting output is affected
- a material access or workflow breakdown occurs
- manual workarounds are masking a structural weakness

## Issue summary
- Issue ID:
- Date identified:
- Issue title:
- Affected asset, report, or process:
- Reported by:
- Severity:
- Current status:

## Problem statement
Describe the issue in one clear sentence.
Example:
A certified reporting output was released with an unexplained variance because the upstream transformation logic no longer aligned with the approved business rule.

## Business impact
Describe:
- who was affected
- what decisions or operations were affected
- whether output use was restricted
- whether there was financial, operational, privacy, or reputational risk

## Immediate containment
Document the short-term action taken to reduce risk.
Examples:
- paused report release
- restricted access temporarily
- issued caveat to users
- performed manual correction
- escalated to decision owner

## Root cause analysis

### Symptom
What visible failure occurred?

### Direct cause
What immediate condition caused the issue?

### Contributing causes
What made the issue more likely or harder to detect?

Suggested categories:
- unclear ownership
- weak control design
- business rule ambiguity
- metadata gap
- system configuration issue
- manual handling error
- change communication failure
- inadequate access governance
- missing review cadence
- insufficient training

### Root cause
What underlying structural reason allowed the issue to occur?

## 5 Whys
1. Why did the issue occur?
2. Why was that condition present?
3. Why was that not prevented earlier?
4. Why was it not detected sooner?
5. Why does the process or operating model allow this?

## Evidence reviewed
List the evidence used:
- issue log
- control results
- source and target comparisons
- workflow documentation
- access records
- change notices
- stakeholder interviews
- metadata records

## Corrective actions

| Action | Owner | Due Date | Status | Preventive or Corrective |
|---|---|---|---|---|
| Example: Update transformation logic and validate downstream outputs | Control Owner | YYYY-MM-DD | Open | Corrective |
| Example: Add threshold exception alert for variance > 0.5% | Data Steward | YYYY-MM-DD | Open | Preventive |

## Control implications
Identify whether:
- existing controls failed
- threshold settings were insufficient
- escalation should have happened earlier
- a new control is required
- ownership must be clarified

## Lessons learned
What should change in the operating model, documentation, training, or control environment?

## Closure criteria
The issue should not be considered closed until:
- corrective action is implemented
- validation evidence exists
- owner confirms acceptable risk state
- recurrence monitoring is defined if needed
