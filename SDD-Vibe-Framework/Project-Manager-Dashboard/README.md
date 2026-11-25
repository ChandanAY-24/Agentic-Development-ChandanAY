# Project-Manager-Dashboard (In-IDE Subproject)
### Local-Only, Zero-Dependency Telemetry Mission Control for SDD-Vibe

<div align="center">

[![Port](https://img.shields.io/badge/Port-4200-blue?style=for-the-badge&logo=visualstudiocode)](.)
[![Runtime](https://img.shields.io/badge/Runtime-Native_Node.js-green?style=for-the-badge&logo=nodedotjs)](.)
[![Dependencies](https://img.shields.io/badge/Dependencies-Zero_External-teal?style=for-the-badge)](.)
[![Security](https://img.shields.io/badge/Security-Local_127.0.0.1_Only-red?style=for-the-badge)](.)

**Framework Track:** SDD-Vibe (1-in-2 Single Workflow) · **Host Mode:** In-IDE Simple Browser & Local Daemons  
**Access URL:** `http://127.0.0.1:4200` · **Git Status:** Strictly Gitignored / Machine-Local Only

[🌟 Overview](#-overview) • [🏛️ Architecture](#️-mission-control-architecture) • [⚡ Quick Start](#-quick-start-inside-your-ide) • [📊 Telemetry Modules](#-visual-telemetry-modules) • [🔒 Security Model](#-security-model)

</div>

---

## 🌟 Overview

The **Project-Manager-Dashboard** is an embedded telemetry mission control designed exclusively for local IDE development within the **SDD-Vibe (1-in-2 Single Workflow)** framework. It runs side-by-side with your source code in an IDE split tab (Simple Browser), providing immediate, real-time visibility into task execution, acceptance criteria contracts, git commits, milestone gates, defect triage, and agent token usage.

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 44}}}%%
flowchart TB
    classDef store fill:#1e293b,stroke:#64748b,stroke-width:1.5px,color:#f8fafc;
    classDef daemon fill:#082f49,stroke:#0284c7,stroke-width:2px,color:#f0f9ff;
    classDef client fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef sec fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fffbeb;

    subgraph FilesystemState ["📁 LOCAL WORKSPACE ARTIFACTS & DATA STREAMS"]
        direction LR
        Tasks[("`**📋 docs/task.md**
Tasks`")]:::store
        Phases[("`**🏁 docs/phases.md**
Milestones`")]:::store
        Specs[("`**📑 docs/features/**
AC Specs`")]:::store
        Errors[("`**🐛 docs/error-tracker.md**
Defects`")]:::store
        GitMeta[("`**🗄️ .git/ Repo**
HEAD Commit`")]:::store
        LogsStream[("`**🪵 logs/*.log**
Log Streams`")]:::store
        Transcripts[("`**🤖 JSONL Logs**
Tokens`")]:::store
    end

    subgraph DaemonEngine ["⚙️ ZERO-DEPENDENCY LOCAL DAEMON (PORT 4200)"]
        direction LR
        Watcher[["`**📁 File Watcher**
Poll 2s`"]]:::daemon
        ASTParser[["`**🔍 parser.js AST**
JSON Synthesizer`"]]:::daemon
        Server[["`**🔌 server.js Daemon**
Port 4200`"]]:::daemon
        SecFilter["`**🛡️ DNS-Rebind**
Host Guard`"]:::sec
        CSRFManager["`**🔑 CSRF Guard**
Token Injector`"]:::sec
    end

    subgraph UIClient ["🖥️ IN-IDE SIMPLE BROWSER (127.0.0.1:4200)"]
        DashboardUI["`**📊 Mission Control Bento Viewport**
Active Task • HEAD Commit • AC Engine • Live Logs • Gauges`"]:::client
    end

    FilesystemState -->|"Real-Time Watch"| Watcher
    Watcher -->|"Raw Content"| ASTParser
    ASTParser -->|"Synthesized State"| Server
    SecFilter -->|"Enforces Isolation"| Server
    CSRFManager -->|"Session Token"| Server
    Server ==>|"⚡ Live SSE Telemetry"| DashboardUI
    DashboardUI -.->|"🔒 Interactive Action"| Server

    style FilesystemState fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style DaemonEngine fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style UIClient fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
```

---

## 🏛️ Mission Control Architecture

### Dynamic Prioritization Pipeline
The dashboard dynamically prioritizes the items developers care about most:

```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef active fill:#451a03,stroke:#fbbf24,stroke-width:2px,color:#fffbeb;
    classDef normal fill:#1e293b,stroke:#64748b,stroke-width:1.5px,color:#f8fafc;
    classDef git fill:#082f49,stroke:#38bdf8,stroke-width:2px,color:#f0f9ff;

    subgraph TaskStream ["📋 TASK STREAM RE-ORDERING ENGINE"]
        IncomingTasks["`**Raw Task List**
Task 1, Task 2, Task 3...`"]:::normal --> StateCheck{"Task Active?"}
        StateCheck -->|"Yes"| FloatTop["`**⚡ CURRENT RUNNING TASK**
Dynamically Floated to Index 0`"]:::active
        StateCheck -->|"No"| NaturalOrder["`**Preserve Order**
Sequential Numbering`"]:::normal
    end

    subgraph GitStream ["🗄️ GIT TELEMETRY STREAM"]
        GitLog["`**Raw Git Log**
Recent Commit History`"]:::git --> PinHead["`**📅 HEAD COMMIT PINNED**
Index 0 • DD-MM-YYYY Date`"]:::git
    end

    style TaskStream fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style GitStream fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
```

---

## ⚡ Quick Start (Inside Your IDE)

### 1. Start the Local Daemon
In your terminal or command prompt:
```bash
# Windows
open-in-ide.bat

# macOS / Linux
bash open-in-ide.sh

# Or directly with Node.js (Port 4200):
node server.js
```

### 2. Dock the Dashboard in Your IDE (Side-by-Side Viewport)
```mermaid
%%{init: {'flowchart': {'curve': 'basis', 'padding': 16, 'nodeSpacing': 28, 'rankSpacing': 40}}}%%
flowchart LR
    classDef code fill:#0f172a,stroke:#38bdf8,stroke-width:1.5px,color:#f8fafc;
    classDef dash fill:#082f49,stroke:#0284c7,stroke-width:2px,color:#f0f9ff;

    subgraph IDEWindow ["🖥️ IDE WORKSPACE WINDOW"]
        direction LR
        subgraph Col1 ["📝 Editor Group 1 (Active Code)"]
            Code["`**Active Source Code & Specs**
src/components/ • tests/unit/`"]:::code
        end
        subgraph Col2 ["📊 Editor Group 2 (Simple Browser Tab)"]
            Dash["`**Docked Simple Browser Viewport**
127.0.0.1:4200 • Live Telemetry`"]:::dash
        end
    end

    style IDEWindow fill:#0b1120,stroke:#334155,stroke-width:1.5px,color:#e2e8f0
    style Col1 fill:#0f172a,stroke:#1e293b,stroke-width:1px,color:#cbd5e1
    style Col2 fill:#082f49,stroke:#0369a1,stroke-width:1px,color:#e0f2fe
```

1. In your IDE (Cursor, VS Code, Windsurf, Antigravity), press `Ctrl + Shift + P` (or `Cmd + Shift + P` on macOS).
2. Type **`Simple Browser: Show`** and press **Enter**.
3. In the URL prompt, enter:
   ```text
   http://127.0.0.1:4200
   ```
4. Drag the tab to **Editor Group 2** (docked to the right of your active editor).

---

## 📊 Visual Telemetry Modules

1. **Active Running Task on Top:** The currently running task floats to the top of the Kanban with a highlighted `⚡ CURRENT RUNNING TASK` badge.
2. **HEAD Commit Pinned on Top:** The latest commit is locked at Index 0 with an exact `📅 DD-MM-YYYY` timestamp and author chip.
3. **Interactive AC Contract Engine:** Live inspection of Acceptance Criteria (`AC-FEAT###-##`) with Given/When/Then scenarios and clickable status toggling (`GREEN` / `RED` / `PENDING`).
4. **Prev Error Tracker:** Comprehensive defect triage matrix with instant search, P0 blocker tracking, and 1-click status persistence to `docs/error-tracker.md`.
5. **Live Logs Explorer:** Real-time stream viewing of `logs/dev.log`, `logs/test.log`, and `logs/error.log` with semantic line highlighting.
6. **Token Telemetry:** Active context usage, cache hit rate, and session savings tracking.

---

## 🔒 Security Model

```mermaid
sequenceDiagram
    autonumber
    participant IDE as "🖥️ IDE Simple Browser (127.0.0.1)"
    participant Daemon as "🔌 server.js Daemon (Port 4200)"
    participant Core as "📁 docs/ & tests/ Harness"

    IDE->>Daemon: 📡 GET / (Initial Connection)
    Note over Daemon: 🔒 Validates Host 127.0.0.1:4200<br/>Generates Per-Process CSRF Token
    Daemon-->>IDE: 200 OK (index.html + X-Dashboard-Token)

    IDE->>Daemon: 🔐 POST /api/action (Header: X-Dashboard-Token)
    Note over Daemon: 🛡️ Verifies CSRF Token & Same-Origin<br/>Blocks External DNS Rebinding
    Daemon->>Core: ⚙️ Executes Child Process Command
    Core-->>Daemon: 📊 Command Output Stream
    Daemon-->>IDE: 200 OK (success, output)
```

- **Localhost 127.0.0.1 Binding Only:** Strictly rejects all external and LAN network traffic.
- **DNS-Rebinding Protection:** Rejects any HTTP request whose `Host` header does not match `127.0.0.1:4200` or `localhost:4200`.
- **CSRF Token Validation:** All mutating requests require a valid per-process `X-Dashboard-Token`.
- **Source Code Protection:** Server daemon is strictly read-only regarding application source code.
