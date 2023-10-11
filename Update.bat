@echo off
pushd %~dp0

git pull
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call src\Update-animatediff-cli-prompt-travel.bat
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

call src\Update-ECCV2022-RIFE.bat
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

call src\Update-sd-scripts.bat
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

call src\Setup.bat
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

popd rem %~dp0
