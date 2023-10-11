@echo off
call %~dp0Setup-animatediff-cli-prompt-travel.bat
if %errorlevel% neq 0 ( exit /b %errorlevel% )

call %~dp0Setup-ECCV2022-RIFE.bat
if %errorlevel% neq 0 ( exit /b %errorlevel% )

call %~dp0Setup-SdScripts.bat
if %errorlevel% neq 0 ( exit /b %errorlevel% )

call %~dp0Setup-ffmpeg-master-latest-win64-gpl.bat
if %errorlevel% neq 0 ( exit /b %errorlevel% )
