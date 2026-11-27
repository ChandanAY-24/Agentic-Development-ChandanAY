# Memory

> **Document class:** Living feature/specification  
> **Framework:** SDD-Vibe  
> **Guideline baseline:** 1.0.0  
> **Status:** Template; project-specific content requires review  

## Purpose

Verified project-state recap, never source of new requirements.

## Agent read trigger

**MUST** read or consult this file: At session start and end; after approvals or incidents.

## Normative sections and rules

### 1. Metadata

- **MUST** — State last update, updater, guideline version and current approved feature baseline.

### 2. Progress

- **MUST** — Record active milestone, tasks, completed work and associated evidence.

### 3. Blockers

- **MUST** — Track unresolved questions, decisions, risks and current owners.

### 4. Next steps

- **MUST** — Distinguish next authorized action from proposed future work.

### 5. Reconciliation

- **MUST** — Re-check source files, approved specs, repository state and CI before relying on memory.

### 6. Confidentiality

- **MUST** — Do not store credentials, tokens or unnecessary personal data.

### 7. Compactness

- **SHOULD** — Link to canonical documents instead of duplicating policy or entire specs.

### 8. Staleness

- **MUST** — Remove or correct entries that are older than the current phase or contradicted by source documents; do not append contradictory notes.

### 9. Session handoff

- **MUST** — End every agent session by updating the next authorized action, open questions and evidence links.

### 10. Scoped Project Memory for Related Agents

- **MUST** — Partition shared project memory into **Global Verified State** plus **Related-Agent Memory Lanes** so sub-agents and specialized teams read/write only their relevant lane without polluting unrelated context windows.
- **MUST** — Include a `source:` file/commit link and `DD-MM-YYYY` date on every lane entry, and prune stale entries when a feature reaches `APPROVED` or a phase closes.

## Instantiation template

Copy into the project instantiation (below this section or into a dedicated file) and replace every placeholder. Keep IDs from `docs/requirements-traceability.md`.

```markdown
### Global Verified State
| Field | Value |
|---|---|
| Last reconciled | DD-MM-YYYY by [agent/person] against commit [SHA] |
| Current phase | Phase N (docs/phases.md) |
| Active task | TASK-### for FEAT-### (version) |
| Next authorized action | [Exact next approved step] |

### Related-Agent Memory Lanes (Read/Write Scoped by Role)

#### 1. Architecture & Domain Lane (Team 2, `/plan-ca-agent`, `architecture-review`)
- [Verified HLD/LLD invariant or domain rule] — source: [docs/system-architecture.md or ADR-####] (DD-MM-YYYY)

#### 2. UI/UX & Sensory Demo Lane (Team 3, `ui-fidelity-review`, `accessibility-auditor`)
- [Design token, layout decision, or `:3000` sensory sign-off] — source: [docs/design.md or docs/plan.md] (DD-MM-YYYY)

#### 3. Implementation & TDD Lane (Team 4, `/tdd-ca-agent`, `/implement-ca-agent`, `tdd-enforcer`)
- [Active `AC-FEAT###-##` test state or API/DB contract note] — source: [docs/features/NNN-name.md] (DD-MM-YYYY)

#### 4. Security, QA & Error Triage Lane (Team 5/6/7/8, `security-auditor`, `/errorlogs-ca-agent`)
- [Open finding, bot-probe signature, or `ERR-###` do-not-repeat lesson] — source: [docs/error-tracker.md or logs/] (DD-MM-YYYY)

#### 5. Ops, Release & GEO/Growth Lane (Team 9/10/11/13, `release-validator`)
- [Deployment target, `llms.txt`/GEO endpoint, or store publishing state] — source: [docs/deployment.md] (DD-MM-YYYY)

### Open questions / assumptions
- [Question] — owner: [Name] — raised: DD-MM-YYYY
```

## Evidence and change control

- **MUST** record owner, revision/date, relevant approval reference, and traceable evidence in the applicable project instantiation.
- **MUST** route changes to process rules through `docs/guideline-CHANGELOG.md` and formal baseline revision; route feature behavior through approved versioned specs and `docs/CHANGELOG.md`.
- **SHOULD** keep links to canonical artifacts instead of duplicating definitions.

## SDD-Vibe enforcement

- **MUST** reconcile memory against `docs/spec.md` and feature headers at the start of every session; on conflict the feature file wins.
- **MUST NOT** record new requirements here; route them to a CR.
