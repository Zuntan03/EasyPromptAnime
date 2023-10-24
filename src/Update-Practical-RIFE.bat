@echo off

if exist %~dp0..\Practical-RIFE (
	pushd %~dp0..\Practical-RIFE
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\Practical-RIFE
)
