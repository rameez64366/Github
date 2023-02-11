@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 4636)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 6604)

del /F cleanup-ansys-DESKTOP-H7DA5IC-6604.bat
