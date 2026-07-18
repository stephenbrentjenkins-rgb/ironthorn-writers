@echo off
setlocal
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

:: Faction Influence Dashboard launcher.
::  1. Refreshes the vault state snapshot.
::  2. Starts a local HTTP server on port 7844 in Tools/.
::  3. Opens the dashboard in the default browser.
::
:: The server keeps running; close this window to stop it.

echo.
echo  [1/3] Refreshing vault state snapshot...
"%PYTHON%" "%~dp0vault_state_snapshot.py" --no-timestamped
if errorlevel 1 (
    echo.
    echo  Snapshot reported errors. Continuing anyway.
    echo.
)

echo.
echo  [2/3] Starting local server at http://localhost:7844 ...
start "" http://localhost:7844/faction-influence-dashboard.html

echo.
echo  [3/3] Server running. Close this window to stop.
echo.
cd /d "%~dp0"
"%PYTHON%" -m http.server 7844
