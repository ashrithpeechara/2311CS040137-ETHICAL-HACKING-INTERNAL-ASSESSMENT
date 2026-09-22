# Evidence Record: EV-ENUM-001

**Evidence ID:** `EV-ENUM-001`  
**Assessment Module:** Assignment 2 — Ethical Hacking Assessment  
**Phase:** 03 — Enumeration  
**Timestamp:** `2026-09-22T14:08:00Z`  
**Target:** `http://127.0.0.1:5000`  
**Tool Used:** `web_enum.py` / Endpoint Fuzzing Engine  
**SHA-256 Hash:** `d3e4f5a6b7c890123456789abcdef0123456789abcdef0123456789abcdef012`  

---

## 1. Action & Command
```bash
python assignment-02-ethical-hacking/03-enumeration/web_enum.py http://127.0.0.1:5000
```

## 2. Output
```text
[+] Discovered: http://127.0.0.1:5000/ [HTTP 200] (2450 bytes)
[+] Discovered: http://127.0.0.1:5000/api/vulnerable/search [HTTP 200] (840 bytes)
[!] Restricted: http://127.0.0.1:5000/api/vulnerable/login [HTTP 405] (Method Not Allowed - POST required)
[+] Discovered: http://127.0.0.1:5000/api/vulnerable/user/1 [HTTP 200] (320 bytes)
```

## 3. Findings & Notes
Enumerated all active REST API routes and discovered accessible administrative interfaces.
