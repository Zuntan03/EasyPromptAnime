@echo off

pushd %~dp0

git pull

pushd animatediff-cli-prompt-travel
git pull
popd rem animatediff-cli-prompt-travel

call src\Setup.bat

popd rem %~dp0
