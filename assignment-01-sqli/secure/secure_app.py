#!/usr/bin/env python3
"""
Secure Web API Endpoints Service.
Provides a hardened HTTP interface demonstrating parameterized endpoints.
"""

from flask import Blueprint, request, jsonify
from .secure_queries import secure_login, secure_product_search, secure_user_profile

secure_bp = Blueprint("secure_api", __name__, url_prefix="/api/secure")

@secure_bp.route("/login", methods=["POST"])
def api_login():
    """Secure login endpoint enforcing input validation and prepared statements."""
    data = request.get_json(silent=True) or request.form
    username = data.get("username", "")
    password = data.get("password", "")
    
    result = secure_login(username, password)
    if result.get("status") == "validation_error":
        return jsonify(result), 400
    status_code = 200 if result.get("authenticated") else 401
    return jsonify(result), status_code

@secure_bp.route("/search", methods=["GET"])
def api_search():
    """Secure search endpoint using parameterized LIKE queries."""
    query = request.args.get("q", "")
    result = secure_product_search(query)
    return jsonify(result), 200

@secure_bp.route("/user/<path:user_id>", methods=["GET"])
def api_user(user_id):
    """Secure user detail endpoint enforcing integer validation."""
    result = secure_user_profile(user_id)
    if result.get("status") == "validation_error":
        return jsonify(result), 400
    return jsonify(result), 200
