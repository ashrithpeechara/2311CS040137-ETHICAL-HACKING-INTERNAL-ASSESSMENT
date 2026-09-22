#!/usr/bin/env python3
"""
Master Assessment Test Runner & Validation Harness.
Executes the full test lifecycle across both Assignment 1 and Assignment 2:
1. Database Seeding & Setup
2. Assignment 1 Vulnerability Confirmation Suite
3. Assignment 1 Remediation Verification Suite
4. Assignment 2 Automated Retesting Matrix
5. Evidence Discovery & SHA-256 Cryptographic Hasher
6. Technical & Executive Report Compilation (Markdown & HTML)
7. Academic Multi-Page PDF Deliverables Generation
"""

import subprocess
import os
import sys
import time

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def run_step(step_name: str, script_rel_path: str) -> bool:
    print("\n" + "=" * 80)
    print(f"[*] STEP: {step_name}")
    print("=" * 80)
    script_full_path = os.path.join(PROJECT_ROOT, script_rel_path)
    
    start_time = time.time()
    result = subprocess.run([sys.executable, script_full_path], cwd=PROJECT_ROOT)
    duration = time.time() - start_time
    
    if result.returncode == 0:
        print(f"[+] COMPLETED: {step_name} in {duration:.2f}s (Return Code: 0)")
        return True
    else:
        print(f"[-] FAILED: {step_name} (Return Code: {result.returncode})")
        return False

def main():
    print("""
    ============================================================================
      WEB APPLICATION SECURITY & ETHICAL HACKING ASSESSMENT PLATFORM
      Unified Assessment Test Suite (2311CS040137-EH)
    ============================================================================
    """)

    steps = [
        ("Database Setup & Lab Seeding", "assignment-01-sqli/lab/setup_db.py"),
        ("Assignment 1 - Vulnerable SQLi Exploit Harness", "assignment-01-sqli/tests/test_sqli_vulnerable.py"),
        ("Assignment 1 - Secure Remediation Verification", "assignment-01-sqli/tests/test_sqli_secure.py"),
        ("Assignment 2 - Automated Retest & Regression Suite", "assignment-02-ethical-hacking/07-retesting/retest_all.py"),
        ("Platform - Standardized Evidence Indexer & SHA-256 Hasher", "scripts/evidence_manager.py"),
        ("Platform - Comprehensive Report Generator (Markdown/HTML)", "scripts/generate_final_report.py"),
        ("Platform - Professional PDF Reports Generator", "scripts/generate_pdf_reports.py")
    ]

    all_passed = True
    for name, script in steps:
        success = run_step(name, script)
        if not success:
            all_passed = False
            break

    print("\n" + "=" * 80)
    if all_passed:
        print(" [SUCCESS] ALL 7 ASSESSMENT MILESTONES PASSED 100% SUCCESSFULLY!")
        print(" Platform and both PDF reports are fully verified and ready for demonstration.")
    else:
        print(" [FAILURE] One or more assessment steps failed. Review logs above.")
    print("=" * 80 + "\n")

    sys.exit(0 if all_passed else 1)

if __name__ == "__main__":
    main()
