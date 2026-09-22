# Security Hardening Directives & Configuration Patches

**Phase:** 06 — Remediation  
**Target:** Web Application Server & Environment  

---

## 1. Web Application Server Configuration Patches

### A. HTTP Security Header Injection (Flask / WSGI)
```python
@app.after_request
def apply_security_headers(response):
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    response.headers['Server'] = 'Protected-Gateway'
    return response
```

### B. Database Connection Hardening (SQLite / MySQL)
- **Least Privilege Principle**: Create dedicated read-only database roles for public catalog queries.
- **Connection Timeout**: Enforce a 5000ms query timeout to prevent resource exhaustion via complex subqueries.
- **Prepared Statements**: Disable multi-statement query execution in production database connection strings.
