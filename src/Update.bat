@echo off

call "%~dp0Update-animatediff-cli-prompt-travel.bat"
if %errorlevel% neq 0 ( exit /b %errorlevel% )

@REM call "%~dp0Update-ECCV2022-RIFE.bat"
@REM if %errorlevel% neq 0 ( exit /b %errorlevel% )

call "%~dp0Update-Practical-RIFE.bat"
if %errorlevel% neq 0 ( exit /b %errorlevel% )

call "%~dp0Update-sd-scripts.bat"
if %errorlevel% neq 0 ( exit /b %errorlevel% )

call "%~dp0Setup.bat"
if %errorlevel% neq 0 ( exit /b %errorlevel% )
