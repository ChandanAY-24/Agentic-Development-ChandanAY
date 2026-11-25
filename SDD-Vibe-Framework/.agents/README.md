# `.agents/` — Portable Autonomous Agent Assets & Engine
### Unified Cross-IDE Capability Layer for SDD-Vibe (1-in-2 Single Workflow)

<div align="center">

[![Agent Layer](https://img.shields.io/badge/Agent_Engine-Canonical_Source_of_Truth-blue?style=for-the-badge&logo=probot)](.)
[![Commands](https://img.shields.io/badge/Commands-17_Collision--Free_(ca--agent)-indigo?style=for-the-badge)](commands/README.md)
[![Skills](https://img.shields.io/badge/Skills-19_Deterministic_Playbooks-teal?style=for-the-badge)](skills/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](../LICENSE.md)

**Framework Track:** Spec-Driven Development · **Standard:** Cross-IDE Portability Release 2.0.0  
**Supported Hosts:** Claude Code · Cursor · Windsurf · Antigravity · OpenCode · Codex · VS Code

[🌟 Purpose](#-purpose) • [🏛️ Architecture](#️-agent-asset-architecture) • [🔄 Discovery Pipeline](#-multi-ide-discovery--dispatch-pipeline) • [🛡️ Collision Prevention](#️-collision-prevention-policy) • [📦 Activation](#-active-agent-activation)

</div>

---

## 🌟 Purpose

The `.agents/` directory is the single cross-IDE canonical source of truth for autonomous AI coding agents operating within this framework. It houses deterministic commands, executable skills, runtime lifecycle hooks, and reporting templates that function uniformly across all major AI code editors without vendor lock-in.

---

## 🏛️ Agent Asset Architecture

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef asset fill:#0f172a,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc;
    classDef ide fill:#1e293b,stroke:#818cf8,stroke-width:1.5px,color:#f8fafc;

    subgraph AgentsRoot ["🛠️ .agents/ CANONICAL ASSET STORE"]
        direction TB
        Commands["`**⚡ commands/ Catalog**
17 Collision-Free *-ca-agent.md Commands`"]:::asset
        Skills["`**📚 skills/ Playbooks**
18 Reusable Skills & Ecosystem Playbooks`"]:::asset
        Hooks["`**🪝 hooks/ & hooks.json**
SessionStart, PreToolUse, PostToolUse`"]:::asset
        Templates["`**📑 templates/ Contracts**
Standardized Task & Completion Reports`"]:::asset
    end

    subgraph HostIDEs ["🖥️ SUPPORTED AI CODING HOST IDES"]
        direction TB
        IDE1(["`**Claude Code**
Anthropic CLI`"]):::ide
        IDE2(["`**Cursor / Windsurf**
VS Code Forks`"]):::ide
        IDE3(["`**Antigravity**
Native Engine`"]):::ide
        IDE4(["`**OpenCode / VS Code**
AI Extensions`"]):::ide
    end

    AgentsRoot ==>|"Walk-Up Directory Discovery"| HostIDEs

    style AgentsRoot fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style HostIDEs fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
```

---

## 🔄 Multi-IDE Discovery & Dispatch Pipeline

All supported IDEs discover `.agents/` by walking up the directory tree to the workspace root:

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef root fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef disc fill:#172554,stroke:#60a5fa,stroke-width:1.5px,color:#eff6ff;
    classDef ui fill:#064e3b,stroke:#34d399,stroke-width:2px,color:#ecfdf5;

    WorkspaceRoot[("`**📁 Workspace / Git Root**
.agents/ Asset Store Located`")]:::root -->|"Discovers"| DiscoverCommands["`**⚡ Parse Commands**
commands/*.md -> /<name>-ca-agent`"]:::disc
    WorkspaceRoot -->|"Discovers"| DiscoverSkills["`**📚 Load Skills**
skills/*/SKILL.md Playbooks`"]:::disc
    WorkspaceRoot -->|"Discovers"| DiscoverHooks["`**🪝 Bind Lifecycle Hooks**
hooks.json -> scripts/hooks/*.py`"]:::disc

    DiscoverCommands ==>|"Registers in Chat UI"| IDEPalette["`**💬 AI Chat Palette Autocomplete**
Typing '/' Displays All 17 Commands`"]:::ui
```

---

## 📁 Directory Structure

| Subdirectory / File | Purpose & Operational Contract |
| :--- | :--- |
| `commands/` | 17 canonical, collision-free agent commands named `<name>-ca-agent.md` (see [`commands/README.md`](commands/README.md)). |
| `workflows/` | Antigravity-native slash-command mirrors (`<name>-ca-agent.md`) synced from `commands/` so `/<name>-ca-agent` appears in the `/` dropdown. |
| `skills/` | 18 domain-specific capability playbooks, each `skills/<name>/SKILL.md` with standardized `name`/`description` frontmatter. |
| `hooks.json` | Executable Antigravity lifecycle hooks (`SessionStart`, `PreToolUse`, `PostToolUse`) backed by `scripts/hooks/*.py`. |
| `hooks/` | Lifecycle hook execution contracts and security matrices ([`hooks/HOOK-MATRIX.md`](hooks/HOOK-MATRIX.md)). |
| `templates/` | Standardized reporting artifacts (`AGENT-TASK-CONTRACT.md`, `AGENT-COMPLETION-REPORT.md`). |

---

## 🛡️ Collision Prevention Policy

> [!CRITICAL]
> Assets within `.agents/` (commands, skills, hooks, templates) **MUST NOT** use generic names or identifiers (such as `/run`, `/plan`, `/test` or `/review`) that overlap or shadow native features of host coding IDEs.

1. **Explicit Namespace:** Commands **MUST** use the `-ca-agent` suffix (e.g. `/plan-ca-agent`, `/run-ca-agent`, `/tdd-ca-agent`).
2. **Deterministic Skills:** Skills **MUST** reside in explicit subdirectories with a standardized `SKILL.md` definition whose `name` matches the directory.
3. **Execution Bounding:** Hooks **MUST** declare execution criteria, timeouts, and fallbacks in `hooks/HOOK-MATRIX.md`.

---

## 📦 Active Agent Activation

When copying this framework into another project:
1. Place `.agents/` (and `AGENTS.md`, `docs/`, `scripts/`) at the **workspace/git root**.
2. Run `python scripts/init_project.py --ides antigravity` (or `--ides all` / `--ides claude,cursor,windsurf,copilot`) to sync native adapters.
3. Verify that typing `/` in your chat palette displays all 17 custom `-ca-agent` commands (with `/team-ecosystem-ca-agent` as the first-choice orchestrator for `skills/agentic-team-ecosystem/`).
