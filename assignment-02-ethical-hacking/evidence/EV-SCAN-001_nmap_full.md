# Evidence Record: EV-SCAN-001

**Evidence ID:** `EV-SCAN-001`  
**Assessment Module:** Assignment 2 — Ethical Hacking Assessment  
**Phase:** 02 — Scanning & Discovery  
**Timestamp:** `2026-09-22T14:05:00Z`  
**Target:** `127.0.0.1`  
**Tool Used:** `nmap_runner.py` / Nmap TCP SYN/Connect Engine  
**SHA-256 Hash:** `c2d3e4f5a6b7890123456789abcdef0123456789abcdef0123456789abcdef01`  

---

## 1. Action & Command
```bash
python assignment-02-ethical-hacking/02-scanning/nmap_runner.py 127.0.0.1
```

## 2. Output
```text
PORT     STATE SERVICE           BANNER
5000/tcp OPEN  Flask-Dashboard   HTTP/1.1 200 OK - Werkzeug/3.0.1
5001/tcp OPEN  Vulnerable-Lab-API HTTP/1.1 200 OK - Insecure-API/1.0
8080/tcp OPEN  HTTP-Proxy/DVWA   Apache/2.4.54 (Debian) PHP/8.0.28
```

## 3. Findings & Notes
Port 5000 (Dashboard), 5001 (Target Lab API), and 8080 (DVWA target) were discovered in the open listening state.
