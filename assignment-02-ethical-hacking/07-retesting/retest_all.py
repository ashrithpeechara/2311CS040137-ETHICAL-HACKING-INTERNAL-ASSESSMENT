#!/usr/bin/env python3
"""
Automated Retesting & Regression Verification Suite.
Re-executes all exploit payloads against both vulnerable and remediated endpoints
to generate an empirical Before/After Security Retest Matrix.
"""

import json
import os
import sys

# Ensure module directories are in path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ETHICAL_HACKING_DIR = os.path.dirname(SCRIPT_DIR)
PROJECT_ROOT = os.path.dirname(ETHICAL_HACKING_DIR)
SQLI_DIR = os.path.join(PROJECT_ROOT, "assignment-01-sqli")

if SQLI_DIR not in sys.path:
    sys.path.insert(0, SQLI_DIR)

from vulnerable.vuln_queries import (
    vulnerable_login,
    vulnerable_product_search,
    vulnerable_user_profile
)
from secure.secure_queries import (
    secure_login,
    secure_product_search,
    secure_user_profile
)
from lab.setup_db import initialize_database

def run_retest_suite() -> dict:
    print("=" * 80)
    print("      AUTOMATED ETHICAL HACKING RETEST & VERIFICATION MATRIX")
    print("=" * 80)
    
    initialize_database()
    
    results = []

    # 1. Retest VULN-001 (Auth Bypass)
    payload_auth = "admin' OR '1'='1' --"
    vuln_auth = vulnerable_login(payload_auth, "password123")
    sec_auth = secure_login(payload_auth, "password123")
    
    results.append({
        "finding_id": "VULN-001",
        "title": "SQL Injection in Authentication",
        "payload": payload_auth,
        "before_status": "EXPLOITABLE (Gained admin session)" if vuln_auth.get("authenticated") else "FAILED",
        "after_status": "REMEDIATED (Blocked)" if not sec_auth.get("authenticated") else "STILL EXPLOITABLE",
        "verification": "PASS" if (vuln_auth.get("authenticated") and not sec_auth.get("authenticated")) else "FAIL"
    })

    # 2. Retest VULN-002 (UNION-Based Data Theft)
    payload_union = "' UNION SELECT 99, account_number, account_type, balance, 1, ssn_last4, 0 FROM accounts --"
    vuln_search = vulnerable_product_search(payload_union)
    sec_search = secure_product_search(payload_union)
    
    vuln_leaked = any("ACC-" in str(x.get("name")) for x in vuln_search.get("data", []))
    sec_leaked = any("ACC-" in str(x.get("name")) for x in sec_search.get("data", []))

    results.append({
        "finding_id": "VULN-002",
        "title": "UNION Data Extraction in Search",
        "payload": payload_union[:35] + "...",
        "before_status": f"EXPLOITABLE ({vuln_search.get('results_count')} rows leaked)" if vuln_leaked else "FAILED",
        "after_status": f"REMEDIATED (0 rows leaked)" if not sec_leaked else "STILL EXPLOITABLE",
        "verification": "PASS" if (vuln_leaked and not sec_leaked) else "FAIL"
    })

    # 3. Retest VULN-003 / VULN-007 (Numeric / IDOR Injection)
    payload_num = "1 OR 1=1"
    vuln_num = vulnerable_user_profile(payload_num)
    sec_num = secure_user_profile(payload_num)

    vuln_num_success = vuln_num.get("results_count", 0) > 1
    sec_num_success = sec_num.get("status") == "validation_error"

    results.append({
        "finding_id": "VULN-003",
        "title": "Numeric SQLi & IDOR Data Dumping",
        "payload": payload_num,
        "before_status": f"EXPLOITABLE (Dumped all users)" if vuln_num_success else "FAILED",
        "after_status": "REMEDIATED (Type validation blocked)" if sec_num_success else "STILL EXPLOITABLE",
        "verification": "PASS" if (vuln_num_success and sec_num_success) else "FAIL"
    })

    # Display clean table
    print(f"\n{'ID':<10} {'VULNERABILITY TITLE':<35} {'BEFORE REMEDIATION':<25} {'AFTER REMEDIATION':<25} {'STATUS'}")
    print("-" * 105)
    for r in results:
        print(f"{r['finding_id']:<10} {r['title']:<35} {r['before_status']:<25} {r['after_status']:<25} [{r['verification']}]")
    print("-" * 105)

    return {
        "timestamp": "2026-09-22T14:30:00Z",
        "total_retested": len(results),
        "total_passed": sum(1 for r in results if r["verification"] == "PASS"),
        "retest_matrix": results
    }

if __name__ == "__main__":
    retest_data = run_retest_suite()
    out_path = os.path.join(SCRIPT_DIR, "retest_results.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(retest_data, f, indent=2)
    print(f"\n[+] Retest matrix serialized to: {out_path}")
