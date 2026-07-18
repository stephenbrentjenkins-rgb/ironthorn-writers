@echo off
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

:: GameVault Vault State Snapshot
:: Walks the vault and produces a single JSON snapshot at
:: Tools/snapshots/latest.json (plus a timestamped archive copy).
:: Used by the Faction Influence Dashboard and other admin web tools.

"%PYTHON%" "%~dp0vault_state_snapshot.py" %*
echo.
pause
