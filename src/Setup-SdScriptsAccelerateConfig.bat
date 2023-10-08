@echo off
if not exist %~dp0..\sd-scripts ( echo Not exist sd-scripts. & pause & popd & exit /b 1 )

pushd %~dp0..\sd-scripts
call venv\Scripts\activate.bat
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

echo ------------------------------------------------------------------------------------------------------------------------
echo This machine [Enter], No distributed training [Enter], NO [Enter], NO [Enter], NO [Enter],
echo all [Enter], bf16(RTX 30X0~) [2][Enter][Enter] fp16(~RTX 20X0) [1][Enter][Enter]
accelerate config
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat
popd rem %~dp0..\sd-scripts
