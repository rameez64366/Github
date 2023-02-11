@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 11040)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 9508)

del /F cleanup-ansys-DESKTOP-H7DA5IC-9508.bat
