@echo off

pushd %~dp0..
if not exist animatediff-cli-prompt-travel (
	echo git clone https://github.com/s9roll7/animatediff-cli-prompt-travel
	git clone https://github.com/s9roll7/animatediff-cli-prompt-travel
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem %~dp0..

pushd %~dp0..\animatediff-cli-prompt-travel
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)

call venv\Scripts\activate.bat

echo pip install animatediff-cli-prompt-travel venv
python -m pip install -q --upgrade pip
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q torch==2.1.0+cu121 torchvision==0.16.0+cu121 torchaudio==2.1.0+cu121 --index-url https://download.pytorch.org/whl/cu121
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q xformers==0.0.22.post7 --index-url https://download.pytorch.org/whl/cu121
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q mediapipe pytorch_lightning
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

pip install -q -e .
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

@REM chcp 65001 rem stylize_mask
pip install -q -e .[stylize]
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat

if not exist data\lora ( mkdir data\lora )
if not exist data\vae ( mkdir data\vae )

if not exist data\models\sd\real_model_N.safetensors (
	echo curl https://huggingface.co/fcski/real_model_L
	curl -Lo data\models\sd\real_model_N.safetensors^
		https://huggingface.co/fcski/real_model_L/resolve/main/real_model_N.safetensors
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	timeout /t 1 /nobreak >nul
)

if not exist data\models\motion-module\mm_sd_v15_v2.ckpt (
	echo curl https://huggingface.co/guoyww/animatediff
	curl -Lo data\models\motion-module\mm_sd_v15_v2.ckpt^
		https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	timeout /t 1 /nobreak >nul
)

if not exist data\vae\kl-f8-anime2.ckpt (
	echo curl https://huggingface.co/hakurei/waifu-diffusion-v1-4
	curl -Lo data\vae\kl-f8-anime2.ckpt^
		https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	timeout /t 1 /nobreak >nul
)

if not exist data\vae\vae-ft-mse-840000-ema-pruned.safetensors (
	echo curl https://huggingface.co/stabilityai/sd-vae-ft-mse-original
	curl -Lo data\vae\vae-ft-mse-840000-ema-pruned.safetensors^
		https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	timeout /t 1 /nobreak >nul
)
popd rem %~dp0..\animatediff-cli-prompt-travel
