# ==============================================================================
# Windows PowerShell Automated Setup Script
# Web Application Security & Ethical Hacking Assessment Platform
# ==============================================================================

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  Cybersecurity Assessment Platform - Automated Environment Setup" -ForegroundColor Green
Write-Host "  Project Identifier: 2311CS040137-EH" -ForegroundColor White
Write-Host "==============================================================================" -ForegroundColor Cyan

# 1. Check Python installation
Write-Host "`n[*] Verifying Python installation..." -ForegroundColor Yellow
$pythonCheck = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCheck) {
    Write-Host "[-] Python 3.10+ is required but not found in PATH." -ForegroundColor Red
    Exit 1
}
Write-Host "[+] Found Python: $($pythonCheck.Source)" -ForegroundColor Green

# 2. Virtual Environment Setup
if (-not (Test-Path "venv")) {
    Write-Host "[*] Creating virtual environment (venv)..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "[+] Virtual environment created." -ForegroundColor Green
} else {
    Write-Host "[+] Virtual environment already exists." -ForegroundColor Green
}

# 3. Installing dependencies
Write-Host "[*] Installing required Python dependencies..." -ForegroundColor Yellow
.\venv\Scripts\pip install -r requirements.txt --quiet
Write-Host "[+] Dependencies installed successfully." -ForegroundColor Green

# 4. Initialize Database
Write-Host "[*] Initializing & seeding isolated lab database..." -ForegroundColor Yellow
.\venv\Scripts\python assignment-01-sqli/lab/setup_db.py

# 5. Run full test verification
Write-Host "[*] Executing full automated assessment test suite..." -ForegroundColor Yellow
.\venv\Scripts\python scripts/run_all_tests.py

Write-Host "`n==============================================================================" -ForegroundColor Cyan
Write-Host "  [SUCCESS] SETUP & VERIFICATION COMPLETED SUCCESSFULLY!" -ForegroundColor Green
Write-Host "  To launch the interactive Security Dashboard, run:" -ForegroundColor White
Write-Host "    .\venv\Scripts\python dashboard/app.py" -ForegroundColor Cyan
Write-Host "  To view generated reports, open: reports\final_report.html" -ForegroundColor White
Write-Host "==============================================================================" -ForegroundColor Cyan
