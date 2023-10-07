@echo off
echo.

set LENGTH=30
set WIDTH=384
set HEIGHT=512
set CONTEXT=16

set RIFE_DIV=2
set RIFE_FPS=0
set FFMPEG_FPS=0
set FFMPEG_CRF=20
set TILE_UPSCALE_FPS=10

set /a REFINER_CONTEXT=%CONTEXT%/2

set UPSCALE1=
set UPSCALE1_HEIGHT=
set UPSCALE2=
set UPSCALE2_HEIGHT=

set GENERATE_USE_XFORMERS=
set GENERATE_FORCE_HALF_VAE=
set UPSCALE_USE_XFORMERS=
set UPSCALE_FORCE_HALF_VAE=

if "%~1" == "" (
	echo [ERROR] Drag and drop the configuration .+[OPTIONS].json file.
	echo -L[Lenght]-W[Width]-H[Height]-C[Context]-T[TileHeight]
	pause & exit /b 1
)

set CONFIG_PATH=%~f1
set CONFIG_DIR=%~dp1
set CONFIG_TEMP_PATH=temp\%~nx1

pushd %~dp0animatediff-cli-prompt-travel
call venv\Scripts\activate.bat

for /f "tokens=2-12 delims=-" %%a in ("%~n1") do (
	call :PARSE_ARG %%a
	call :PARSE_ARG %%b
	call :PARSE_ARG %%c
	call :PARSE_ARG %%d
	call :PARSE_ARG %%e
	call :PARSE_ARG %%f
	call :PARSE_ARG %%g
	call :PARSE_ARG %%h
	call :PARSE_ARG %%i
	call :PARSE_ARG %%j
	call :PARSE_ARG %%k
)

if not exist temp\ ( mkdir temp )
copy /Y "%CONFIG_PATH%" "%CONFIG_TEMP_PATH%" > nul

echo CONFIG_PATH: %CONFIG_PATH%
echo generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT%
if not "%UPSCALE1%" == "" ( echo %UPSCALE1% -H %UPSCALE1_HEIGHT% )
if not "%UPSCALE2%" == "" ( echo %UPSCALE2% -H %UPSCALE2_HEIGHT% )
echo.

echo animatediff generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT% -c "%CONFIG_TEMP_PATH%" %GENERATE_USE_XFORMERS% %GENERATE_FORCE_HALF_VAE%
animatediff generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT% -c "%CONFIG_TEMP_PATH%" %GENERATE_USE_XFORMERS% %GENERATE_FORCE_HALF_VAE%
if %ERRORLEVEL% neq 0 ( goto :ERROR_EXIT )

call :FIND_NEW_DIR output
set GENERATE_DIR=output\%NEW_DIR%
echo Generate: %GENERATE_DIR%

call :FIND_NEW_DIR %GENERATE_DIR%
set GENERATE_FRAMES_DIR=%GENERATE_DIR%\%NEW_DIR%
echo GenerateFrames: %GENERATE_FRAMES_DIR%

setlocal enabledelayedexpansion

if "%UPSCALE1%" == "" (
	copy /Y !GENERATE_DIR!\*.mp4 "%CONFIG_DIR%" > nul
	goto :END
) else if "%UPSCALE1%" == "tile-upscale" (
	echo animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% %GENERATE_FRAMES_DIR% %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% %GENERATE_FRAMES_DIR% %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	if %ERRORLEVEL% neq 0 ( endlocal & goto :ERROR_EXIT )

	call :FIND_NEW_DIR upscaled
	set UPSCALE1_DIR=upscaled\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_FRAMES_DIR=!UPSCALE1_DIR!\!NEW_DIR!

	@REM echo Frames2Mp4.bat !UPSCALE1_FRAMES_DIR! %TILE_UPSCALE_FPS% %FFMPEG_CRF%
	@REM call ..\Frames2Mp4.bat "!UPSCALE1_FRAMES_DIR!" %TILE_UPSCALE_FPS% %FFMPEG_CRF%
) else if "%UPSCALE1%" == "refine" (
	echo animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% -C %REFINER_CONTEXT% %GENERATE_FRAMES_DIR% %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% -C %REFINER_CONTEXT% %GENERATE_FRAMES_DIR% %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	if %ERRORLEVEL% neq 0 ( endlocal & goto :ERROR_EXIT )

	call :FIND_NEW_DIR refine
	set UPSCALE1_DIR=refine\!NEW_DIR!
	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_DIR=!UPSCALE1_DIR!\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_FRAMES_DIR=!UPSCALE1_DIR!\!NEW_DIR!
) else (
	echo [ERROR] Unknown upscale type: %UPSCALE1%
	pause
	goto :END
)

echo UPSCALE1_DIR: !UPSCALE1_DIR!
echo UPSCALE1_FRAMES_DIR: !UPSCALE1_FRAMES_DIR!
echo UPSCALE2: !UPSCALE2!

if "%UPSCALE2%" == "" (
	copy /Y !UPSCALE1_DIR!\*.mp4 "%CONFIG_DIR%" > nul
	goto :END
) else if "%UPSCALE2%" == "tile-upscale" (
	echo animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% !UPSCALE1_FRAMES_DIR! %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% !UPSCALE1_FRAMES_DIR! %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	if %ERRORLEVEL% neq 0 ( endlocal & goto :ERROR_EXIT )

	call :FIND_NEW_DIR upscaled
	set UPSCALE2_DIR=upscaled\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_FRAMES_DIR=!UPSCALE2_DIR!\!NEW_DIR!

	@REM echo Frames2Mp4.bat !UPSCALE2_FRAMES_DIR! %TILE_UPSCALE_FPS% %FFMPEG_CRF%
	@REM call ..\Frames2Mp4.bat "!UPSCALE2_FRAMES_DIR!" %TILE_UPSCALE_FPS% %FFMPEG_CRF%
) else if "%UPSCALE2%" == "refine" (
	echo animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% -C %REFINER_CONTEXT% !UPSCALE1_FRAMES_DIR! %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% -C %REFINER_CONTEXT% !UPSCALE1_FRAMES_DIR! %UPSCALE_USE_XFORMERS% %UPSCALE_FORCE_HALF_VAE%
	if %ERRORLEVEL% neq 0 ( endlocal & goto :ERROR_EXIT )

	call :FIND_NEW_DIR refine
	set UPSCALE2_DIR=refine\!NEW_DIR!
	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_DIR=!UPSCALE2_DIR!\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_FRAMES_DIR=!UPSCALE2_DIR!\!NEW_DIR!
) else (
	echo [ERROR] Unknown upscale type: %UPSCALE1%
	pause
	goto :END
)

echo UPSCALE2_DIR: !UPSCALE2_DIR!
echo UPSCALE2_FRAMES_DIR: !UPSCALE2_FRAMES_DIR!
copy /Y !UPSCALE2_DIR!\*.mp4 "%CONFIG_DIR%" > nul

:END
endlocal
call venv\Scripts\deactivate.bat
popd rem %~dp0animatediff-cli-prompt-travel

set ZERO_PADDING_TIME=%TIME: =0%
for /f "tokens=2-7 delims=/:. " %%a in ("echo %DATE% %ZERO_PADDING_TIME%") do (
	set MMDD_HHMM_SS=%%b%%c_%%d%%e_%%f
)
call :FIND_NEW_MP4 "%CONFIG_DIR%"
rename "%CONFIG_DIR%\%NEW_MP4%" "%MMDD_HHMM_SS%-%NEW_MP4:~3%"

if "%RIFE_DIV%" == "0" ( exit /b 0 )
call :FIND_NEW_MP4 "%CONFIG_DIR%"

echo FpsX4.bat "%CONFIG_DIR%\%NEW_MP4%" %RIFE_DIV% %RIFE_FPS% %FFMPEG_FPS% %FFMPEG_CRF%
call %~dp0FpsX4.bat "%CONFIG_DIR%\%NEW_MP4%" %RIFE_DIV% %RIFE_FPS% %FFMPEG_FPS% %FFMPEG_CRF%

exit /b 0

:ERROR_EXIT
call venv\Scripts\deactivate.bat
popd rem %~dp0animatediff-cli-prompt-travel
echo [ERROR EXIT]
exit /b 1

:PARSE_ARG
if "%~1" == "" ( exit /b 0 )
set ARG=%1
set ARG_KEY=%ARG:~0,1%
set ARG_VALUE=%ARG:~1%

if "%ARG_KEY%" == "L" (
	set LENGTH=%ARG_VALUE%
) else if "%ARG_KEY%" == "W" (
	set WIDTH=%ARG_VALUE%
) else if "%ARG_KEY%" == "H" (
	set HEIGHT=%ARG_VALUE%
) else if "%ARG_KEY%" == "C" (
	set CONTEXT=%ARG_VALUE%
) else if "%ARG_KEY%" == "T" (
	if "%UPSCALE1%" == "" (
		set UPSCALE1=tile-upscale
		set UPSCALE1_HEIGHT=%ARG_VALUE%
	) else if "%UPSCALE2%" == "" (
		set UPSCALE2=tile-upscale
		set UPSCALE2_HEIGHT=%ARG_VALUE%
	)
) else if "%ARG_KEY%" == "R" (
	if "%UPSCALE1%" == "" (
		set UPSCALE1=refine
		set UPSCALE1_HEIGHT=%ARG_VALUE%
	) else if "%UPSCALE2%" == "" (
		set UPSCALE2=refine
		set UPSCALE2_HEIGHT=%ARG_VALUE%
	)
) else if "%ARG_KEY%" == "D" (
	set RIFE_DIV=%ARG_VALUE%
) else if "%ARG_KEY%" == "I" (
	set RIFE_FPS=%ARG_VALUE%
) else if "%ARG_KEY%" == "F" (
	set FFMPEG_FPS=%ARG_VALUE%
) else if "%ARG_KEY%" == "M" (
	set FFMPEG_CRF=%ARG_VALUE%
) else if "%ARG_KEY%" == "U" (
	set TILE_UPSCALE_FPS=%ARG_VALUE%
) else if "%ARG_KEY%" == "x" (
	set GENERATE_USE_XFORMERS=--xformers
) else if "%ARG_KEY%" == "v" (
	set GENERATE_FORCE_HALF_VAE=--half-vae
) else if "%ARG_KEY%" == "X" (
	set UPSCALE_USE_XFORMERS=--xformers
) else if "%ARG_KEY%" == "V" (
	set UPSCALE_FORCE_HALF_VAE=--half-vae
) else (
	echo [ERROR] Unknown argument: %ARG%
	pause
)
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
