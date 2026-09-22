# System Architecture & Technical Design

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

## 1. Core Subsystems

### Subsystem A: SQLi Engine (Module 1)
- **Vulnerable Component (`assignment-01-sqli/vulnerable/`)**: Implements raw string interpolation (`f"SELECT * FROM users WHERE user = '{username}'"`), explicitly exposing endpoints to classic and second-order SQL injection vectors.
- **Secure Component (`assignment-01-sqli/secure/`)**: Re-engineers identical business logic using prepared statements (`cursor.execute("SELECT * FROM users WHERE user = ?", (username,))`) combined with strict regex validation and type coercions.
- **Automated Verification Harness (`assignment-01-sqli/tests/`)**: Programmatically launches 10+ attack payloads against both targets to mathematically verify 100% vulnerability on the vulnerable endpoint and 0% breach rate on the remediated endpoint.

### Subsystem B: Ethical Hacking Assessment Framework (Module 2)
- Structured execution modules from Reconnaissance to Retesting.
- Integrates with standard tools (Nmap, Netcat, Gobuster, Nikto) while providing standalone Python fallback engines for self-contained, offline evaluation.

### Subsystem C: Evidence & Finding Management Engine
- Cryptographic hash generation (`SHA-256`) for every evidence artifact (terminal logs, query outputs, HTTP dumps).
- Standardized finding registry (`reports/vulnerability_registry.json`) mapping findings to CVSS v3.1, CWE, remediation status, and retest evidence.

### Subsystem D: Reporting & Presentation Layer
- Dynamic Jinja2 report compiler generating both GitHub-friendly Markdown documents and professional PDF/HTML deliverables.
- Interactive Web Dashboard for live evaluation, query comparison, and faculty demonstration.
