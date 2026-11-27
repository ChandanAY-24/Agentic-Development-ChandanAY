---
name: task-planner
description: "Break an approved feature version into TASK-### entries in docs/task.md with file ownership, tests and Definition of Done."
---

# Skill: task-planner

**Purpose:** Decompose a `FEAT-###` specification into atomic, reviewable `TASK-###` units in `docs/task.md` with explicit file ownership, dependency ordering, effort sizing, and Definition of Done.

## Trigger

- **MUST** invoke via `/task-ca-agent` or after Phase 1/3 spec approval before any implementation work begins.

## Inputs

- **MUST** read `AGENTS.md`, `docs/task.md`, `docs/phases.md`, `docs/system-architecture.md`, and the target feature spec in `docs/features/`.

## Workflow

1. **Feature Decomposition:**
   - Map every `FR-FEAT###-##`, `NFR-FEAT###-##`, and `AC-FEAT###-##` in the feature spec to one or more atomic `TASK-###` items sized for a single reviewable PR.
2. **Ownership, Dependencies & Sizing:**
   - Assign `Allowed files` (strict path boundaries), priority (`P0`–`P3`), T-shirt effort (`S` / `M` / `L`), and explicit prerequisite `TASK-###` dependencies.
   - Ensure no two concurrent tasks own overlapping files without a declared dependency.
3. **Definition of Done & TDD Checklist:**
   - Populate each `TASK-###` block with failing test step (`TEST-FEAT###-##`), minimal implementation step, and verification gate (`check_docs.py` + test suite).
4. **Document Update:**
   - Write the structured `TASK-###` entries into `docs/task.md` (status `READY` or `BACKLOG`) and verify `DashboardParser.parseTasks()` parses them cleanly.

## Restrictions

- **MUST NOT** create tasks for unapproved scope or features absent from `docs/spec.md`.
- **MUST NOT** mark a task `READY` if its prerequisite dependencies are incomplete or its `AC-FEAT###-##` links are missing.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
