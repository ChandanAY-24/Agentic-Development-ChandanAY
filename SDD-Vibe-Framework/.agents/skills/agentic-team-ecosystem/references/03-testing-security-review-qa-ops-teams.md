# 03 — Group 3 Teams (Testing, Security, Review, QA, Ops, Maintenance)

## Team 5 — Testing Team

**Scope:** Full SDLC & STLC test coverage—never mark a task complete without real passing evidence in `logs/test.log`.

- **Test Types Executed:**
  - **Static & Unit:** Linters, type-checks, isolated unit tests (TDD Red-Green-Refactor).
  - **Box Methodologies:** White-box (branch/path coverage), Black-box (spec/acceptance criteria), Grey-box (API + DB state).
  - **Build & Change Gates:** Smoke testing, Sanity testing, Regression testing, Dynamic testing.
  - **Discovery & Release:** Ad-hoc testing, Exploratory testing, API contract testing, **Alpha testing**, **Beta testing**, and **Manual Testing Checklist** guided for the Developer.
- **Domain Extensions:**
  - *ML / DL / CV:* Data validation, train/eval split leakage checks, confusion matrix / mAP / latency regression tests.
  - *OS / Systems:* QEMU/VM boot tests, syscall fuzzing, memory leak & race condition checks.

---

## Team 6 — Security Testing Team

**Scope:** Adversarial verification before any release or external integration.

- **Checks:**
  - Cyber security & OWASP Top 10 audit (SQLi, XSS, CSRF, SSRF, IDOR, broken authz).
  - Ethical hacking / penetration simulation & **Bruteforce / Rate-limit** verification.
  - **Secrets Leak Scanning:** `.env`, API keys, tokens, private keys, git history, and `logs/` PII redaction.
  - **Supply-Chain & Skill Audit:** Verify third-party packages, MCP servers, and GitHub skills before installation; enforce **authorized-targets-only** rules for headless browser tools (e.g., `obscura`) and **human-approved sends + session isolation** for messaging gateways (e.g., `OpenWA`).
- **Reporting:** Severity-ranked findings (`CRITICAL` / `HIGH` / `MEDIUM` / `LOW`) reported directly to Developer and Team 4.

---

## Team 7 — Review Team

**Scope:** Independent pre-commit and pre-merge code review.

- Verify spec conformance (`docs/features/`), no dead code/hardcoding, clean coupling/cohesion, error handling, and logging hygiene.
- Reject unverified claims or out-of-scope edits; report review verdict to Developer (optionally using `plannotator` for local-first visual diff annotation before `/review-ca-agent`).

---

## Team 8 — Quality Assurance (QA) Team

**Scope:** Holistic **Product Quality** + **Code Quality** gatekeeper.

- Verify all Acceptance Criteria (`AC-FEAT###-##`), UI/UX fidelity against Team 3's design, NFRs (latency, accessibility, responsiveness), and release checklist (`docs/release-checklist.md`).
- Issue formal `QA SIGN-OFF` or `BLOCKED` report to Developer.

---

## Team 9 — Deployment Operations Team

**Scope:** Reliable, scalable, observable production launches.

- **Architecture & Hosting:** Monolith vs. Microservices, Git & GitHub CI/CD, AWS, VPS, Docker, Nginx, Redis, Vercel, Render, GPU/inference servers (for ML/CV), or binary/ISO release pipelines (for Software/OS).
- **Scale & Reliability:** Throughput tuning, Uptime/Downtime SLOs, Horizontal scaling, Database sharding & replication, Rate limiting, CDN/caching, zero-downtime rollouts & rollback runbooks.

---

## Team 10 — Maintenance Team (24×7 Post-Deployment)

**Scope:** Continuous post-deployment monitoring and rapid incident escalation.

- **24×7 Monitoring:** Track uptime, error rates (`logs/error.log`), latency spikes, model drift (ML/CV), and CVE advisories.
- **Vulnerability Escalation Loop:** Immediately alert **Team 4 (Dev)** with reproduction steps + severity if vulnerabilities or unwanted runtime errors occur, and report status to the **Developer**.
- **Unwanted Error Handling:** Graceful degradation, circuit breakers, automated alerting, and post-mortem updates.
