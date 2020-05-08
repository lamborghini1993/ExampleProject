@echo off
cd ../Script/
REM 需要安装pyarmor: pip install pyarmor
pyarmor pack --name example main.py
Robocopy dist/example ../example
rd /s/q build dist
pause