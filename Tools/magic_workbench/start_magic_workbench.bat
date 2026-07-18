@echo off
title Ironthorn Magic Workbench
set PYTHON=%~dp0.venv\Scripts\python.exe

cd /d "%~dp0"
echo.
echo  Ironthorn Magic Workbench v0.1
echo  ===============================
echo  Starting on http://localhost:7844
echo.

if not exist "%PYTHON%" (
    echo  ERROR: venv not found at %PYTHON%
    echo.
    echo  Create it with:
    echo    "C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe" -m venv "%~dp0.venv"
    echo.
    echo  Then install Flask:
    echo    "%~dp0.venv\Scripts\python.exe" -m pip install flask
    echo.
    pause
    exit /b 1
)

echo  Python: %PYTHON%
echo  Ctrl+C in this window stops the server.
echo.

"%PYTHON%" "%~dp0workbench_server.py"
echo.
pause
