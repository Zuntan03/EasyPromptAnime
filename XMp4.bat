@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the mp4 file.
	pause & exit /b 1
)

set PATH=%~dp0ffmpeg-master-latest-win64-gpl\bin;%PATH%

set SRC_PATH="%~f1"
set DEST_PATH="%~dpn1x.mp4"

set VF_SCALE=
if not "%~2" == "" if not "%~2" == "0" (
	set VF_SCALE=-vf scale=%~2
)

set FPS=-r 40
if not "%~3" == "" (
	if "%~3" == "0" (
		set FPS=
	) else (
		set FPS=-r %~3
	)
)

set BPS=25M
if not "%~4" == "" if not "%~4" == "0" (
	set BPS=%~4
)

pushd %~dp0animatediff-cli-prompt-travel

echo ffmpeg.exe -y -i %SRC_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation %FPS% -vb %BPS% -maxrate %BPS% -bufsize %BPS% %VF_SCALE% %DEST_PATH%

ffmpeg.exe -y^
	-i %SRC_PATH%^
	-pix_fmt yuv420p^
	-vcodec libx264^
	-tune animation^
	%FPS%^
	-vb %BPS%^
	-maxrate %BPS%^
	-bufsize %BPS%^
	%VF_SCALE%^
	%DEST_PATH%

popd rem %~dp0animatediff-cli-prompt-travel

