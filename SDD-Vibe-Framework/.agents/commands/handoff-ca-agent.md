---
description: "Summarize verified state, docs, test evidence, blockers and next authorized tasks."
argument-hint: "[recipient and scope]"
---

# /handoff-ca-agent

<!-- SDD-VIBE-3D-DIAGRAM -->
![SDD-Vibe 1-in-2 Single Workflow 3D Stack](../../docs/diagrams/3d-sdd-vibe-pipeline.svg)

**Purpose:** Summarize verified state, docs, test evidence, blockers and next authorized tasks.

## When to run

**MUST** invoke only for a task whose intent and permissions match this command.

## Inputs

- **MUST** capture task ID, goal, guideline baseline, applicable approved spec/version, acceptance IDs and allowed files.
- **MUST** identify required tools and human approval for destructive, external or production effects.

## Procedure

1. **MUST** read `AGENTS.md`, `docs/memory.md`, and the relevant `docs/` source of truth.
2. **MUST** inspect existing artifacts and identify missing approvals or conflicts.
3. **MUST** perform only the approved operation: Summarize verified state, docs, test evidence, blockers and next authorized tasks.
4. **MUST** update `docs/memory.md` (Global Verified State and relevant Related-Agent Memory Lane with a compact Memory Delta) and `docs/handoff.md`.
5. **MUST** run applicable objective checks; never invent execution results.
6. **MUST** report changed files, actual results, deviations and next authorized action.

## Stop conditions

**MUST** stop on an unauthorized feature, baseline conflict, credential exposure, failed blocking gate, or missing approval.