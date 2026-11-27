---
name: requirements-analysis
description: "Analyze requests against docs/product.md boundaries and docs/prd.md; identify gaps, conflicts and missing acceptance criteria."
---

# Skill: requirements-analysis

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](../../../docs/diagrams/3d-sdd-vibe-pipeline.svg)

**Purpose:** Enforce accurate pre-start domain research, pin-point developer grilling, and zero-ambiguity requirements analysis before any architecture, PRD, prototype, or feature spec is written.

## Trigger

- **MUST** use at Phase 1 / Step 1 (or `/plan-ca-agent`) before creating `docs/prd.md`, `docs/system-architecture.md`, or any `FEAT-###` spec, and whenever requirements contain unverified assumptions.

## Inputs

- **MUST** read `AGENTS.md`, `docs/product.md`, `docs/domains/README.md`, relevant `docs/` policy, and any existing `docs/domains/<domain>.md`.

## Workflow

1. **MUST** separate facts from guesses: tag every domain rule, API capability, compliance requirement, or benchmark as `[VERIFIED: <source/file>]` or `[ASSUMPTION — NEEDS CONFIRMATION]`.
2. **MUST** conduct **Accurate Domain & Market Research** before proposing solutions:
   - Identify industry vocabulary, business rules, regulatory/compliance standards (e.g., PCI-DSS, HIPAA, GDPR, SOC2, WCAG, OWASP), and technical/latency/cost constraints.
   - Persist verified domain rules into `docs/domains/<domain>.md` (following `docs/domains/README.md`) when base guidelines are insufficient.
3. **MUST** execute **Adaptive Pin-Point Developer Grilling** until `0` `CRITICAL` ambiguities remain:
   - **1-question-at-a-time** when a single critical architectural/security/scope fork blocks downstream decisions.
   - **Focused batch (3–5 pin-point questions)** when gathering independent baseline parameters across: *(a) Target Personas & Problem, (b) Core Flows & Edge Cases, (c) Scale / Latency / Cost Budget, (d) Data Isolation, Auth & Compliance, (e) Failure Modes & Rollback, (f) Explicit Non-Goals*.
4. **MUST** flag conflicts, incomplete acceptance criteria, unverified assumptions, or high-risk side effects transparently to the developer (never silently assume or work around).
5. **MUST** output a **Domain & Ambiguity Scorecard** (`Verified Facts`, `Open Assumptions`, `Blocking Status`, `Evidence Links`, and `Next Approved Step`).

## Restrictions

- **MUST NOT** generate `docs/prd.md`, `docs/system-architecture.md`, or `FEAT-###` specs while any `CRITICAL` ambiguity or unconfirmed `[ASSUMPTION]` remains.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
- **MUST NOT** implement feature behavior absent from the approved spec.
- **SHOULD** maintain repeatable examples/evaluations before promoting this skill to automated use.