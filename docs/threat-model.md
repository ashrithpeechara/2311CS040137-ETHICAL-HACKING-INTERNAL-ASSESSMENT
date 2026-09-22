# Threat Modeling & Risk Assessment

**Target System**: Web Application Security & Assessment Perimeter  
**Methodology**: STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) + DREAD Risk Scoring  

---

## 1. STRIDE Threat Analysis Matrix

| Threat Category | Target Component | Threat Scenario | Mitigation Strategy | Severity |
| :--- | :--- | :--- | :--- | :--- |
| **Spoofing** | Authentication Endpoint (`/login`) | Attacker bypasses password check via `' OR 1=1 --` | Parameterized SQL queries & Argon2/Bcrypt hash validation | **CRITICAL** |
| **Tampering** | User Account & Role State | Attacker manipulates SQL payload to alter balance or role | Least-privilege DB users & prepared UPDATE queries | **HIGH** |
| **Repudiation** | Audit & Security Logs | Lack of centralized tamper-evident audit logging | Immutable append-only audit trail with SHA-256 hash chains | **MEDIUM** |
| **Information Disclosure** | Search & Profile Endpoints | Attacker extracts full database schema and hashes via `UNION SELECT` | Strict parameterized statements & generic error masking | **HIGH** |
| **Denial of Service** | Database Query Processor | Heavy recursive or sleep SQL injection (`WAITFOR DELAY` / CPU exhaustion) | Query timeouts, rate limiting, and input length constraints | **MEDIUM** |
| **Elevation of Privilege** | Administrative Controls | Non-privileged user forces admin session via SQL injection | Role-Based Access Control (RBAC) validated against session token | **CRITICAL** |

---

## 2. DREAD Risk Scoring Calculation

$$\text{Risk Rating} = \frac{\text{Damage} + \text{Reproducibility} + \text{Exploitability} + \text{Affected Users} + \text{Discoverability}}{5}$$

- **SQL Injection (Unauthenticated)**: $(10 + 10 + 10 + 10 + 9) / 5 = \mathbf{9.8 \text{ (CRITICAL)}}$
- **Missing Security Headers**: $(3 + 10 + 4 + 10 + 10) / 5 = \mathbf{7.4 \text{ (HIGH)}}$
- **Directory / Sensitive Exposure**: $(6 + 10 + 8 + 6 + 9) / 5 = \mathbf{7.8 \text{ (HIGH)}}$
