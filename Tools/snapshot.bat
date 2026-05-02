@echo off
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

:: GameVault Version Snapshot
:: Drag any canonical file onto this batch file to snapshot it before editing

if "%~1"=="" (
    echo.
    echo  GameVault Version Snapshot Tool
    echo  ================================
    echo  Drag a file onto this batch file to snapshot it before editing.
    echo  Or run from command line: snapshot.bat "path\to\file.md"
    echo.
    pause
    exit /b
)

"%PYTHON%" "%~dp0version_snapshot.py" "%~1"
echo.
pause
