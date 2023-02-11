@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 2600)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 14172)

del /F cleanup-ansys-DESKTOP-H7DA5IC-14172.bat
