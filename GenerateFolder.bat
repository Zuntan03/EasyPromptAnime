@echo off
if "%~1" == "" ( goto ERROR_EXIT )
if not exist "%~1\*" ( goto ERROR_EXIT )
if not exist "%~1\*.json" ( goto ERROR_EXIT )

for /f %%a in ('dir /b "%~1\*.json"') do (
	call "%~dp0Generate.bat" "%~f1\%%a"
	@REM if !ERRORLEVEL! neq 0 ( pause & exit /b 1 )
)
exit /b 0

:ERROR_EXIT
echo [ERROR] Drag and drop the FOLDER containing the configuration .+[OPTIONS].json files.
echo -L[Lenght]-W[Width]-H[Height]-C[Context]-T[TileHeight]-R[RefineHeight]
pause
exit /b 1
