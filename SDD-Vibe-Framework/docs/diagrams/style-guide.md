# SDD-Vibe Diagram Design Style Guide

> **Skill Reference:** [`cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design)  
> **Scope:** All SVG and HTML diagrams in `docs/diagrams/` and `SDD-Vibe-Framework/docs/diagrams/`, plus Unicode diagrams in `playbooks/*.txt`.

---

## 1. Pure 3D vs. Editorial 2D Selection Rule

Never force every diagram into 3D. Choose the projection that maximizes structural clarity:

| Diagram Mode | When to Use | Examples |
|---|---|---|
| **Pure 3D Axonometric (2:1 Dimetric)** | Layered stacks, vertical tier hierarchies, testing pyramids, and elevated hub-and-spoke topologies | `3d-sdd-vibe-pipeline.svg`, `3d-system-architecture.svg`, `3d-testing-pyramid.svg`, `3d-security-defense.svg`, `3d-database-persistence.svg`, `3d-api-gateway.svg`, `3d-token-optimization.svg`, `3d-cross-ide-portability.svg`, `3d-agentic-ecosystem.svg` |
| **Editorial 2D (`diagram-design`)** | Sequential workflows, swimlane pipelines, state machines, cyclic loops, and traceability chains | `workflow-prompt-pipeline.svg`, `workflow-traceability-contract.svg`, `workflow-staged-web-dev.svg`, `workflow-5step-cyclic-loop.svg`, `flow-mission-control-dashboard.svg`, `flow-cicd-devops.svg`, `flow-feature-lifecycle.svg` |

---

## 2. Color Tokens (Dark-Slate Editorial Canvas)

All diagrams render on a high-contrast dark-slate card canvas (`#090d16` → `#0f172a` → `#111827`) so they look crisp on both GitHub Light and GitHub Dark themes.

| Semantic Role | Primary / Top | Left Shade | Right Shade | Stroke / Accent | Text |
|---|---|---|---|---|---|
| **Architecture / Core (`sky`)** | `#0284c7` | `#0369a1` | `#075985` | `#38bdf8` | `#e0f2fe` |
| **Orchestration / Contract (`indigo`)** | `#4f46e5` | `#4338ca` | `#3730a3` | `#818cf8` | `#e0e7ff` |
| **Vibe / UI / E2E (`violet`)** | `#7c3aed` | `#6d28d9` | `#5b21b6` | `#c084fc` | `#f3e8ff` |
| **TDD Green / Approved (`emerald`)** | `#059669` | `#047857` | `#065f46` | `#34d399` | `#d1fae5` |
| **Gate / Auth / Review (`amber`)** | `#d97706` | `#b45309` | `#92400e` | `#fbbf24` | `#fef3c7` |
| **TDD Red / Security (`rose`)** | `#e11d48` | `#be123c` | `#9f1239` | `#fb7185` | `#ffe4e6` |
| **Baseplate / Infra (`slate`)** | `#334155` | `#1e293b` | `#0f172a` | `#94a3b8` | `#f1f5f9` |

---

## 3. Typography, Spacing & Zero-Clipping Contract

1. **Font Stack:** `Inter, Segoe UI, system-ui, sans-serif` for titles/labels; `JetBrains Mono, Consolas, monospace` for technical metadata, ports, IDs, and commands.
2. **Auto-Computed `viewBox`:** Every SVG **MUST** compute its exact geometric bounding box across all shapes, labels, callouts, and legends, then apply `>= 48px` padding on all sides so `minX >= 0`, `minY >= 0`, `maxX <= viewBoxWidth`, and `maxY <= viewBoxHeight` (zero clipping).
3. **Text-Fit & Readability:**
   - Titles and subtitles on 3D slabs must fit comfortably inside the slab's projected width; never overflow polygon edges.
   - 2D cards use generous internal padding (`16px+`), crisp `1.5px` strokes, `rx="10"`, and clean orthogonal/bezier connectors with directional arrowheads.
4. **Canonical Asset Counts:** Always state **`18 Commands`** (`*-ca-agent.md`) and **`18 Skills`** (`.agents/skills/`).

---

## 4. Dual Output & Playbook `.txt` Rules

- **GitHub Markdown:** Standalone `.svg` files in `docs/diagrams/` and `SDD-Vibe-Framework/docs/diagrams/`.
- **Interactive Editorial Gallery:** `docs/diagrams/gallery.html` (and `SDD-Vibe-Framework/docs/diagrams/gallery.html`) embedding all SVGs for local browser inspection.
- **Playbooks (`playbooks/*.txt`):**
  - Layered/stack playbooks (`04-Authentication-Security.txt`, `07-Testing-QA.txt`) use **3D isometric Unicode box diagrams**.
  - Sequential playbooks (`01`–`03`, `05`–`06`, `08`–`11`) use **aligned 2D Unicode workflow diagrams** with exact box-width padding.
