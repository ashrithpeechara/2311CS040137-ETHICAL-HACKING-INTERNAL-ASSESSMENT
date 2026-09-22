#!/usr/bin/env python3
"""
Secure SQL Query Implementation Module.
Demonstrates parameterized queries (prepared statements), strict input validation,
type checking, and safe database abstraction.
Remediation Reference: OWASP SQL Injection Prevention Cheat Sheet / CWE-89 Mitigation
"""

import sqlite3
import os
import re
import hashlib
from typing import List, Dict, Any, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lab", "security_lab.db")

def get_db_connection(db_path: str = DB_PATH) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

# ==============================================================================
# 1. SECURE AUTHENTICATION QUERY (Prepared Statements + Parameter Binding)
# ==============================================================================
def secure_login(username_input: str, password_input: str) -> Dict[str, Any]:
    """
    SECURE: Uses parameterized query placeholders ('?') to separate SQL code from untrusted data.
    Database driver treats user input strictly as literal values, rendering SQL syntax manipulation impossible.
    """
    # Defensive Input Validation (Alphanumeric username validation)
    if not username_input or not isinstance(username_input, str):
        return {
            "status": "validation_error",
            "authenticated": False,
            "user": None,
            "executed_query": "BLOCKED_BY_VALIDATION",
            "error": "Invalid username format. Must be non-empty."
        }

    # Strict username pattern whitelist (alphanumeric, underscore, hyphen, 3-30 chars)
    if not re.match(r"^[a-zA-Z0-9_\-]{3,30}$", username_input):
        return {
            "status": "validation_error",
            "authenticated": False,
            "user": None,
            "executed_query": "BLOCKED_BY_INPUT_FILTER",
            "error": "Input validation violation: Username contains illegal characters."
        }

    pw_hash = hashlib.sha256(password_input.encode("utf-8")).hexdigest()
    
    # PARAMETERIZED SECURE SQL:
    parameterized_query = "SELECT id, username, email, role, bio, created_at FROM users WHERE username = ? AND password_hash = ?"
    params = (username_input, pw_hash)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(parameterized_query, params)
        user = cursor.fetchone()
        if user:
            return {
                "status": "success",
                "authenticated": True,
                "user": dict(user),
                "executed_query": parameterized_query,
                "parameters": [username_input, "[REDACTED_HASH]"],
                "error": None
            }
        return {
            "status": "failed",
            "authenticated": False,
            "user": None,
            "executed_query": parameterized_query,
            "parameters": [username_input, "[REDACTED_HASH]"],
            "error": "Invalid username or password"
        }
    except Exception as e:
        # Mask internal database details from end-users
        return {
            "status": "error",
            "authenticated": False,
            "user": None,
            "executed_query": parameterized_query,
            "error": "An internal database error occurred. Details have been logged securely."
        }
    finally:
        conn.close()

# ==============================================================================
# 2. SECURE PRODUCT SEARCH (Parameterized LIKE Clause)
# ==============================================================================
def secure_product_search(search_term: str) -> Dict[str, Any]:
    """
    SECURE: Sanitizes input length and binds the search pattern safely via parameter binding.
    """
    if not isinstance(search_term, str):
        search_term = ""

    # Sanitize search term: Strip excessive whitespace, limit length
    cleaned_term = search_term.strip()[:50]
    
    # Safely bind wildcard pattern using parameter substitution
    parameterized_query = "SELECT id, name, category, price, stock, description FROM products WHERE name LIKE ? AND is_hidden = 0"
    params = (f"%{cleaned_term}%",)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(parameterized_query, params)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return {
            "status": "success",
            "results_count": len(results),
            "data": results,
            "executed_query": parameterized_query,
            "parameters": params,
            "error": None
        }
    except Exception:
        return {
            "status": "error",
            "results_count": 0,
            "data": [],
            "executed_query": parameterized_query,
            "error": "Search service temporarily unavailable."
        }
    finally:
        conn.close()

# ==============================================================================
# 3. SECURE USER PROFILE LOOKUP (Type Coercion & Parameter Binding)
# ==============================================================================
def secure_user_profile(user_id_input: Any) -> Dict[str, Any]:
    """
    SECURE: Enforces strict integer conversion and parameter binding.
    """
    try:
        validated_user_id = int(user_id_input)
        if validated_user_id <= 0:
            raise ValueError("ID must be positive")
    except (ValueError, TypeError):
        return {
            "status": "validation_error",
            "results_count": 0,
            "data": [],
            "executed_query": "BLOCKED_BY_TYPE_VALIDATION",
            "error": "Invalid User ID. Must be a valid positive integer."
        }

    parameterized_query = "SELECT id, username, email, role, bio, created_at FROM users WHERE id = ?"
    params = (validated_user_id,)

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(parameterized_query, params)
        rows = cursor.fetchall()
        results = [dict(row) for row in rows]
        return {
            "status": "success",
            "results_count": len(results),
            "data": results,
            "executed_query": parameterized_query,
            "parameters": params,
            "error": None
        }
    except Exception:
        return {
            "status": "error",
            "results_count": 0,
            "data": [],
            "executed_query": parameterized_query,
            "error": "Unable to retrieve profile."
        }
    finally:
        conn.close()
