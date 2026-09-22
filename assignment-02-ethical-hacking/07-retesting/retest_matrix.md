# Vulnerability Retest & Remediation Verification Matrix

**Phase:** 07 — Retesting & Regression Testing  
**Evaluation Date:** 2026-09-22  
**Assessor Identifier:** `2311CS040082-EH`  

---

## 1. Consolidated Retest Matrix

| Finding ID | Vulnerability Title | Severity | Pre-Patch Status | Post-Patch Status | Retest Result | Evidence Link |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VULN-001** | SQL Injection in Authentication | **CRITICAL (9.8)** | Exploitable (Admin session gained via `' OR '1'='1' --`) | Remediated (Regex filter & parameterized query) | **VERIFIED CLOSED** | `EV-RETEST-001` |
| **VULN-002** | UNION-Based Data Extraction in Search | **HIGH (8.6)** | Exploitable (Extracted accounts & password hashes) | Remediated (Prepared statement with parameter binding) | **VERIFIED CLOSED** | `EV-RETEST-002` |
| **VULN-003** | Numeric SQLi & Parameter Injection | **HIGH (7.5)** | Exploitable (Dumped all users via `1 OR 1=1`) | Remediated (Strict integer coercion & query binding) | **VERIFIED CLOSED** | `EV-RETEST-003` |
| **VULN-004** | Missing HTTP Security Headers | **MEDIUM (6.5)** | Exploitable (Missing HSTS, CSP, X-Frame-Options) | Remediated (Injected via response middleware) | **VERIFIED CLOSED** | `EV-RETEST-004` |
| **VULN-005** | Verbose Server Banner Disclosures | **MEDIUM (5.3)** | Exploitable (Exposing Werkzeug/Python version) | Remediated (Server header masked to generic name) | **VERIFIED CLOSED** | `EV-RETEST-005` |
| **VULN-006** | Unauthenticated Route Exposure | **HIGH (8.2)** | Exploitable (Accessible without auth token) | Remediated (Enforced session validation middleware) | **VERIFIED CLOSED** | `EV-RETEST-006` |
| **VULN-007** | Insecure Direct Object Reference (IDOR) | **HIGH (7.5)** | Exploitable (Arbitrary profile enumeration) | Remediated (Object authorization checks applied) | **VERIFIED CLOSED** | `EV-RETEST-007` |
| **VULN-008** | Weak Cryptographic Hash Storage | **MEDIUM (5.9)** | Identified (Unsalted SHA-256 in prototype schema) | Remediated (Upgraded hashing standard & salt architecture) | **VERIFIED CLOSED** | `EV-RETEST-008` |

---

## 2. Conclusion
All identified vulnerabilities have been successfully remediated and verified through automated test suites. The security posture has progressed from high risk to hardened baseline.
