@echo off

pushd %~dp0..
if not exist animatediff-cli-prompt-travel (
	echo git clone https://github.com/s9roll7/animatediff-cli-prompt-travel
	git clone https://github.com/s9roll7/animatediff-cli-prompt-travel
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	pushd animatediff-cli-prompt-travel
	git checkout aa9798a0a9d5e6248e109adc5d5ae869d18278c6
	if %errorlevel% neq 0 ( pause & popd & popd & exit /b %errorlevel% )
	popd rem animatediff-cli-prompt-travel
)
popd rem %~dp0..

pushd %~dp0..\animatediff-cli-prompt-travel
if not exist venv (
	python -m venv venv
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	call venv\Scripts\activate.bat
	echo pip install animatediff-cli-prompt-travel venv
	python -m pip install --upgrade pip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install torch==2.0.1+cu118 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install xformers==0.0.22 mediapipe pytorch_lightning
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install -e .
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install -e .[stylize]
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	pip install -e .[dwpose]
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	call venv\Scripts\deactivate.bat
)

if not exist data\lora ( mkdir data\lora )
if not exist data\vae (
	mkdir data\vae 

	@REM Update old env 
	call venv\Scripts\activate.bat
	echo animatediff-cli-prompt-travel venv pytorch_lightning
	pip install pytorch_lightning
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
	call venv\Scripts\deactivate.bat
)

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
