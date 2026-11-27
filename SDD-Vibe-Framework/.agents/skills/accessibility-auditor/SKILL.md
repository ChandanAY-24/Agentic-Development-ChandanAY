---
name: accessibility-auditor
description: "Audit UI features against docs/accessibility.md targets and NFR-FEAT accessibility criteria; use when reviewing or verifying user-facing screens."
---

# Skill: accessibility-auditor

**Purpose:** Audit user-facing interfaces against WCAG 2.1 AA standards and `docs/accessibility.md` for semantic structure, keyboard operability, screen-reader clarity, and contrast compliance.

## Trigger

- **MUST** invoke during Phase 2/4 UI verification (`/verify-ca-agent`, `/release-check-ca-agent`) and whenever interactive components, forms, or navigation views are added or changed.

## Inputs

- **MUST** read `AGENTS.md`, `docs/accessibility.md`, `docs/design.md`, and `NFR-FEAT###-##` accessibility criteria in `docs/features/`.

## Workflow

1. **Semantic HTML & Landmark Audit:**
   - Verify proper heading hierarchy (`h1`–`h6` without skipped levels), `<main>`, `<nav>`, `<header>`, `<button>`, and `<label>` associations (no clickable `<div>` without role/keyboard handlers).
2. **Keyboard Navigation & Focus Management:**
   - Confirm full Tab/Shift+Tab/Enter/Space/Escape operability, visible `:focus-visible` outlines, logical tab order, and focus trapping/restoration in modals/sheets.
3. **ARIA & Screen Reader Parity:**
   - Validate `aria-label`, `aria-describedby`, `aria-expanded`, `aria-live` regions for dynamic updates, and `alt` text on informative images (`alt=""` on decorative).
4. **Color Contrast & Motion:**
   - Check text contrast (`>= 4.5:1` normal, `>= 3:1` large/UI) across both dark and light themes and honor `prefers-reduced-motion`.

## Restrictions

- **MUST NOT** sign off on accessibility without verifying keyboard navigation and ARIA semantics in the actual markup.
- **MUST NOT** use color alone to convey status or error states.
- **MUST NOT** alter controlled guidelines without recorded approved revision.
