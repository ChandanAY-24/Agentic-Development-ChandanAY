---
name: tdd-enforcer
description: "Enforce red-green-refactor: failing tests mapped to AC-FEAT IDs before production code, with recorded evidence."
---

# Skill: tdd-enforcer

**Purpose:** Enforce strict Red-Green-Refactor test-driven development, ensuring failing automated tests mapped to `AC-FEAT###-##` exist and fail for the expected reason before any production backend, persistence, or business logic is written.

## Trigger

- **MUST** invoke during Phase 3 (`/tdd-ca-agent`, `/testing-ca-agent`, `/implement-ca-agent`) and before modifying or creating any production source file under `src/`, `api/`, or `services/`.

## Inputs

- **MUST** read `AGENTS.md`, `docs/code-testing.md`, `docs/requirements-traceability.md`, the `APPROVED` feature spec in `docs/features/`, and the active `TASK-###` in `docs/task.md`.

## Workflow

1. **Gate Check — Spec & Test-First Verification:**
   - Confirm the target `FEAT-###` spec has `Status: APPROVED` and a valid `Approval reference` in `docs/approvals/`.
   - Verify no production code changes exist for the target `AC-FEAT###-##` prior to test creation (`git diff --name-only`).
2. **RED Phase — Failing Test Authoring & Execution:**
   - Require each test title to explicitly declare `TEST-FEAT###-## / AC-FEAT###-##`.
   - Run the test runner (`npm test` / `pytest` / `node scripts/run-tests.js`) and pipe output to `logs/test.log`.
   - Confirm the new test fails due to missing/unimplemented behavior (not syntax or import errors) and record the failing evidence.
3. **GREEN Phase — Minimal Implementation:**
   - Implement the smallest possible production code change within `Allowed files` to turn the failing tests green.
   - Re-run the targeted suite and full regression suite; verify 0 skipped/relaxed assertions.
4. **REFACTOR Phase — Clean & Verify:**
   - Remove duplication, enforce shallow nesting and clear naming without altering behavior.
   - Re-run tests and coverage check; update `docs/requirements-traceability.md` and `docs/task.md` with observed pass counts.

## Restrictions

- **MUST NOT** write production implementation code before a failing test mapped to `AC-FEAT###-##` is observed.
- **MUST NOT** weaken, skip, or mock out assertions to make a failing test pass.
- **MUST NOT** alter controlled guidelines or `APPROVED` specs without `/change-request-ca-agent`.
