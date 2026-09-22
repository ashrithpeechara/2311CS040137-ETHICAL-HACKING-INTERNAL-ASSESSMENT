#!/usr/bin/env python3
"""
Vulnerable Web API Endpoints Service.
Provides an isolated HTTP interface demonstrating vulnerable SQL endpoints.
"""

from flask import Blueprint, request, jsonify
from .vuln_queries import vulnerable_login, vulnerable_product_search, vulnerable_user_profile

vuln_bp = Blueprint("vulnerable_api", __name__, url_prefix="/api/vulnerable")

@vuln_bp.route("/login", methods=["POST"])
def api_login():
    """Vulnerable login endpoint accepting JSON or form parameters."""
    data = request.get_json(silent=True) or request.form
    username = data.get("username", "")
    password = data.get("password", "")
    
    result = vulnerable_login(username, password)
    status_code = 200 if result.get("authenticated") else 401
    return jsonify(result), status_code

@vuln_bp.route("/search", methods=["GET"])
def api_search():
    """Vulnerable search endpoint accepting 'q' parameter."""
    query = request.args.get("q", "")
    result = vulnerable_product_search(query)
    return jsonify(result), 200

@vuln_bp.route("/user/<path:user_id>", methods=["GET"])
def api_user(user_id):
    """Vulnerable user detail endpoint accepting numeric/injected user ID."""
    result = vulnerable_user_profile(user_id)
    return jsonify(result), 200
