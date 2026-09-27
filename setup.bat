@echo off
title AgriYield - Setup Dependencies
echo ========================================================
echo   Installing AgriYield Dependencies (One-time setup)...
echo ========================================================
echo.
python -m pip install -r requirements.txt
echo.
echo ========================================================
echo   Installation Complete!
echo   You can now double-click 'run.bat' to start AgriYield.
echo ========================================================
pause
