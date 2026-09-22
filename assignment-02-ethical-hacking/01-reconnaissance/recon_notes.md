# Reconnaissance & Target Footprinting Documentation

**Phase:** 01 — Reconnaissance  
**Target Perimeter:** Localized Sandboxed Lab (`127.0.0.1`)  
**Scope Status:** Fully Authorized  

---

## 1. Network & Host Identification
- **Target Hostname:** `localhost` / `sec-lab.internal`
- **Assigned IP:** `127.0.0.1` (IPv4 Loopback)
- **Subnet Allocation:** `127.0.0.0/8`
- **Operating Environment:** Windows / Python Runtime

---

## 2. Technology Stack Profile
From passive metadata and active header fingerprinting:
- **Web Application Server:** Werkzeug / Python WSGI Stack
- **Database Backend:** SQLite3 (Sandboxed SQL engine)
- **Containerization:** Docker Bridge `172.18.0.0/16` (Optional DVWA instance on port `8080`)
- **Exposed Attack Surfaces:**
  - Administrative Login Portal (`/api/vulnerable/login` & `/dashboard`)
  - Product Catalog & Search Engine (`/api/vulnerable/search`)
  - User Directory Management API (`/api/vulnerable/user/<id>`)
  - Static Resource Repository (`/static`)

---

## 3. Threat Surface Summary
The target hosts multiple interdependent web applications with varying security controls, making it an optimal candidate for structured port scanning and web directory fuzzing.
