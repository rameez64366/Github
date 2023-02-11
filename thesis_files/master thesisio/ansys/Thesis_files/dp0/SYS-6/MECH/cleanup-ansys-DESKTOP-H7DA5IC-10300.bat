@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 6964)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 10300)

del /F cleanup-ansys-DESKTOP-H7DA5IC-10300.bat
