@echo off
echo.

set LENGTH=30
set WIDTH=384
set HEIGHT=512
set CONTEXT=16

set INTERPOLATION=FpsX8
set TILE_UPSCALE_MP4_FPS=10
set TILE_UPSCALE_MP4_CRF=20

set /a REFINER_CONTEXT=%CONTEXT%/2

@REM set UPSCALE_MODEL=
@REM set UPSCALE1_MODEL=%UPSCALE_MODEL%
@REM set UPSCALE2_MODEL=%UPSCALE_MODEL%

@REM set UPSCALE1_STRENGTH=
@REM set UPSCALE2_STRENGTH=

set UPSCALE1=
set UPSCALE1_HEIGHT=
set UPSCALE2=
set UPSCALE2_HEIGHT=

if "%~1" == "" (
	echo Drag and drop the configuration *[OPTIONS].json file.
	echo -L[Lenght]-W[Width]-H[Height]-C[Context]-T[TileWidth]-R[RefineWidth]
	pause & exit /b 1
)

set CONFIG_PATH=%~f1
set CONFIG_DIR=%~dp1
set CONFIG_TEMP_PATH=temp\%~nx1

echo pushd %~dp0animatediff-cli-prompt-travel
pushd %~dp0animatediff-cli-prompt-travel
call venv\Scripts\activate.bat

for /f "tokens=2-8 delims=-" %%a in ("%~n1") do (
	call :PARSE_ARG %%a
	call :PARSE_ARG %%b
	call :PARSE_ARG %%c
	call :PARSE_ARG %%d
	call :PARSE_ARG %%e
	call :PARSE_ARG %%f
	call :PARSE_ARG %%g
)

if not exist temp\ ( mkdir temp )
copy /Y "%CONFIG_PATH%" %CONFIG_TEMP_PATH% > nul

echo CONFIG_PATH: %CONFIG_PATH%
echo generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT%
if not "%UPSCALE1%" == "" ( echo %UPSCALE1% -H %UPSCALE1_HEIGHT% )
if not "%UPSCALE2%" == "" ( echo %UPSCALE2% -H %UPSCALE2_HEIGHT% )
echo.

echo animatediff generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT% -c %CONFIG_TEMP_PATH%
animatediff generate -L %LENGTH% -W %WIDTH% -H %HEIGHT% -C %CONTEXT% -c %CONFIG_TEMP_PATH%

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
	echo animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% %GENERATE_FRAMES_DIR%
	animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% %GENERATE_FRAMES_DIR%

	call :FIND_NEW_DIR upscaled
	set UPSCALE1_DIR=upscaled\!NEW_DIR!
	echo UPSCALE1_DIR: !UPSCALE1_DIR!

	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_FRAMES_DIR=!UPSCALE1_DIR!\!NEW_DIR!
	echo UPSCALE1_FRAMES_DIR: !UPSCALE1_FRAMES_DIR!

	echo Frames2Mp4.bat !UPSCALE1_FRAMES_DIR! %TILE_UPSCALE_MP4_FPS% %TILE_UPSCALE_MP4_CRF%
	call ..\Frames2Mp4.bat "!UPSCALE1_FRAMES_DIR!" %TILE_UPSCALE_MP4_FPS% %TILE_UPSCALE_MP4_CRF%
) else if "%UPSCALE1%" == "refine" (
	echo animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% -C %REFINER_CONTEXT% %GENERATE_FRAMES_DIR%
	animatediff %UPSCALE1% -H %UPSCALE1_HEIGHT% -C %REFINER_CONTEXT% %GENERATE_FRAMES_DIR%

	call :FIND_NEW_DIR refine
	set UPSCALE1_DIR=refine\!NEW_DIR!
	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_DIR=!UPSCALE1_DIR!\!NEW_DIR!
	echo UPSCALE1_DIR: !UPSCALE1_DIR!

	call :FIND_NEW_DIR !UPSCALE1_DIR!
	set UPSCALE1_FRAMES_DIR=!UPSCALE1_DIR!\!NEW_DIR!
	echo UPSCALE1_FRAMES_DIR: !UPSCALE1_FRAMES_DIR!
) else (
	echo [ERROR] Unknown upscale type: %UPSCALE1%
	goto :END
)

echo UPSCALE1_DIR: !UPSCALE1_DIR!
echo UPSCALE1_FRAMES_DIR: !UPSCALE1_FRAMES_DIR!
echo UPSCALE2: !UPSCALE2!

if "%UPSCALE2%" == "" (
	copy /Y !UPSCALE1_DIR!\*.mp4 "%CONFIG_DIR%" > nul
	goto :END
) else if "%UPSCALE2%" == "tile-upscale" (
	echo animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% !UPSCALE1_FRAMES_DIR!
	animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% !UPSCALE1_FRAMES_DIR!

	call :FIND_NEW_DIR upscaled
	set UPSCALE2_DIR=upscaled\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_FRAMES_DIR=!UPSCALE2_DIR!\!NEW_DIR!

	echo Frames2Mp4.bat !UPSCALE2_FRAMES_DIR! %TILE_UPSCALE_MP4_FPS% %TILE_UPSCALE_MP4_CRF%
	call ..\Frames2Mp4.bat "!UPSCALE2_FRAMES_DIR!" %TILE_UPSCALE_MP4_FPS% %TILE_UPSCALE_MP4_CRF%
) else if "%UPSCALE2%" == "refine" (
	echo animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% -C %REFINER_CONTEXT% !UPSCALE1_FRAMES_DIR!
	animatediff %UPSCALE2% -H %UPSCALE2_HEIGHT% -C %REFINER_CONTEXT% !UPSCALE1_FRAMES_DIR!

	call :FIND_NEW_DIR refine
	set UPSCALE2_DIR=refine\!NEW_DIR!
	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_DIR=!UPSCALE2_DIR!\!NEW_DIR!

	call :FIND_NEW_DIR !UPSCALE2_DIR!
	set UPSCALE2_FRAMES_DIR=!UPSCALE2_DIR!\!NEW_DIR!
) else (
	echo [ERROR] Unknown upscale type: %UPSCALE1%
	goto :END
)

echo UPSCALE2_DIR: !UPSCALE2_DIR!
echo UPSCALE2_FRAMES_DIR: !UPSCALE2_FRAMES_DIR!
copy /Y !UPSCALE2_DIR!\*.mp4 "%CONFIG_DIR%" > nul

:END
endlocal
call venv\Scripts\deactivate.bat
popd rem %~dp0animatediff-cli-prompt-travel

if "%INTERPOLATION%" == "" ( exit /b 0 )
call :FIND_NEW_MP4 "%CONFIG_DIR%"
call %~dp0%INTERPOLATION%.bat "%CONFIG_DIR%\%NEW_MP4%"

exit /b 0

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
) else (
	echo [ERROR] Unknown argument: %ARG%
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
echo %DIR_COMMAND%
for /f %%f in ('%DIR_COMMAND%') do (
	set NEW_MP4=%%f
	exit /b 0
)
exit /b 0
