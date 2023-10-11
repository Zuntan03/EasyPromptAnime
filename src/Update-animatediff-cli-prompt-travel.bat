@echo off

if exist %~dp0..\animatediff-cli-prompt-travel (
	pushd %~dp0..\animatediff-cli-prompt-travel
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\animatediff-cli-prompt-travel
)
