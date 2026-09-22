# Defense-in-Depth Architecture & Layered Security

**Phase:** 06 — Remediation  
**Framework:** Defense-in-Depth Strategy  

---

## 1. Architectural Defense Layers

```text
       +-------------------------------------------------------------+
Layer 1| Edge / Network: IP Allowlisting, Rate Limiting, TLS 1.3     |
       +-------------------------------------------------------------+
                                      |
       +-------------------------------------------------------------+
Layer 2| Web Application Firewall (WAF): Payload Inspection / Signatures
       +-------------------------------------------------------------+
                                      |
       +-------------------------------------------------------------+
Layer 3| App Framework: Security Headers, Session Verification, RBAC |
       +-------------------------------------------------------------+
                                      |
       +-------------------------------------------------------------+
Layer 4| Code Logic: Strict Regex Input Validation & Prepared Stmts  |
       +-------------------------------------------------------------+
                                      |
       +-------------------------------------------------------------+
Layer 5| Database Engine: Least Privilege Roles, Encryption, Auditing|
       +-------------------------------------------------------------+
```

---

## 2. Core Hardening Principles Applied
1. **Parameterized Queries as Primary Defense**: Ensures application inputs cannot break out of data context into SQL command context.
2. **Input Validation as Secondary Defense**: Filters malformed or unexpected data at the boundary.
3. **HTTP Response Hardening**: Enforces strict browser-side sandbox policies (CSP, X-Frame-Options).
4. **Least Privilege & Role-Based Access Control**: Prevents horizontal and vertical privilege escalation.
