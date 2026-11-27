---
name: code-reviewer
description: "Review diffs for scope fidelity to the approved feature version, tests, security and maintainability per docs/code-review.md."
---

# Skill: code-reviewer

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](../../../docs/diagrams/3d-sdd-vibe-pipeline.svg)

**Purpose:** Perform a deterministic pre-commit/pre-merge diff audit verifying scope fidelity, architectural boundaries, test coverage, secret hygiene, and maintainability against `docs/code-review.md`.

## Trigger

- **MUST** invoke via `/review-ca-agent`, before committing changes, or prior to transitioning any `TASK-###` to `DONE`.

## Inputs

- **MUST** read `AGENTS.md`, `docs/code-review.md`, the active `TASK-###` (`Allowed files`), and the `APPROVED` feature spec in `docs/features/`.
- **MUST** inspect `git diff` and `git status` across the working tree and staged changes.

## Workflow

1. **Diff Scope & Boundary Audit:**
   - Compare `git diff --name-only` against `Allowed files` in `docs/task.md`. Flag any out-of-scope edits or unapproved refactors.
   - Verify no `APPROVED` spec or protected policy (`AGENTS.md`, `docs/constitution.md`) was modified without a `CR-###`.
2. **Correctness, Coupling & Maintainability Check:**
   - Inspect changed functions for single-responsibility, shallow nesting, early returns, and absence of duplicated logic.
   - Verify error handling is explicit (no swallowed exceptions or silent fallbacks) and naming follows repository conventions.
3. **Test & AC Traceability Verification:**
   - Confirm every new/changed behavior has corresponding `TEST-FEAT###-##` coverage and real pass output in `logs/test.log`.
4. **Secret & Hygiene Scan:**
   - Scan diffs for hardcoded API keys, tokens, passwords, PII, or leftover debug statements (`console.log`, `print`).
5. **Verdict Output:**
   - Emit structured findings grouped by severity (`BLOCKER`, `MAJOR`, `MINOR`), evidence file/line links, and an explicit `APPROVE` or `REQUEST_CHANGES` decision.

## Restrictions

- **MUST NOT** approve changes that lack test evidence or touch files outside authorized `TASK-###` scope.
- **MUST NOT** invent review checks or report files as inspected without reading the actual diff.
- **MUST NOT** alter controlled guidelines without recorded approved revision.