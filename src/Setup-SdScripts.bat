@echo off

pushd %~dp0..
if not exist sd-scripts (
	echo git clone https://github.com/kohya-ss/sd-scripts
	git clone https://github.com/kohya-ss/sd-scripts
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	pushd sd-scripts
	git checkout 2a23713f71628b2d1b88a51035b3e4ee2b5dbe46
	if %errorlevel% neq 0 ( pause & popd & popd & exit /b %errorlevel% )
	popd rem sd-scripts
)
popd rem %~dp0..

pushd %~dp0..\sd-scripts
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	call venv\Scripts\activate.bat
	echo pip install sd-scripts venv
	python -m pip install --upgrade pip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install torch==2.0.1+cu118 torchvision==0.15.2+cu118 --index-url https://download.pytorch.org/whl/cu118
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install --upgrade -r requirements.txt
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install xformers==0.0.20
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	call venv\Scripts\deactivate.bat
)
popd rem %~dp0..\sd-scripts
