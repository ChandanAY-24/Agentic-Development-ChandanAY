---
name: debugging-analyst
description: "Diagnose failures from real logs and tests, link findings to docs/error-tracker.md and propose regression tests mapped to ACs."
---

# Skill: debugging-analyst

**Purpose:** Perform structured root-cause analysis from real logs and failing tests, classify defects, scaffold failing regression tests, and record findings in `docs/error-tracker.md`.

## Trigger

- **MUST** invoke via `/errorlogs-ca-agent` or whenever encountering unexpected test failures, runtime exceptions, or regression reports.

## Inputs

- **MUST** read `AGENTS.md`, `docs/error-tracker.md`, `logs/error.log`, `logs/test.log`, `logs/server.log`, and the relevant feature spec in `docs/features/`.

## Workflow

1. **Log & Stack Trace Extraction:**
   - Inspect `logs/*.log` (redact any PII/secrets if discovered) and extract the exact failing command, stack trace, timestamp, and impacted file/line.
2. **Reproduction & 5-Whys Root Cause Analysis:**
   - Reproduce the failure deterministically. Trace from symptom to underlying root cause (avoiding surface-level patches).
   - Identify the violated `AC-FEAT###-##` or declare a formal `SPEC-GAP`.
3. **Severity Classification & Tracker Entry:**
   - Classify severity (`P0` Critical, `P1` High, `P2` Medium, `P3` Low) per `docs/error-tracker.md`.
   - Log a new `ERR-###` row in `docs/error-tracker.md` with date (`DD-MM-YYYY`), impacted path, root cause, and status `ACTIVE`.
4. **Regression Test Scaffolding (RED → GREEN):**
   - Author a failing regression test reproducing the defect before applying the minimal fix.
   - Verify the fix turns the regression test and full suite green, then update `ERR-###` to `RESOLVED` with commit/test evidence.

## Restrictions

- **MUST NOT** close an `ERR-###` entry without an automated regression test passing.
- **MUST NOT** guess root causes or fabricate log lines not observed in `logs/` or test output.
- **MUST NOT** expose raw secrets or PII when quoting logs into `docs/error-tracker.md`.
