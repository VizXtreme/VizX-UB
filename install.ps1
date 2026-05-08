#Requires -Version 5.1
<#
.SYNOPSIS
    Windows installer for VizX-UB.
.DESCRIPTION
    PowerShell counterpart to install.sh. Sets up a virtual environment,
    installs requirements, and writes a .env file. Run from the project root:
        powershell -ExecutionPolicy Bypass -File .\install.ps1
#>

$ErrorActionPreference = "Stop"

function Write-Color($Text, $Color = "White") {
    Write-Host $Text -ForegroundColor $Color
}

function Read-Default($Prompt, $Default = "") {
    $suffix = if ($Default) { " [$Default]" } else { "" }
    $val = Read-Host "$Prompt$suffix"
    if ([string]::IsNullOrWhiteSpace($val)) { return $Default }
    return $val
}

# --- Verify we're in the project root ---
if (-not (Test-Path "main.py") -or -not (Test-Path "requirements.txt")) {
    Write-Color "main.py / requirements.txt not found. Run this from the VizX-UB project root." Red
    exit 1
}

if ((Test-Path ".env") -and (Test-Path "my_account.session")) {
    Write-Color "It seems VizX-UB is already installed (.env and session present). Exiting." Green
    exit 0
}

# --- Locate Python ---
$python = $null
foreach ($cmd in @("py", "python", "python3")) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        $version = & $found.Source --version 2>&1
        if ($version -match "Python 3\.(1[1-9]|[2-9]\d)") {
            $python = $found.Source
            Write-Color "Using $python ($version)" Green
            break
        }
    }
}
if (-not $python) {
    Write-Color "Python 3.11+ not found. Install from https://www.python.org/downloads/windows/ and re-run." Red
    exit 1
}

# --- Virtualenv ---
$create_venv = Read-Default "Create a virtual environment? (Y/n)" "Y"
if ($create_venv -notmatch "^[nN]") {
    if (-not (Test-Path ".venv") -and -not (Test-Path "venv")) {
        Write-Color "Creating virtual environment in .venv..." Yellow
        & $python -m venv .venv
        if ($LASTEXITCODE -ne 0) { exit 2 }
    }
}

if (Test-Path ".venv\Scripts\python.exe") {
    $python = (Resolve-Path ".venv\Scripts\python.exe").Path
} elseif (Test-Path "venv\Scripts\python.exe") {
    $python = (Resolve-Path "venv\Scripts\python.exe").Path
}
Write-Color "Python: $python" Green

# --- Install requirements ---
Write-Color "Upgrading pip..." Yellow
& $python -m pip install --upgrade pip
Write-Color "Installing requirements..." Yellow
& $python -m pip install -U -r requirements.txt
if ($LASTEXITCODE -ne 0) {
    Write-Color "pip install failed." Red
    exit 2
}

# --- Collect env values ---
Write-Color "`nEnter API_ID and API_HASH (https://my.telegram.org/)" Cyan
Write-Color "Leave empty to use defaults (NOT recommended; significantly raises ban risk)." Yellow
$api_id = Read-Host "API_ID"
$api_hash = ""
if ([string]::IsNullOrWhiteSpace($api_id)) {
    $confirm = Read-Host "Type 'I agree' to use shared default keys"
    if ($confirm -ne "I agree") {
        Write-Color "Confirmation not provided. Exiting." Red
        exit 1
    }
    $api_id = "2040"
    $api_hash = "b18441a1ff607e10a989891a5462e627"
} else {
    $api_hash = Read-Host "API_HASH"
}

$pm_limit = Read-Default "PM_LIMIT warn limit" "3"

$musicbot = Read-Default "Use musicbot? (y/N)" "N"
$second_session = ""
if ($musicbot -match "^[yY]") {
    $second_session = Read-Host "SECOND_SESSION (string session for musicbot)"
}

$apiflash_key = Read-Host "APIFLASH_KEY (optional, https://apiflash.com/)"
$rmbg_key     = Read-Host "RMBG_KEY (optional, https://www.remove.bg/)"
$vt_key       = Read-Host "VT_KEY (optional, https://www.virustotal.com/)"
$gemini_key   = Read-Host "GEMINI_KEY (optional)"
$cohere_key   = Read-Host "COHERE_KEY (optional)"
$port         = Read-Default "PORT for the web UI" "8000"

Write-Color "`nChoose database type:" Yellow
Write-Host "  [1] MongoDB (your URL)"
Write-Host "  [3] SQLite (default)"
$db_choice = Read-Default ">" "3"
if ($db_choice -eq "1") {
    $db_url = Read-Host "Mongo db_url"
    $db_name = "VizX_UB"
    $db_type = "mongodb"
} else {
    $db_url = ""
    $db_name = "db.sqlite3"
    $db_type = "sqlite3"
}

# --- Write .env ---
$envContent = @"
API_ID=$api_id
API_HASH=$api_hash
STRINGSESSION=
# sqlite/sqlite3 or mongo/mongodb
DATABASE_TYPE=$db_type
# file name for sqlite3, database name for mongodb
DATABASE_NAME=$db_name
# only for mongodb
DATABASE_URL=$db_url
APIFLASH_KEY=$apiflash_key
RMBG_KEY=$rmbg_key
VT_KEY=$vt_key
GEMINI_KEY=$gemini_key
COHERE_KEY=$cohere_key
PM_LIMIT=$pm_limit
SECOND_SESSION=$second_session
PORT=$port
"@
[System.IO.File]::WriteAllText((Join-Path (Get-Location) ".env"), $envContent)

Write-Color "`nRunning install.py to log in..." Yellow
& $python install.py 3
if ($LASTEXITCODE -ne 0) {
    Write-Color "install.py failed." Red
    exit 3
}

Write-Color "`n============================" Green
Write-Color " VizX-UB installed!" Green
Write-Color " Start with: .\start.bat   (or)   .\start.ps1" Green
Write-Color "============================" Green
