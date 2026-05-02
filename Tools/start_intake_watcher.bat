@echo off
title Ironthorn NPC Intake Watcher
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

echo.
echo  Ironthorn NPC Intake Watcher v1.1
echo  ====================================
echo  Uses Claude Code CLI — no pip install needed.
echo.
echo  Drop NPC description files into:
echo  GameVault\NPCs\_Pending\_Intake\
echo.
echo  Name the file after the NPC:
echo    Factor-Renne-Saul.md
echo    Solta-Byrne.txt
echo.
echo  Ctrl+C to stop.
echo.

"%PYTHON%" "%~dp0intake_watcher.py"
echo.
pause
