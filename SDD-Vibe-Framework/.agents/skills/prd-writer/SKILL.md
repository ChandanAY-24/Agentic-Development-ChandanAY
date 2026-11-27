---
name: prd-writer
description: "Draft or update docs/prd.md requirements (REQ-###/NFR-###) derived from docs/product.md capabilities and personas."
---

# Skill: prd-writer

**Purpose:** Author and maintain `docs/prd.md` with unambiguous, testable `REQ-###` and `NFR-###` requirements traced directly to `docs/product.md` capabilities (`CAP-###`) and personas (`PER-##`).

## Trigger

- **MUST** invoke after Phase 1 domain research and pin-point grilling (`requirements-analysis`) reaches `0` `CRITICAL` ambiguities, before authoring feature specs.

## Inputs

- **MUST** read `AGENTS.md`, `docs/product.md`, `docs/domains/`, `docs/decision-log.md`, and `docs/requirements-traceability.md`.

## Workflow

1. **Capability & Persona Traceability:**
   - Map every `REQ-###` to a parent `CAP-###` and target persona `PER-##` in `docs/product.md`.
2. **Non-Goal Boundary Check:**
   - Cross-check proposed requirements against `docs/product.md` explicit non-goals; escalate any conflict to `docs/decision-log.md` before inclusion.
3. **Testable Requirement & NFR Authoring:**
   - Write measurable functional requirements (`REQ-###`) and concrete non-functional requirements (`NFR-###` covering performance, security, accessibility, availability) with objective pass/fail thresholds.
4. **Stakeholder Review & Handoff:**
   - Verify `0` `[ASSUMPTION]` blockers remain, update `docs/requirements-traceability.md`, and obtain developer sign-off before decomposing into `FEAT-###` specs.

## Restrictions

- **MUST NOT** draft `docs/prd.md` while any `CRITICAL` ambiguity from `requirements-analysis` remains unresolved.
- **MUST NOT** invent capabilities or personas absent from `docs/product.md`.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
