@echo off

pushd %~dp0..
if not exist Practical-RIFE (
	echo git clone https://github.com/hzwer/Practical-RIFE
	git clone https://github.com/hzwer/Practical-RIFE
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem %~dp0..

pushd %~dp0..\Practical-RIFE
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
call venv\Scripts\activate.bat

echo pip install Practical-RIFE venv
python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q torch==2.0.1+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM pip install numpy>=1.16 tqdm>=4.35.0 sk-video>=1.1.10 opencv-python>=4.1.2 moviepy>=1.0.3
pip install -q tqdm sk-video opencv-python moviepy
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM pip install -q -r requirements.txt
@REM pip install -r requirements.txt
@REM if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )


@REM numpy>=1.16
@REM tqdm>=4.35.0
@REM sk-video>=1.1.10
@REM torch>=1.3.0
@REM opencv-python>=4.1.2
@REM moviepy>=1.0.3
@REM torchvision==0.7.0

pip install -q numpy==1.23.5
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat


if not exist train_log (
	echo curl https://github.com/hzwer/Practical-RIFE/blob/main/README.md#model-list
	curl -Lo RifeModel.zip https://drive.google.com/uc?id=1V6yJsfZgxfx3l03k1sex3YpLdqsJbj61
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo Unzip RifeModel.zip
	PowerShell -Version 5.1 -ExecutionPolicy Bypass Expand-Archive -Path RifeModel.zip -DestinationPath .
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo del RifeModel.zip
	del RifeModel.zip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem Practical-RIFE
