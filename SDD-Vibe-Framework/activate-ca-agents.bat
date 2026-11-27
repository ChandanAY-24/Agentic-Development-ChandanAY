@echo off
setlocal
REM SDD-Vibe Collision-Free Terminal Activator (Windows CMD / PowerShell)
REM Wraps scripts/init_project.py without conflicting with Python venv 'activate' or PowerShell 'start'.
cd /d "%~dp0"

set "PY_CMD="
where python >nul 2>nul && set "PY_CMD=python"
if "%PY_CMD%"=="" (
    where py >nul 2>nul && set "PY_CMD=py -3"
)
if "%PY_CMD%"=="" (
    echo [activate-ca-agents] ERROR: Python 3 not found on PATH.
    exit /b 1
)

echo [activate-ca-agents] Bootstrapping SDD-Vibe IDE adapters and verifying workspace...
%PY_CMD% scripts\init_project.py --ides all %*
if errorlevel 1 exit /b %errorlevel%

%PY_CMD% scripts\check_docs.py
if errorlevel 1 exit /b %errorlevel%

%PY_CMD% scripts\manifest.py --check
if errorlevel 1 exit /b %errorlevel%

echo.
echo [activate-ca-agents] READY!
echo   - Chat: type "activate ca agents" or "/team-ecosystem-ca-agent" or "/plan-ca-agent"
echo   - Dashboard: type "/dashboard-ca-agent" or run Project-Manager-Dashboard\open-in-ide.bat
exit /b 0
