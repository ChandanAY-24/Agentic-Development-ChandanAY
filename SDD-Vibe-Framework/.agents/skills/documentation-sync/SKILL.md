---
name: documentation-sync
description: "Keep docs consistent: product.md, prd.md, docs/features, spec.md index, traceability matrix, INDEX.md and CHANGELOGs after any change."
---

# Skill: documentation-sync

**Purpose:** Maintain 100% synchronization across living documentation, traceability matrices, registries, and changelogs after any feature, spec, or architectural change.

## Trigger

- **MUST** invoke after any feature spec transition, task completion, architecture decision (`ADR-####`), change request (`CR-###`), or before committing/releasing.

## Inputs

- **MUST** read `AGENTS.md`, `docs/INDEX.md`, `docs/spec.md`, `docs/requirements-traceability.md`, `docs/CHANGELOG.md`, and `docs/guideline-CHANGELOG.md`.

## Workflow

1. **Cross-Reference Traceability Chain:**
   - Verify end-to-end consistency: `docs/product.md` (`CAP-###`) ⇄ `docs/prd.md` (`REQ-###`) ⇄ `docs/features/` (`FEAT-###` / `AC-FEAT###-##`) ⇄ `docs/spec.md` ⇄ `docs/requirements-traceability.md` ⇄ `tests/`.
2. **Orphan & Stale Version Detection:**
   - Identify any `docs/*.md` file missing from `docs/INDEX.md`, any `FEAT-###` missing from `docs/spec.md`, or any stale spec version references in `docs/task.md`.
3. **Changelog & Memory Update:**
   - Record feature/behavior changes in `docs/CHANGELOG.md`, process changes in `docs/guideline-CHANGELOG.md`, and verified state recaps in `docs/memory.md`.
4. **Automated Gate Execution:**
   - Run `python scripts/check_docs.py` and `python scripts/manifest.py --check` and confirm **0 errors** before reporting completion.

## Restrictions

- **MUST NOT** report documentation as synced without running `check_docs.py` and `manifest.py --check` and observing 0 errors.
- **MUST NOT** duplicate canonical definitions across docs (link to the authoritative source instead).
- **MUST NOT** alter controlled guidelines without recorded approved revision.
