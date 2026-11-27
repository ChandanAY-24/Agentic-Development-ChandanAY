# Defect & Error Tracker — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

Track defects, root causes, and regression tests for TaskFlow SaaS.

## Agent read trigger

**MUST** read or consult this file: Whenever encountering test failures or regressions.

## Active & Resolved Defect Log

| Defect ID | Date | Sev | Summary | Impacted Path | Violated AC / Spec Gap | Root Cause | Fix (Commit / PR) | Regression Test | Status |
|---|---|---|---|---|---|---|---|---|---|
| `ERR-001` | 27-11-2026 | `P1` | Empty task title accepted on whitespace-only input | `src/lib/contracts.ts` | `AC-FEAT001-02` | Missing `.trim()` before `.min(1)` in Zod schema | `contracts.ts` `.trim()` | `tests/unit/task-contracts.test.ts` | `RESOLVED` |

## Evidence and change control

- **MUST** link every defect to an `AC-FEAT###-##` and regression test.

## SDD-Vibe enforcement

- **MUST** never close a defect without a passing regression test.
