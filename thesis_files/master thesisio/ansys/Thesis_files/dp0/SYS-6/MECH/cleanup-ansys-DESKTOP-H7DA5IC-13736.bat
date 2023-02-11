@echo off
set LOCALHOST=%COMPUTERNAME%
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 11136)
if /i "%LOCALHOST%"=="DESKTOP-H7DA5IC" (taskkill /f /pid 13736)

del /F cleanup-ansys-DESKTOP-H7DA5IC-13736.bat
