# 07 — Curated, Trust-Tiered & Ranked External Skills Registry

**Policy:** All external skills, MCPs, and packages listed here are **optional (Developer Choice)** per `docs/skills.md`. Never pre-bundle, never load randomly, and **never install from unverified forks**. Always verify the official GitHub org / npm / Vercel / Anthropic source and pass the **5-Point Security Vetting Checklist** ([02-discovery-design-dev-teams.md](02-discovery-design-dev-teams.md)) before enabling.

---

## 1. Intuition, Frequency & Category-Ranking Rules

1. **No Random Loading:** Activate **at most 1–3 external tools/skills per step**, strictly matched to the project's domain and current bottleneck.
2. **Frequency Tiers:**
   - **Every-Project Core:** High-frequency baseline tools needed on almost every web/software build.
   - **Phase-Gate:** Triggered only at specific gates (Discovery, Security Audit, Docs/Release).
   - **Domain-Intuition:** Triggered only when the domain or UI/data requirement demands it (e.g., 3D, charts, SEO, pentesting).
3. **Category Ranking Rule (Pick Rank #1 Only):** Within each category below, tools are ranked `#1, #2, #3` by **Trust Tier → Cross-Harness Portability → Token Efficiency**. **Use Rank #1 by default**; only fall back to `#2` or `#3` if `#1` lacks a required capability. Never load two overlapping tools of the same kind at once.

---

## 2. Trust Tiers

| Tier | Source Standard | Verification Requirement |
|---|---|---|
| **Tier 1 (Official / Vendor)** | Official vendor orgs (`anthropics/skills`, `vercel-labs/agent-skills`, `microsoft/playwright`, `semgrep`, `aquasecurity/trivy`, `gitleaks`, `trufflesecurity/trufflehog`) | Verify exact org/package name; standard lockfile/checksum check |
| **Tier 2 (Established OSS)** | Well-known open-source ecosystems (`superpowers`, `serena`, `graphify`, `openhands`, `dify`, `mantine`, `recharts`, `anime.js`, `motion.dev`, `SecLists`, `PayloadsAllTheThings`) | Verify official repo & license; read scripts before running |
| **Tier 3 (Trending / Community)** | Specialized community skills (`grill-me`, `claude-mem`, `ui-ux-pro-max`, `find-skill`, etc.) | **Mandatory 5-Point Security Vetting Checklist** + sandbox dry-run before use |

---

## 3. Ranked Category Catalog (Select Rank #1 per Need)

### A. Discovery, Grilling, Planning & Meta-Workflow (Team 1, Team 2, Team 14)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition & Cross-Harness Note |
|---|---|---|---|---|
| **#1** | `anthropic` skills (`anthropics/skills`) | Tier 1 | Every-Project Core | Official baseline skill patterns; portable across Claude, Codex, Antigravity, Cursor |
| **#2** | `superpowers` | Tier 2 | Every-Project Core | Structured brainstorming, planning, and TDD discipline |
| **#3** | `andrej-karpathy` skill | Tier 2 | Domain-Intuition | Minimal-complexity coding & verification discipline |
| **#1** | `grill-me` | Tier 3 | Phase-Gate (Step 1) | **Team 2 + Team 14:** Relentless requirement & design-decision grilling before coding |
| **#2** | `ai-weekend-build` / `gstack` | Tier 3 | Domain-Intuition | Rapid MVP scoping & founder-mode execution sprints |
| **#1** | `find-skill` | Tier 3 | Phase-Gate (Step 2) | **Team 2:** Discover & verify official skills on demand (replaces guessing) |
| **#2** | `awesome-skills` / `skillopt` | Tier 3 | Domain-Intuition | Skill discovery & prompt/token optimization auditing |
| **#3** | `ponytail` / `i-have-adhd` / `bla` / `hallmark` / `godmod` / `openclaw` / `ruflo` / `claude-octopus` | Tier 3 | Domain-Intuition | Specialized workflow/orchestration helpers; adapt `.agents/` contracts for all harnesses |

---

### B. Cross-Harness Memory, Code Intelligence & Reverse Engineering (Team 2 & Team 4)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition & Cross-Harness Note |
|---|---|---|---|---|
| **#1** | `claude-mem` *(Cross-Harness Adapter)* | Tier 3 | Every-Project Core | Persistent session memory; pair with `docs/memory.md` + `logs/` so it works for **Claude, Codex, Antigravity, Cursor, Windsurf**—not Claude-only |
| **#1** | `serena` | Tier 2 | Every-Project Core | Semantic symbol-level code retrieval & editing for large codebases |
| **#2** | `graphify` | Tier 2 | Domain-Intuition | Knowledge/dependency graph visualization & architectural mapping |
| **#1** | `REA` (Reverse Engineering Anything) | Tier 3 | Domain-Intuition | **Team 2 (REA Agent):** Reverse-engineer legacy apps, APIs, or binaries |
| **#2** | `cli-anything` / `EEC` | Tier 3 | Domain-Intuition | Wrap workflows/APIs into deterministic CLIs |
| **#1** | `dify` / `openhands` | Tier 2 | Domain-Intuition | **Team 4 (AI Stack):** Trigger only when building LLM agent pipelines or autonomous workflows |
| **#2** | `Mirofish` | Tier 3 | Domain-Intuition | Multi-agent simulation & scenario modeling |

---

### C. Frontend Design, UI Kits, Motion & Data Visualization (Team 3)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition (Pick 1 per Sub-Need) |
|---|---|---|---|---|
| **#1** | `vercel-labs` skills / `modern-web-guidance` | Tier 1 | Every-Project Core | Official React/Next.js/Web best practices & performance |
| **#2** | `ui-ux-pro-max` / `impeccable` | Tier 3 | Domain-Intuition | High-craft UI/UX design system & polish rules |
| **#3** | `emilkowalski` skill / `awesome-design-skill` | Tier 3 | Domain-Intuition | Micro-interactions, tactile UI feel, and curated design patterns |
| **#1** | `21st` (21st.dev) / `mantine` | Tier 2/3 | Domain-Intuition | Production component library (`mantine` for full app suite; `21st` for marketing/hero blocks) |
| **#2** | `kokonut-ui` / `bklit-ui` | Tier 3 | Domain-Intuition | Lightweight animated React/Tailwind UI primitives |
| **#1** | `motion-dev` (`motion`) | Tier 2 | Domain-Intuition | Spring physics & React layout animations |
| **#2** | `anime.js` (`anime`) / `reanimate` | Tier 2/3 | Domain-Intuition | Timeline/SVG choreography (`anime.js`) or programmatic video/motion (`reanimate`) |
| **#1** | `recharts` | Tier 2 | Domain-Intuition | Data dashboards, SaaS analytics, ML/business charts |
| **#1** | `react-spline` | Tier 3 | Domain-Intuition | Interactive 3D hero scenes (only when 3D adds clear product value) |
| **Ref** | `Mobbin` / `Dribbble` | Reference | Phase-Gate (Step 3) | Visual inspiration & pattern benchmarking (read-only research) |

---

### D. Browser Automation & Testing (Team 5 & Team 8)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition |
|---|---|---|---|---|
| **#1** | `playwright` | Tier 1 | Every-Project Core | Deterministic E2E, cross-browser, and visual regression testing |
| **#2** | `agent-browser` | Tier 3 | Domain-Intuition | Lightweight agent-driven browser inspection during Phase 2 sensory demo |
| **#3** | `test-skill` | Tier 3 | Domain-Intuition | Supplementary test-case generation when framework defaults are insufficient |

---

### E. Security Testing, SAST & Secrets Scanning (Team 6)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition |
|---|---|---|---|---|
| **#1** | `gitleaks` | Tier 1 | Every-Project Core | Fast pre-commit & repo-wide secret leak detection |
| **#2** | `trufflehog` | Tier 1 | Phase-Gate (Step 6) | Deep git-history & verified credential scanning |
| **#1** | `semgrep` | Tier 1 | Phase-Gate (Step 6) | Static analysis (SAST) for OWASP Top 10 & injection flaws |
| **#2** | `trivy` | Tier 1 | Phase-Gate (Step 6) | Container, OS package, and dependency CVE scanning |
| **#3** | `security-audit-skill` / `strix` / `sigma` / `awesome-security` | Tier 3 | Domain-Intuition | AI-assisted security review & detection rules |
| **Ref** | `SecLists` / `PayloadsAllTheThings` | Tier 2 | Domain-Intuition | **Authorized defensive testing only** against owned staging targets |

---

### F. Documentation, SEO, Growth & Distribution (Team 11 & Team 13)

| Rank | Tool / Skill | Tier | Frequency | Trigger Intuition |
|---|---|---|---|---|
| **#1** | `ppt-master` | Tier 3 | Phase-Gate (Step 7) | **Team 11:** Client pitch decks, architecture slides, and executive PPTs |
| **#2** | `github-profile-readme-maker` | Tier 3 | Domain-Intuition | Polished repository/org `README.md` presentation |
| **#1** | `claude-seo` | Tier 3 | Domain-Intuition | **Team 13:** Technical SEO, AEO, and GEO audits for SaaS/E-commerce |
| **#1** | `postiz-app` | Tier 3 | Domain-Intuition | **Team 13:** Scheduled social distribution (LinkedIn/IG/FB) after human approval |
