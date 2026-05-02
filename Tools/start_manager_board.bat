@echo off
title Ironthorn Manager Board
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

cd /d "%~dp0"
echo.
echo  Ironthorn Manager Board v1.0
echo  =============================
echo  Starting on http://localhost:7843
echo.
echo  Ctrl+C in this window stops the server.
echo.

"%PYTHON%" "%~dp0manager_server.py"
echo.
pause
