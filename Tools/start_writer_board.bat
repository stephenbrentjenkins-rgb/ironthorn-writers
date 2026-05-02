@echo off
title GameVault Writer Board
set PYTHON=C:\Users\steph\AppData\Local\Packages\Claude_pzs8sxrjxfjjc\LocalCache\Roaming\uv\python\cpython-3.13.9-windows-x86_64-none\python.exe

echo.
echo  GameVault Writer Board
echo  =======================
echo  Starting local server and opening browser...
echo  Board will open at: http://localhost:7842
echo.
echo  Keep this window open while using the board.
echo  Press Ctrl+C to stop.
echo.

"%PYTHON%" "%~dp0writer_board_server.py"
echo.
pause
