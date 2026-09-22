#!/usr/bin/env python3
"""
Database Setup & Seeding Script for SQL Injection Assessment Lab.
Creates tables and seeds initial realistic mock records.
"""

import sqlite3
import os
import hashlib

DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, "security_lab.db")
SCHEMA_PATH = os.path.join(DB_DIR, "schema.sql")

def hash_pw(plaintext: str) -> str:
    """Helper to generate SHA-256 password hash for demonstration."""
    return hashlib.sha256(plaintext.encode("utf-8")).hexdigest()

def initialize_database(db_path: str = DB_PATH):
    """Initializes the database schema and populates seed records."""
    print(f"[*] Initializing Security Lab Database at: {db_path}")
    
    if os.path.exists(db_path):
        os.remove(db_path)
        print("[-] Removed existing legacy database instance.")

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Read and apply schema
    with open(SCHEMA_PATH, "r", encoding="utf-8") as schema_file:
        schema_sql = schema_file.read()
    cursor.executescript(schema_sql)
    print("[+] Applied schema definitions successfully.")

    # Seed Users
    users_data = [
        ("admin", hash_pw("AdminSecure2026!"), "admin@corp-sec.internal", "admin", "System Administrator with root privileges"),
        ("john_doe", hash_pw("Password123!"), "jdoe@corp-sec.internal", "analyst", "Senior Security Analyst"),
        ("jane_smith", hash_pw("Winter2026$"), "jsmith@corp-sec.internal", "developer", "Full Stack Web Developer"),
        ("bob_wilson", hash_pw("Welcome99#"), "bwilson@corp-sec.internal", "user", "Standard Staff Member")
    ]
    cursor.executemany(
        "INSERT INTO users (username, password_hash, email, role, bio) VALUES (?, ?, ?, ?, ?)",
        users_data
    )

    # Seed Accounts (Confidential Financial Data)
    accounts_data = [
        ("ACC-9001-ADMIN", 1, "Executive Reserve", 500000.00, "9821"),
        ("ACC-8002-JDOE", 2, "Payroll Account", 8450.75, "4412"),
        ("ACC-7003-JSMITH", 3, "Operational Checking", 6200.50, "1190"),
        ("ACC-6004-BWILSON", 4, "Standard Savings", 1450.00, "3388")
    ]
    cursor.executemany(
        "INSERT INTO accounts (account_number, user_id, account_type, balance, ssn_last4) VALUES (?, ?, ?, ?, ?)",
        accounts_data
    )

    # Seed Products Catalog (Target for search queries & UNION injection)
    products_data = [
        ("Enterprise Firewall Appliance", "Hardware", 2499.99, 15, "Next-Gen Layer 7 Network Inspection Firewall", 0),
        ("Endpoint Detection Agent License", "Software", 120.00, 500, "Per-seat EDR Endpoint Agent", 0),
        ("Hardware Security Module (HSM)", "Hardware", 8500.00, 4, "FIPS 140-2 Level 3 Cryptographic Key Storage", 0),
        ("Red Team Penetration Testing Toolkit", "Services", 4500.00, 10, "Comprehensive vulnerability assessment package", 0),
        ("CONFIDENTIAL: Prototype Zero-Day Exploit Framework", "Restricted", 99999.99, 1, "INTERNAL RESEARCH ONLY - DO NOT EXPOSE", 1)
    ]
    cursor.executemany(
        "INSERT INTO products (name, category, price, stock, description, is_hidden) VALUES (?, ?, ?, ?, ?, ?)",
        products_data
    )

    conn.commit()
    conn.close()
    print("[+] Database seeding complete! Total tables: users, accounts, products, system_audit_logs.\n")

if __name__ == "__main__":
    initialize_database()
