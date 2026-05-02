@echo off
rem Copy the latest writer board HTML to the Tools folder for the server to serve
rem Run this whenever you download a new version of the board

set SRC=%USERPROFILE%\Downloads\ironthorn-writer-board.html
set DST=C:\Users\steph\Desktop\Game\GameVault\Tools\ironthorn-writer-board.html

if not exist "%SRC%" (
    echo ERROR: File not found at %SRC%
    echo Download ironthorn-writer-board.html to your Downloads folder first.
    pause
    exit /b
)

copy /Y "%SRC%" "%DST%"
echo.
echo  Writer board updated at:
echo  %DST%
echo.
pause
