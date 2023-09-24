@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the mp4 file.
	pause & exit /b 1
)

set CRF=20
if not "%~2" == "" if not "%~2" == "0" (
	set CRF=%~2
)

set SRC_PATH="%~f1"
set DEST_PATH="%~dpn1-crf%CRF%.mp4"

pushd %~dp0animatediff-cli-prompt-travel


echo ffmpeg.exe -y -i %SRC_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation -crf %CRF% %DEST_PATH%
ffmpeg.exe -y -i %SRC_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation -crf %CRF% %DEST_PATH%

popd rem %~dp0animatediff-cli-prompt-travel

