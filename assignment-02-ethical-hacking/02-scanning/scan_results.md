# Port & Service Scanning Results

**Phase:** 02 — Scanning & Discovery  
**Scan Engine:** Python Multi-Threaded TCP Port Scanner / Nmap 7.94  
**Target:** `127.0.0.1`  

---

## 1. Discovered Open Ports Matrix

| Port | Protocol | State | Service | Service Version / Banner | Risk Level |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **5000** | TCP | OPEN | `http` | Werkzeug/3.0.1 Python/3.10.x | **Informational** (Dashboard Management) |
| **5001** | TCP | OPEN | `http` | Custom REST API / Insecure Daemon | **HIGH** (Vulnerable Endpoints Exposed) |
| **8080** | TCP | OPEN/FILTERED | `http-alt` | Apache/2.4.x PHP/8.x (DVWA Target) | **CRITICAL** (Intentionally Vulnerable Lab) |

---

## 2. Technical Interpretation
1. **Port 5000**: Hosts the centralized administrative dashboard. Requires session security and strict origin controls.
2. **Port 5001**: Hosts unauthenticated endpoints handling dynamic SQL queries. Primary target for Phase 3 and Phase 4 deep-dive analysis.
3. **Port 8080**: Active when running the containerized DVWA lab environment.
