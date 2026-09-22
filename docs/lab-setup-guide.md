# Lab Setup & Environment Guide

This guide describes how to configure and run the isolated security assessment environment on your local machine.

---

## 1. Prerequisites

- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: Version 3.10 or higher
- **Optional Tools**: Docker (for containerized DVWA), Nmap, cURL

---

## 2. Quick Installation (Self-Contained Local Mode)

### Step 1: Clone and Enter Repository
```bash
git clone https://github.com/your-username/2311CS040137-EH.git
cd 2311CS040137-EH
```

### Step 2: Create and Activate Virtual Environment
**On Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**On Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Initialize the Isolated Security Database
```bash
python assignment-01-sqli/lab/setup_db.py
```
*This creates `security_lab.db` seeded with mock user, product, and account tables.*

---

## 3. Running the Platform

### Option A: Run Full Automated Assessment Suite
To execute all tests, verify SQLi attacks/defenses, and validate remediations in one command:
```bash
python scripts/run_all_tests.py
```

### Option B: Launch Interactive Security Operations Dashboard
To start the web dashboard on `http://127.0.0.1:5000`:
```bash
python dashboard/app.py
```

---

## 4. Optional: Running Standard DVWA in Docker

If you wish to test against the official Damn Vulnerable Web Application container:
```bash
docker compose up -d
```
Access DVWA at: `http://localhost:8080` (Default credentials: `admin` / `password`).
To shut down the lab:
```bash
docker compose down
```
