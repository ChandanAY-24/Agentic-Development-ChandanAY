# Task Board — TaskFlow SaaS

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 2.0.0  
> **Status:** Active

## Purpose

Scoped, traceable units of work for TaskFlow SaaS.

## Agent read trigger

**MUST** read or consult this file: Before assigning or implementing any task.

### TASK-001: Phase 2 Frontend Sensory Demo UI [DONE] [P1]

| Field | Value |
|---|---|
| Feature | FEAT-001 (version 1.0.0) |
| Acceptance criteria | AC-FEAT001-01 |
| Owner | agent |
| Allowed files | src/app/page.tsx, src/app/layout.tsx, src/app/globals.css |
| Definition of Done | Interactive board verified on :3000 |

- [x] Build responsive Tailwind Kanban board with status filters
- [x] Verify Phase 2 sensory demo on `:3000`

### TASK-002: Zod Task Contracts & SQLite Persistence [DONE] [P1]

| Field | Value |
|---|---|
| Feature | FEAT-001 (version 1.0.0) |
| Acceptance criteria | AC-FEAT001-02, AC-FEAT001-03 |
| Owner | agent |
| Allowed files | src/lib/contracts.ts, src/db/index.ts, src/app/api/tasks/route.ts |
| Definition of Done | Tests TEST-FEAT001-01..03 red → green |

- [x] Write failing tests TEST-FEAT001-01..02 in `tests/unit/task-contracts.test.ts`
- [x] Implement Zod contracts and SQLite persistence

### TASK-003: Signed Session Auth & Mutation Guard [DONE] [P0]

| Field | Value |
|---|---|
| Feature | FEAT-002 (version 1.0.0) |
| Acceptance criteria | AC-FEAT002-01, AC-FEAT002-02 |
| Owner | agent |
| Allowed files | src/lib/auth.ts, src/app/api/auth/route.ts |
| Definition of Done | Tests TEST-FEAT002-01..02 red → green |

- [x] Write failing auth tests TEST-FEAT002-01..02 in `tests/integration/auth-and-tasks.test.ts`
- [x] Implement HMAC session signing and 401 guard

## Evidence and change control

- **MUST** record real test evidence before marking tasks `DONE`.

## SDD-Vibe enforcement

- **MUST** verify `APPROVED` feature spec version before backend implementation.
