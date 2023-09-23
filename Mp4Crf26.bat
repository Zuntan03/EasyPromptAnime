@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the mp4 file.
	pause & exit /b 1
)

pushd %~dp0animatediff-cli-prompt-travel

set SRC_PATH="%~f1"
set DEST_PATH="%~dpn1crf26.mp4"

echo ffmpeg.exe -y -i %SRC_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation -crf 26 %DEST_PATH%
ffmpeg.exe -y -i %SRC_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation -crf 26 %DEST_PATH%

popd rem %~dp0animatediff-cli-prompt-travel

