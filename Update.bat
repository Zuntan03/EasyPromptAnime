@echo off

pushd %~dp0

pushd animatediff-cli-prompt-travel
git pull

popd rem animatediff-cli-prompt-travel

git pull
call src\Setup.bat

popd rem %~dp0
