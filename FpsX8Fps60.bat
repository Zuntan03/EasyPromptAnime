@echo off
pushd %~dp0ECCV2022-RIFE
call venv\Scripts\activate.bat

if "%~1" == "" (
	echo Drag and drop the mp4 file.
	pause & exit /b 1
)

python inference_video.py --exp=3 --video "%~1" --output "%~dpn1_x8.mp4"
ffmpeg.exe -y -i "%~dpn1_x8.mp4" -pix_fmt yuv420p -vcodec libx265 -tune animation -r 60 -crf 20 "%~dpn1_x8e.mp4"

call venv\Scripts\deactivate.bat
popd rem %~dp0ECCV2022-RIFE
