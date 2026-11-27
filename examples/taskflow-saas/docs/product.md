# Product Vision — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

Define product vision, personas (`PER-##`), capabilities (`CAP-###`), and explicit non-goals for TaskFlow SaaS.

## Agent read trigger

**MUST** read or consult this file: Before authoring `docs/prd.md` or any `FEAT-###` specification.

## Personas

- **PER-01 (Engineering Lead):** Creates sprint tasks, assigns priorities, and reviews board progress.
- **PER-02 (Developer):** Updates task status (`BACKLOG` → `IN_PROGRESS` → `DONE`) after signing in.

## Capabilities

- **CAP-001:** Interactive Kanban / Sprint Task Board with status transitions and priority filtering.
- **CAP-002:** Persistent SQLite storage with Zod contract validation.
- **CAP-003:** Signed HTTP-only session authentication and role-based mutation guards.

## Non-Goals

- External OAuth providers, billing/Stripe integration, or multi-region replication (out of scope for v1.0.0).

## Evidence and change control

- **MUST** record owner, revision/date, and approval references.

## SDD-Vibe enforcement

- **MUST** keep `docs/prd.md` traced to `CAP-###` and `PER-##`.
