#!/usr/bin/env python3
"""SessionStart hook: verify framework root, canonical docs, and IDE discovery."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent


def main() -> int:
    is_sdd = (ROOT / "docs" / "spec.md").exists()
    framework = "SDD-Vibe" if is_sdd else "Vibe Coding"
    required = [
        ROOT / "AGENTS.md",
        ROOT / "docs" / "INDEX.md",
        ROOT / "docs" / "rules.md",
        ROOT / "docs" / "memory.md",
        ROOT / "docs" / "features",
        ROOT / ".agents" / "workflows",
        ROOT / ".agents" / "skills",
    ]
    if is_sdd:
        required.append(ROOT / "docs" / "spec.md")

    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    adapters_synced = any((ROOT / d).exists() for d in (".claude", ".cursor", ".windsurf"))
    status = {
        "framework": framework,
        "root": str(ROOT),
        "git_present": (ROOT / ".git").exists(),
        "adapters_synced": adapters_synced,
        "memory_file": "docs/memory.md" if (ROOT / "docs" / "memory.md").exists() else None,
        "missing": missing,
    }
    if not adapters_synced:
        status["activation_hint"] = (
            "Type 'activate ca agents' (or /activate-ca-agent) in chat, "
            "or run .\\activate-ca-agents.bat / ./activate-ca-agents "
            "(or python scripts/init_project.py --ides all) in terminal."
        )
    if missing:
        print(f"[session_start] WARN ({framework}): missing {', '.join(missing)}", file=sys.stderr)
    else:
        print(json.dumps(status))
    return 0


if __name__ == "__main__":
    sys.exit(main())
