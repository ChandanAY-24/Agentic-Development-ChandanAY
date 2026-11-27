#!/usr/bin/env python3
"""Generate 3D axonometric (2:1 dimetric) SVG diagrams for SDD-Vibe.

Follows the cathrynlavery/diagram-design editorial HTML+SVG approach:
- 2:1 dimetric projection for crisp 3D exploded layer slabs and isometric pyramids
- High-contrast dark-slate card canvas that renders cleanly on both GitHub Light & Dark
- Zero external dependencies (Python stdlib only)
"""
from __future__ import annotations

import shutil
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FW_DIAGRAMS = ROOT / "docs" / "diagrams"
REPO_DIAGRAMS = ROOT.parent / "docs" / "diagrams"

PALETTE = {
    "sky": ("#0284c7", "#0369a1", "#075985", "#38bdf8", "#e0f2fe"),
    "indigo": ("#4f46e5", "#4338ca", "#3730a3", "#818cf8", "#e0e7ff"),
    "violet": ("#7c3aed", "#6d28d9", "#5b21b6", "#c084fc", "#f3e8ff"),
    "emerald": ("#059669", "#047857", "#065f46", "#34d399", "#d1fae5"),
    "amber": ("#d97706", "#b45309", "#92400e", "#fbbf24", "#fef3c7"),
    "rose": ("#e11d48", "#be123c", "#9f1239", "#fb7185", "#ffe4e6"),
    "slate": ("#334155", "#1e293b", "#0f172a", "#94a3b8", "#f1f5f9"),
}


def iso(x: float, y: float, z: float, ox: float = 460.0, oy: float = 120.0) -> tuple[float, float]:
    """2:1 dimetric projection: (x, y, z) -> (screen_x, screen_y)."""
    sx = ox + (x - y) * 0.866
    sy = oy + (x + y) * 0.433 - z
    return round(sx, 1), round(sy, 1)


def pts(points: list[tuple[float, float]]) -> str:
    return " ".join(f"{x},{y}" for x, y in points)


def draw_box(
    x: float, y: float, z: float,
    w: float, d: float, h: float,
    color_key: str,
    title: str = "",
    subtitle: str = "",
    ox: float = 460.0, oy: float = 120.0,
) -> str:
    """Render an extruded 3D isometric slab with top, left, and right faces + label."""
    top_c, left_c, right_c, stroke_c, text_c = PALETTE[color_key]

    # 8 corners: bottom (z) and top (z + h)
    t0 = iso(x, y, z + h, ox, oy)
    t1 = iso(x + w, y, z + h, ox, oy)
    t2 = iso(x + w, y + d, z + h, ox, oy)
    t3 = iso(x, y + d, z + h, ox, oy)

    b1 = iso(x + w, y, z, ox, oy)
    b2 = iso(x + w, y + d, z, ox, oy)
    b3 = iso(x, y + d, z, ox, oy)

    cx, cy = iso(x + w / 2, y + d / 2, z + h, ox, oy)

    parts = [
        f'<polygon points="{pts([t3, t2, b2, b3])}" fill="{left_c}" stroke="{stroke_c}" stroke-width="1.2" opacity="0.95"/>',
        f'<polygon points="{pts([t1, t2, b2, b1])}" fill="{right_c}" stroke="{stroke_c}" stroke-width="1.2" opacity="0.95"/>',
        f'<polygon points="{pts([t0, t1, t2, t3])}" fill="{top_c}" stroke="{stroke_c}" stroke-width="1.6"/>',
    ]
    if title:
        parts.append(
            f'<text x="{cx}" y="{cy - (4 if subtitle else -4)}" text-anchor="middle" '
            f'font-family="Inter, Segoe UI, system-ui, sans-serif" font-size="13" font-weight="700" fill="{text_c}">{escape(title)}</text>'
        )
    if subtitle:
        parts.append(
            f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" '
            f'font-family="JetBrains Mono, Consolas, monospace" font-size="10.5" fill="#e2e8f0" opacity="0.92">{escape(subtitle)}</text>'
        )
    return "\n  ".join(parts)


def wrap_svg(title: str, subtitle: str, body: str, width: int = 920, height: int = 540, legend: list[tuple[str, str]] | None = None) -> str:
    legend_svg = ""
    if legend:
        items = []
        lx = 36
        for color_key, label in legend:
            top_c, _, _, stroke_c, _ = PALETTE[color_key]
            items.append(
                f'<rect x="{lx}" y="{height - 34}" width="12" height="12" rx="3" fill="{top_c}" stroke="{stroke_c}" stroke-width="1.2"/>'
                f'<text x="{lx + 18}" y="{height - 24}" font-family="Inter, Segoe UI, sans-serif" font-size="11" fill="#cbd5e1">{escape(label)}</text>'
            )
            lx += 24 + len(label) * 6.8 + 18
        legend_svg = "\n  ".join(items)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="55%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <pattern id="isoGrid" width="40" height="23.1" patternUnits="userSpaceOnUse">
      <path d="M 0 11.55 L 20 0 L 40 11.55 L 20 23.1 Z" fill="none" stroke="#1e293b" stroke-width="0.6" opacity="0.55"/>
    </pattern>
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>
  <rect width="{width}" height="{height}" rx="14" fill="url(#bgGrad)" stroke="#1e293b" stroke-width="1.5"/>
  <rect width="{width}" height="{height}" rx="14" fill="url(#isoGrid)"/>
  <text x="32" y="38" font-family="Inter, Segoe UI, system-ui, sans-serif" font-size="19" font-weight="800" fill="#f8fafc">{escape(title)}</text>
  <text x="32" y="58" font-family="JetBrains Mono, Consolas, monospace" font-size="11.5" fill="#94a3b8">{escape(subtitle)}</text>
  <g filter="url(#glow)">
  {body}
  </g>
  {legend_svg}
  <text x="{width - 28}" y="{height - 24}" text-anchor="end" font-family="JetBrains Mono, Consolas, monospace" font-size="10" fill="#64748b">SDD-Vibe · 2:1 Axonometric 3D</text>
</svg>
'''


def build_exploded_stack(
    title: str,
    subtitle: str,
    layers: list[tuple[str, str, str]],
    base_label: str | None = None,
) -> str:
    """Build a vertical exploded 3D axonometric stack of slabs (bottom to top)."""
    body_parts = []
    # Vertical axis guide line
    top_pt = iso(105, 105, 30 + len(layers) * 62 + 30, 460, 390)
    bot_pt = iso(105, 105, -10, 460, 390)
    body_parts.append(
        f'<line x1="{bot_pt[0]}" y1="{bot_pt[1]}" x2="{top_pt[0]}" y2="{top_pt[1]}" '
        f'stroke="#475569" stroke-width="1.5" stroke-dasharray="5,5"/>'
    )

    if base_label:
        body_parts.append(draw_box(-30, -30, -24, 270, 270, 18, "slate", base_label, "Shared Governance Baseplate", 460, 390))

    for i, (color_key, l_title, l_sub) in enumerate(layers):
        z = 16 + i * 62
        body_parts.append(draw_box(0, 0, z, 210, 210, 26, color_key, l_title, l_sub, 460, 390))

    # Side callout index badges
    for i, (color_key, l_title, _) in enumerate(layers):
        z = 16 + i * 62 + 16
        edge = iso(210, 105, z, 460, 390)
        _, _, _, stroke_c, _ = PALETTE[color_key]
        body_parts.append(
            f'<line x1="{edge[0]}" y1="{edge[1]}" x2="{edge[0] + 48}" y2="{edge[1]}" stroke="{stroke_c}" stroke-width="1.2" stroke-dasharray="3,3"/>'
            f'<circle cx="{edge[0] + 54}" cy="{edge[1]}" r="11" fill="#0f172a" stroke="{stroke_c}" stroke-width="1.5"/>'
            f'<text x="{edge[0] + 54}" y="{edge[1] + 4}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="{stroke_c}">L{i + 1}</text>'
        )

    return wrap_svg(title, subtitle, "\n  ".join(body_parts), width=920, height=540)


def build_grid_3d(
    title: str,
    subtitle: str,
    blocks: list[tuple[float, float, float, float, float, float, str, str, str]],
    legend: list[tuple[str, str]] | None = None,
    ox: float = 460,
    oy: float = 240,
) -> str:
    body = "\n  ".join(draw_box(x, y, z, w, d, h, c, t, s, ox, oy) for x, y, z, w, d, h, c, t, s in blocks)
    return wrap_svg(title, subtitle, body, width=920, height=540, legend=legend)


def build_pyramid_3d() -> str:
    """3D Isometric Testing Pyramid (Unit -> Integration -> E2E + AC Traceability)."""
    parts = [
        draw_box(-20, -20, -20, 250, 250, 16, "slate", "logs/test.log & AC Traceability", "AC-FEAT###-## -> TEST-FEAT###-##", 460, 390),
        draw_box(0, 0, 12, 210, 210, 44, "sky", "UNIT TESTS (60-70%)", "tests/unit/ · Pure Domain & Contracts", 460, 390),
        draw_box(32, 32, 74, 146, 146, 42, "indigo", "INTEGRATION (20-30%)", "tests/integration/ · API & DB", 460, 390),
        draw_box(66, 66, 134, 78, 78, 38, "violet", "E2E (10%)", "Browser Journeys", 460, 390),
    ]
    return wrap_svg(
        "3D Isometric Testing Pyramid & AC Traceability",
        "Red-Green-Refactor TDD Gate · Zero-Regression Verification",
        "\n  ".join(parts),
        legend=[("sky", "Unit"), ("indigo", "Integration"), ("violet", "E2E"), ("slate", "Audit Log")],
    )


def generate_all() -> list[Path]:
    FW_DIAGRAMS.mkdir(parents=True, exist_ok=True)
    REPO_DIAGRAMS.mkdir(parents=True, exist_ok=True)

    specs: dict[str, str] = {
        "3d-sdd-vibe-pipeline.svg": build_exploded_stack(
            "SDD-Vibe: 1-in-2 Single Workflow (3D Exploded Stack)",
            "Phase 1 Architecture -> Phase 2 Sensory Demo (:3000) -> Phase 3 Spec Lock & TDD -> Phase 4 Ship",
            [
                ("sky", "Phase 1: Architecture & Vibe", "Domain Research · HLD/LLD · Tokens"),
                ("violet", "Phase 2: Frontend Sensory Demo", "PROTOTYPE -> DRAFT · Live UI (:3000)"),
                ("emerald", "Phase 3: Spec Lock & TDD", "APPROVED Spec · Red-Green-Refactor"),
                ("amber", "Phase 4: Quality Audit & Ship", "/review · /security-audit · /release"),
            ],
            base_label=".agents/ (18 Commands & 18 Skills) + Dashboard (:4200)",
        ),
        "3d-agentic-ecosystem.svg": build_grid_3d(
            "14-Team Agentic Ecosystem (3D Topology)",
            "Just-In-Time Opt-In Activation · Main Agent + Team 14 Orchestrator",
            [
                (-160, -20, 0, 140, 120, 28, "amber", "Group 1: Strategy & PM", "Team 1 Kanban · Team 2 REA"),
                (20, -20, 0, 140, 120, 28, "violet", "Group 2: Design & Build", "Team 3 UI/UX · Team 4 Dev"),
                (-160, 130, 0, 140, 120, 28, "emerald", "Group 3: Verify & Ops", "Teams 5-8 QA · Teams 9-10 Ops"),
                (20, 130, 0, 140, 120, 28, "sky", "Group 4: Docs & Growth", "Teams 11-13 · Team 14 Guider"),
                (-65, 55, 85, 130, 110, 32, "indigo", "Main Orchestrator", "/team-ecosystem-ca-agent"),
            ],
            legend=[("indigo", "Orchestrator"), ("amber", "Strategy"), ("violet", "Build"), ("emerald", "Verify/Ops"), ("sky", "Docs/Growth")],
            ox=460,
            oy=220,
        ),
        "3d-system-architecture.svg": build_exploded_stack(
            "5-Tier System Architecture & Clean Layers (3D)",
            "High-Level Topology & Dependency Direction (Presentation -> App -> Domain -> Data)",
            [
                ("slate", "Tier 5: Persistence & Cache", "PostgreSQL / RLS · Redis · Logs"),
                ("emerald", "Tier 4: Domain & App Core", "Clean Entities · Use Cases · TDD"),
                ("indigo", "Tier 3: API & Auth Gateway", "Zod Contracts · RBAC · Rate Limit"),
                ("sky", "Tier 2: Edge & SSR", "Next.js / CDN · WAF · Headers"),
                ("violet", "Tier 1: Client & Ingress", "Responsive UI · WCAG AA · TLS"),
            ],
        ),
        "3d-mission-control-dashboard.svg": build_grid_3d(
            "In-IDE Project-Manager-Dashboard (3D Dataflow)",
            "Zero-Dependency Local Daemon (127.0.0.1:4200) · Live SSE Telemetry",
            [
                (-170, 10, 0, 130, 130, 26, "slate", "docs/ & .git/ & logs/", "Markdown AST + HEAD + Logs"),
                (-10, 10, 35, 135, 130, 30, "sky", "parser.js + server.js", "AST Synthesis · SSE Stream"),
                (155, 10, 70, 130, 130, 28, "indigo", "IDE Simple Browser", "127.0.0.1:4200 Bento UI"),
                (-10, 170, 10, 135, 95, 22, "rose", "Security Guard", "Host Check · CSRF Token"),
            ],
            legend=[("slate", "Workspace"), ("sky", "Daemon"), ("indigo", "IDE Viewport"), ("rose", "Security")],
            ox=430,
            oy=210,
        ),
        "3d-cross-ide-portability.svg": build_grid_3d(
            "Cross-IDE Portability Engine (3D Sync Hub)",
            "Canonical .agents/ -> scripts/sync_ide_adapters.py -> 8 AI Coding IDEs",
            [
                (-65, 55, 80, 145, 120, 34, "indigo", "Canonical .agents/", "18 Commands · 18 Skills · Hooks"),
                (-180, -20, 0, 120, 95, 24, "sky", "Claude & Antigravity", ".claude/ · .agents/workflows/"),
                (60, -20, 0, 120, 95, 24, "violet", "Cursor & Windsurf", ".cursor/ · .windsurf/"),
                (-180, 135, 0, 120, 95, 24, "emerald", "Codex & Copilot", ".codex/ · .github/prompts/"),
                (60, 135, 0, 120, 95, 24, "amber", "OpenCode & Trae", "AGENTS.md Discovery"),
            ],
            ox=455,
            oy=220,
        ),
        "3d-testing-pyramid.svg": build_pyramid_3d(),
        "3d-security-defense.svg": build_exploded_stack(
            "Defense-in-Depth Security Stack (3D)",
            "SAST · Secret Redaction · AuthN/RBAC · Row-Level Security",
            [
                ("slate", "Layer 1: Data & RLS Isolation", "Tenant Policies · Encrypted Secrets"),
                ("rose", "Layer 2: SAST & Secret Scan", "Gitleaks · Semgrep · /security-audit"),
                ("amber", "Layer 3: AuthN, RBAC & 2FA", "Signed Sessions · CSRF · Rate Limit"),
                ("sky", "Layer 4: Input & Edge Guard", "Zod Schemas · Upload Magic Bytes"),
            ],
        ),
        "3d-database-persistence.svg": build_exploded_stack(
            "Persistence & Zero-Downtime Migration Stack (3D)",
            "Schema Contract -> Expand/Contract Migration -> RLS & Backup",
            [
                ("slate", "Backup & Point-in-Time Recovery", "Pre-Migration Snapshot · Rollback"),
                ("emerald", "Primary Store + RLS", "Parameterized SQL · Indexes"),
                ("indigo", "Migration & Seed Layer", "Reversible Up/Down DDL"),
                ("sky", "Repository & Query Layer", "Typed Contracts · N+1 Guard"),
            ],
        ),
        "3d-api-gateway.svg": build_exploded_stack(
            "API Contract & Request Lifecycle (3D)",
            "docs/apis.md -> Schema Validation -> Auth Guard -> Deterministic JSON",
            [
                ("emerald", "Structured JSON Response", "Semantic HTTP Codes · Zero Stack Leaks"),
                ("indigo", "Domain Service Execution", "Idempotency · Transaction Scope"),
                ("amber", "AuthN / RBAC Middleware", "401/403 Guards · Rate Limiting"),
                ("sky", "Zod / Schema Validation", "400/422 Field-Level Errors"),
            ],
        ),
        "3d-cicd-devops.svg": build_grid_3d(
            "CI/CD & Quality Gate Pipeline (3D)",
            ".github/workflows/frameworks-ci.yml · Zero-Error Release Gate",
            [
                (-190, 40, 0, 110, 110, 24, "sky", "1. Lint & Format", "ESLint · Prettier"),
                (-55, 40, 25, 115, 110, 26, "indigo", "2. Docs & Manifest", "check_docs · manifest"),
                (85, 40, 50, 115, 110, 28, "emerald", "3. Test Suites", "run-tests.js (10/10)"),
                (225, 40, 75, 110, 110, 30, "rose", "4. Secret Scan", "Gitleaks · Regex"),
            ],
            ox=390,
            oy=240,
        ),
        "3d-feature-lifecycle.svg": build_grid_3d(
            "Feature Spec Lifecycle & Change Control (3D)",
            "PROTOTYPE -> DRAFT -> IN REVIEW -> APPROVED (APR-###) -> CR-###",
            [
                (-185, 40, 0, 110, 110, 22, "violet", "PROTOTYPE", "Phase 2 Sensory Demo"),
                (-55, 40, 24, 110, 110, 24, "sky", "DRAFT", "AC-FEAT###-## Authoring"),
                (75, 40, 48, 110, 110, 26, "amber", "IN REVIEW", "/spec-check-ca-agent"),
                (205, 40, 72, 115, 110, 28, "emerald", "APPROVED", "APR-### · TDD Locked"),
            ],
            ox=395,
            oy=240,
        ),
        "3d-token-optimization.svg": build_exploded_stack(
            "Dual-Budget Token Optimization Architecture (3D)",
            "50-80% Savings on Routine Work · Full-Potential Models on Planning & Security",
            [
                ("emerald", "Tier 3: Context & Cache Layer", "Prompt Caching · Memory Lanes"),
                ("sky", "Tier 2: Routine Execution", "Flash/Fast Tier · Bounded Edits"),
                ("violet", "Tier 1: Deep Reasoning Gates", "Pro/Opus Tier · Plan & Security"),
            ],
        ),
    }

    written: list[Path] = []
    for filename, svg_content in specs.items():
        # Validate XML before writing
        ET.fromstring(svg_content)
        fw_path = FW_DIAGRAMS / filename
        fw_path.write_text(svg_content, encoding="utf-8", newline="\n")
        shutil.copy2(fw_path, REPO_DIAGRAMS / filename)
        written.append(fw_path)

    print(f"Generated and XML-validated {len(written)} 3D axonometric SVG diagrams.")
    return written


if __name__ == "__main__":
    generate_all()
