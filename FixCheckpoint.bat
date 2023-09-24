@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the model file.
	pause & exit /b 1
)

set MODEL_PATH="%~f1"

pushd %~dp0animatediff-cli-prompt-travel
call venv\Scripts\activate.bat

echo animatediff fix-checkpoint %MODEL_PATH%
animatediff fix-checkpoint %MODEL_PATH%

echo.
echo If you see "This file works fine." then the model has not been changed.

pause 

call venv\Scripts\deactivate.bat
popd rem %~dp0%~dp0animatediff-cli-prompt-travel
