@echo off

pushd %~dp0..
if not exist ECCV2022-RIFE (
	echo git clone https://github.com/megvii-research/ECCV2022-RIFE
	git clone https://github.com/megvii-research/ECCV2022-RIFE
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem %~dp0..

pushd %~dp0..\ECCV2022-RIFE
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
call venv\Scripts\activate.bat

echo pip install ECCV2022-RIFE venv
python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q torch==2.0.1+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q -r requirements.txt
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q numpy==1.23.5
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat


if not exist train_log (
	echo curl https://github.com/hzwer/Practical-RIFE/blob/main/README.md#model-list
	curl -Lo RifeModel.zip https://drive.google.com/uc?id=1APIzVeI-4ZZCEuIRE1m6WYfSCaOsi_7_
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo Unzip RifeModel.zip
	PowerShell -Version 5.1 -ExecutionPolicy Bypass Expand-Archive -Path RifeModel.zip -DestinationPath .
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo del RifeModel.zip
	del RifeModel.zip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem ECCV2022-RIFE
