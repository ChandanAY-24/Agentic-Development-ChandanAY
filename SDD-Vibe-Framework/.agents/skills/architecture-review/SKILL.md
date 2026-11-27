---
name: architecture-review
description: "Review designs against docs/system-architecture.md and accepted ADRs; use when a task changes boundaries, components or dependencies."
---

# Skill: architecture-review

**Purpose:** Validate HLD/LLD designs and code changes against `docs/system-architecture.md` and `docs/adrs/` to preserve Clean Architecture boundaries, modularity, and scalability.

## Trigger

- **MUST** invoke during Phase 1 (`/plan-ca-agent`) and whenever a task introduces new modules, external dependencies, cross-layer imports, or infrastructure changes.

## Inputs

- **MUST** read `AGENTS.md`, `docs/system-architecture.md`, `docs/tech-stacks.md`, and relevant records in `docs/adrs/`.

## Workflow

1. **Clean Architecture & Dependency Direction Audit:**
   - Verify dependencies point inward (Presentation → Application → Domain; Infrastructure implements Domain/Application interfaces). Flag domain logic leaking into controllers or UI.
2. **ADR & Tech Stack Conformance:**
   - Confirm new libraries, datastores, or patterns align with `docs/tech-stacks.md` and accepted `ADR-####` records; require a new ADR for material architectural shifts.
3. **Coupling, Cohesion & Single Responsibility:**
   - Identify god modules, circular dependencies, or tight coupling between bounded contexts.
4. **Scalability & Resilience Check:**
   - Verify statelessness, caching boundaries, circuit breakers/timeouts for external calls, and async queuing for heavy/long-running tasks.
5. **Verdict & ADR Action:**
   - Report boundary violations, trade-offs, and required `ADR-####` updates before implementation proceeds.

## Restrictions

- **MUST NOT** approve circular dependencies or direct database access from presentation/UI layers.
- **MUST NOT** introduce unapproved third-party dependencies without updating `docs/dependencies.md` and `docs/tech-stacks.md`.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
