# SDD-Vibe External Skills Reference & Team Ownership Guide
### Complete Parameter Matrix, Rank #1 Critical Selection, Multi-Use Tiers & 14-Team Mapping

<!-- SDD-VIBE-3D-DIAGRAM -->
![14-Team Agentic Ecosystem 3D Topology](docs/diagrams/3d-agentic-ecosystem.svg)

<div align="center">

[![Policy](https://img.shields.io/badge/Policy-Developer's_Choice_(Opt--In)-blue?style=for-the-badge)](SDD-Vibe-Framework/docs/skills.md)
[![Selection](https://img.shields.io/badge/Default_Criteria-Rank_%231_Only-indigo?style=for-the-badge)](.)
[![Teams](https://img.shields.io/badge/Mapping-14_Agentic_Teams-teal?style=for-the-badge)](SDD-Vibe-Team-Based-Guide.md)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE.md)

**Engineering Lead:** Chandan Adhikary · **Release:** SDD-Vibe 2.0.0 Universal  
**Canonical Registry:** [07-curated-external-skills-registry.md](SDD-Vibe-Framework/.agents/skills/agentic-team-ecosystem/references/07-curated-external-skills-registry.md) · **Policy:** [docs/skills.md](SDD-Vibe-Framework/docs/skills.md)

</div>

---

## 1. Selection Criteria & Developer-Suggestion Protocol

All external skills in SDD-Vibe are **100% optional (Developer's Choice)**—never pre-bundled, never loaded randomly, and never installed from unverified forks. Every external skill is evaluated across **all 6 operational parameters** before an agent uses or suggests it:

| Parameter | How It Works in SDD-Vibe | Critical Rule |
| :--- | :--- | :--- |
| **1. Rank (`#1` Critical)** | Ordered within each sub-category by **Trust Tier → Cross-Harness Portability → Token Efficiency**. | **Always pick Rank `#1` by default.** Only fall back to `#2`/`#3` if `#1` lacks a required capability. Never load two overlapping skills in the same sub-category. |
| **2. Trust Tier** | `Tier 1` (Official vendor org), `Tier 2` (Established OSS), `Tier 3` (Community), `Reference` (Read-only). | **Tier 3** skills require the **5-Point Security Vetting Checklist** + sandbox dry-run before use. |
| **3. Multiple-Times Use** | `Every-Project Core` (reused across multiple projects & steps), `Phase-Gate` (at specific gates), `Domain-Intuition` (only when domain demands it). | Prioritize **Every-Project Core** skills for repeatable ROI; keep `Domain-Intuition` skills dormant until needed. |
| **4. Developer's Choice** | External skills are never forced or hardcoded into `.agents/`. | Core `.agents/skills/` + `*-ca-agent` commands always run first; external skills are strictly opt-in. |
| **5. Suggest to Developer/User** | **Mode 1:** Auto-Active (stack-native). **Mode 2:** Suggest **at most 1 Rank `#1`** skill at a matching gate and wait for `"yes"`. **Mode 3:** **Never auto-suggest**; developer-instructed only. | Always emit the **Transparent Skill Disclosure** before enabling:<br>`Skill: <name> \| Ecosystem: <Core/Antigravity/Vercel/Claude/GitHub> \| Why Now: <phase & feature> \| Mode: <Mode 1 / Mode 2 (awaiting "yes") / Mode 3>` |
| **6. Belongs To (Team)** | Maps each skill to its owning Team(s) in the **4-Group / 14-Team** `agentic-team-ecosystem`. | Only the owning Team activates or suggests its mapped external skills at its designated SDLC step. |

### 5-Point Security Vetting Checklist (Before Installing Any External Skill)
1. **Verified Source:** Confirm official GitHub org / npm / vendor publisher (never unverified forks).
2. **Script & Prompt Inspection:** Read `SKILL.md`, `scripts/`, and hooks before execution.
3. **Least-Privilege Scope:** Run in sandboxed / least-privilege mode; never expose production secrets.
4. **No Spec Override:** External skills **MUST NOT** modify `APPROVED` specs or `docs/approvals/`.
5. **Clean Removal:** Revoke any granted tokens and clear cached data if uninstalled.

---

## 2. Rank #1 Critical Skills & Multi-Use Quick Table

Use this quick-reference table to see every **Rank `#1`** default external skill, its **Tag** (`Skill`, `Plugin`, `MCP`), **GitHub Stars** *(late-2026 snapshot)*, whether it qualifies for **Multiple-Times Use**, how it is **suggested to the developer/user**, and which **Team** owns it:

| Category | Rank | Tag | Rank #1 Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team) | Primary Working Role |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **A. Baseline Workflow** | **#1** | `Skill` | `anthropics/skills` | ~201.8k | Tier 1 | **Yes** (`Every-Project Core`) | **Mode 1/2** — Auto-active baseline or suggest at Step 0 | **Teams 2, 4, 14** | Official cross-IDE baseline skill patterns |
| **A. Grilling & Scoping** | **#1** | `Skill` | `grill-me` | Community | Tier 3 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest 1 at Step 1 if deep grilling needed | **Team 2, Team 14** | Relentless requirement & design-decision grilling |
| **A. Claude Code Setup** | **#1** | `Plugin` | `claude-code-setup` (`anthropics/claude-plugins-official`) | Official Dir | Tier 1 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest at Step 0 for Claude Code setups | **Teams 2, 14** | Analyzes codebase to recommend hooks, skills & MCPs |
| **A. Skill Discovery** | **#1** | `CLI / Skill` | `vercel-labs/skills` (`skills.sh`) / `find-skill` | ~40.6k | Tier 1/3 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest at Step 2 when specialized skill needed | **Team 2** | Discovers & installs Agent Skills (`npx skills add`) |
| **A. Visual Plan Review** | **#1** | `Plugin / Skill` | `plannotator` (`backnotprop/plannotator`) | ~14.1k–15.4k | Tier 2 | **Yes** (Steps 2 & 6) | **Mode 2** — Suggest at Step 2 & Step 6 review gates | **Teams 1, 2, 7** | Local-first visual plan, spec & diff annotation UI |
| **A. Architecture Diagrams** | **#1** | `Skill` | `diagram-design` (`cathrynlavery/diagram-design`) | ~73.7k | Tier 3 | **Yes** (Steps 2 & 7) | **Mode 2** — Suggest when editorial HTML+SVG diagrams needed | **Team 2, Team 11** | 52+ editorial HTML+SVG diagrams (HLD/LLD/ER/UML) |
| **A. Agent Control Plane** | **#1** | `Platform / Plugin` | `paperclip` (`paperclipai/paperclip`) | ~117.6k | Tier 2 | Domain (`Domain-Intuition`) | **Mode 3** — Developer-instructed multi-agent org/budget plane | **Teams 1, 14** | Virtual org charts, BYOA adapters, token budgets & approvals |
| **B. Persistent Memory** | **#1** | `Plugin / MCP` | `claude-mem` *(Cross-Harness)* | ~120k | Tier 3 | **Yes** (`Every-Project Core`) | **Mode 2** — Suggest on large multi-session repos | **Teams 2, 4, 14** | Persistent cross-session memory paired with `docs/memory.md` |
| **B. Code Intelligence** | **#1** | `MCP` | `serena` (`oraios/serena`) | ~31.8k | Tier 2 | **Yes** (`Every-Project Core`) | **Mode 2** — Suggest on large multi-module codebases | **Team 2, Team 4** | Semantic symbol-level code retrieval & editing |
| **B. Live Library Docs** | **#1** | `MCP` | `Context7` (`upstash/context7`) | ~65.6k | Tier 1 | **Yes** (`Every-Project Core`) | **Mode 2** — Suggest for live version-specific API/SDK docs | **Team 2, Team 4** | Live library doc lookup (`resolve-library-id`, `query-docs`) |
| **B. Reverse Engineering** | **#1** | `Skill` | `REA` *(Reverse Engineering Anything)* | Community | Tier 3 | Domain (`Domain-Intuition`) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 2 (REA)** | Reverse-engineers legacy apps, APIs, or binaries |
| **B. AI Agent Pipelines** | **#1** | `Platform / Skill` | `dify` / `openhands` | ~162k / ~94.5k | Tier 2 | Domain (`Domain-Intuition`) | **Mode 2/3** — Suggest only on AI/LLM agent builds | **Team 4 (AI Stack)** | Builds LLM agent pipelines & autonomous workflows |
| **C. Web / React Craft** | **#1** | `Skill` | `vercel-labs/agent-skills` | ~35.1k | Tier 1 | **Yes** (`Every-Project Core`) | **Mode 1/2** — Auto-active on React/Next.js/Vercel stacks | **Team 3, Team 4 (UI)** | Official React/Next.js performance & UI best practices |
| **C. UI Component Kit** | **#1** | `MCP / Skill` | `21st` MCP (`21st-dev/magic-mcp`) / `mantine` | ~6.6k / ~32k | Tier 2/3 | Domain (`Domain-Intuition`) | **Mode 2** — Suggest at Step 3 if UI kit accelerates demo | **Team 3** | Unified 21st MCP UI blocks (`@21st-dev/magic`) or `mantine` suite |
| **C. Motion & Spring UI** | **#1** | `Skill / Lib` | `motion-dev` / `motion-primitives` | ~6.9k+ | Tier 2 | Domain (`Domain-Intuition`) | **Mode 3** — Developer-instructed for micro-interactions | **Team 3** | Spring physics (`motion`) & accessible Tailwind motion |
| **C. Color & Typography** | **#1** | `Skill / Web` | `Realtime-color` (`juxtopposed/realtimecolors`) | ~930 | Tier 2 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest at Step 3 visual token setup | **Team 3, Team 13** | Live palette/typography preview & CSS/Tailwind token export |
| **C. Data Visualization** | **#1** | `Lib / Skill` | `recharts` (`recharts/recharts`) | ~28k | Tier 2 | Domain (`Domain-Intuition`) | **Mode 2** — Suggest when building analytics/BI dashboards | **Team 3, Team 12** | Responsive React charts for SaaS, ML & BI metrics |
| **C. 3D Hero Scenes** | **#1** | `Lib / Skill` | `react-spline` (`splinetool/react-spline`) | ~1.4k | Tier 3 | Domain (`Domain-Intuition`) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3** | Interactive 3D hero scenes (only when 3D adds value) |
| **D. E2E Browser Testing** | **#1** | `Skill / MCP` | `playwright` (`microsoft/playwright`) | ~101k | Tier 1 | **Yes** (`Every-Project Core`) | **Mode 2** — Suggest at Step 5–6 for E2E verification | **Team 5, Team 8** | Deterministic E2E, cross-browser & visual regression tests |
| **E. Secret Leak Scan** | **#1** | `CLI / Skill` | `gitleaks` (`gitleaks/gitleaks`) | ~31k–31.4k | Tier 1 | **Yes** (`Every-Project Core`) | **Mode 2** — Suggest at pre-commit & Step 6 security gate | **Team 6** | Fast pre-commit & repo-wide secret leak detection |
| **E. SAST Security Scan** | **#1** | `CLI / Skill` | `semgrep` (`semgrep/semgrep`) | ~18k | Tier 1 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest at Step 6 (`/security-audit-ca-agent`) | **Team 6** | OWASP Top 10 & injection static analysis (SAST) |
| **F. Pitch & Arch Decks** | **#1** | `Skill` | `ppt-master` | Community | Tier 3 | Gate-based (`Phase-Gate`) | **Mode 2** — Suggest at Step 7 for executive/client decks | **Team 11** | Client pitch decks, architecture slides & executive PPTs |
| **F. Technical SEO / GEO** | **#1** | `Skill` | `claude-seo` | Community | Tier 3 | Domain (`Domain-Intuition`) | **Mode 3** — Developer-instructed for SaaS/E-commerce GTM | **Team 13** | Technical SEO, AEO & GEO (`llms.txt`) audits |
| **F. WhatsApp Gateway** | **#1** | `MCP / Tool` | `OpenWA` (`rmyndharis/OpenWA` / `open-wa`) | ~14.3k | Tier 2/3 | Domain (`Domain-Intuition`) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 13, Team 4** | Self-hosted WhatsApp REST/webhook gateway (human-approved sends) |

---

## 3. Master External Skills Catalog (All Parameters Viewed)

### Category A — Discovery, Grilling, Planning & Meta-Workflow

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Baseline Workflow** | **#1** | `Skill` | `anthropics/skills` *(Official)* | ~201.8k | Tier 1 | **Every-Project Core** (Multi-use) | **Mode 1 / 2** — Auto-active baseline or suggest at Step 0 | **Team 2, Team 4, Team 14** *(Groups 1, 2, Orchestrator)* | Provides portable baseline skill patterns across Claude, Codex, Antigravity, and Cursor. |
| **Baseline Workflow** | **#2** | `Skill` | `superpowers` (`obra/superpowers`) | ~328k | Tier 2 | **Every-Project Core** (Multi-use) | **Mode 2** — Fallback only if `#1` lacks structured TDD flow | **Team 2, Team 4, Team 5** *(Groups 1, 2, 3)* | Enforces structured brainstorming, planning, and TDD discipline. |
| **Baseline Workflow** | **#3** | `Skill` | `andrej-karpathy` skill | Community | Tier 2 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 4, Team 7** *(Groups 2, 3)* | Applies minimal-complexity coding and strict verification discipline. |
| **Grilling & Scoping** | **#1** | `Skill` | `grill-me` | Community | Tier 3 | `Phase-Gate` (Step 1) | **Mode 2** — Suggest 1 at Step 1 (`/plan-ca-agent`) | **Team 2, Team 14** *(Group 1, Orchestrator)* | Relentlessly grills requirements and design decisions before any code is written. |
| **Grilling & Scoping** | **#2** | `Skill` | `ai-weekend-build` / `gstack` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Fallback for rapid founder-mode sprints | **Team 2, Team 4** *(Groups 1, 2)* | Accelerates rapid MVP scoping and time-boxed execution sprints. |
| **Skill Discovery** | **#1** | `CLI / Skill` | `vercel-labs/skills` (`skills.sh`) / `find-skill` | ~40.6k | Tier 1/3 | `Phase-Gate` (Step 2) | **Mode 2** — Suggest at Step 2 when niche capability needed | **Team 2** *(Group 1)* | Open Agent Skills standard (`SKILL.md`) & CLI (`npx skills add` / `npx skills find`). |
| **Claude Code Setup** | **#1** | `Plugin` | `claude-code-setup` (`anthropics/claude-plugins-official`) | Official Dir | Tier 1 | `Phase-Gate` (Step 0) | **Mode 2** — Suggest at Step 0 for Claude Code setups | **Team 2, Team 14** *(Group 1, Orchestrator)* | Analyzes codebases to recommend tailored Claude Code hooks, skills, and MCP servers. |
| **Skill Discovery** | **#2** | `Skill` | `awesome-skills` / `skillopt` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Fallback for skill discovery & token audit | **Team 2, Team 14** *(Group 1, Orchestrator)* | Curates external skills and audits prompt/token efficiency. |
| **Visual Plan Review** | **#1** | `Plugin / Skill` | `plannotator` (`backnotprop/plannotator`) | ~14.1k–15.4k | Tier 2 | `Phase-Gate` (Steps 2 & 6) | **Mode 2** — Suggest at Step 2 plan & Step 6 review gates | **Team 1, Team 2, Team 7** *(Groups 1, 3)* | Local-first visual plan, spec, and diff annotation UI with structured feedback loops. |
| **Adversarial Spec Review** | **#2** | `Plugin / Skill` | `elephant-goldfish-model` (`google/elephant-goldfish-model`) | ~10.7k–23.5k | Tier 1 | `Phase-Gate` (Step 2) | **Mode 2** — Suggest at Step 2 for adversarial spec audit | **Team 2, Team 7** *(Groups 1, 3)* | Long-horizon `Elephant` spec drafter + zero-context `Goldfish` adversarial reviewer to prevent context-rot. |
| **Architecture Diagrams** | **#1** | `Skill` | `diagram-design` (`cathrynlavery/diagram-design`) | ~73.7k | Tier 3 | `Phase-Gate` (Steps 2 & 7) | **Mode 2** — Suggest when editorial HTML+SVG visuals needed | **Team 2, Team 11** *(Groups 1, 4)* | Generates 52+ zero-dependency editorial HTML+SVG diagrams (HLD/LLD/DFD/UML/ER/Sankey). |
| **Verification Ledger** | **#2** | `Skill / CLI` | `100x-engineer-skill` (`DeadInternetStudios/100x-engineer-skill`) | ~400–1.5k+ | Tier 3 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 4, Team 5, Team 7** *(Groups 2, 3)* | Enforces formal state/invariant mapping (`verify/ledger.tsv`) and multi-model review rounds. |
| **Agent Control Plane** | **#1** | `Platform / Plugin` | `paperclip` (`paperclipai/paperclip`) | ~117.6k | Tier 2 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 1, Team 14** *(Group 1, Orchestrator)* | Open-source multi-agent control plane (org charts, BYOA adapters, token budgets, heartbeats, approvals). |
| **Meta-Orchestration** | **#3** | `Skill / Plugin` | `ponytail` / `i-have-adhd` / `bla` / `hallmark` / `godmod` / `openclaw` / `ruflo` / `claude-octopus` | Multi-repo | Tier 3 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 14** *(Orchestrator)* | Specialized meta-workflow helpers; must adapt to `.agents/` contracts. |

---

### Category B — Cross-Harness Memory, Code Intelligence & Reverse Engineering

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Persistent Memory** | **#1** | `Plugin / MCP` | `claude-mem` (`thedotmack/claude-mem`) | ~120k | Tier 3 | **Every-Project Core** (Multi-use) | **Mode 2** — Suggest on large multi-session repositories | **Team 2, Team 4, Team 14** *(Groups 1, 2, Orchestrator)* | Persists session memory across harnesses when paired with `docs/memory.md` and `logs/`. |
| **Code Intelligence** | **#1** | `MCP` | `serena` (`oraios/serena`) | ~31.8k | Tier 2 | **Every-Project Core** (Multi-use) | **Mode 2** — Suggest on large multi-module codebases | **Team 2, Team 4** *(Groups 1, 2)* | Performs semantic, symbol-level code retrieval and precise refactoring edits. |
| **Live Library Docs** | **#1** | `MCP` | `Context7` (`upstash/context7`) | ~65.6k | Tier 1 | **Every-Project Core** (Multi-use) | **Mode 2** — Suggest for live version-specific API/SDK docs | **Team 2, Team 4** *(Groups 1, 2)* | Fetches real-time, version-specific library docs & examples (`resolve-library-id`, `query-docs`). |
| **Code Intelligence** | **#2** | `Skill / MCP` | `graphify` | Community | Tier 2 | `Domain-Intuition` | **Mode 2/3** — Fallback for visual dependency graphs | **Team 2** *(Group 1)* | Builds knowledge and dependency graphs for architectural mapping. |
| **Reverse Engineering** | **#1** | `Skill` | `REA` *(Reverse Engineering Anything)* | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 2 (REA Agent)** *(Group 1)* | Reverse-engineers legacy codebases, undocumented APIs, or binaries into specs. |
| **CLI Wrapping** | **#2** | `Skill / CLI` | `cli-anything` / `EEC` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 4** *(Group 2)* | Wraps repetitive workflows or APIs into deterministic CLI commands. |
| **AI Agent Pipelines** | **#1** | `Platform / Skill` | `dify` / `openhands` (`langgenius/dify`, `All-Hands-AI/OpenHands`) | ~162k / ~94.5k | Tier 2 | `Domain-Intuition` (Step 5) | **Mode 2** — Suggest only when building AI/LLM agent apps | **Team 4 (AI Stack)** *(Group 2)* | Scaffolds and orchestrates LLM agent pipelines and autonomous workflows. |
| **Agent Workspaces** | **#2** | `MCP / Skill` | `OpenBot` (`CopilotKit/OpenBot` / `nightly-labs/openbot`) | ~13.9k | Tier 2/3 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 4 (AI Stack)** *(Group 2)* | Self-hostable MCP agent workspace (`CopilotKit`) or local-first persistent task runner (`nightly-labs`). |
| **Multi-Agent Sim** | **#3** | `Skill` | `Mirofish` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 2, Team 4** *(Groups 1, 2)* | Runs multi-agent simulation and scenario modeling for complex systems. |
| **Web/Social Research** | **#3** | `Skill / MCP` | `Agent-Reach` (`Panniantong/Agent-Reach`) | ~114.7k–115.2k | Tier 3 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 2, Team 13** *(Groups 1, 4)* | Zero-API-key multi-platform web/social search & scrape skill + MCP (never bypass auth/CAPTCHAs). |

---

### Category C — Frontend Design, UI Kits, Motion & Data Visualization

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Web / React Craft** | **#1** | `Skill` | `vercel-labs/agent-skills` | ~35.1k | Tier 1 | **Every-Project Core** (Multi-use) | **Mode 1 / 2** — Auto-active on React/Next.js/Vercel stacks | **Team 3, Team 4 (UI)** *(Group 2)* | Official React/Next.js performance, routing, and UI engineering best practices. |
| **Web / React Craft** | **#2** | `Skill` | `ui-ux-pro-max` / `impeccable` | Community | Tier 3 | `Domain-Intuition` | **Mode 2** — Fallback when `#1` needs extra UI polish rules | **Team 3** *(Group 2)* | High-craft UI/UX design system rules and visual hierarchy polish. |
| **Web / React Craft** | **#3** | `Skill` | `emilkowalski` / `awesome-design-skill` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed for tactile micro-UX | **Team 3** *(Group 2)* | Curated design patterns and tactile micro-interaction polish. |
| **UI De-Slop Review** | **#3** | `Skill / Plugin` | `unslop` (`heydamir/unslop`) | ~22.9k | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3** *(Group 2)* | Redline UI & copy review scrubbing generic "AI slop" from vibecoded interfaces. |
| **Landing Page Design** | **#3** | `Skill` | `ai-design-skills` (`elayadesign/ai-design-skills`) | ~16.7k | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3, Team 13** *(Groups 2, 4)* | Structured `landing-page-design` checklist (CTA intake, section architecture, spacing, typography, a11y). |
| **UI Component Kits** | **#1** | `MCP / Skill` | `21st` MCP (`21st-dev/magic-mcp`) / `mantine` (`mantinedev/mantine`) | ~6.6k / ~32k | Tier 2/3 | `Domain-Intuition` (Step 3) | **Mode 2** — Suggest at Step 3 (`21st` MCP hero/UI, `mantine` full app) | **Team 3** *(Group 2)* | Unified 21st.dev MCP (`@21st-dev/magic`) & production React/Tailwind component libraries. |
| **UI Component Kits** | **#2** | `Skill / Lib` | `glass-ui` (`AndreyBegma/glass-ui` / `alexburlis/glassyui`) | Niche OSS | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3** *(Group 2)* | Frosted/Liquid Glass React+Tailwind primitives (never mix with flat/brutalist kits). |
| **UI Component Kits** | **#3** | `Skill / Lib` | `kokonut-ui` / `bklit-ui` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 3** *(Group 2)* | Lightweight animated React/Tailwind UI primitives. |
| **Motion & Physics** | **#1** | `Lib / Skill` | `motion-dev` / `motion-primitives` (`ibelick/motion-primitives`) | ~6.9k+ | Tier 2 | `Domain-Intuition` (Step 3) | **Mode 3** — Developer-instructed for motion-rich UIs | **Team 3** *(Group 2)* | Spring physics, layout animations, and copy-paste accessible React micro-interactions. |
| **Motion & Physics** | **#2** | `Lib / Skill` | `anime.js` (`juliangarnier/anime`) / `reanimate` | ~75.2k | Tier 2/3 | `Domain-Intuition` | **Mode 3** — Developer-instructed for SVG/video motion | **Team 3** *(Group 2)* | Timeline/SVG choreography (`anime.js`) or programmatic video (`reanimate`). |
| **Color & Typography** | **#1** | `Skill / Web` | `Realtime-color` (`juxtopposed/realtimecolors`) | ~930 | Tier 2 | `Phase-Gate` (Step 3) | **Mode 2** — Suggest at Step 3 visual token setup | **Team 3, Team 13** *(Groups 2, 4)* | Live palette/typography playground exporting CSS & Tailwind tokens for `docs/design.md`. |
| **Data Visualization** | **#1** | `Lib / Skill` | `recharts` (`recharts/recharts`) | ~28k | Tier 2 | `Domain-Intuition` (Steps 3 & 9) | **Mode 2** — Suggest when building analytics/BI dashboards | **Team 3, Team 12** *(Groups 2, 4)* | Composable React charts for SaaS analytics, ML metrics, and BI dashboards. |
| **3D Hero Scenes** | **#1** | `Lib / Skill` | `react-spline` (`splinetool/react-spline`) | ~1.4k | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3** *(Group 2)* | Embeds interactive 3D Spline scenes (only when 3D adds clear product value). |
| **Brand & Logo SVG** | **#2** | `Skill` | `logo-design` (`kaankiziltug/logo-design-skill`) | ~7.9k | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3, Team 13** *(Groups 2, 4)* | Structured SVG logo design (1,400+ offline SVG refs, geometric construction, optical/squint/pixel tests). |
| **Pixel VFX & Sprites** | **#3** | `Skill` | `pixelfx` (`patch-gg/pixelfx`) | ~9.7k | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 3** *(Group 2)* | Code-driven pixel-art VFX & sprite sheet generator for Godot, Unity, Phaser, and HTML5 Canvas. |
| **SVG Backgrounds** | `Ref` | `Web Ref` | `Haikei` (`haikei.app`) | N/A (Web) | Reference | `Domain-Intuition` (Steps 3 & 7) | **Mode 2** — Reference when custom SVG waves/blobs needed | **Team 3, Team 13** *(Groups 2, 4)* | Generates organic SVG waves, blobs, and gradient backgrounds for web & brand pages. |
| **UI Benchmarking** | `Ref` | `Web Ref` | `Mobbin` / `Dribbble` | N/A (Web) | Reference | `Phase-Gate` (Step 3) | **Mode 2** — Read-only visual pattern research | **Team 3** *(Group 2)* | Visual pattern benchmarking and layout inspiration before Step 3 UI build. |

---

### Category D — Browser Automation & Testing

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **E2E Browser Testing** | **#1** | `Skill / MCP` | `playwright` (`microsoft/playwright`) | ~101k | Tier 1 | **Every-Project Core** (Multi-use) | **Mode 2** — Suggest at Step 5–6 for E2E & regression | **Team 5, Team 8** *(Group 3)* | Deterministic cross-browser E2E tests, screenshots, and visual regression (`logs/test.log`). |
| **Headless Recon** | **#2** | `MCP / Plugin` | `obscura` (`h4ckf0r0day/obscura`, `obscura-mcp`) | ~37.9k | Tier 3 | `Domain-Intuition` (Steps 1, 5, 6) | **Mode 3** — **Never auto-suggest**; owned targets only | **Team 5, Team 6** *(Group 3)* | Lightweight Rust/V8 CDP headless browser (~30MB RAM); never use to bypass auth/CAPTCHAs. |
| **UI Demo Inspection** | **#3** | `CLI / Skill` | `agent-browser` (`vercel-labs/agent-browser`) | ~51k+ | Tier 3 | `Domain-Intuition` (Step 3) | **Mode 2** — Fallback for lightweight Step 3 UI checks | **Team 3, Team 5** *(Groups 2, 3)* | Lightweight agent-driven browser inspection during Phase 2 sensory demo. |
| **Test Generation** | **#4** | `Skill` | `test-skill` | Community | Tier 3 | `Domain-Intuition` | **Mode 3** — Fallback when framework defaults are insufficient | **Team 5** *(Group 3)* | Generates supplementary edge-case tests when standard harnesses need coverage boost. |

---

### Category E — Security Testing, SAST & Secrets Scanning

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Secret Scanning** | **#1** | `CLI / Skill` | `gitleaks` (`gitleaks/gitleaks`) | ~31k–31.4k | Tier 1 | **Every-Project Core** (Multi-use) | **Mode 2** — Suggest at pre-commit & Step 6 security gate | **Team 6** *(Group 3)* | Fast pre-commit and repo-wide secret/API-key leak detection. |
| **Secret Scanning** | **#2** | `CLI / Skill` | `trufflehog` (`trufflesecurity/trufflehog`) | ~29.6k–29.8k | Tier 1 | `Phase-Gate` (Step 6) | **Mode 2** — Fallback/companion for deep git history | **Team 6** *(Group 3)* | Deep git-history scanning with live credential verification. |
| **SAST Analysis** | **#1** | `CLI / Skill` | `semgrep` (`semgrep/semgrep`) | ~18k | Tier 1 | `Phase-Gate` (Step 6) | **Mode 2** — Suggest at Step 6 (`/security-audit-ca-agent`) | **Team 6** *(Group 3)* | Static analysis (SAST) for OWASP Top 10, SQLi, XSS, and auth flaws. |
| **CVE & Container Scan** | **#2** | `CLI / Skill` | `trivy` (`aquasecurity/trivy`) | ~25k+ | Tier 1 | `Phase-Gate` (Step 6) | **Mode 2** — Suggest alongside `semgrep` for containers/deps | **Team 6** *(Group 3)* | Scans Docker images, OS packages, and dependency lockfiles for CVEs. |
| **AI Code Review** | **#2** | `CLI / Skill` | `open-code-review` (`alibaba/open-code-review`) | ~57k | Tier 2 | `Phase-Gate` (Step 6) | **Mode 2** — Suggest at Step 6 (`/review-ca-agent`) | **Team 7, Team 6** *(Group 3)* | Hybrid deterministic + LLM line-level code review (`ocr` CLI) for NPEs, thread-safety, XSS & SQLi. |
| **AI Security Review** | **#3** | `Skill` | `security-audit-skill` / `strix` / `sigma` / `awesome-security` | Multi-repo | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 6** *(Group 3)* | AI-assisted security review and detection ruleset augmentation. |
| **Defensive Wordlists** | `Ref` | `Ref / Data` | `SecLists` (`danielmiessler/SecLists`) / `PayloadsAllTheThings` (`swisskyrepo/PayloadsAllTheThings`) | ~69k–70k / ~82.9k | Tier 2 | `Domain-Intuition` | **Mode 3** — **Never auto-suggest**; owned staging only | **Team 6** *(Group 3)* | Authorized defensive fuzzing/security testing reference against owned staging targets. |

---

### Category F — Documentation, SEO, Growth & Distribution

| Sub-Category | Rank | Tag | External Skill (Source) | GitHub Stars | Trust Tier | Multiple-Times Use | Developer's Choice & Suggest Policy | Belongs To (Team & Group) | Brief Working Details |
| :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **Pitch & Arch Decks** | **#1** | `Skill` | `ppt-master` | Community | Tier 3 | `Phase-Gate` (Step 7) | **Mode 2** — Suggest at Step 7 (pair with `diagram-design`) | **Team 11** *(Group 4)* | Generates client pitch decks, architecture slides, and executive PPTs. |
| **Repo Presentation** | **#2** | `Skill / Web` | `github-profile-readme-maker` (`rahuldkjain/github-profile-readme-maker`) | ~24.5k | Tier 3 | `Domain-Intuition` | **Mode 3** — Developer-instructed only | **Team 11, Team 13** *(Group 4)* | Polishes repository and organization `README.md` presentation. |
| **Technical SEO / GEO** | **#1** | `Skill` | `claude-seo` | Community | Tier 3 | `Domain-Intuition` (Steps 7 & 9) | **Mode 3** — Developer-instructed for SaaS/E-commerce GTM | **Team 13** *(Group 4)* | Audits technical SEO, AEO, and AI search readiness (`llms.txt`). |
| **WhatsApp Gateway** | **#1** | `MCP / Tool` | `OpenWA` (`rmyndharis/OpenWA` / `open-wa`) | ~14.3k | Tier 2/3 | `Domain-Intuition` (Steps 5, 7, 9) | **Mode 3** — **Never auto-suggest**; human-approved sends only | **Team 13, Team 4** *(Groups 4, 2)* | Self-hosted WhatsApp REST/webhook gateway with strict Team 6 session isolation. |
| **Social Distribution** | **#2** | `Platform / Skill` | `postiz-app` (`gitroomhq/postiz-app`) | ~42.5k | Tier 3 | `Domain-Intuition` (Step 9) | **Mode 3** — **Never auto-suggest**; developer-instructed | **Team 13** *(Group 4)* | Schedules social distribution (LinkedIn/IG/FB) after explicit human approval. |

---

## 4. Team-by-Team Ownership Matrix (Teams 1–14)

Use this reverse-lookup table to see **which external skills belong to each Team** and when that Team suggests them to the developer/user:

| Team | Group | Rank #1 Primary External Skill(s) | Optional Fallback (`#2` / `#3` / `Ref`) | Suggest-to-User Timing |
| :--- | :--- | :--- | :--- | :--- |
| **Team 1** *(PM / Kanban)* | Group 1 | `plannotator` | `paperclip` *(Mode 3)* | Step 2 & Step 4 plan/task visual review (**Mode 2**; `paperclip` **Mode 3**) |
| **Team 2** *(Research / Arch / REA)* | Group 1 | `anthropics/skills`, `claude-code-setup`, `vercel-labs/skills`, `Context7` MCP, `grill-me`, `find-skill`, `plannotator`, `diagram-design`, `claude-mem`, `serena`, `REA` *(Mode 3)* | `superpowers`, `elephant-goldfish-model`, `ai-weekend-build`, `awesome-skills`, `graphify`, `Mirofish`, `Agent-Reach` *(Mode 3)* | Steps 0–2 discovery, grilling, and architecture gates (**Mode 2**; `REA`/`Agent-Reach` **Mode 3**) |
| **Team 3** *(UI / UX / Brand)* | Group 2 | `vercel-labs/agent-skills`, `21st` MCP/`mantine`, `motion-dev`/`motion-primitives`, `Realtime-color`, `recharts`, `react-spline` *(Mode 3)* | `ui-ux-pro-max`, `emilkowalski`, `unslop` *(Mode 3)*, `ai-design-skills` *(Mode 3)*, `logo-design` *(Mode 3)*, `pixelfx` *(Mode 3)*, `glass-ui` *(Mode 3)*, `kokonut-ui`, `anime.js`, `Haikei`, `Mobbin`, `agent-browser` | Step 3 Frontend Sensory Demo (`vercel-labs` **Mode 1/2**; visual kits **Mode 2/3**) |
| **Team 4** *(Core Dev / AI / OS)* | Group 2 | `anthropics/skills`, `Context7` MCP, `claude-mem`, `serena`, `dify`/`openhands`, `vercel-labs` *(UI)*, `OpenWA` *(Mode 3)* | `superpowers`, `andrej-karpathy`, `100x-engineer-skill` *(Mode 3)*, `ai-weekend-build`, `cli-anything`, `OpenBot` *(Mode 3)*, `Mirofish` | Step 3 (UI) & Step 5 (TDD/AI/Backend) (**Mode 1/2**; `OpenBot`/`OpenWA`/`100x` **Mode 3**) |
| **Team 5** *(Testing)* | Group 3 | `playwright` | `superpowers`, `100x-engineer-skill` *(Mode 3)*, `obscura` *(Mode 3)*, `agent-browser`, `test-skill` | Step 6 Gate 1 E2E & cross-browser suite (**Mode 2**) |
| **Team 6** *(Security Testing)* | Group 3 | `gitleaks`, `semgrep` | `trufflehog`, `trivy`, `open-code-review`, `obscura` *(Mode 3)*, `security-audit-skill`, `SecLists` *(Mode 3)* | Pre-commit & Step 6 Gate 2 SAST/secret/CVE audit (**Mode 2**; `SecLists`/`obscura` **Mode 3**) |
| **Team 7** *(Code Review)* | Group 3 | `plannotator` | `open-code-review`, `elephant-goldfish-model`, `andrej-karpathy` *(Mode 3)*, `100x-engineer-skill` *(Mode 3)* | Step 6 Gate 3 diff & spec-traceability review (**Mode 2**) |
| **Team 8** *(Quality Assurance)* | Group 3 | `playwright` | — | Step 6 Gate 4 visual regression & QA scorecard (**Mode 2**) |
| **Team 9** *(Deployment Ops)* | Group 3 | *(Uses Core `release-validator` + Team 6 `trivy`)* | — | Step 8 container/infra CVE check via Team 6 |
| **Team 10** *(24×7 Maintenance)* | Group 3 | *(Uses Core `debugging-analyst` + `logs/`)* | — | Step 9 incident triage; escalates code fixes to Team 4 |
| **Team 11** *(Documentation)* | Group 4 | `diagram-design`, `ppt-master` | `github-profile-readme-maker` | Step 7 handoff docs, architecture diagrams & pitch decks (**Mode 2**) |
| **Team 12** *(BI / ROI / Finance)* | Group 4 | `recharts` | — | Step 1 ROI charts & Step 9 BI analytics (**Mode 2**) |
| **Team 13** *(Marketing / GEO)* | Group 4 | `Realtime-color`, `claude-seo` *(Mode 3)*, `OpenWA` *(Mode 3)* | `ai-design-skills` *(Mode 3)*, `logo-design` *(Mode 3)*, `Agent-Reach` *(Mode 3)*, `Haikei`, `github-profile-readme-maker`, `postiz-app` *(Mode 3)* | Steps 1, 7 & 9 Brand/SEO/GTM (**Mode 3** developer-instructed for outreach/SEO) |
| **Team 14** *(Workflow Guider)* | Orchestrator | `anthropics/skills`, `claude-code-setup`, `grill-me`, `claude-mem` | `paperclip` *(Mode 3)*, `awesome-skills`/`skillopt`, meta-orchestration helpers *(Mode 3)* | Steps 0–9 continuous guidance & Transparent Skill Disclosure (**Mode 1/2**; `paperclip` **Mode 3**) |
