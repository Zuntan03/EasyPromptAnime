@echo off
pushd %~dp0..\animatediff-cli-prompt-travel\data\vae

call :DOWNLOAD kl-f8-anime2.ckpt https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/main/vae/kl-f8-anime2.ckpt
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call :DOWNLOAD orangemix.pt https://huggingface.co/WarriorMama777/OrangeMixs/resolve/main/VAEs/orangemix.vae.pt
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call :DOWNLOAD vae-ft-ema-560000.safetensors https://huggingface.co/stabilityai/sd-vae-ft-ema-original/resolve/main/vae-ft-ema-560000-ema-pruned.safetensors
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call :DOWNLOAD vae-ft-mse-840000.safetensors https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call :DOWNLOAD clearvae_v22.safetensors https://civitai.com/api/download/models/80518
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

popd rem %~dp0..\animatediff-cli-prompt-travel\data\vae
exit /b 0

:DOWNLOAD
if not exist %1 (
	curl -Lo %1 %2
	if %errorlevel% neq 0 ( exit /b %errorlevel% )
	timeout /t 1 /nobreak >nul
)
exit /b 0
