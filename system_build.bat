@echo off
REM python3.8.2 X64
set PYTHON_PATH="D:\Python\Python38\python.exe"
set LIB="./lib"
%PYTHON_PATH% -m pip install -r requirements.txt --target=%LIB%
PAUSE
