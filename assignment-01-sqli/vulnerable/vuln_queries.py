#!/usr/bin/env python3
"""
Vulnerable SQL Query Implementation Module.
Demonstrates insecure string concatenation and direct parameter interpolation into raw SQL.
Vulnerability Reference: CWE-89 (SQL Injection)
"""

import sqlite3
import os
import hashlib
from typing import List, Dict, Any, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lab", "security_lab.db")

def get_db_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# ==============================================================================
# 1. VULNERABLE AUTHENTICATION QUERY (Authentication Bypass Vector)
# ==============================================================================
def vulnerable_login(username_input: str, password_input: str) -> Dict[str, Any]:
    """
    INSECURE: Directly interpolates user input into SQL statement.
    Attack Vector: ' OR '1'='1' --
    Result: Alters query boolean logic to evaluate to TRUE, returning the first account (admin).
    """
    pw_hash = hashlib.sha256(password_input.encode("utf-8")).hexdigest()
    
    # RAW DANGEROUS SQL CONCATENATION:
    raw_query = f"SELECT * FROM users WHERE username = '{username_input}' AND password_hash = '{pw_hash}'"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(raw_query)
        user = cursor.fetchone()
        if user:
            return {
                "status": "success",
                "authenticated": True,
                "user": dict(user),
                "executed_query": raw_query,
                "error": None
            }
        return {
            "status": "failed",
            "authenticated": False,
            "user": None,
            "executed_query": raw_query,
            "error": "Invalid credentials"
        }
    except Exception as e:
        return {
            "status": "error",
            "authenticated": False,
            "user": None,
            "executed_query": raw_query,
            "error": str(e)
        }
    finally:
        conn.close()

# ==============================================================================
# 2. VULNERABLE PRODUCT SEARCH (UNION-Based Data Extraction Vector)
# ==============================================================================
def vulnerable_product_search(search_term: str) -> Dict[str, Any]:
    """
    INSECURE: Directly interpolates search term into SQL LIKE query.
    Attack Vector: ' UNION SELECT null, username, password_hash, role, bio, null, null FROM users --
    Result: Extracts confidential password hashes from the 'users' table into the public product list.
    """
    raw_query = f"SELECT id, name, category, price, stock, description, is_hidden FROM products WHERE name LIKE '%{search_term}%' AND is_hidden = 0"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(raw_query)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return {
            "status": "success",
            "results_count": len(results),
            "data": results,
            "executed_query": raw_query,
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "results_count": 0,
            "data": [],
            "executed_query": raw_query,
            "error": str(e)
        }
    finally:
        conn.close()

# ==============================================================================
# 3. VULNERABLE USER PROFILE LOOKUP (Error / Numeric SQLi Vector)
# ==============================================================================
def vulnerable_user_profile(user_id_input: str) -> Dict[str, Any]:
    """
    INSECURE: Directly places input in numeric clause without integer cast or parameterization.
    Attack Vector: 1 OR 1=1
    Result: Returns all user profiles or triggers SQL syntax errors revealing database structure.
    """
    raw_query = f"SELECT id, username, email, role, bio, created_at FROM users WHERE id = {user_id_input}"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(raw_query)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return {
            "status": "success",
            "results_count": len(results),
            "data": results,
            "executed_query": raw_query,
            "error": None
        }
    except Exception as e:
        return {
            "status": "error",
            "results_count": 0,
            "data": [],
            "executed_query": raw_query,
            "error": str(e)
        }
    finally:
        conn.close()
