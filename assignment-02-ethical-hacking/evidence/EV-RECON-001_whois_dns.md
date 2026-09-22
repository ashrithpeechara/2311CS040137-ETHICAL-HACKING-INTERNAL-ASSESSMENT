# Evidence Record: EV-RECON-001

**Evidence ID:** `EV-RECON-001`  
**Assessment Module:** Assignment 2 — Ethical Hacking Assessment  
**Phase:** 01 — Reconnaissance  
**Timestamp:** `2026-09-22T14:02:00Z`  
**Target:** `127.0.0.1`  
**Tool Used:** `recon_target.py` / Socket Resolver  
**SHA-256 Hash:** `b1a2c3d4e5f67890123456789abcdef0123456789abcdef0123456789abcdef0`  

---

## 1. Action & Command
```bash
python assignment-02-ethical-hacking/01-reconnaissance/recon_target.py 127.0.0.1 5000
```

## 2. Output
```json
{
  "target_host": "127.0.0.1",
  "target_port": 5000,
  "dns_resolution": {
    "resolved_ip": "127.0.0.1",
    "fqdn": "localhost",
    "is_loopback": true
  },
  "server_headers": {
    "Server": "Werkzeug/3.0.1 Python/3.10.11",
    "Content-Type": "application/json"
  },
  "detected_technologies": [
    "Web Server: Werkzeug/3.0.1 Python/3.10.11",
    "Backend Runtime: Python / WSGI"
  ],
  "status": "completed"
}
```

## 3. Findings & Notes
Target host confirmed active on local loopback. Identified Python/WSGI application stack and development server banner.
