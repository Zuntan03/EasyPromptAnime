@echo off

if exist %~dp0..\animatediff-cli-prompt-travel (
	pushd %~dp0..\animatediff-cli-prompt-travel
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	git checkout aa9798a0a9d5e6248e109adc5d5ae869d18278c6
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\animatediff-cli-prompt-travel
)
