@echo off

if exist %~dp0animatediff-cli-prompt-travel (
	pushd %~dp0animatediff-cli-prompt-travel
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0animatediff-cli-prompt-travel
)

if exist %~dp0sd-scripts (
	pushd %~dp0sd-scripts
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0sd-scripts
)

pushd %~dp0
git pull
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call src\Setup.bat
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
popd rem %~dp0
