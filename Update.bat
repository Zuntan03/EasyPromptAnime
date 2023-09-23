@echo off
pushd %~dp0

git pull
call src\Setup.bat

popd rem %~dp0
