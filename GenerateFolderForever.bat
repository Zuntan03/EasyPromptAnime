@echo off
:BEGIN
call "%~dp0GenerateFolder.bat" "%~1"
if %ERRORLEVEL% neq 0 ( exit /b 1 )
timeout /t 3 /nobreak >nul
goto BEGIN
