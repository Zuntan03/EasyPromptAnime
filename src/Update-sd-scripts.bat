@echo off

if exist %~dp0..\sd-scripts (
	pushd %~dp0..\sd-scripts
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\sd-scripts
)
