# Assignment 2: Integrated Ethical Hacking Assessment

**Module Code:** `ASSIGNMENT-02-ETHICAL-HACKING`  
**Assessment Target:** Isolated Lab Network & Application Perimeter (`127.0.0.1`)  
**Methodology:** PTES, NIST SP 800-115, OWASP WSTG v4.2  

---

## 1. Assessment Lifecycle Overview

This module conducts an end-to-end, multi-stage penetration test demonstrating the structured progression of an ethical hacking engagement:

```text
+-----------------------------------------------------------------------------------+
|                            ETHICAL HACKING WORKFLOW                               |
+-----------------------------------------------------------------------------------+
  [Phase 1] Reconnaissance      --> Footprinting, DNS, WHOIS, tech stack profiling
  [Phase 2] Scanning            --> Host discovery, TCP/UDP port mapping (Nmap)
  [Phase 3] Enumeration         --> Service banner grabbing, web directory fuzzing
  [Phase 4] Vuln Analysis       --> CVE/CWE identification, CVSS v3.1 scoring, triage
  [Phase 5] Exploitation        --> Controlled, non-destructive Proof-of-Concepts
  [Phase 6] Remediation         --> Security header injection, code fixes, hardening
  [Phase 7] Retesting           --> Automated re-verification of all discovered flaws
+-----------------------------------------------------------------------------------+
```

---

## 2. Directory Structure

```text
assignment-02-ethical-hacking/
├── README.md                       # This assessment manual
├── 01-reconnaissance/              # Target footprinting & OSINT automation
├── 02-scanning/                    # Port & service discovery tooling
├── 03-enumeration/                 # Web directory & banner enumeration
├── 04-vulnerability-analysis/     # Findings database & false positive analysis
├── 05-exploitation/                # Safe proof-of-concept exploit scripts
├── 06-remediation/                 # Defensive configuration patches & code fixes
├── 07-retesting/                   # Automated retest & regression verification
├── evidence/                       # Standardized evidence repository
└── report/                         # Full technical penetration test report
```

---

## 3. Tool Justification & Strategy

| Tool | Purpose | Output & Value |
| :--- | :--- | :--- |
| **Nmap** | Port scanning & Service Fingerprinting | Uncovers exposed daemon ports and service version strings |
| **WhatWeb / Custom Profiler** | Technology stack identification | Reveals server software, frameworks, and header disclosures |
| **Gobuster / Python Web Fuzzer** | Content & endpoint discovery | Discovers unlinked admin portals, backups, and secret routes |
| **Custom Security Auditor** | Misconfiguration detection | Identifies missing security headers (`HSTS`, `CSP`, `X-Frame-Options`) |
| **Python Exploit PoCs** | Controlled exploitation | Demonstrates risk impact without causing availability loss |
