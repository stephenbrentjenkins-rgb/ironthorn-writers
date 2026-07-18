@echo off
setlocal

set PYTHON_EXE=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe
set SCRIPT_DIR=%~dp0
set WATCHER=%SCRIPT_DIR%beat_watcher.py

if not exist "%PYTHON_EXE%" (
    echo ERROR: Python not found at:
    echo   %PYTHON_EXE%
    echo.
    echo Update PYTHON_EXE in this .bat file or install Claude Desktop's bundled Python.
    pause
    exit /b 1
)

if not exist "%WATCHER%" (
    echo ERROR: beat_watcher.py not found at:
    echo   %WATCHER%
    pause
    exit /b 1
)

title Ironthorn Beat Intake Watcher
"%PYTHON_EXE%" "%WATCHER%"

pause
