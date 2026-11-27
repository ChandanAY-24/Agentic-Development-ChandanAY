# Defect & Error Tracker

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active Standard  

## Purpose

Systematic tracking, root cause analysis, regression prevention, and defect history.

## Agent read trigger

**MUST** read or consult this file: Whenever encountering unexpected test failures.

## 3. Active & Resolved Defect Log

| Defect ID | Date | Sev | Summary | Impacted Path | Violated AC / Spec Gap | Root Cause | Fix (Commit / PR) | Regression Test | Status |
|---|---|---|---|---|---|---|---|---|---|
| `ERR-001` | 13-11-2026 | `P1` | Null pointer on enrollment | `src/enrollment/service.ts` | `AC-FEAT002-01` | Missing validation | commit `a1b2c3d` | `tests/unit/enrollment.test.ts` | `RESOLVED` |
| `ERR-002` | 16-11-2026 | `P0` | ENOENT crash on missing pkg | `server.js` | `AC-FEAT001-03` | Hardcoded npm path | commit `f9ef182` | `tests/test_ac_contracts.js` | `RESOLVED` |
| `ERR-003` | 18-11-2026 | `P2` | CSS overflow on mobile | `dashboard.css` | `AC-FEAT003-01` | Missing media query | - | - | `ACTIVE` |

## Evidence and change control

- **MUST** record owner, revision/date.

## SDD-Vibe enforcement

- **MUST** verify the latest approved feature spec version.
