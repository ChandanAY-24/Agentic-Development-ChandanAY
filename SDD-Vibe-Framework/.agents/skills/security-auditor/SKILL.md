---
name: security-auditor
description: "Audit code, configuration and dependencies against docs/security.md; record findings with severity and remediation."
---

# Skill: security-auditor

**Purpose:** Apply the controlled security auditor workflow to a clearly scoped project task.

## Trigger

- **MUST** use only when current task requires this capability.
## Inputs

- **MUST** read `AGENTS.md`, relevant `docs/` policy, current approved feature/spec and task.
## Workflow

1. **MUST** state assumptions, required facts, authorization and intended output.
2. **MUST** inspect authoritative source and project-specific constraints.
3. **MUST** execute domain checks without inventing facts, specs or test evidence, including concrete pre-launch checks from `agentic-team-ecosystem/references/08-production-security-geo-checklist.md` when applicable:
   - Secret & git-history leak scan + `logs/*.log` PII redaction check.
   - Admin 2FA/MFA enforcement, recovery-code rotation, and session invalidation edge cases.
   - File upload safety (reject deceptive double extensions like `.jpg.exe`, validate magic bytes, enforce size/storage isolation).
   - Payment webhook cryptographic signature verification and idempotency key enforcement.
4. **MUST** flag conflicts, incomplete acceptance criteria or high-risk side effects.
5. **MUST** produce findings, evidence links, blocking status and next approved step.
## Restrictions

- **MUST** not alter controlled guidelines without recorded approved revision.
- **MUST** not implement feature behavior absent from the approved spec.
- **SHOULD** maintain repeatable examples/evaluations before promoting this skill to automated use.
