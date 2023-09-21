@echo off

pushd %~dp0animatediff-cli-prompt-travel
if "%~1" == "" (
	echo Drag and drop the frames directory.
	pause & exit /b 1
)
set FRAMES_DIR=%~dpn1
set FPS=10
set CRF=20
if not "%2" == "" ( set FPS=%2 )
if not "%3" == "" ( set CRF=%3 )

echo ffmpeg.exe -y -framerate %FPS% -i "%FRAMES_DIR%\%%08d.png" -pix_fmt yuv420p -vcodec libx265 -tune animation -r %FPS% -crf %CRF% "%FRAMES_DIR%.mp4"

ffmpeg.exe -y -framerate %FPS%^
	-i "%FRAMES_DIR%\%%08d.png"^
	-pix_fmt yuv420p^
	-vcodec libx265^
	-tune animation^
	-r %FPS%^
	-crf %CRF%^
	"%FRAMES_DIR%.mp4"

popd rem %~dp0animatediff-cli-prompt-travel
