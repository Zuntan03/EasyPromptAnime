@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the C3Lier LoRA or LoCon LoRA file.
	pause & exit /b 1
)

set DIM=32
if not "%~2" == "" if not "%~2" == "0" (
	set DIM=%~2
)

set MODEL_PATH="%~dp0animatediff-cli-prompt-travel\data\models\sd\featurelessMix_v2020237Clearvae.safetensors"
if not "%~3" == ""  (
	set MODEL_PATH="%~f3"
)

set SRC_PATH="%~f1"
set MERGED_PATH="%~dpn1-merged.safetensors"
set DEST_PATH="%~dp0animatediff-cli-prompt-travel\data\lora\%~n1.safetensors"

pushd %~dp0sd-scripts
call venv\Scripts\activate.bat

echo SRC_PATH: %SRC_PATH%
echo MERGED_PATH: %MERGED_PATH%
echo DEST_PATH: %DEST_PATH%

python networks\merge_lora.py^
	--sd_model %MODEL_PATH%^
	--save_to %MERGED_PATH%^
	--models %SRC_PATH%^
	--ratios 1.0^
	--save_precision float
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

python networks\extract_lora_from_models.py^
	--model_org %MODEL_PATH%^
	--model_tuned %MERGED_PATH%^
	--save_to %DEST_PATH%^
	--dim %DIM%^
	--save_precision bf16^
	--device cpu
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

del %MERGED_PATH%
if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

call venv\Scripts\deactivate.bat
popd rem %~dp0sd-scripts
