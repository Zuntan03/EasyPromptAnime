@echo off

pushd %~dp0..
if not exist sd-scripts (
	echo git clone https://github.com/kohya-ss/sd-scripts
	git clone https://github.com/kohya-ss/sd-scripts
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem %~dp0..

pushd %~dp0..\sd-scripts
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)

call venv\Scripts\activate.bat

echo pip install sd-scripts venv
python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q --upgrade -r requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q xformers==0.0.20
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat

popd rem %~dp0..\sd-scripts
