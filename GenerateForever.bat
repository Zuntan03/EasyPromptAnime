@echo off
:BEGIN
call "%~dp0Generate.bat" "%~1"
if %ERRORLEVEL% neq 0 ( exit /b 1 )
goto BEGIN
