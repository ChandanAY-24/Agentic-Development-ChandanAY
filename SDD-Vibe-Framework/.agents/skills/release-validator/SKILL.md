---
name: release-validator
description: "Validate release readiness against docs/release-checklist.md, the traceability matrix and approved feature versions."
---

# Skill: release-validator

**Purpose:** Apply the controlled release validator workflow to a clearly scoped project task.

## Trigger

- **MUST** use only when current task requires this capability.
## Inputs

- **MUST** read `AGENTS.md`, relevant `docs/` policy, current approved feature/spec and task.
## Workflow

1. **MUST** state assumptions, required facts, authorization and intended output.
2. **MUST** inspect authoritative source and project-specific constraints.
3. **MUST** execute domain checks without inventing facts, specs or test evidence, including domain-gated readiness checks from `agentic-team-ecosystem/references/08-production-security-geo-checklist.md` when applicable:
   - **Web / SaaS releases:** Verify pre-launch production checks, `robots.txt` / `sitemap.xml`, and optional GEO/AI-discoverability (`llms.txt`, JSON-LD).
   - **Mobile releases:** Verify signed build artifact, closed-testing readiness, Data Safety vs. SDK permission parity, and reviewer demo credentials.
4. **MUST** flag conflicts, incomplete acceptance criteria or high-risk side effects.
5. **MUST** produce findings, evidence links, blocking status and next approved step.
## Restrictions

- **MUST** not alter controlled guidelines without recorded approved revision.
- **MUST** not implement feature behavior absent from the approved spec.
- **SHOULD** maintain repeatable examples/evaluations before promoting this skill to automated use.
