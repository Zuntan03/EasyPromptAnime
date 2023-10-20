@echo off

pushd %~dp0
call editor\venv\Scripts\activate.bat

if not exist output ( mkdir output )
if not exist editor\log ( mkdir editor\log )
set ZERO_PADDING_TIME=%TIME: =0%
for /f "tokens=2-7 delims=/:. " %%a in ("echo %DATE% %ZERO_PADDING_TIME%") do (
	set YYYY_MMDD_HHMM_SS=%%a_%%b%%c_%%d%%e_%%f
)

python editor\src\EasyPromptAnimeEditor.py > editor\log\EasyPromptAnimeEditorLog-%YYYY_MMDD_HHMM_SS%.txt

call editor\venv\Scripts\deactivate.bat
popd rem %~dp0
