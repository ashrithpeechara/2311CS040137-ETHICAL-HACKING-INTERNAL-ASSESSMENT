# Assignment 1: SQL Injection Detection and Prevention

**Module Code:** `ASSIGNMENT-01-SQLI`  
**Target Vulnerability:** CWE-89 (Improper Neutralization of Special Elements used in an SQL Command)  
**Standard Reference:** OWASP Top 10:2021 — A03: Injection  

---

## 1. Module Overview
SQL Injection (SQLi) occurs when untrusted user input is directly concatenated or interpolated into database queries, allowing attackers to manipulate query structure, bypass authentication, extract unauthorized data, or alter database contents.

This module provides a complete, controlled laboratory environment demonstrating:
1. **The Vulnerable Architecture**: Direct string interpolation and unsanitized dynamic SQL.
2. **Attack Vectors & Exploitation**:
   - Authentication Bypass (`' OR 1=1 --`)
   - UNION-Based Data Extraction (Dumping schema, credential hashes, and private tables)
   - Error-Based and Boolean Blind Information Disclosure
3. **The Secure Architecture**:
   - Parameterized Queries (Prepared Statements)
   - Strict Input Validation and Type Safety
   - Principle of Least Privilege & Error Masking
4. **Automated Verification**:
   - Regression test suites confirming exploitability on vulnerable endpoints and complete mitigation on secure endpoints.

---

## 2. Directory Structure

```text
assignment-01-sqli/
├── README.md                   # This specification and guide
├── lab/
│   ├── schema.sql              # Database schema definition
│   └── setup_db.py             # SQLite database initializer and seeder
├── vulnerable/
│   ├── vuln_queries.py         # Vulnerable raw query functions
│   └── vuln_app.py             # Vulnerable Flask service routes
├── secure/
│   ├── secure_queries.py       # Hardened parameterized query engine
│   └── secure_app.py           # Secure Flask service routes
├── tests/
│   ├── payloads.json           # Categorized attack vector dictionary
│   ├── test_sqli_vulnerable.py # Exploit validation test suite
│   └── test_sqli_secure.py     # Remediation verification test suite
├── evidence/
│   ├── EV-SQLI-001_auth_bypass.md
│   ├── EV-SQLI-002_union_extract.md
│   └── EV-SQLI-003_blind_boolean.md
└── report/
    └── sqli-technical-report.md# Formal academic technical assessment
```

---

## 3. Quick Run & Verification Commands

1. **Initialize the Lab Database:**
   ```bash
   python assignment-01-sqli/lab/setup_db.py
   ```

2. **Run the Vulnerability Proof Suite:**
   ```bash
   python -m unittest assignment-01-sqli/tests/test_sqli_vulnerable.py
   ```
   *Expected Result: Confirms all SQLi payloads successfully exploit the vulnerable query engine.*

3. **Run the Remediation Verification Suite:**
   ```bash
   python -m unittest assignment-01-sqli/tests/test_sqli_secure.py
   ```
   *Expected Result: Confirms 100% of attack payloads are neutralized by prepared statements and input validation.*
