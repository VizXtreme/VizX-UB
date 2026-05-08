@echo off
REM Windows launcher for VizX-UB. Activates a venv if present, then runs main.py.

setlocal
cd /d "%~dp0"

if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
    goto :eof
)
if exist "venv\Scripts\python.exe" (
    "venv\Scripts\python.exe" main.py
    goto :eof
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -3 main.py
    goto :eof
)

python main.py
