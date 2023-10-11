@echo off

pushd %~dp0
git pull
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
popd rem %~dp0

call "%~dp0src\Update.bat"
