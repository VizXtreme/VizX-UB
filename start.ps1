# Windows launcher for VizX-UB. Activates a venv if present, then runs main.py.
$ErrorActionPreference = "Stop"
Set-Location -Path $PSScriptRoot

if (Test-Path ".venv\Scripts\python.exe") {
    & ".venv\Scripts\python.exe" main.py
    exit $LASTEXITCODE
}
if (Test-Path "venv\Scripts\python.exe") {
    & "venv\Scripts\python.exe" main.py
    exit $LASTEXITCODE
}
if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 main.py
    exit $LASTEXITCODE
}
& python main.py
exit $LASTEXITCODE
