@echo off

@REM If you want to disable (y/n), delete the three lines below.
echo Delete output/*/  upscaled/*/  refine/*/ (y/n)
set /p YES_OR_NO=
if /i not "%YES_OR_NO%" == "Y" ( exit /b 0 )

pushd %~dp0animatediff-cli-prompt-travel

for /d %%d in ("output\*") do ( rmdir /s /q "%%~d" )
for /d %%d in ("upscaled\*") do ( rmdir /s /q "%%~d" )
for /d %%d in ("refine\*") do ( rmdir /s /q "%%~d" )

popd rem %~dp0animatediff-cli-prompt-travel
