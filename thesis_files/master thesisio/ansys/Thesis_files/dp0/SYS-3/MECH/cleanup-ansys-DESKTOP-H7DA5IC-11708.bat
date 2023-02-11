@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 1056)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 11708)

del /F cleanup-ansys-DESKTOP-H7DA5IC-11708.bat
