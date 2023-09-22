@echo off
pushd %~dp0

where findstr > nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] findstr not found. Add C:\Windows\System32 to PATH.
	pause
    exit /b 1
)

python --version | findstr "3.10." || (
	echo [ERROR] Invalid python version. require 3.10.6.
	python --version
	echo Ctrl + Click: https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe
	pause
	exit /b 1
)

where git
if %ERRORLEVEL% neq 0 (
	echo [ERROR] git not found. require Git for Windows.
	echo Ctrl + Click: https://gitforwindows.org/
	pause
	exit /b 1
)

git clone https://github.com/Zuntan03/EasyPromptAnime
robocopy .\EasyPromptAnime\ . /s /move

call src\Setup.bat
start OpenColabEditor.bat

popd
del %~f0
