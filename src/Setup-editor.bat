@echo off
pushd %~dp0..

if not exist editor\venv (
	python -m venv editor\venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)

call editor\venv\Scripts\activate.bat
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q darkdetect tkinterdnd2
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call editor\venv\Scripts\deactivate.bat

popd rem %~dp0..
