echo off
REM python3.8.2 X64
set PYTHON_PATH="D:\Python\Python38\python.exe"
%PYTHON_PATH% -m venv ./venv
set PIP_PATH="./venv/Scripts/pip.exe"
%PIP_PATH% install -r requirements.txt
PAUSE
