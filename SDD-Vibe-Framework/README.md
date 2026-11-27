# SDD-Vibe Framework (1-in-2 Single Workflow)
### Hybrid Sensory Prototyping + Spec-Driven Development (SDD) & TDD with AI Agents

<div align="center">

[![Framework](https://img.shields.io/badge/Framework-1--in--2_Single_Workflow-blue?style=for-the-badge&logo=shield)](.)
[![Methodology](https://img.shields.io/badge/Methodology-Vibe_UI_+_SDD_TDD-indigo?style=for-the-badge)](.)
[![Governance](https://img.shields.io/badge/Governance-Zero_Speculative_Backend-red?style=for-the-badge)](.)
[![In-IDE Dashboard](https://img.shields.io/badge/Dashboard-Port_4200-teal?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](../LICENSE.md)

**Framework Lead:** Chandan Adhikary · **Standard:** Production-Grade Universal Release 2.0.0  
**Target Domains:** SaaS MVPs · Enterprise Core · FinTech · HealthTech · Modern Web Apps · Regulated Systems

[🌟 Framework Overview](#-framework-overview) • [🏛️ Hybrid Pipeline](#️-1-in-2-hybrid-staged-pipeline) • [🤖 Agentic Skill Workflow](#-agentic-team-ecosystem-workflow-first-choice) • [🔄 Traceability Flow](#-spec-to-code-traceability-contract) • [⚡ Quick-Start](#-quick-start-guide) • [🛡️ Slash Commands](#️-collision-free-agent-slash-commands--ca-agent) • [📁 Structure](#-repository-structure--component-map) • [📋 Governance](#-governance-rules--policies)

</div>

---

## 🌟 Framework Overview

**SDD-Vibe** is a unified **1-in-2 Single Workflow Framework** that combines **Vibe-Coding's** frontend-first sensory prototyping and fluid conversational iteration with **Spec-Driven Development (SDD) + Test-Driven Development (TDD)** contract authority, Red-Green-Refactor discipline, and production quality gates.

### The 4 Pillars of SDD-Vibe:
1. **Architecture & Vibe Discovery First:** Synthesize domain knowledge, HLD/LLD (`docs/system-architecture.md`), aesthetic tokens (`docs/design.md`), and living prompts (`docs/plan.md`, `docs/prompts.md`) before generating code.
2. **Frontend-First Sensory Demo:** Build the frontend UI first with `PROTOTYPE` → `DRAFT` living specs, verify interactively via `/run-ca-agent` (`http://localhost:3000`), and tune the experience conversationally until approved.
3. **Formal Spec Lock & Red-Green-Refactor TDD:** Lock feature specs (`IN REVIEW` → `APPROVED` in `docs/spec.md` & `docs/approvals/`), write failing tests against `AC-FEAT###-##` (`RED`), implement minimal backend/persistence/auth/logic (`GREEN`), and refactor cleanly.
4. **Mandatory Development Logging (`logs/` Folder):** Always record clean, sanitized development logs (`logs/dev.log`, `logs/test.log`, `logs/server.log`, `logs/error.log`) inside a dedicated `logs/` directory.

---

## 🏛️ 1-in-2 Hybrid Staged Pipeline

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 44}}}%%
flowchart TB
    classDef gov fill:#0f172a,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc;
    classDef vibe fill:#2e1065,stroke:#c084fc,stroke-width:1.5px,color:#faf5ff;
    classDef red fill:#4c0519,stroke:#fb7185,stroke-width:2px,color:#fff1f2;
    classDef green fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;
    classDef gate fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fffbeb;

    subgraph Row1 ["🎨 STAGE A — DISCOVERY & FRONTEND SENSORY DEMO"]
        direction LR
        subgraph Phase1 ["🏛️ 1. ARCHITECTURE & VIBE DISCOVERY"]
            ProductVision["`**💡 Product & Plan**
CAP-### • docs/plan.md`"]:::gov
            SysArch["`**🏛️ System Architecture**
HLD/LLD • docs/design.md`"]:::gov
            HumanP1{"Design Approved?"}:::gate
        end

        subgraph Phase2 ["🎨 2. FRONTEND SENSORY DEMO"]
            ProtoUI["`**💻 Scaffold UI Shell**
PROTOTYPE → DRAFT • Mock State`"]:::vibe
            LiveDemo["`**🌐 Run /run-ca-agent**
Inspect at :3000 • Tune Vibe`"]:::vibe
            VibeGate{"Sensory UI Approved?"}:::gate
        end
    end

    subgraph Row2 ["🧪 STAGE B — FORMAL SPEC LOCK, TDD & RELEASE"]
        direction LR
        subgraph Phase3 ["🔒 3. SPEC LOCK & TDD CYCLE"]
            LockSpec["`**📋 Lock Feature Spec**
IN REVIEW → APPROVED`"]:::gov
            RedTest["`**🔴 RED: Failing Tests**
/testing-ca-agent`"]:::red
            GreenCode["`**🟢 GREEN: Backend & Auth**
/tdd-ca-agent • /implement`"]:::green
        end

        subgraph Phase4 ["🚀 4. QUALITY AUDIT & SHIP"]
            CodeReview["`**🔍 Review & Verify**
/review & /verify Scorecard`"]:::gov
            SecurityScan["`**🛡️ Security Audit**
/security-audit-ca-agent`"]:::gov
            ReleaseGate{"Release Gate Passed?"}:::gate
            ProductionDeploy(["`**🎉 Production Ship**
/release-check-ca-agent`"]):::green
        end
    end

    ProductVision -->|"Architects"| SysArch
    SysArch -->|"Submits"| HumanP1
    HumanP1 -->|"Revise"| ProductVision
    HumanP1 -->|"Approved"| ProtoUI

    ProtoUI -->|"Launch"| LiveDemo
    LiveDemo -->|"Tune"| VibeGate
    VibeGate -->|"Iterate UI"| ProtoUI
    VibeGate ==>|"UI Signed Off"| LockSpec

    LockSpec -->|"Contract"| RedTest
    RedTest -->|"Minimal Code"| GreenCode
    GreenCode -->|"Verify"| CodeReview

    CodeReview -->|"Pass"| SecurityScan
    SecurityScan -->|"Clean"| ReleaseGate
    ReleaseGate -->|"Authorized"| ProductionDeploy

    style Row1 fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style Row2 fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style Phase1 fill:#0f172a,stroke:#1e293b,stroke-width:1px,color:#cbd5e1
    style Phase2 fill:#1e1b4b,stroke:#312e81,stroke-width:1px,color:#e0e7ff
    style Phase3 fill:#0f172a,stroke:#1e293b,stroke-width:1px,color:#cbd5e1
    style Phase4 fill:#064e3b,stroke:#065f46,stroke-width:1px,color:#d1fae5
```

---

## 🤖 Agentic Team Ecosystem Workflow (First Choice)

> **First-Choice Feature Development:** Whole features are developed through [`.agents/skills/agentic-team-ecosystem/SKILL.md`](.agents/skills/agentic-team-ecosystem/SKILL.md) (`/team-ecosystem-ca-agent`), with **SDD-Vibe's 18 `-ca-agent` slash commands, spec locks, and TDD gates triggering at each step** and **Team 14 (Manual Workflow Guider)** coaching the developer at every gate. *(See `SDD-Vibe-Team-Based-Guide.md` in the root repo for the detailed "When & What to Use" guide for all 14 teams.)*

### Steps 0–9 Execution & Trigger Matrix

| Step | Owning Group / Teams | SDD-Vibe Commands Triggered | External Skills Triggered (Max 1–3/Step, Rank #1 Only) |
|---|---|---|---|
| **0. Intake** | Main Agent + Team 14 | `/team-ecosystem-ca-agent` | `anthropics/skills`, `claude-mem` (Core) |
| **1. Discovery** | Group 1 (Team 2) + Team 12 (+13 Brand) | `/plan-ca-agent` | `grill-me` (Phase-Gate) |
| **2. Architecture** | Group 1 (Team 2) | `/plan-ca-agent` → `/task-ca-agent` | `find-skill` (Phase-Gate), `serena` (Core) |
| **3. Sensory Demo** | Group 2 (Team 3 + Team 4) | `/implement-ca-agent` (UI) → `/run-ca-agent` (`:3000`) | `vercel-labs` / `modern-web-guidance`, `recharts` / `motion-dev` (Domain) |
| **4. Kanban Sync** | Group 1 (Team 1) | `/dashboard-ca-agent` (`#ecosystem` + `/api/kanban-export`) | — |
| **5. Spec Lock & TDD** | Group 2 (Team 4) | `/spec-check-ca-agent` → `/testing-ca-agent` → `/tdd-ca-agent` | `playwright` (Core), `dify` / `openhands` / `REA` (Domain) |
| **6. Audit & QA** | Group 3 (Teams 5, 6, 7, 8) | `/review-ca-agent` → `/verify-ca-agent` → `/security-audit-ca-agent` | `gitleaks` (Core), `semgrep` · `trivy` · `trufflehog` (Phase-Gate) |
| **7. Docs & Brand** | Group 4 (Team 11 + Team 13) | `/handoff-ca-agent` | `ppt-master` (Phase-Gate), `claude-seo` · `postiz-app` (Domain) |
| **8. Deploy Ops** | Group 3 (Team 9) | `/release-check-ca-agent` | — |
| **9. 24×7 Ops** | Group 3 (Team 10) + Teams 12, 13 | `/errorlogs-ca-agent` • `/gitlogs-ca-agent` | — |

### Adding New Custom Features Later & Preset Multi-IDE Chat Tabs
- **New Custom Features (Mid-Project or Post-Launch):** Run `/change-request-ca-agent` if touching an `APPROVED` spec, then invoke `/team-ecosystem-ca-agent` for the new feature so Team 14 guides it through `/plan-ca-agent` → `/task-ca-agent` → `/run-ca-agent` → `/dashboard-ca-agent` → `/spec-check-ca-agent` → `/testing-ca-agent` → `/tdd-ca-agent` → `/review-ca-agent` → `/security-audit-ca-agent`.
- **Preset Multi-IDE Chat Tabs:** Run `python scripts/sync_ide_adapters.py --ides all` (or `python scripts/init_project.py --ides all`) to preset all `17` commands and `18` skills in **Claude Code** (`.claude/`), **Antigravity** (`.agents/workflows/`), **Cursor**, **Windsurf**, **Codex**, and **Copilot**. Use separate chat tabs per Group/Step to keep context windows lean.

---

## 🔄 Spec-to-Code Traceability Contract

Every line of production code traces back to a root business capability:

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef cap fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef req fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;
    classDef feat fill:#172554,stroke:#60a5fa,stroke-width:1.5px,color:#eff6ff;
    classDef ac fill:#312e81,stroke:#a5b4fc,stroke-width:1.5px,color:#e0e7ff;
    classDef test fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;
    classDef code fill:#022c22,stroke:#10b981,stroke-width:2px,color:#d1fae5;

    CAP["`**💡 CAPABILITY**
CAP-001: Student Lifecycle`"]:::cap -->|"Deconstructs to"| REQ["`**📑 REQUIREMENT**
REQ-002: Enrollment Service`"]:::req
    REQ -->|"Specified by"| FEAT["`**📝 FEATURE SPEC**
FEAT-002: Admission Workflow`"]:::feat
    FEAT -->|"Enforces Contract"| AC["`**🧪 ACCEPTANCE CRITERIA**
AC-FEAT002-01: Unique ID Check`"]:::ac
    AC -->|"Verified by"| TEST["`**🔬 AUTOMATED TEST**
TEST-FEAT002-01 (tests/unit/)`"]:::test
    TEST ==>|"Guarantees"| CODE["`**💻 PRODUCTION CODE**
src/modules/students/enroll.ts`"]:::code
```

---

## ⚡ Quick-Start Guide

### Step 1: Scaffolding into Your Project Workspace
Extract or copy the `SDD-Vibe-Framework/` directory into your project root:
```bash
# Rename to your target project name (kebab-case)
mv SDD-Vibe-Framework my-production-app
cd my-production-app
```

### Step 2: Collision-Free Activation (`activate ca agents`) & Slash Commands
After renaming `SDD-Vibe-Framework/` to `my-production-app/` (see `SDD-Vibe-Activation-Guide.md` in the root repo for full details):
1. **In AI Chat (Zero-Friction):** Type **`activate ca agents`** (or `/activate-ca-agent`) — automatically runs `python scripts/init_project.py --ides all`, verifies `logs/` + `check_docs.py` + `manifest.py --check`, and readies all `18` `*-ca-agent` commands. *(Uses `activate ca agents` instead of bare `activate`/`start`/`run` to avoid conflicts with Python `venv`, PowerShell `Start-Process`, and IDE built-ins.)*
2. **In Terminal (Wrapper or `.py`):**
   ```bash
   # Windows (CMD / PowerShell)
   .\activate-ca-agents.bat
   # macOS / Linux
   ./activate-ca-agents
   # Direct Python method (always supported)
   python scripts/init_project.py --ides all
   ```
3. Focus your AI agent chat and type `/`. Confirm all `18` `*-ca-agent` commands appear with descriptions.

### Step 3: Launch In-IDE Project-Manager-Dashboard
Launch the dedicated telemetry dashboard on port `4200`:
- **Slash Command:** Type `/dashboard-ca-agent` in agent chat.
- **Terminal:** Run `Project-Manager-Dashboard/open-in-ide.bat` (Windows) or `bash Project-Manager-Dashboard/open-in-ide.sh` (macOS/Linux).
- **Dock in IDE:** Open `Simple Browser: Show`, navigate to `http://127.0.0.1:4200`, and dock in Editor Group 2.

---

## 🛡️ Collision-Free Agent Slash Commands (`-ca-agent`)

All custom commands carry the `-ca-agent` namespace to guarantee zero collisions with IDE-reserved tokens:

| Command | Category | Operational Purpose |
| :--- | :--- | :--- |
| `/plan-ca-agent` | Planning | Scoped, read-only system design and architectural alignment. |
| `/task-ca-agent` | Planning | Atomic task harness initialization and contract tracking. |
| `/spec-check-ca-agent` | Specs | Validates feature spec compliance against acceptance criteria. |
| `/change-request-ca-agent` | Specs | Formal change request, impact assessment, and spec revision. |
| `/testing-ca-agent` | Execution | Targeted test execution; confirms failing tests in Red phase. |
| `/tdd-ca-agent` | Execution | Red-Green-Refactor implementation satisfying acceptance criteria. |
| `/implement-ca-agent` | Execution | Scope-restricted feature implementation. |
| `/run-ca-agent` | Execution | Local runtime verification (Phase 2 sensory demo & backend runtime). |
| `/review-ca-agent` | Quality | Pre-commit diff, lint, and security review. |
| `/verify-ca-agent` | Quality | Objective scorecard validation against specification contracts. |
| `/security-audit-ca-agent` | Security | SAST, secret leak, and dependency audit across codebase. |
| `/release-check-ca-agent` | Release | Production readiness gate and ship/no-ship decision. |
| `/dashboard-ca-agent` | Dashboard | Launches local In-IDE Project-Manager-Dashboard on port 4200. |
| `/errorlogs-ca-agent` | Diagnostics | Structured runtime error triage and stack trace analysis. |
| `/gitlogs-ca-agent` | Diagnostics | Commit history and git traceability validation against task IDs. |
| `/handoff-ca-agent` | Handoff | Generates verifiable engineering handoff report for team transfer. |
| `/team-ecosystem-ca-agent` | Orchestration | **First-choice** 14-team `agentic-team-ecosystem` orchestrator across Steps 0–9. |

---

## 📁 Repository Structure & Component Map

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef agent fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef doc fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;
    classDef dash fill:#082f49,stroke:#0284c7,stroke-width:2px,color:#f0f9ff;
    classDef test fill:#064e3b,stroke:#34d399,stroke-width:1.5px,color:#ecfdf5;
    classDef log fill:#2e1065,stroke:#c084fc,stroke-width:1.5px,color:#faf5ff;

    subgraph RepoRoot ["🧭 SDD-VIBE-FRAMEWORK /"]
        direction LR
        AGENTS["`**🤖 Agent Master Directives**
AGENTS.md • GEMINI.md • CLAUDE.md`"]:::agent
        AgentsDir["`**🛠️ .agents/ Canonical Asset Store**
17 Commands • 18 Skills • Hooks`"]:::agent
        DocsDir["`**📑 docs/ Living Specs & Architecture**
Plan • Prompts • Spec • ADRs • Approvals`"]:::doc
        DashboardDir["`**🖥️ Project-Manager-Dashboard**
In-IDE Mission Control • Port 4200`"]:::dash
        TestsDir["`**🧪 tests/ Automated Test Harness**
Unit, Integration & E2E Suites`"]:::test
        LogsDir["`**🪵 logs/ Audit Directory**
Structured Runtime Logs • Redacted PII`"]:::log
    end

    style RepoRoot fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
```

---

## 📋 Governance Rules & Policies

- **Guideline Baseline:** Fixed baseline `2.0.0`; modifications require explicit justification and logging in `docs/guideline-CHANGELOG.md`.
- **Feature Lifecycle:** `PROTOTYPE` (Frontend Sensory Demo) → `DRAFT` → `IN REVIEW` → `APPROVED` (Formal Lock for Backend/Auth/Persistence) → `SUPERSEDED` / `DEPRECATED`.
- **Dual Format Policy:**
  - **Flat Format (`docs/features/NNN-name.md`):** Tier 1 (Easy) and Tier 2 (Intermediate) features.
  - **Modular Format (`docs/features/NNN-name/{feature,acceptance,test-plan}.md`):** Tier 3 (Complex / Distributed) features.
- **Traceability Requirement:** All tests must carry `TEST-FEAT###-## / AC-FEAT###-##: <behavior>` in their title.
- **Development Logging:** All command runs and background test suites must write sanitized output to `logs/*.log`.
- **Execution Playbooks (`playbooks/`):** Operational `.txt` runbooks (`01-Setup-Project.txt` through `11-Checklist.txt`) govern setup, implementation, feature specs, auth, MCP, integrations, QA, debugging, validation, error handling, and release checklists.
- **Granular Feature Workflow & External Skills:** Follow [`docs/granular-feature-workflow.md`](docs/granular-feature-workflow.md) for Tier 1–3 feature pacing, and [`07-curated-external-skills-registry.md`](.agents/skills/agentic-team-ecosystem/references/07-curated-external-skills-registry.md) for verified GitHub/official external skills and plugins.
