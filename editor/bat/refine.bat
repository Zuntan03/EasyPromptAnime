@echo off
echo.
set PATH=%~dp0..\..\ffmpeg-master-latest-win64-gpl\bin;%PATH%

set RIFE_DIV=3
set RIFE_FPS=0
set FFMPEG_FPS=0
set FFMPEG_CRF=20

pushd %~dp0..\..\animatediff-cli-prompt-travel
call venv\Scripts\activate.bat
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )

echo animatediff refine %*
animatediff refine %*
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )

setlocal enabledelayedexpansion

call :FIND_NEW_DIR refine
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )
set REFINE_DIR=refine\!NEW_DIR!
echo REFINE_DIR: %REFINE_DIR%

call :FIND_NEW_DIR %REFINE_DIR%
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )
set UPSCALE_DIR=%REFINE_DIR%\!NEW_DIR!
echo UPSCALE_DIR: %UPSCALE_DIR%

call :FIND_NEW_MP4 "%UPSCALE_DIR%\"
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )

set ZERO_PADDING_TIME=%TIME: =0%
for /f "tokens=2-7 delims=/:. " %%a in ("echo %DATE% %ZERO_PADDING_TIME%") do (
	set YYYY_MMDD_HHMM_SS=%%a_%%b%%c_%%d%%e_%%f
)

rename %UPSCALE_DIR%\!NEW_MP4! %YYYY_MMDD_HHMM_SS%-!NEW_MP4:~3!
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )

set UPSCALE_MP4=%UPSCALE_DIR%\%YYYY_MMDD_HHMM_SS%-!NEW_MP4:~3!
echo UPSCALE_MP4: %UPSCALE_MP4%

echo FpsX4.bat "%UPSCALE_MP4%" %RIFE_DIV% %RIFE_FPS% %FFMPEG_FPS% %FFMPEG_CRF%
call "%~dp0..\..\FpsX4.bat" "%UPSCALE_MP4%" %RIFE_DIV% %RIFE_FPS% %FFMPEG_FPS% %FFMPEG_CRF%
if %ERRORLEVEL% neq 0 ( popd & exit /b %ERRORLEVEL% )

endlocal
popd rem %~dp0..\..\animatediff-cli-prompt-travel
exit /b 0

:FIND_NEW_DIR
set NEW_DIR=
set DIR_COMMAND=dir /b /ad /o-d /tw %1
for /f %%d in ('%DIR_COMMAND%') do (
	set NEW_DIR=%%d
	exit /b 0
)
exit /b 0

:FIND_NEW_MP4
set NEW_MP4=
set DIR_COMMAND=dir /b /a-d /o-d /tw "%~1*.mp4"
for /f %%f in ('%DIR_COMMAND%') do (
	set NEW_MP4=%%f
	exit /b 0
)
exit /b 0
