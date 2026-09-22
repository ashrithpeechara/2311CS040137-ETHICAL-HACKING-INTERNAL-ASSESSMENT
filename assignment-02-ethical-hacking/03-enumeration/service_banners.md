# Service Banners & Protocol Fingerprints

**Phase:** 03 — Enumeration  
**Target:** Localized Lab Infrastructure  

---

## 1. Captured Service Banners

### A. Web Server Banner (Port 5000 / 5001)
```http
HTTP/1.1 200 OK
Server: Werkzeug/3.0.1 Python/3.10.11
Date: Tue, 22 Sep 2026 14:00:00 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 142
```
- **Interpretation**: Werkzeug development server in use. Development servers typically lack production concurrency controls and defensive HTTP header injection by default.

### B. Database Subsystem Banner
```sql
SQLite version 3.40.1
Interface: Python sqlite3 Driver (PEP 249 compliant)
```
- **Interpretation**: SQLite allows multiple query syntax structures (tautology, error disclosure) and does not support stacked queries (`DROP TABLE`) by default in standard Python sqlite3 executions without script mode.
