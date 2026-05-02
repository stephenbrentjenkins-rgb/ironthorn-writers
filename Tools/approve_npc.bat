@echo off
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

:: GameVault NPC Approval Tool
:: Usage: approve_npc.bat NPC-Name
:: Example: approve_npc.bat Factor-Renne-Saul

if "%~1"=="" (
    echo.
    echo  GameVault NPC Approval Tool
    echo  ============================
    echo  Usage: approve_npc.bat NPC-Name
    echo  Example: approve_npc.bat Factor-Renne-Saul
    echo.
    echo  The NPC name must match the folder name in NPCs/_Pending/
    echo.
    pause
    exit /b
)

"%PYTHON%" "%~dp0approve_npc.py" "%~1"
echo.
pause
