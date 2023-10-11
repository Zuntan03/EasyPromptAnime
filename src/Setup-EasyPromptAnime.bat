@echo off
pushd %~dp0

where findstr > nul 2>&1
if %ERRORLEVEL% neq 0 (
	echo [ERROR] findstr not found. Add C:\Windows\System32 to PATH.
	pause & popd & exit /b 1
)

echo "%~dp0" | findstr /r /c:"[^a-zA-Z0-9:/\\]+" >nul
if %ERRORLEVEL% equ 0 (
	echo [ERROR] "%~dp0" contains non-alphanumeric characters.
	pause & popd & exit /b 1
)

python --version | findstr "3.10." || (
	echo [ERROR] Invalid python version. require 3.10.6.
	python --version
	echo Ctrl + Click: https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe
	pause & popd & exit /b 1
)

where git
if %ERRORLEVEL% neq 0 (
	echo [ERROR] git not found. require Git for Windows.
	echo Ctrl + Click: https://gitforwindows.org/
	pause & popd & exit /b 1
)

git clone https://github.com/Zuntan03/EasyPromptAnime
if %ERRORLEVEL% neq 0 (
	echo [ERROR] git clone https://github.com/Zuntan03/EasyPromptAnime
	echo Disable virus checking software.
	pause & popd & exit /b 1
)

robocopy .\EasyPromptAnime\ . /s /move

call src\Setup.bat
if %errorlevel% neq 0 ( popd & exit /b %errorlevel% )

start cmd /c EasyPromptAnimeEditor.bat

popd rem %~dp0
echo The following error messages are not a problem.
del "%~f0"
