@echo off
pushd %~dp0..

if not exist animatediff-cli-prompt-travel (
	git clone https://github.com/s9roll7/animatediff-cli-prompt-travel
)

pushd animatediff-cli-prompt-travel

if not exist venv (
	python -m venv venv
	call venv\Scripts\activate.bat
	python -m pip install --upgrade pip
	pip install torch==2.0.1+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
	pip install xformers==0.0.22 mediapipe
	pip install -e .
	pip install -e .[stylize]
	pip install -e .[dwpose]
	call venv\Scripts\deactivate.bat
)

if not exist data\lora ( mkdir data\lora )
if not exist data\vae ( mkdir data\vae )

pushd data\models\sd
if not exist xxmix9realistic_v40.safetensors (
	curl -Lo xxmix9realistic_v40.safetensors https://civitai.com/api/download/models/102222
	timeout /t 1 /nobreak >nul
)
if not exist featurelessMix_v2020237Clearvae.safetensors (
	curl -Lo featurelessMix_v2020237Clearvae.safetensors https://civitai.com/api/download/models/168615
	timeout /t 1 /nobreak >nul
)
if not exist featurelessCuteMix_v10Clearvae.safetensors (
	curl -Lo featurelessCuteMix_v10Clearvae.safetensors https://civitai.com/api/download/models/168584
	timeout /t 1 /nobreak >nul
)
@REM if not exist onigiriMix_v10Clearvae.safetensors (
@REM 	curl -Lo onigiriMix_v10Clearvae.safetensors https://civitai.com/api/download/models/168600
@REM 	timeout /t 1 /nobreak >nul
@REM )
@REM if not exist nadenadesitai_v10.safetensors (
@REM 	curl -Lo nadenadesitai_v10.safetensors https://civitai.com/api/download/models/84669
@REM 	timeout /t 1 /nobreak >nul
@REM )
for %%f in (*.safetensors) do (
	if %%~zf LSS 10240 if %%~zf GTR 0 ( echo [BROKEN FILE]: "%%f" & del "%%f" )
)
popd rem data\models\sd

pushd data\models\motion-module
if not exist mm_sd_v15_v2.ckpt (
	curl -LO https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt
	timeout /t 1 /nobreak >nul
)
@REM if not exist mm_sd_v15.ckpt (
@REM 	curl -LO https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15.ckpt
@REM 	timeout /t 1 /nobreak >nul
@REM )
@REM if not exist mm_sd_v14.ckpt (
@REM 	curl -LO https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v14.ckpt
@REM 	timeout /t 1 /nobreak >nul
@REM )
@REM if not exist mm-Stabilized_high.pth (
@REM 	curl -LO https://huggingface.co/manshoety/AD_Stabilized_Motion/resolve/main/mm-Stabilized_high.pth
@REM 	timeout /t 1 /nobreak >nul
@REM )
@REM if not exist mm-Stabilized_mid.pth (
@REM 	curl -LO https://huggingface.co/manshoety/AD_Stabilized_Motion/resolve/main/mm-Stabilized_mid.pth
@REM 	timeout /t 1 /nobreak >nul
@REM )
for %%f in (*.ckpt) do (
	if %%~zf LSS 10240 if %%~zf GTR 0 ( echo [BROKEN FILE]: "%%f" & del "%%f" )
)
for %%f in (*.pth) do (
	if %%~zf LSS 10240 if %%~zf GTR 0 ( echo [BROKEN FILE]: "%%f" & del "%%f" )
)
popd rem data\models\motion-module

pushd data\embeddings
if not exist EasyNegative.safetensors (
	curl -LO https://huggingface.co/datasets/gsdf/EasyNegative/resolve/main/EasyNegative.safetensors
	timeout /t 1 /nobreak >nul
)
if not exist EasyNegativeV2.safetensors (
	curl -LO https://huggingface.co/gsdf/Counterfeit-V3.0/resolve/main/embedding/EasyNegativeV2.safetensors
	timeout /t 1 /nobreak >nul
)
for %%f in (*.safetensors) do (
	if %%~zf LSS 3072 if %%~zf GTR 0 ( echo [BROKEN FILE]: "%%f" & del "%%f" )
)
popd rem data\embeddings

popd rem animatediff-cli-prompt-travel\data

if not exist ECCV2022-RIFE (
	git clone https://github.com/megvii-research/ECCV2022-RIFE
)
pushd ECCV2022-RIFE
if not exist venv (
	python -m venv venv
	call venv\Scripts\activate.bat
	python -m pip install --upgrade pip
	pip install torch==2.0.1+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
	pip install -r requirements.txt
	pip install numpy==1.23.5
	call venv\Scripts\deactivate.bat
)
if not exist train_log (
	curl -Lo RifeModel.zip https://drive.google.com/uc?id=1APIzVeI-4ZZCEuIRE1m6WYfSCaOsi_7_
	PowerShell -Version 5.1 -ExecutionPolicy Bypass Expand-Archive -Path RifeModel.zip -DestinationPath .
	del RifeModel.zip
)
popd rem ECCV2022-RIFE

set FFMPEG_DIR=ffmpeg-master-latest-win64-gpl
if not exist %FFMPEG_DIR% (
	curl -Lo ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
	PowerShell -Version 5.1 -ExecutionPolicy Bypass Expand-Archive -Path ffmpeg.zip -DestinationPath .
	del ffmpeg.zip
	copy /Y %FFMPEG_DIR%\bin\*.exe animatediff-cli-prompt-travel
	copy /Y %FFMPEG_DIR%\bin\*.exe ECCV2022-RIFE
)

call src\Setup-SdScripts.bat
call src\Setup-Vae.bat
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

popd rem %~dp0..
