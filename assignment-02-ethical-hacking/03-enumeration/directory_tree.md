# Enumerated Web Directory & Route Tree

**Phase:** 03 — Enumeration  
**Tool:** Python Custom Web Fuzzer / Directory Spider  

---

## 1. Discovered Route Map

```text
http://127.0.0.1:5000/ (Dashboard & Assessment Core)
│
├── /                           [HTTP 200]  Main Overview Dashboard
├── /sqli                       [HTTP 200]  Interactive SQLi Playground & Query Comparator
├── /ethical-hacking            [HTTP 200]  Ethical Hacking Findings Matrix & Execution Hub
├── /evidence                   [HTTP 200]  Evidence Vault & Artifact Explorer
├── /reports                    [HTTP 200]  Generated Audit Deliverables
│
├── /api/
│   ├── /api/assessment-summary [HTTP 200]  Consolidated Telemetry & Retest Statuses
│   │
│   ├── /api/vulnerable/        [Vulnerable Attack Surface]
│   │   ├── /login              [HTTP 405/401] Insecure Authentication Endpoint (SQLi Target)
│   │   ├── /search             [HTTP 200]     Insecure Product Query Endpoint (UNION SQLi)
│   │   └── /user/<id>          [HTTP 200]     Insecure User Record Lookup (Numeric SQLi)
│   │
│   └── /api/secure/            [Remediated Attack Surface]
│       ├── /login              [HTTP 405/401] Hardened Login with Prepared Statements
│       ├── /search             [HTTP 200]     Hardened Search with Parameter Binding
│       └── /user/<id>          [HTTP 200]     Type-Validated & Parameterized User Lookup
│
└── /static/
    ├── /css/style.css          [HTTP 200]  Modern Dark-Cyber Glassmorphism Styling
    └── /js/dashboard.js        [HTTP 200]  Asynchronous Assessment UI Controller
```
