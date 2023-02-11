@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 11132)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 6808)

del /F cleanup-ansys-DESKTOP-H7DA5IC-6808.bat
