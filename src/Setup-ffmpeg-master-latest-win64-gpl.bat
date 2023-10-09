@echo off

pushd %~dp0..
set FFMPEG_DIR=ffmpeg-master-latest-win64-gpl
if not exist %FFMPEG_DIR% (
	echo curl -Lo ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
	curl -Lo ffmpeg.zip https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo Unzip ffmpeg.zip
	PowerShell -Version 5.1 -ExecutionPolicy Bypass Expand-Archive -Path ffmpeg.zip -DestinationPath .
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	echo del ffmpeg.zip
	del ffmpeg.zip
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )

	copy /Y %FFMPEG_DIR%\bin\ffmpeg.exe animatediff-cli-prompt-travel
	if %errorlevel% neq 0 ( pause & popd & exit /b %errorlevel% )
)
popd rem %~dp0..
