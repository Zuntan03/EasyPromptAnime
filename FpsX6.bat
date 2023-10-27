@echo off
if "%~1" == "" (
	echo [ERROR] Drag and drop the mp4 file.
	pause & exit /b 1
)
set PATH=%~dp0ffmpeg-master-latest-win64-gpl\bin;%PATH%

set RIFE_MULTI_NUM=6
set RIFE_FPS_NAME=
set RIFE_FPS_OPTION=
set FFMPEG_FPS_NAME=
set FFMPEG_FPS_OPTION=
set FFMPEG_CRF=20

if not "%~2" == "" if not "%~2" == "0" (
	set RIFE_MULTI_NUM=%~2
)
if not "%~3" == "" if not "%~3" == "0" (
	set RIFE_FPS_NAME=-f%~3
	set RIFE_FPS_OPTION=--fps=%~3
)
if not "%~4" == "" if not "%~4" == "0" (
	set FFMPEG_FPS_NAME=-F%~4
	set FFMPEG_FPS_OPTION=-r %~4
)
if not "%~5" == "" if not "%~5" == "0" (
	set FFMPEG_CRF=%~5
)

set SRC_PATH="%~f1"
set RIFE_DEST_PATH="%~dpn1-M%RIFE_MULTI_NUM%%RIFE_FPS_NAME%.mp4"
set FFMPEG_DEST_PATH="%~dpn1-M%RIFE_MULTI_NUM%%RIFE_FPS_NAME%e%FFMPEG_FPS_NAME%.mp4"

pushd %~dp0Practical-RIFE
call venv\Scripts\activate.bat

@REM echo ARGS: %1 %2 %3 %4 %5
@REM echo RIFE_MULTI_NUM: %RIFE_MULTI_NUM%
@REM echo RIFE_FPS_NAME: %RIFE_FPS_NAME%
@REM echo RIFE_FPS_OPTION: %RIFE_FPS_OPTION%
@REM echo FFMPEG_FPS_NAME: %FFMPEG_FPS_NAME%
@REM echo FFMPEG_FPS_OPTION: %FFMPEG_FPS_OPTION%
@REM echo FFMPEG_CRF: %FFMPEG_CRF%
@REM echo SRC_PATH: %SRC_PATH%
@REM echo RIFE_DEST_PATH: %RIFE_DEST_PATH%
@REM echo FFMPEG_DEST_PATH: %FFMPEG_DEST_PATH%
@REM pause

echo python inference_video.py --multi=%RIFE_MULTI_NUM% --video %SRC_PATH% %RIFE_FPS_OPTION% --output %RIFE_DEST_PATH%
python inference_video.py --multi=%RIFE_MULTI_NUM% --video %SRC_PATH% %RIFE_FPS_OPTION% --output %RIFE_DEST_PATH%

echo ffmpeg.exe -y -i %RIFE_DEST_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation %FFMPEG_FPS_OPTION% -crf %FFMPEG_CRF% %FFMPEG_DEST_PATH%
ffmpeg.exe -y -i %RIFE_DEST_PATH% -pix_fmt yuv420p -vcodec libx264 -tune animation %FFMPEG_FPS_OPTION% -crf %FFMPEG_CRF% %FFMPEG_DEST_PATH%

call venv\Scripts\deactivate.bat
popd rem %~dp0Practical-RIFE
