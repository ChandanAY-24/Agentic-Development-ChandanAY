#!/usr/bin/env python3
"""Embed pure 3D axonometric & editorial 2D SVG diagrams across .md files
and aligned 3D/2D Unicode workflow diagrams across playbooks/*.txt files.

Idempotent: refreshes existing <!-- SDD-VIBE-3D-DIAGRAM --> blocks and
=== 3D AXONOMETRIC WORKFLOW DIAGRAM === / === WORKFLOW DIAGRAM === blocks.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

FW_ROOT = Path(__file__).resolve().parent.parent
REPO_ROOT = FW_ROOT.parent
FW_DIAGRAMS = FW_ROOT / "docs" / "diagrams"
REPO_DIAGRAMS = REPO_ROOT / "docs" / "diagrams"

MARKER = "<!-- SDD-VIBE-3D-DIAGRAM -->"
TXT_MARKER_OLD = "=== 3D AXONOMETRIC WORKFLOW DIAGRAM ==="
TXT_MARKER_NEW = "=== WORKFLOW DIAGRAM (diagram-design) ==="

SKIP_NAMES = {
    "LICENSE.md",
    "LICENSE-DECISION.md",
    "CHANGELOG.md",
    "guideline-CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "PULL_REQUEST_TEMPLATE.md",
    "SOURCE-NOTES.md",
    "style-guide.md",
}


def pick_diagram(rel_posix: str) -> tuple[str, str]:
    """Return (svg_filename, caption) choosing Pure 3D vs Editorial 2D per domain."""
    p = rel_posix.lower()
    # Editorial 2D flows & workflows
    if "dashboard" in p:
        return "flow-mission-control-dashboard.svg", "In-IDE Project-Manager-Dashboard Architecture"
    if "prompt" in p:
        return "workflow-prompt-pipeline.svg", "SDD-Vibe Prompt Workflow (Stage A -> Stage B)"
    if "traceability" in p or "spec-check" in p or p.endswith("docs/spec.md"):
        return "workflow-traceability-contract.svg", "Spec-to-Code Traceability Contract"
    if "granular" in p or p.endswith("docs/design.md"):
        return "workflow-staged-web-dev.svg", "Staged Web App Development Pipeline"
    if "rules.md" in p or "constitution.md" in p:
        return "workflow-5step-cyclic-loop.svg", "5-Step Cyclic Loop & Spec-by-Spec Pacing"
    if "devops" in p or "deploy" in p or "environment" in p or "release" in p or "ci" in p or "runbook" in p or "observability" in p or "performance" in p:
        return "flow-cicd-devops.svg", "CI/CD & Quality Gate Pipeline"
    if "feature" in p or "spec" in p or "change" in p or "approval" in p or "prd" in p or "product" in p or "plan" in p or "task" in p or "phase" in p:
        return "flow-feature-lifecycle.svg", "Feature Spec Lifecycle & Change Control"

    # Pure 3D stacks, pyramids & spatial hubs
    if "token" in p:
        return "3d-token-optimization.svg", "Dual-Budget Token Optimization 3D Stack"
    if "team" in p or "ecosystem" in p or "hierarchy" in p:
        return "3d-agentic-ecosystem.svg", "14-Team Agentic Ecosystem 3D Topology"
    if "activation" in p or "ide" in p or "claude.md" in p or "gemini.md" in p or "agents.md" in p or "hooks" in p or "plugins" in p or "connectors" in p:
        return "3d-cross-ide-portability.svg", "Cross-IDE Portability Engine 3D Sync Hub"
    if "test" in p or "tdd" in p or "acceptance" in p or "verify" in p or "error" in p or "debug" in p:
        return "3d-testing-pyramid.svg", "3D Isometric Testing Pyramid & AC Traceability"
    if "security" in p or "audit" in p:
        return "3d-security-defense.svg", "Defense-in-Depth Security 3D Stack"
    if "database" in p or "migration" in p:
        return "3d-database-persistence.svg", "Persistence & Migration 3D Stack"
    if "api" in p:
        return "3d-api-gateway.svg", "API Contract & Request Lifecycle 3D Stack"
    if "architecture" in p or "adr" in p or "tech-stack" in p or "accessibility" in p:
        return "3d-system-architecture.svg", "5-Tier System Architecture & Clean Layers 3D"
    return "3d-sdd-vibe-pipeline.svg", "SDD-Vibe 1-in-2 Single Workflow 3D Stack"


def insert_or_refresh_marker(text: str, block: str) -> str:
    """Refresh existing MARKER block or insert cleanly after frontmatter + H1."""
    pattern = re.compile(rf"{re.escape(MARKER)}\n!\[[^\]]*\]\([^\)]+\)")
    if pattern.search(text):
        return pattern.sub(block, text, count=1)

    lines = text.splitlines()
    idx = 0
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                idx = i + 1
                break

    while idx < len(lines) and not lines[idx].startswith("# "):
        idx += 1
    if idx < len(lines) and lines[idx].startswith("# "):
        idx += 1

    while idx < len(lines) and (
        lines[idx].strip() == ""
        or lines[idx].startswith("### ")
        or lines[idx].startswith(">")
    ):
        idx += 1

    before = "\n".join(lines[:idx]).rstrip()
    after = "\n".join(lines[idx:]).lstrip("\n")
    return f"{before}\n\n{block}\n\n{after}" if after else f"{before}\n\n{block}\n"


def embed_markdown() -> int:
    count = 0
    for md in sorted(REPO_ROOT.rglob("*.md")):
        rel = md.relative_to(REPO_ROOT).as_posix()
        if any(part in rel.split("/") for part in ("node_modules", "examples", ".git", "fixtures")):
            continue
        if md.name in SKIP_NAMES:
            continue

        content = md.read_text(encoding="utf-8").replace("\r\n", "\n")
        svg_name, caption = pick_diagram(rel)
        target_dir = FW_DIAGRAMS if md.is_relative_to(FW_ROOT) else REPO_DIAGRAMS
        svg_path = target_dir / svg_name
        rel_img = os.path.relpath(svg_path, md.parent).replace("\\", "/")

        block = f"{MARKER}\n![{caption}]({rel_img})"
        updated = insert_or_refresh_marker(content, block)
        if updated != content:
            md.write_text(updated, encoding="utf-8", newline="\n")
            count += 1
    return count


# Playbook diagrams: Pure 3D isometric for layered/stack playbooks (04, 07),
# clean 2D Unicode flowcharts for sequential playbooks.
PLAYBOOK_SPECS: dict[str, tuple[str, list[str], str]] = {
    "01-Setup-Project.txt": (
        "2d",
        ["1. Copy Framework", "2. activate-ca-agent", "3. sync_ide_adapters", "4. check_docs.py"],
        "3d-cross-ide-portability.svg",
    ),
    "02-Project-Implementation.txt": (
        "2d",
        ["1. Plan & HLD/LLD", "2. UI Demo (:3000)", "3. Spec Lock + TDD", "4. Audit & Ship"],
        "workflow-prompt-pipeline.svg",
    ),
    "03-Features-Development.txt": (
        "2d",
        ["PROTOTYPE", "DRAFT (AC-*)", "IN REVIEW (/spec-check)", "APPROVED (APR-###)"],
        "flow-feature-lifecycle.svg",
    ),
    "04-Authentication-Security.txt": (
        "3d",
        ["L4: Edge & Zod Input Guard", "L3: AuthN, RBAC & 2FA", "L2: SAST & Secret Scan", "L1: RLS & Encrypted Data"],
        "3d-security-defense.svg",
    ),
    "05-MCP-Connection.txt": (
        "2d",
        ["Agent Request", "Policy & Scope Guard", "Sandboxed MCP Tool", "Sanitized Output"],
        "3d-cross-ide-portability.svg",
    ),
    "06-Integrations.txt": (
        "2d",
        ["API Contract", "Webhook Sig Verify", "Idempotency Key", "Error & Retry Log"],
        "3d-api-gateway.svg",
    ),
    "07-Testing-QA.txt": (
        "3d",
        ["TOP: E2E Journeys (10%)", "MID: Integration API/DB (20-30%)", "BASE: Unit & Contracts (60-70%)", "AUDIT: logs/test.log & AC-*"],
        "3d-testing-pyramid.svg",
    ),
    "08-Debugging.txt": (
        "2d",
        ["Read logs/*.log", "5-Whys Root Cause", "Write RED Test", "Fix & Verify GREEN"],
        "3d-testing-pyramid.svg",
    ),
    "09-Validation.txt": (
        "2d",
        ["check_docs.py", "manifest.py verify", "run-tests.js (10/10)", "/verify-ca-agent"],
        "flow-cicd-devops.svg",
    ),
    "10-Error-Handling.txt": (
        "2d",
        ["Capture ERR-###", "Link AC-FEAT###-##", "Add Regression Test", "Close in error-tracker"],
        "3d-testing-pyramid.svg",
    ),
    "11-Checklist.txt": (
        "2d",
        ["All Specs APPROVED", "Tests 100% GREEN", "SAST & Secrets Clean", "APR-### Release Ship"],
        "flow-cicd-devops.svg",
    ),
}


def make_2d_flow_txt(steps: list[str], svg_ref: str) -> str:
    # Render a clean 2-row or single-row aligned 2D Unicode flowchart (max ~84 chars wide)
    boxes: list[list[str]] = []
    for s in steps:
        w = len(s) + 2
        boxes.append([
            f"┌{'─' * w}┐",
            f"│ {s} │",
            f"└{'─' * w}┘",
        ])
    row_top = "    ".join(b[0] for b in boxes)
    row_mid = " ─► ".join(b[1] for b in boxes)
    row_bot = "    ".join(b[2] for b in boxes)
    return (
        f"{TXT_MARKER_NEW}\n"
        f"{row_top}\n"
        f"{row_mid}\n"
        f"{row_bot}\n"
        f"Visual SVG: ../docs/diagrams/{svg_ref}\n"
    )


def make_3d_stack_txt(layers: list[str], svg_ref: str) -> str:
    w = max(len(l) for l in layers) + 4
    border = "─" * w
    lines = [TXT_MARKER_NEW]
    for idx, layer in enumerate(layers):
        lines.append(f"      ┌{border}┐")
        lines.append(f"     ╱ {layer.center(w - 2)} ╱│")
        lines.append(f"    ┌{border}┐ │")
        label_sub = f"(3D Stack Layer {len(layers) - idx})"
        lines.append(f"    │ {label_sub.center(w - 2)} │╱")
        lines.append(f"    └{border}┘")
    lines.append(f"Visual SVG: ../docs/diagrams/{svg_ref}")
    return "\n".join(lines) + "\n"


def embed_playbooks() -> int:
    count = 0
    pb_dir = FW_ROOT / "playbooks"
    for txt in sorted(pb_dir.glob("*.txt")):
        content = txt.read_text(encoding="utf-8").replace("\r\n", "\n")
        # Strip any previous diagram block at the bottom
        for marker in (TXT_MARKER_NEW, TXT_MARKER_OLD):
            if marker in content:
                content = content.split(marker)[0].rstrip()

        mode, items, svg_name = PLAYBOOK_SPECS.get(
            txt.name, ("2d", ["Step 1", "Step 2", "Step 3"], "3d-sdd-vibe-pipeline.svg")
        )
        diagram = make_3d_stack_txt(items, svg_name) if mode == "3d" else make_2d_flow_txt(items, svg_name)
        updated = f"{content.rstrip()}\n\n{diagram}"
        txt.write_text(updated, encoding="utf-8", newline="\n")
        count += 1
    return count


if __name__ == "__main__":
    md_count = embed_markdown()
    txt_count = embed_playbooks()
    print(f"Updated diagrams in {md_count} .md files and {txt_count} .txt playbooks.")
