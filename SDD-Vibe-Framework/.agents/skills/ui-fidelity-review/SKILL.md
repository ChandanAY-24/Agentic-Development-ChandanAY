---
name: ui-fidelity-review
description: "Compare implemented UI against docs/design.md and feature acceptance criteria; report deviations with evidence."
---

# Skill: ui-fidelity-review

**Purpose:** Audit implemented frontend components and Phase 2 sensory demos against `docs/design.md` tokens, responsive breakpoints, interaction states, and `AC-FEAT###-##` UI criteria.

## Trigger

- **MUST** invoke during Phase 2 visual sign-off (`/run-ca-agent`) and whenever UI components, stylesheets, or layouts are modified.

## Inputs

- **MUST** read `AGENTS.md`, `docs/design.md`, `docs/accessibility.md`, and the active feature spec in `docs/features/`.

## Workflow

1. **Design Token & Typography Audit:**
   - Verify colors, spacing, radii, elevation, and font scales match `docs/design.md` CSS custom properties / theme tokens (zero hardcoded off-palette hex values).
2. **Responsive Breakpoint Verification:**
   - Inspect layout behavior across mobile (`375px`), tablet (`768px`), desktop (`1280px`), and ultrawide (`1920px+`) viewports; confirm zero horizontal overflow or clipped controls.
3. **Interactive State & Micro-Interaction Check:**
   - Verify all interactive elements implement `hover`, `focus-visible`, `active`, `disabled`, `loading`, and `empty`/`error` states.
4. **Contrast & Visual Hierarchy Check:**
   - Confirm text/background contrast meets WCAG AA (`4.5:1` normal text, `3:1` large text/UI) and primary CTAs maintain clear visual hierarchy.
5. **Deviation Report:**
   - Output a structured fidelity report listing matched tokens, visual/layout deviations with file/line references, and pass/fail status for Phase 2 sign-off.

## Restrictions

- **MUST NOT** sign off on UI fidelity without inspecting the actual rendered DOM/CSS or live demo output.
- **MUST NOT** introduce unapproved visual libraries or break existing theme tokens (`light`/`dark` parity).
- **MUST NOT** implement backend business logic during a UI fidelity review.
