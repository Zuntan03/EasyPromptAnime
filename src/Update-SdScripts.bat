@echo off

if exist %~dp0..\sd-scripts (
	pushd %~dp0..\sd-scripts
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	git checkout 2a23713f71628b2d1b88a51035b3e4ee2b5dbe46
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\sd-scripts
)
