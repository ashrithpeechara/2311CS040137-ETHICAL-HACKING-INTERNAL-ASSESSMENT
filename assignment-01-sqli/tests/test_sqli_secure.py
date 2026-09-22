#!/usr/bin/env python3
"""
Automated Remediation Verification Test Suite (Secure Hardened Target).
Verifies that all SQL injection attack vectors are completely mitigated by prepared
statements, parameter binding, and strict input validation.
"""

import unittest
import os
import sys

# Ensure module directories are in path
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(TEST_DIR)
PROJECT_ROOT = os.path.dirname(MODULE_DIR)

if MODULE_DIR not in sys.path:
    sys.path.insert(0, MODULE_DIR)

from secure.secure_queries import (
    secure_login,
    secure_product_search,
    secure_user_profile
)
from lab.setup_db import initialize_database

class TestSecureSQLiRemediation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Reset and seed the database prior to tests."""
        initialize_database()

    def test_01_secure_login_valid_credentials(self):
        """Verify legitimate user authentication functions normally."""
        res = secure_login("admin", "AdminSecure2026!")
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["authenticated"])
        self.assertEqual(res["user"]["username"], "admin")
        print("\n[+] Legitimate Access Verified: Valid credentials authenticated successfully.")

    def test_02_secure_auth_bypass_attempt_tautology(self):
        """Verify auth bypass payload is rejected/sanitized."""
        payload = "admin' OR '1'='1' --"
        res = secure_login(payload, "dummy_password")
        # Should be blocked by input filter or fail parameter binding
        self.assertFalse(res.get("authenticated", False))
        self.assertIn(res.get("status"), ["validation_error", "failed"])
        print(f"[+] Remediation Verified: Auth bypass attempt blocked: {payload}")

    def test_03_secure_auth_bypass_attempt_comment(self):
        """Verify comment truncation payload is rejected."""
        payload = "admin' --"
        res = secure_login(payload, "invalid_pw")
        self.assertFalse(res.get("authenticated", False))
        print(f"[+] Remediation Verified: Comment truncation blocked: {payload}")

    def test_04_secure_union_extraction_neutralized(self):
        """Verify UNION query is treated strictly as literal string in search."""
        payload = "' UNION SELECT 99, username || ':' || password_hash, role, 0.00, 1, email, 0 FROM users --"
        res = secure_product_search(payload)
        self.assertEqual(res["status"], "success")
        # The query will treat payload literally as a search string, returning 0 product matches
        self.assertEqual(res["results_count"], 0)
        print(f"[+] Remediation Verified: UNION payload treated as literal string; 0 data leaked.")

    def test_05_secure_numeric_sqli_blocked(self):
        """Verify numeric SQLi attempt is caught by type validation."""
        payload = "1 OR 1=1"
        res = secure_user_profile(payload)
        self.assertEqual(res["status"], "validation_error")
        self.assertEqual(res["results_count"], 0)
        print(f"[+] Remediation Verified: Numeric injection blocked by type checking: {payload}")

    def test_06_secure_error_masking(self):
        """Verify SQL syntax tampering does not reveal raw database exceptions."""
        payload = "1' INVALID SYNTAX --"
        res = secure_user_profile(payload)
        self.assertEqual(res["status"], "validation_error")
        self.assertNotIn("sqlite3.OperationalError", res.get("error", ""))
        print(f"[+] Remediation Verified: Database errors masked; safe error returned.")

if __name__ == "__main__":
    unittest.main()
