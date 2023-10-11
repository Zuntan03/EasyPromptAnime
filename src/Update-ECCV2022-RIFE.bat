@echo off

if exist %~dp0..\ECCV2022-RIFE (
	pushd %~dp0..\ECCV2022-RIFE
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\ECCV2022-RIFE
)
