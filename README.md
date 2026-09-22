# Web Application Security & Ethical Hacking Assessment Platform

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Assessment Standard](https://img.shields.io/badge/Standards-OWASP%20%7C%20PTES%20%7C%20NIST-brightgreen.svg)](docs/methodology.md)
[![Vulnerability Remediation](https://img.shields.io/badge/Remediation%20Status-100%25%20Verified-success.svg)](reports/final_technical_report.md)
[![License](https://img.shields.io/badge/License-MIT%20Academic-lightgrey.svg)](LICENSE)

**Academic Course / Portfolio Code:** `2311CS040137-EH`  
**Lead Assessor / Developer:** Student Security Engineer  
**Classification:** Academic Laboratory Project & Vulnerability Assessment Platform  

---

## 📌 1. Project Overview

The **Web Application Security & Ethical Hacking Assessment Platform** is a unified, production-grade cybersecurity project that combines two major assessment modules into a single, cohesive architecture:

1. **Module 1 (Assignment 1): SQL Injection Detection, Exploitation & Prevention Engine**
   - In-depth vulnerability mechanics of CWE-89 (Authentication Bypass, UNION-based data extraction, and numeric/error SQLi).
   - Direct comparison between insecure string concatenation and secure parameterized prepared statements.
   - Automated regression test harnesses proving 100% exploit prevention on remediated code.
2. **Module 2 (Assignment 2): Integrated Ethical Hacking Assessment Framework**
   - Multi-phase penetration testing engagement following the PTES and NIST SP 800-115 frameworks:
     $$\text{Recon} \longrightarrow \text{Scanning} \longrightarrow \text{Enumeration} \longrightarrow \text{Vuln Analysis} \longrightarrow \text{Exploitation} \longrightarrow \text{Remediation} \longrightarrow \text{Retesting}$$
   - Structured vulnerability catalog (`VULN-001` through `VULN-008`), false positive triage, controlled PoCs, defense hardening, and automated retest matrices.

---

## 🏛️ 2. Unified System Architecture

```text
========================================================================================
                      SECURITY OPERATIONS & ASSESSMENT PLATFORM
========================================================================================

   +-------------------------------------------------------------------------------+
   |               Unified Web Dashboard & Security CLI (Flask / Rich)             |
   |   - Interactive SQLi Visualizer        - Target Reconnaissance Explorer       |
   |   - Vulnerability Ledger (VULN-xxx)    - Evidence Index (EV-xxx / SHA-256)    |
   |   - Retest Regression Suite Engine     - One-Click Report Generator           |
   +-------------------------------------------------------------------------------+
                                      |
         +----------------------------+----------------------------+
         |                                                         |
         v                                                         v
+------------------------------------+   +---------------------------------------------+
|    MODULE 1: SQLi ASSESSMENT       |   |    MODULE 2: ETHICAL HACKING WORKFLOW       |
+------------------------------------+   +---------------------------------------------+
| 1. Vulnerable Query Engine         |   | Phase 1: Recon & Domain Profiling           |
|    - Raw string formatting         |   | Phase 2: Nmap Port & Service Scanning       |
|    - Auth Bypass, UNION, Error SQLi|   | Phase 3: Web & Content Enumeration          |
| 2. Secure Remediation Engine       |   | Phase 4: Vuln Analysis & Triage (VULN-xxx)  |
|    - Parameterized Prepared Stmts  |   | Phase 5: Controlled POC Exploitation        |
|    - Input Type/Format Sanitization|   | Phase 6: Defense Hardening & Patching       |
| 3. Automated Regression Harness    |   | Phase 7: Automated Retest Matrix            |
+------------------------------------+   +---------------------------------------------+
         |                                                         |
         +----------------------------+----------------------------+
                                      |
                                      v
   +-------------------------------------------------------------------------------+
   |                      Isolated Local Lab Perimeter                             |
   |   - SQLite Database Sandbox (Sandboxed Tables: users, products, accounts)     |
   |   - Local Mock HTTP & Service Stack (Endpoints on 127.0.0.1:5001)             |
   |   - Optional Dockerized DVWA Target (Port 8080)                               |
   +-------------------------------------------------------------------------------+
```

---

## 📂 3. Repository Structure

```text
2311CS040137-EH/
│
├── README.md                           # Master Project Overview & Documentation
├── LICENSE                             # Educational / MIT License
├── .gitignore                          # Standard clean exclusions
├── .env.example                        # Template environment variables
├── requirements.txt                    # Minimal core dependencies
├── docker-compose.yml                  # Optional Docker lab environment (DVWA + isolated DB)
│
├── docs/                               # Formal Methodology & Engineering Specifications
│   ├── project-overview.md             # Background, scope, rules of engagement, objectives
│   ├── architecture.md                 # System architecture, data flow, component breakdown
│   ├── methodology.md                  # Ethical hacking methodology (PTES / NIST SP 800-115 / OWASP)
│   ├── lab-setup-guide.md              # Step-by-step isolated environment setup guide
│   └── threat-model.md                 # Threat modeling (STRIDE / DREAD) of target applications
│
├── assignment-01-sqli/                 # MODULE 1: SQL INJECTION DETECTION & PREVENTION
│   ├── README.md                       # Assignment 1 Guide, Objectives, and Rubric Compliance
│   ├── lab/                            # Lab setup & DB seeding scripts (schema.sql, setup_db.py)
│   ├── vulnerable/                     # Vulnerable endpoints & string interpolation queries
│   ├── secure/                         # Hardened endpoints with validation & prepared statements
│   ├── tests/                          # Automated exploit harnesses & remediation verifiers
│   ├── evidence/                       # Standardized evidence logs (EV-SQLI-001..EV-SQLI-003)
│   └── report/                         # Assignment 1 Technical Security Report
│
├── assignment-02-ethical-hacking/      # MODULE 2: INTEGRATED ETHICAL HACKING ASSESSMENT
│   ├── README.md                       # Assignment 2 Guide & Methodology Lifecycle
│   ├── 01-reconnaissance/              # Phase 1: Passive/Active Recon & OSINT
│   ├── 02-scanning/                    # Phase 2: Host Discovery & Port Scanning
│   ├── 03-enumeration/                 # Phase 3: Service Banner & Web Content Enumeration
│   ├── 04-vulnerability-analysis/     # Phase 4: CVE/CWE Identification & False Positive Triage
│   ├── 05-exploitation/                # Phase 5: Controlled Proof-of-Concepts (Safe / Non-destructive)
│   ├── 06-remediation/                 # Phase 6: Defensive Engineering & Patch Implementation
│   ├── 07-retesting/                   # Phase 7: Verification & Regression Testing
│   ├── evidence/                       # Assignment 2 Standardized Evidence Vault
│   └── report/                         # Assignment 2 Technical Security Assessment
│
├── dashboard/                          # UNIFIED SECURITY OPERATIONS DASHBOARD
│   ├── app.py                          # Flask assessment backend & API
│   ├── static/                         # Dark-Cyber UI (CSS Glassmorphism, JS Controllers)
│   └── templates/                      # Interactive HTML views & Query Comparators
│
├── scripts/                            # PLATFORM AUTOMATION & UTILITIES
│   ├── run_all_tests.py                # Single-command end-to-end test execution
│   ├── nmap_parser.py                  # Converts Nmap XML/JSON into structured tables
│   ├── evidence_manager.py             # Indexes, validates, and hashes evidence files (SHA-256)
│   ├── generate_final_report.py        # Compiles unified Markdown & HTML audit reports
│   └── setup_environment.ps1           # Windows PowerShell automated one-click setup script
│
└── reports/                            # FINAL GENERATED AUDIT DELIVERABLES
    ├── evidence_index.json             # Central evidence registry with timestamps & SHA-256 hashes
    ├── final_executive_summary.md      # C-Suite / Management briefing
    ├── final_technical_report.md       # Comprehensive 19-section faculty assessment report
    └── final_report.html               # Printable, high-aesthetic HTML report
```

---

## 🚀 4. Quick Start & Execution

### Prerequisites
- Python 3.10+ installed
- Windows PowerShell / Bash terminal

### Option A: One-Click Setup (Windows PowerShell)
```powershell
.\scripts\setup_environment.ps1
```

### Option B: Manual Setup (Windows / Linux / macOS)
1. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Initialize the isolated security lab database:**
   ```bash
   python assignment-01-sqli/lab/setup_db.py
   ```

---

## 🧪 5. Testing & Validation

### Run Full End-to-End Automated Test Suite (Single Command)
```bash
python scripts/run_all_tests.py
```
This executes:
- ✅ Database Seeding & Setup
- ✅ Assignment 1 Vulnerability Confirmation Suite (`test_sqli_vulnerable.py`)
- ✅ Assignment 1 Remediation Verification Suite (`test_sqli_secure.py`)
- ✅ Assignment 2 Automated Retesting Matrix (`retest_all.py`)
- ✅ Platform Evidence Indexing & SHA-256 Cryptographic Hashing (`evidence_manager.py`)
- ✅ Final Report Compilation (`generate_final_report.py`)

---

## 🖥️ 6. Security Operations Dashboard

To launch the web dashboard:
```bash
python dashboard/app.py
```
Open **`http://127.0.0.1:5000`** in your browser to interact with:
- **Interactive Query Comparator**: Execute real payloads live against vulnerable vs. secure engines.
- **7-Phase Penetration Testing Visualizer**: Step through each phase from Recon to Retesting.
- **Evidence Vault Explorer**: Browse indexed evidence records and verify SHA-256 hashes.

---

## 📊 7. Discovered Findings & Remediation Matrix

| Finding ID | Title | CVSS v3.1 | Severity | Pre-Patch Status | Post-Patch Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **VULN-001** | SQL Injection in Authentication Service | **9.8** | **CRITICAL** | Exploitable (Admin session gained) | **REMEDIATED** (Prepared statements & regex) |
| **VULN-002** | UNION-Based Data Extraction in Search | **8.6** | **HIGH** | Exploitable (Extracted financial tables) | **REMEDIATED** (Parameterized LIKE clause) |
| **VULN-003** | Numeric SQLi & Parameter Injection | **7.5** | **HIGH** | Exploitable (Dumped user database) | **REMEDIATED** (Integer coercion & query binding) |
| **VULN-004** | Missing HTTP Security Headers | **6.5** | **MEDIUM** | Exploitable (Clickjacking / Sniffing risk) | **REMEDIATED** (Response header middleware) |
| **VULN-005** | Verbose Server Software Banner Disclosures | **5.3** | **MEDIUM** | Exploitable (Version info exposed) | **REMEDIATED** (Sanitized server headers) |
| **VULN-006** | Unauthenticated Route Exposure | **8.2** | **HIGH** | Exploitable (Unprotected endpoints) | **REMEDIATED** (Session auth middleware) |
| **VULN-007** | Insecure Direct Object Reference (IDOR) | **7.5** | **HIGH** | Exploitable (Arbitrary profile access) | **REMEDIATED** (Object ownership checks) |
| **VULN-008** | Legacy Cryptographic Hash Usage | **5.9** | **MEDIUM** | Identified (Unsalted SHA-256 in mock) | **REMEDIATED** (Upgraded hashing standard) |

---

## 🔒 8. Security & Legal Disclaimer

> [!CAUTION]
> This platform is developed exclusively for authorized academic, educational, and research purposes within isolated sandbox environments. Do not direct tests or tooling towards systems without explicit prior written authorization.

---

## 📄 9. License

Distributed under the MIT Academic License. See [LICENSE](LICENSE) for more details.
