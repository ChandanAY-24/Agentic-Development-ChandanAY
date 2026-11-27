#!/usr/bin/env python3
"""Embed 3D axonometric SVG diagrams across all substantive .md files
and isometric Unicode 3D diagrams across all playbooks/*.txt files.

Idempotent: uses <!-- SDD-VIBE-3D-DIAGRAM --> marker to avoid duplicate insertion.
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
TXT_MARKER = "=== 3D AXONOMETRIC WORKFLOW DIAGRAM ==="

SKIP_NAMES = {
    "LICENSE.md",
    "LICENSE-DECISION.md",
    "CHANGELOG.md",
    "guideline-CHANGELOG.md",
    "CODE_OF_CONDUCT.md",
    "PULL_REQUEST_TEMPLATE.md",
    "SOURCE-NOTES.md",
}


def pick_diagram(rel_posix: str) -> tuple[str, str]:
    """Return (svg_filename, caption) tailored to the file's domain."""
    p = rel_posix.lower()
    if "dashboard" in p:
        return "3d-mission-control-dashboard.svg", "In-IDE Project-Manager-Dashboard 3D Dataflow"
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
    if "devops" in p or "deploy" in p or "environment" in p or "release" in p or "ci" in p or "runbook" in p or "observability" in p or "performance" in p:
        return "3d-cicd-devops.svg", "CI/CD & Quality Gate Pipeline 3D Flow"
    if "feature" in p or "spec" in p or "change" in p or "approval" in p or "granular" in p or "prd" in p or "product" in p or "plan" in p or "task" in p or "phase" in p:
        return "3d-feature-lifecycle.svg", "Feature Spec Lifecycle & Change Control 3D Flow"
    if "architecture" in p or "adr" in p or "tech-stack" in p or "design" in p or "accessibility" in p:
        return "3d-system-architecture.svg", "5-Tier System Architecture & Clean Layers 3D"
    return "3d-sdd-vibe-pipeline.svg", "SDD-Vibe 1-in-2 Single Workflow 3D Stack"


def insert_after_frontmatter_and_h1(text: str, block: str) -> str:
    """Insert diagram block cleanly after YAML frontmatter + H1 + optional blockquote/Purpose."""
    lines = text.splitlines()
    idx = 0

    # Skip YAML frontmatter
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                idx = i + 1
                break

    # Find H1
    while idx < len(lines) and not lines[idx].startswith("# "):
        idx += 1
    if idx < len(lines) and lines[idx].startswith("# "):
        idx += 1

    # Skip subtitle headings or metadata blockquotes immediately following H1
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
        if MARKER in content:
            continue

        svg_name, caption = pick_diagram(rel)
        target_dir = FW_DIAGRAMS if md.is_relative_to(FW_ROOT) else REPO_DIAGRAMS
        svg_path = target_dir / svg_name
        rel_img = os.path.relpath(svg_path, md.parent).replace("\\", "/")

        block = f"{MARKER}\n![{caption}]({rel_img})"
        updated = insert_after_frontmatter_and_h1(content, block)
        md.write_text(updated, encoding="utf-8", newline="\n")
        count += 1
    return count


PLAYBOOK_DIAGRAMS: dict[str, tuple[str, str]] = {
    "01-Setup-Project.txt": ("SETUP & IDE SYNC", "init_project.py -> .agents/ -> 8 IDEs"),
    "02-Project-Implementation.txt": ("PHASED IMPLEMENTATION", "Phase 1 Plan -> Phase 2 UI -> Phase 3 TDD"),
    "03-Features-Development.txt": ("FEATURE LIFECYCLE", "PROTOTYPE -> DRAFT -> IN REVIEW -> APPROVED"),
    "04-Authentication-Security.txt": ("SECURITY & AUTH", "Edge -> RBAC/2FA -> Zod -> RLS -> Audit"),
    "05-MCP-Connection.txt": ("MCP CONNECTORS", "Agent -> Policy Guard -> Sandboxed MCP"),
    "06-Integrations.txt": ("EXTERNAL INTEGRATIONS", "Contract -> Webhook Sig -> Idempotency"),
    "07-Testing-QA.txt": ("TESTING PYRAMID", "Unit (70%) -> Integration (20%) -> E2E (10%)"),
    "08-Debugging.txt": ("ROOT CAUSE TRIAGE", "logs/*.log -> 5-Whys -> Red Test -> Fix"),
    "09-Validation.txt": ("QUALITY GATE", "check_docs -> manifest -> run-tests -> Ship"),
    "10-Error-Handling.txt": ("DEFECT TRACKER", "ERR-### -> AC Link -> Regression Test"),
    "11-Checklist.txt": ("RELEASE CHECKLIST", "Specs Green -> SAST Clean -> APR-### Sign-Off"),
}


def make_iso_txt_box(title: str, subtitle: str, svg_ref: str) -> str:
    w = max(len(title), len(subtitle)) + 6
    top_border = "─" * w
    return (
        f"{TXT_MARKER}\n"
        f"      ╔{top_border}╗\n"
        f"     ╱ {title.center(w - 2)} ╱│\n"
        f"    ╔{top_border}╗ │\n"
        f"    ║ {subtitle.center(w - 2)} ║ │\n"
        f"    ║ {'(3D Isometric Layer)'.center(w - 2)} ║╱\n"
        f"    ╚{top_border}╝\n"
        f"    Visual SVG: ../docs/diagrams/{svg_ref}\n"
    )


def embed_playbooks() -> int:
    count = 0
    pb_dir = FW_ROOT / "playbooks"
    for txt in sorted(pb_dir.glob("*.txt")):
        content = txt.read_text(encoding="utf-8").replace("\r\n", "\n")
        if TXT_MARKER in content:
            continue
        title, sub = PLAYBOOK_DIAGRAMS.get(txt.name, ("SDD-VIBE PLAYBOOK", "Guided Execution"))
        svg_name, _ = pick_diagram(txt.name)
        diagram = make_iso_txt_box(title, sub, svg_name)
        txt.write_text(f"{content.rstrip()}\n\n{diagram}", encoding="utf-8", newline="\n")
        count += 1
    return count


if __name__ == "__main__":
    md_count = embed_markdown()
    txt_count = embed_playbooks()
    print(f"Embedded 3D diagrams into {md_count} .md files and {txt_count} .txt playbooks.")
