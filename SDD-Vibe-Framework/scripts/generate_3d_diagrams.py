#!/usr/bin/env python3
"""Generate editorial 2D and pure 3D axonometric SVG diagrams for SDD-Vibe.

Follows the cathrynlavery/diagram-design editorial HTML+SVG approach:
- Pure 3D (2:1 dimetric axonometric) ONLY for layered stacks, pyramids, and spatial hubs
- Editorial 2D flowcharts/state-machines for sequential workflows, loops, and dataflows
- Auto-verified viewBox bounds (zero clipping) and XML well-formedness
- Outputs standalone .svg files (for GitHub Markdown) + gallery.html (editorial viewer)
"""
from __future__ import annotations

import re
import shutil
import xml.etree.ElementTree as ET
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FW_DIAGRAMS = ROOT / "docs" / "diagrams"
REPO_DIAGRAMS = ROOT.parent / "docs" / "diagrams"

OBSOLETE_SVGS = (
    "3d-cicd-devops.svg",
    "3d-feature-lifecycle.svg",
    "3d-mission-control-dashboard.svg",
)

PALETTE = {
    "sky": ("#0284c7", "#0369a1", "#075985", "#38bdf8", "#e0f2fe", "#082f49"),
    "indigo": ("#4f46e5", "#4338ca", "#3730a3", "#818cf8", "#e0e7ff", "#1e1b4b"),
    "violet": ("#7c3aed", "#6d28d9", "#5b21b6", "#c084fc", "#f3e8ff", "#2e1065"),
    "emerald": ("#059669", "#047857", "#065f46", "#34d399", "#d1fae5", "#022c22"),
    "amber": ("#d97706", "#b45309", "#92400e", "#fbbf24", "#fef3c7", "#451a03"),
    "rose": ("#e11d48", "#be123c", "#9f1239", "#fb7185", "#ffe4e6", "#4c0519"),
    "slate": ("#334155", "#1e293b", "#0f172a", "#94a3b8", "#f1f5f9", "#0f172a"),
}


def iso(x: float, y: float, z: float, ox: float = 480.0, oy: float = 360.0) -> tuple[float, float]:
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
    ox: float = 480.0, oy: float = 360.0,
) -> str:
    """Render an extruded 3D isometric slab with top, left, and right faces + centered label."""
    top_c, left_c, right_c, stroke_c, text_c, _ = PALETTE[color_key]

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
            f'font-family="Inter, Segoe UI, system-ui, sans-serif" font-size="12.5" font-weight="700" fill="{text_c}">{escape(title)}</text>'
        )
    if subtitle:
        parts.append(
            f'<text x="{cx}" y="{cy + 13}" text-anchor="middle" '
            f'font-family="JetBrains Mono, Consolas, monospace" font-size="10" fill="#e2e8f0" opacity="0.92">{escape(subtitle)}</text>'
        )
    return "\n  ".join(parts)


def draw_card(
    x: float, y: float, w: float, h: float,
    color_key: str,
    title: str,
    subtitle: str = "",
    badge: str = "",
) -> str:
    """Render an editorial 2D card (cathrynlavery/diagram-design style)."""
    _, _, _, stroke_c, text_c, fill_c = PALETTE[color_key]
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill_c}" stroke="{stroke_c}" stroke-width="1.6"/>',
    ]
    if badge:
        bw = max(26, len(badge) * 7.2 + 12)
        parts.append(
            f'<rect x="{x + 12}" y="{y + 10}" width="{bw:.1f}" height="18" rx="5" fill="{stroke_c}" opacity="0.18"/>'
            f'<text x="{x + 12 + bw / 2:.1f}" y="{y + 22.5}" text-anchor="middle" '
            f'font-family="JetBrains Mono, Consolas, monospace" font-size="9.5" font-weight="700" fill="{stroke_c}">{escape(badge)}</text>'
        )
        ty = y + 45
    else:
        ty = y + (h / 2 - 4 if subtitle else h / 2 + 4)

    parts.append(
        f'<text x="{x + w / 2:.1f}" y="{ty:.1f}" text-anchor="middle" '
        f'font-family="Inter, Segoe UI, system-ui, sans-serif" font-size="13" font-weight="700" fill="{text_c}">{escape(title)}</text>'
    )
    if subtitle:
        parts.append(
            f'<text x="{x + w / 2:.1f}" y="{ty + 17:.1f}" text-anchor="middle" '
            f'font-family="JetBrains Mono, Consolas, monospace" font-size="10.2" fill="#cbd5e1" opacity="0.9">{escape(subtitle)}</text>'
        )
    return "\n  ".join(parts)


def draw_diamond(cx: float, cy: float, rx: float, ry: float, color_key: str, label: str) -> str:
    _, _, _, stroke_c, text_c, fill_c = PALETTE[color_key]
    p = pts([(cx, cy - ry), (cx + rx, cy), (cx, cy + ry), (cx - rx, cy)])
    return (
        f'<polygon points="{p}" fill="{fill_c}" stroke="{stroke_c}" stroke-width="1.8"/>\n  '
        f'<text x="{cx}" y="{cy + 4}" text-anchor="middle" font-family="Inter, Segoe UI, sans-serif" '
        f'font-size="11.5" font-weight="700" fill="{text_c}">{escape(label)}</text>'
    )


def draw_arrow(
    x1: float, y1: float, x2: float, y2: float,
    color: str = "#64748b", label: str = "", dashed: bool = False,
    label_dx: float = 0, label_dy: float = -7,
) -> str:
    dash = ' stroke-dasharray="5,4"' if dashed else ""
    parts = [
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1.8"{dash} marker-end="url(#arrow-{color.lstrip("#")})"/>'
    ]
    if label:
        mx, my = (x1 + x2) / 2 + label_dx, (y1 + y2) / 2 + label_dy
        parts.append(
            f'<text x="{mx:.1f}" y="{my:.1f}" text-anchor="middle" font-family="JetBrains Mono, monospace" '
            f'font-size="9.5" font-weight="600" fill="{color}">{escape(label)}</text>'
        )
    return "\n  ".join(parts)


def wrap_svg(
    title: str,
    subtitle: str,
    body: str,
    width: int = 960,
    height: int = 620,
    legend: list[tuple[str, str]] | None = None,
    mode_label: str = "SDD-Vibe · diagram-design",
    is_3d: bool = True,
) -> str:
    legend_svg = ""
    if legend:
        items = []
        lx = 36.0
        for color_key, label in legend:
            top_c, _, _, stroke_c, _, _ = PALETTE[color_key]
            items.append(
                f'<rect x="{lx}" y="{height - 34}" width="12" height="12" rx="3" fill="{top_c}" stroke="{stroke_c}" stroke-width="1.2"/>'
                f'<text x="{lx + 18}" y="{height - 24}" font-family="Inter, Segoe UI, sans-serif" font-size="11" fill="#cbd5e1">{escape(label)}</text>'
            )
            lx += 24 + len(label) * 6.8 + 18
        legend_svg = "\n  ".join(items)

    pattern_def = (
        '<pattern id="bgGrid" width="40" height="23.1" patternUnits="userSpaceOnUse">'
        '<path d="M 0 11.55 L 20 0 L 40 11.55 L 20 23.1 Z" fill="none" stroke="#1e293b" stroke-width="0.6" opacity="0.5"/>'
        '</pattern>'
        if is_3d
        else '<pattern id="bgGrid" width="24" height="24" patternUnits="userSpaceOnUse">'
             '<circle cx="12" cy="12" r="0.9" fill="#1e293b" opacity="0.75"/>'
             '</pattern>'
    )

    arrow_colors = ["64748b", "38bdf8", "818cf8", "c084fc", "34d399", "fbbf24", "fb7185"]
    markers = "\n    ".join(
        f'<marker id="arrow-{c}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 1.5 L 9 5 L 0 8.5 z" fill="#{c}"/></marker>'
        for c in arrow_colors
    )
    group_open = '<g filter="url(#glow)">' if is_3d else "<g>"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" role="img" aria-label="{escape(title)}">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="55%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    {pattern_def}
    <filter id="glow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="8" stdDeviation="6" flood-color="#000000" flood-opacity="0.42"/>
    </filter>
    {markers}
  </defs>
  <rect width="{width}" height="{height}" rx="14" fill="url(#bgGrad)" stroke="#1e293b" stroke-width="1.5"/>
  <rect width="{width}" height="{height}" rx="14" fill="url(#bgGrid)"/>
  <text x="32" y="38" font-family="Inter, Segoe UI, system-ui, sans-serif" font-size="19" font-weight="800" fill="#f8fafc">{escape(title)}</text>
  <text x="32" y="58" font-family="JetBrains Mono, Consolas, monospace" font-size="11.2" fill="#94a3b8">{escape(subtitle)}</text>
  {group_open}
  {body}
  </g>
  {legend_svg}
  <text x="{width - 28}" y="{height - 24}" text-anchor="end" font-family="JetBrains Mono, Consolas, monospace" font-size="10" fill="#64748b">{escape(mode_label)}</text>
</svg>
'''


# ==============================================================================
# PURE 3D AXONOMETRIC DIAGRAMS (Layered Stacks, Pyramids & Spatial Hubs)
# ==============================================================================

def build_exploded_stack(
    title: str,
    subtitle: str,
    layers: list[tuple[str, str, str]],
    base_label: str | None = None,
) -> str:
    """Build a vertical exploded 3D axonometric stack with guaranteed zero clipping and zero label overlap."""
    n = len(layers)
    ox = 480.0
    z_step = 96 if n >= 5 else 104
    slab_w, slab_d, slab_h = 200.0, 116.0, 22.0
    height = 175 + n * z_step + (155 if base_label else 35)
    oy = height - (275.0 if base_label else 160.0)

    body_parts = []
    top_pt = iso(slab_w / 2, slab_d / 2, 16 + (n - 1) * z_step + slab_h + 24, ox, oy)
    bot_pt = iso(slab_w / 2, slab_d / 2, -60 if base_label else 10, ox, oy)
    body_parts.append(
        f'<line x1="{bot_pt[0]}" y1="{bot_pt[1]}" x2="{top_pt[0]}" y2="{top_pt[1]}" '
        f'stroke="#475569" stroke-width="1.5" stroke-dasharray="5,5"/>'
    )

    if base_label:
        body_parts.append(draw_box(-25, -20, -82, 250, 156, 18, "slate", base_label, "Shared Governance Baseplate", ox, oy))

    for i, (color_key, l_title, l_sub) in enumerate(layers):
        z = 16 + i * z_step
        body_parts.append(draw_box(0, 0, z, slab_w, slab_d, slab_h, color_key, l_title, l_sub, ox, oy))

    for i, (color_key, _, _) in enumerate(layers):
        z = 16 + i * z_step + slab_h / 2 + 4
        edge = iso(slab_w, slab_d / 2, z, ox, oy)
        _, _, _, stroke_c, _, _ = PALETTE[color_key]
        body_parts.append(
            f'<line x1="{edge[0]}" y1="{edge[1]}" x2="{edge[0] + 46}" y2="{edge[1]}" stroke="{stroke_c}" stroke-width="1.2" stroke-dasharray="3,3"/>'
            f'<circle cx="{edge[0] + 54}" cy="{edge[1]}" r="11" fill="#0f172a" stroke="{stroke_c}" stroke-width="1.5"/>'
            f'<text x="{edge[0] + 54}" y="{edge[1] + 4}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" font-weight="700" fill="{stroke_c}">L{i + 1}</text>'
        )

    return wrap_svg(title, subtitle, "\n  ".join(body_parts), width=960, height=height, mode_label="SDD-Vibe · Pure 3D Axonometric", is_3d=True)


def build_hub_3d(
    title: str,
    subtitle: str,
    hub: tuple[float, float, float, float, float, float, str, str, str],
    satellites: list[tuple[float, float, float, float, float, float, str, str, str]],
    legend: list[tuple[str, str]],
) -> str:
    """Build a centered 3D hub-and-spoke topology with non-overlapping satellites and isometric connectors."""
    ox, oy = 480.0, 315.0
    hx, hy, hz, hw, hd, hh, hc, ht, hs = hub
    hub_bot = iso(hx + hw / 2, hy + hd / 2, hz, ox, oy)

    parts: list[str] = []
    # Draw baseplate satellites first
    for sx, sy, sz, sw, sd, sh, sc, st, ss in satellites:
        parts.append(draw_box(sx, sy, sz, sw, sd, sh, sc, st, ss, ox, oy))

    # Draw isometric dashed connectors from satellites up to elevated hub
    for sx, sy, sz, sw, sd, sh, sc, _, _ in satellites:
        sat_top = iso(sx + sw / 2, sy + sd / 2, sz + sh, ox, oy)
        _, _, _, stroke_c, _, _ = PALETTE[sc]
        parts.append(
            f'<line x1="{sat_top[0]}" y1="{sat_top[1]}" x2="{hub_bot[0]}" y2="{hub_bot[1]}" '
            f'stroke="{stroke_c}" stroke-width="1.5" stroke-dasharray="4,4" opacity="0.85"/>'
            f'<circle cx="{sat_top[0]}" cy="{sat_top[1]}" r="3.5" fill="{stroke_c}"/>'
        )

    # Draw elevated hub last (painter's order)
    parts.append(draw_box(hx, hy, hz, hw, hd, hh, hc, ht, hs, ox, oy))

    return wrap_svg(
        title, subtitle, "\n  ".join(parts),
        width=960, height=600, legend=legend,
        mode_label="SDD-Vibe · Pure 3D Topology", is_3d=True,
    )


def build_pyramid_3d() -> str:
    """3D Isometric Testing Pyramid (Unit -> Integration -> E2E + AC Traceability) with non-overlapping tiers."""
    ox, oy = 410.0, 395.0
    parts = [
        draw_box(-20, -15, -82, 240, 150, 16, "slate", "logs/test.log & AC Traceability", "AC-FEAT###-## -> TEST-FEAT###-##", ox, oy),
        draw_box(0, 0, 22, 200, 120, 30, "sky", "UNIT TESTS (60-70%)", "tests/unit/ · Domain & Contracts", ox, oy),
        draw_box(28, 18, 118, 144, 84, 28, "indigo", "INTEGRATION (20-30%)", "tests/integration/ · API & DB", ox, oy),
        draw_box(55, 34, 204, 90, 52, 26, "violet", "E2E (10%)", "Browser Journeys", ox, oy),
    ]
    callouts = [
        (37, 200, 60, "sky", "60-70% Unit"),
        (132, 172, 60, "indigo", "20-30% Integration"),
        (217, 145, 60, "violet", "10% E2E"),
    ]
    for cz, ex, ey, ckey, clabel in callouts:
        edge = iso(ex, ey, cz, ox, oy)
        _, _, _, stroke_c, text_c, _ = PALETTE[ckey]
        parts.append(
            f'<line x1="{edge[0]}" y1="{edge[1]}" x2="725" y2="{edge[1]}" stroke="{stroke_c}" stroke-width="1.2" stroke-dasharray="3,3"/>'
            f'<rect x="730" y="{edge[1] - 12}" width="155" height="24" rx="6" fill="#0f172a" stroke="{stroke_c}" stroke-width="1.3"/>'
            f'<text x="807.5" y="{edge[1] + 4}" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="{text_c}">{clabel}</text>'
        )
    return wrap_svg(
        "3D Isometric Testing Pyramid & AC Traceability",
        "Red-Green-Refactor TDD Gate · Zero-Regression Verification",
        "\n  ".join(parts),
        width=960, height=665,
        legend=[("sky", "Unit"), ("indigo", "Integration"), ("violet", "E2E"), ("slate", "Audit Log")],
        mode_label="SDD-Vibe · Pure 3D Pyramid", is_3d=True,
    )


# ==============================================================================
# EDITORIAL 2D DIAGRAMS (cathrynlavery/diagram-design Style)
# ==============================================================================

def build_prompt_workflow_2d() -> str:
    parts = [
        # Stage A container
        '<rect x="32" y="84" width="896" height="205" rx="12" fill="#0b1120" stroke="#334155" stroke-width="1.3"/>',
        '<text x="48" y="108" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#c084fc">STAGE A — ARCHITECTURE DISCOVERY &amp; FRONTEND SENSORY DEMO</text>',
        draw_card(48, 124, 170, 74, "sky", "1. Setup & Verify", "Check 18 /-ca-agent", "STEP 0"),
        draw_card(254, 124, 185, 74, "indigo", "2. Prompt 1: Plan", "HLD/LLD · Design Tokens", "PHASE 1"),
        draw_diamond(505, 161, 44, 34, "amber", "OK?"),
        draw_card(585, 124, 165, 74, "violet", "3. UI Sensory Shell", "PROTOTYPE · Mock State", "PHASE 2"),
        draw_card(780, 124, 132, 74, "violet", "4. Live Demo", "/run-ca-agent :3000", "VERIFY"),
        draw_arrow(218, 161, 254, 161, "#38bdf8"),
        draw_arrow(439, 161, 461, 161, "#818cf8"),
        draw_arrow(549, 161, 585, 161, "#34d399", "Yes", label_dy=-8),
        draw_arrow(750, 161, 780, 161, "#c084fc"),
        # Revise loop
        '<path d="M 505 195 L 505 245 L 346 245 L 346 198" fill="none" stroke="#fbbf24" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arrow-fbbf24)"/>',
        '<text x="425" y="262" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#fbbf24">Revise Plan / Architecture</text>',
        # Iterate UI loop
        '<path d="M 846 198 L 846 245 L 667 245 L 667 198" fill="none" stroke="#c084fc" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arrow-c084fc)"/>',
        '<text x="756" y="262" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#c084fc">Tune UI / Vibe</text>',

        # Transition Stage A -> Stage B
        draw_arrow(846, 289, 846, 325, "#34d399", "UI Signed Off", label_dx=54, label_dy=-10),

        # Stage B container
        '<rect x="32" y="325" width="896" height="215" rx="12" fill="#0b1120" stroke="#334155" stroke-width="1.3"/>',
        '<text x="48" y="349" font-family="JetBrains Mono, monospace" font-size="11" font-weight="700" fill="#34d399">STAGE B — FORMAL SPEC LOCK, TDD RED-GREEN-REFACTOR &amp; SHIP</text>',
        draw_card(48, 370, 175, 74, "emerald", "8. Release Gate", "/release-check-ca-agent", "PHASE 4"),
        draw_card(260, 370, 195, 74, "amber", "7. Review & SAST", "/review · /security-audit", "AUDIT"),
        draw_card(495, 370, 185, 74, "emerald", "6. GREEN: Implement", "/tdd · /implement", "TDD"),
        draw_card(720, 370, 192, 74, "rose", "5. Spec Lock & RED", "APPROVED · /testing", "PHASE 3"),
        draw_arrow(720, 407, 680, 407, "#fb7185", "Fail", label_dy=-8),
        draw_arrow(495, 407, 455, 407, "#34d399", "Pass", label_dy=-8),
        draw_arrow(260, 407, 223, 407, "#fbbf24", "Clean", label_dy=-8),
        # Next feature loop
        '<path d="M 587 444 L 587 498 L 816 498 L 816 444" fill="none" stroke="#38bdf8" stroke-width="1.6" stroke-dasharray="5,4" marker-end="url(#arrow-38bdf8)"/>',
        '<text x="701" y="515" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10" fill="#38bdf8">Next Feature Spec (1 Spec at a Time)</text>',
    ]
    return wrap_svg(
        "SDD-Vibe Prompt Workflow (Stage A -> Stage B)",
        "Editorial 2D Swimlane · Frontend Sensory Sign-Off -> Contract-First TDD & Release",
        "\n  ".join(parts),
        width=960, height=595,
        legend=[("sky", "Plan"), ("violet", "Vibe UI"), ("rose", "TDD Red"), ("emerald", "TDD Green / Ship"), ("amber", "Gate / Audit")],
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_traceability_contract_2d() -> str:
    nodes = [
        ("sky", "CAP-###", "Capability", "docs/product.md"),
        ("indigo", "REQ-###", "Requirement", "docs/prd.md"),
        ("violet", "FEAT-###", "Feature Spec", "docs/features/"),
        ("amber", "AC-FEAT###", "Acceptance", "Given/When/Then"),
        ("emerald", "TEST-###", "TDD Suite", "tests/ + run-tests"),
        ("slate", "APR-###", "Approval", "docs/approvals/"),
    ]
    parts = []
    start_x = 36
    card_w = 132
    gap = 20
    for i, (ck, badge, title, sub) in enumerate(nodes):
        cx = start_x + i * (card_w + gap)
        parts.append(draw_card(cx, 128, card_w, 92, ck, title, sub, badge))
        if i < len(nodes) - 1:
            parts.append(draw_arrow(cx + card_w, 174, cx + card_w + gap, 174, "#38bdf8"))

    # Evidence & Audit bar underneath
    parts.append('<rect x="36" y="268" width="892" height="74" rx="10" fill="#0b1120" stroke="#334155" stroke-width="1.4"/>')
    parts.append('<text x="482" y="296" text-anchor="middle" font-family="Inter, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#f8fafc">Continuous Verification &amp; Evidence Chain</text>')
    parts.append('<text x="482" y="318" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10.8" fill="#94a3b8">/spec-check-ca-agent  ·  logs/test.log  ·  Dashboard AC Engine (:4200)  ·  /verify-ca-agent</text>')
    for i in range(6):
        cx = start_x + i * (card_w + gap) + card_w / 2
        parts.append(f'<line x1="{cx}" y1="220" x2="{cx}" y2="268" stroke="#475569" stroke-width="1.3" stroke-dasharray="4,3"/>')

    return wrap_svg(
        "Spec-to-Code Traceability Contract",
        "Every Line of Production Code Traces Back to an Approved Capability & Acceptance Criterion",
        "\n  ".join(parts),
        width=960, height=400,
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_staged_web_dev_2d() -> str:
    stages = [
        ("violet", "STAGE A", "Frontend & Sensory Demo", "UI · Responsive · Mock State · :3000"),
        ("sky", "STAGE B", "Backend & Persistence", "APIs · DB Schema · Migrations"),
        ("amber", "STAGE C", "Auth, RBAC & Security", "Sessions · RLS · Zod · Rate Limit"),
        ("emerald", "STAGE D", "Testing, SAST & Ship", "Unit/E2E · /security-audit · Release"),
    ]
    parts = []
    w, gap = 205, 26
    x0 = 32
    for i, (ck, badge, title, sub) in enumerate(stages):
        x = x0 + i * (w + gap)
        parts.append(draw_card(x, 125, w, 106, ck, title, sub, badge))
        if i < len(stages) - 1:
            parts.append(draw_arrow(x + w, 178, x + w + gap, 178, "#34d399", "Gate", label_dy=-8))

    parts.append('<rect x="32" y="272" width="898" height="58" rx="10" fill="#0b1120" stroke="#334155" stroke-width="1.3"/>')
    parts.append('<text x="481" y="305" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="11.2" fill="#e2e8f0">Directive 8 Rule: Never build all features at once — verify Stage A visually (/run-ca-agent) before Stage B/C/D</text>')
    return wrap_svg(
        "Staged Web App Development Pipeline",
        "Frontend-First Sensory Verification -> Progressive Backend, Auth & QA Hardening",
        "\n  ".join(parts),
        width=960, height=390,
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_5step_cyclic_loop_2d() -> str:
    steps = [
        ("sky", "STEP 1", "Read Prompt", "Scope & constraints"),
        ("indigo", "STEP 2", "Analyze & Plan", "HLD/LLD & risk"),
        ("violet", "STEP 3", "Check docs/ & playbooks/", "Rules & architecture"),
        ("amber", "STEP 4", "Review *.md Guidelines", "Identify doc updates"),
        ("emerald", "STEP 5", "Update Living Docs", "Sync before coding"),
        ("rose", "STEP 6", "Spec-by-Spec Build", "One FEAT-### at a time"),
    ]
    parts = []
    # Top row 1 -> 2 -> 3, Bottom row 6 <- 5 <- 4
    coords = [
        (48, 112), (355, 112), (662, 112),
        (48, 264), (355, 264), (662, 264),
    ]
    # Note: 1->2->3 (top L-to-R), 3->4 (down), 4->5->6 (bottom R-to-L or L-to-R)
    # Let's arrange bottom row R-to-L so flow is a true loop: 4 at right, 5 middle, 6 left!
    layout = [
        (steps[0], 48, 112),
        (steps[1], 355, 112),
        (steps[2], 662, 112),
        (steps[3], 662, 268),
        (steps[4], 355, 268),
        (steps[5], 48, 268),
    ]
    cw, ch = 250, 88
    for (ck, badge, title, sub), x, y in layout:
        parts.append(draw_card(x, y, cw, ch, ck, title, sub, badge))

    parts.append(draw_arrow(48 + cw, 156, 355, 156, "#38bdf8"))
    parts.append(draw_arrow(355 + cw, 156, 662, 156, "#818cf8"))
    parts.append(draw_arrow(787, 200, 787, 268, "#fbbf24"))
    parts.append(draw_arrow(662, 312, 355 + cw, 312, "#34d399"))
    parts.append(draw_arrow(355, 312, 48 + cw, 312, "#fb7185"))
    parts.append(draw_arrow(173, 268, 173, 200, "#64748b", "Next Spec", dashed=True, label_dx=42, label_dy=0))

    return wrap_svg(
        "Directive 1: 5-Step Cyclic Loop & Spec-by-Spec Pacing",
        "Never Code Speculatively · Update Living Documentation Before Implementation",
        "\n  ".join(parts),
        width=960, height=415,
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_mission_control_2d() -> str:
    parts = [
        draw_card(44, 115, 235, 90, "slate", "docs/ & .git/ & logs/", "Markdown AST · HEAD · Logs", "WORKSPACE"),
        draw_card(360, 115, 240, 90, "sky", "parser.js + server.js", "Zero-Dep Node · SSE Stream", "DAEMON :4200"),
        draw_card(680, 115, 235, 90, "indigo", "In-IDE Bento UI", "Task #0 Top · DD-MM-YYYY", "VIEWPORT"),
        draw_card(360, 265, 240, 76, "rose", "Local Security Guard", "127.0.0.1 · Host + CSRF", "HARDENED"),
        draw_arrow(279, 160, 360, 160, "#38bdf8", "Watch"),
        draw_arrow(600, 160, 680, 160, "#818cf8", "SSE"),
        draw_arrow(480, 265, 480, 205, "#fb7185", "Enforce", label_dx=34, label_dy=2),
    ]
    return wrap_svg(
        "In-IDE Project-Manager-Dashboard Architecture",
        "Zero-Dependency Local Daemon (127.0.0.1:4200) · Live SSE Telemetry & AC Engine",
        "\n  ".join(parts),
        width=960, height=405,
        legend=[("slate", "Workspace"), ("sky", "Daemon"), ("indigo", "IDE Viewport"), ("rose", "Security")],
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_cicd_devops_2d() -> str:
    gates = [
        ("sky", "GATE 1", "Lint & Format", "ESLint · Prettier"),
        ("indigo", "GATE 2", "Docs & Manifest", "check_docs · manifest"),
        ("emerald", "GATE 3", "Test Suites", "run-tests.js (10/10)"),
        ("rose", "GATE 4", "Secret Scan", "Gitleaks · Regex"),
    ]
    parts = []
    w, gap, x0 = 198, 32, 36
    for i, (ck, badge, title, sub) in enumerate(gates):
        x = x0 + i * (w + gap)
        parts.append(draw_card(x, 128, w, 92, ck, title, sub, badge))
        if i < len(gates) - 1:
            parts.append(draw_arrow(x + w, 174, x + w + gap, 174, "#34d399"))
    parts.append('<rect x="36" y="264" width="888" height="58" rx="10" fill="#022c22" stroke="#34d399" stroke-width="1.4"/>')
    parts.append('<text x="480" y="298" text-anchor="middle" font-family="Inter, Segoe UI, sans-serif" font-size="13" font-weight="700" fill="#d1fae5">Zero-Error Release Gate Passed -> /release-check-ca-agent Approved</text>')
    return wrap_svg(
        "CI/CD & Quality Gate Pipeline",
        ".github/workflows/frameworks-ci.yml · Automated Zero-Error Release Verification",
        "\n  ".join(parts),
        width=960, height=385,
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_feature_lifecycle_2d() -> str:
    states = [
        ("violet", "STATE 1", "PROTOTYPE", "Phase 2 Sensory Demo"),
        ("sky", "STATE 2", "DRAFT", "AC-FEAT###-## Authoring"),
        ("amber", "STATE 3", "IN REVIEW", "/spec-check-ca-agent"),
        ("emerald", "STATE 4", "APPROVED", "APR-### · TDD Locked"),
    ]
    parts = []
    w, gap, x0 = 198, 32, 36
    for i, (ck, badge, title, sub) in enumerate(states):
        x = x0 + i * (w + gap)
        parts.append(draw_card(x, 120, w, 92, ck, title, sub, badge))
        if i < len(states) - 1:
            parts.append(draw_arrow(x + w, 166, x + w + gap, 166, "#38bdf8"))

    # Change Request feedback loop from APPROVED -> IN REVIEW
    parts.append('<path d="M 825 212 L 825 272 L 595 272 L 595 212" fill="none" stroke="#fbbf24" stroke-width="1.8" stroke-dasharray="5,4" marker-end="url(#arrow-fbbf24)"/>')
    parts.append('<text x="710" y="290" text-anchor="middle" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="600" fill="#fbbf24">CR-### Change Request (/change-request-ca-agent)</text>')

    return wrap_svg(
        "Feature Spec Lifecycle & Change Control",
        "PROTOTYPE -> DRAFT -> IN REVIEW -> APPROVED (APR-###) -> CR-###",
        "\n  ".join(parts),
        width=960, height=360,
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


def build_executive_overview_2d() -> str:
    parts = [
        # Stage A container (left)
        '<rect x="36" y="92" width="420" height="210" rx="12" fill="#0b1120" stroke="#334155" stroke-width="1.4"/>',
        '<text x="52" y="116" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="#c084fc">STAGE A — VIBE DISCOVERY &amp; SENSORY DEMO</text>',
        draw_card(52, 132, 184, 150, "sky", "Phase 1: Architecture", "Domain · HLD/LLD · Tokens", "PHASE 1"),
        draw_card(256, 132, 184, 150, "violet", "Phase 2: Sensory Demo", "PROTOTYPE -> DRAFT (:3000)", "PHASE 2"),

        # Visual Sign-Off arrow Stage A -> Stage B
        draw_arrow(456, 197, 504, 197, "#34d399", "Sign-Off", label_dy=-9),

        # Stage B container (right)
        '<rect x="504" y="92" width="420" height="210" rx="12" fill="#0b1120" stroke="#334155" stroke-width="1.4"/>',
        '<text x="520" y="116" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="#34d399">STAGE B — SPEC LOCK, TDD &amp; RELEASE</text>',
        draw_card(520, 132, 184, 150, "emerald", "Phase 3: Spec & TDD", "APPROVED · Red-Green", "PHASE 3"),
        draw_card(724, 132, 184, 150, "amber", "Phase 4: Audit & Ship", "/review · /security · /release", "PHASE 4"),

        # Governance arrows down to Shared Core
        draw_arrow(246, 302, 246, 354, "#818cf8", "Governed By", label_dx=46, label_dy=0),
        draw_arrow(714, 302, 714, 354, "#38bdf8", "Enforced By", label_dx=46, label_dy=0),

        # Unified Governance & Mission Control Base
        '<rect x="36" y="354" width="888" height="148" rx="12" fill="#0b1120" stroke="#475569" stroke-width="1.5"/>',
        '<text x="52" y="378" font-family="JetBrains Mono, monospace" font-size="10.5" font-weight="700" fill="#94a3b8">UNIFIED GOVERNANCE &amp; MISSION CONTROL CORE</text>',
        draw_card(52, 394, 272, 92, "indigo", ".agents/ Asset Engine", "18 Commands · 18 Skills · Hooks", "PORTABLE"),
        draw_card(344, 394, 272, 92, "sky", "In-IDE Mission Control", "Zero-Dep Daemon (Port 4200)", "TELEMETRY"),
        draw_card(636, 394, 272, 92, "slate", "docs/ Governance Engine", "Plan · Prompts · Spec · ADRs", "CONTRACTS"),
    ]
    return wrap_svg(
        "SDD-Vibe 1-in-2 Executive Overview",
        "Frontend-First Sensory Discovery + Contract-First TDD & Unified Governance",
        "\n  ".join(parts),
        width=960, height=565,
        legend=[("sky", "Architecture"), ("violet", "Vibe UI"), ("emerald", "TDD"), ("amber", "Audit/Ship"), ("indigo", "Governance")],
        mode_label="SDD-Vibe · Editorial 2D", is_3d=False,
    )


# ==============================================================================
# VALIDATION & GALLERY GENERATION
# ==============================================================================

def verify_svg_bounds(name: str, svg_content: str) -> None:
    ET.fromstring(svg_content)
    vb_m = re.search(r'viewBox="([^"]+)"', svg_content)
    assert vb_m, f"{name}: missing viewBox"
    _, _, vw, vh = map(float, vb_m.group(1).split())

    xs, ys = [], []
    for m in re.finditer(r'points="([^"]+)"', svg_content):
        for pair in m.group(1).split():
            x, y = map(float, pair.split(","))
            xs.append(x)
            ys.append(y)
    for m in re.finditer(r'\b(?:x|x1|x2|cx)="([0-9.-]+)"', svg_content):
        xs.append(float(m.group(1)))
    for m in re.finditer(r'\b(?:y|y1|y2|cy)="([0-9.-]+)"', svg_content):
        ys.append(float(m.group(1)))

    if xs and ys:
        assert min(xs) >= 0 and max(xs) <= vw, f"{name}: X bounds [{min(xs)}, {max(xs)}] exceed viewBox width {vw}"
        assert min(ys) >= 0 and max(ys) <= vh, f"{name}: Y bounds [{min(ys)}, {max(ys)}] exceed viewBox height {vh}"


def write_gallery(target_dir: Path, filenames: list[str]) -> None:
    cards = "\n".join(
        f'<section class="card"><h2>{escape(fn)}</h2><img src="{escape(fn)}" alt="{escape(fn)}" loading="lazy"/></section>'
        for fn in filenames
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <title>SDD-Vibe Diagram Gallery (diagram-design)</title>
  <style>
    body {{ margin: 0; padding: 32px; background: #050811; color: #e2e8f0; font-family: Inter, Segoe UI, system-ui, sans-serif; }}
    header {{ max-width: 1200px; margin: 0 auto 28px; }}
    h1 {{ margin: 0 0 6px; font-size: 24px; color: #f8fafc; }}
    p {{ margin: 0; color: #94a3b8; font-size: 14px; }}
    .grid {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(520px, 1fr)); gap: 22px; }}
    .card {{ background: #0b1120; border: 1px solid #1e293b; border-radius: 12px; padding: 14px; }}
    .card h2 {{ margin: 0 0 10px; font-size: 13px; font-family: JetBrains Mono, Consolas, monospace; color: #38bdf8; }}
    .card img {{ width: 100%; height: auto; display: block; border-radius: 8px; }}
  </style>
</head>
<body>
  <header>
    <h1>SDD-Vibe Editorial Diagram Gallery</h1>
    <p>9 Pure 3D Axonometric Diagrams + 7 Editorial 2D Diagrams (cathrynlavery/diagram-design standard)</p>
  </header>
  <main class="grid">{cards}</main>
</body>
</html>
"""
    (target_dir / "gallery.html").write_text(html, encoding="utf-8", newline="\n")


def generate_all() -> list[Path]:
    FW_DIAGRAMS.mkdir(parents=True, exist_ok=True)
    REPO_DIAGRAMS.mkdir(parents=True, exist_ok=True)

    for old_name in OBSOLETE_SVGS:
        for d in (FW_DIAGRAMS, REPO_DIAGRAMS):
            p = d / old_name
            if p.exists():
                p.unlink()

    specs: dict[str, str] = {
        # --- 9 Pure 3D Axonometric Diagrams ---
        "3d-sdd-vibe-pipeline.svg": build_exploded_stack(
            "SDD-Vibe: 1-in-2 Single Workflow (3D Stack)",
            "Phase 1 Architecture -> Phase 2 Sensory Demo (:3000) -> Phase 3 TDD -> Phase 4 Ship",
            [
                ("sky", "Phase 1: Architecture & Vibe", "Domain Research · HLD/LLD · Tokens"),
                ("violet", "Phase 2: Frontend Sensory Demo", "PROTOTYPE -> DRAFT · Live UI (:3000)"),
                ("emerald", "Phase 3: Spec Lock & TDD", "APPROVED Spec · Red-Green-Refactor"),
                ("amber", "Phase 4: Quality Audit & Ship", "/review · /security-audit · /release"),
            ],
            base_label=".agents/ (18 Commands & 18 Skills) + Dashboard (:4200)",
        ),
        "3d-system-architecture.svg": build_exploded_stack(
            "5-Tier System Architecture & Clean Layers (3D)",
            "Presentation -> Edge/SSR -> API Gateway -> Domain Core -> Persistence",
            [
                ("slate", "Tier 5: Persistence & Cache", "PostgreSQL / RLS · Redis · Logs"),
                ("emerald", "Tier 4: Domain & App Core", "Clean Entities · Use Cases · TDD"),
                ("indigo", "Tier 3: API & Auth Gateway", "Zod Contracts · RBAC · Rate Limit"),
                ("sky", "Tier 2: Edge & SSR", "Next.js / CDN · WAF · Headers"),
                ("violet", "Tier 1: Client & Ingress", "Responsive UI · WCAG AA · TLS"),
            ],
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
                ("emerald", "Structured JSON Response", "Semantic HTTP Codes · Zero Leaks"),
                ("indigo", "Domain Service Execution", "Idempotency · Transaction Scope"),
                ("amber", "AuthN / RBAC Middleware", "401/403 Guards · Rate Limiting"),
                ("sky", "Zod / Schema Validation", "400/422 Field-Level Errors"),
            ],
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
        "3d-cross-ide-portability.svg": build_hub_3d(
            "Cross-IDE Portability Engine (3D Sync Hub)",
            "Canonical .agents/ -> scripts/sync_ide_adapters.py -> 8 AI Coding IDEs",
            (-75, -75, 140, 150, 150, 30, "indigo", "Canonical .agents/", "18 Commands · 18 Skills · Hooks"),
            [
                (-250, 20, 0, 150, 110, 24, "sky", "Claude & Antigravity", ".claude/ · .agents/workflows/"),
                (20, -250, 0, 150, 110, 24, "violet", "Cursor & Windsurf", ".cursor/ · .windsurf/"),
                (-120, 175, 0, 150, 110, 24, "emerald", "Codex & Copilot", ".codex/ · .github/prompts/"),
                (175, -120, 0, 150, 110, 24, "amber", "OpenCode & Trae", "AGENTS.md Discovery"),
            ],
            legend=[("indigo", "Canonical Hub"), ("sky", "Claude/AGY"), ("violet", "Cursor/Windsurf"), ("emerald", "Codex/Copilot"), ("amber", "OpenCode/Trae")],
        ),
        "3d-agentic-ecosystem.svg": build_hub_3d(
            "14-Team Agentic Ecosystem (3D Topology)",
            "Just-In-Time Opt-In Activation · Main Agent + Team 14 Orchestrator",
            (-75, -75, 140, 150, 150, 30, "indigo", "Main Orchestrator", "/team-ecosystem-ca-agent"),
            [
                (-250, 20, 0, 150, 110, 24, "amber", "Group 1: Strategy & PM", "Team 1 Kanban · Team 2 REA"),
                (20, -250, 0, 150, 110, 24, "violet", "Group 2: Design & Build", "Team 3 UI/UX · Team 4 Dev"),
                (-120, 175, 0, 150, 110, 24, "emerald", "Group 3: Verify & Ops", "Teams 5-8 QA · Teams 9-10 Ops"),
                (175, -120, 0, 150, 110, 24, "sky", "Group 4: Docs & Growth", "Teams 11-13 · Team 14 Guider"),
            ],
            legend=[("indigo", "Orchestrator"), ("amber", "Strategy"), ("violet", "Build"), ("emerald", "Verify/Ops"), ("sky", "Docs/Growth")],
        ),

        # --- 8 Editorial 2D Diagrams (diagram-design style) ---
        "workflow-executive-overview.svg": build_executive_overview_2d(),
        "workflow-prompt-pipeline.svg": build_prompt_workflow_2d(),
        "workflow-traceability-contract.svg": build_traceability_contract_2d(),
        "workflow-staged-web-dev.svg": build_staged_web_dev_2d(),
        "workflow-5step-cyclic-loop.svg": build_5step_cyclic_loop_2d(),
        "flow-mission-control-dashboard.svg": build_mission_control_2d(),
        "flow-cicd-devops.svg": build_cicd_devops_2d(),
        "flow-feature-lifecycle.svg": build_feature_lifecycle_2d(),
    }

    written: list[Path] = []
    for filename, svg_content in specs.items():
        verify_svg_bounds(filename, svg_content)
        fw_path = FW_DIAGRAMS / filename
        fw_path.write_text(svg_content, encoding="utf-8", newline="\n")
        shutil.copy2(fw_path, REPO_DIAGRAMS / filename)
        written.append(fw_path)

    filenames = list(specs.keys())
    write_gallery(FW_DIAGRAMS, filenames)
    write_gallery(REPO_DIAGRAMS, filenames)

    print(f"Generated, XML-validated, and bounds-checked {len(written)} SVG diagrams (9 Pure 3D + 7 Editorial 2D) + gallery.html.")
    return written


if __name__ == "__main__":
    generate_all()
