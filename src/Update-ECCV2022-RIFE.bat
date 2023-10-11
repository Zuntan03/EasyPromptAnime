@echo off

if exist %~dp0..\ECCV2022-RIFE (
	pushd %~dp0..\ECCV2022-RIFE
	git pull
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	git checkout 1a21b29145d2d8ac557c22ad1a156c4c4aa39348
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	popd rem %~dp0..\ECCV2022-RIFE
)
