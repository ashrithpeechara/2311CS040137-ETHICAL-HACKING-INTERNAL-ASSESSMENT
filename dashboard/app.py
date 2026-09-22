#!/usr/bin/env python3
"""
Security Operations & Assessment Dashboard Service.
Serves interactive SQLi query comparators, findings matrix, evidence viewer,
and live test triggers in a unified Dark-Cyber SecOps interface.
"""

import os
import sys
import json
from flask import Flask, render_template, jsonify, send_from_directory, request

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLI_DIR = os.path.join(PROJECT_ROOT, "assignment-01-sqli")
REMED_DIR = os.path.join(PROJECT_ROOT, "assignment-02-ethical-hacking", "06-remediation")
RETEST_DIR = os.path.join(PROJECT_ROOT, "assignment-02-ethical-hacking", "07-retesting")

for p in [PROJECT_ROOT, SQLI_DIR, REMED_DIR, RETEST_DIR]:
    if p not in sys.path:
        sys.path.insert(0, p)

from patch_auth import inject_security_headers
from retest_all import run_retest_suite
from vulnerable.vuln_app import vuln_bp
from secure.secure_app import secure_bp

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates"),
    static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
)
app.config["SECRET_KEY"] = "secops-dashboard-development-key"

# Register Assessment API Blueprints
app.register_blueprint(vuln_bp)
app.register_blueprint(secure_bp)

# Apply Defensive Security Headers Middleware
@app.after_request
def apply_headers(response):
    return inject_security_headers(response)

def get_findings_data():
    path = os.path.join(PROJECT_ROOT, "assignment-02-ethical-hacking", "04-vulnerability-analysis", "findings_catalog.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def get_evidence_data():
    path = os.path.join(PROJECT_ROOT, "reports", "evidence_index.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"evidence_items": []}

def get_retest_data():
    path = os.path.join(PROJECT_ROOT, "assignment-02-ethical-hacking", "07-retesting", "retest_results.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"retest_matrix": []}

@app.route("/")
def index():
    findings = get_findings_data()
    evidence = get_evidence_data()
    remediated = sum(1 for f in findings if f.get("status") == "REMEDIATED")
    return render_template(
        "index.html",
        findings=findings,
        remediated_count=remediated,
        evidence_count=len(evidence.get("evidence_items", []))
    )

@app.route("/sqli")
def sqli_lab_view():
    return render_template("sqli_lab.html")

@app.route("/ethical-hacking")
def ethical_hacking_view():
    retest_data = get_retest_data()
    return render_template("ethical_hacking.html", retest_matrix=retest_data.get("retest_matrix", []))

@app.route("/evidence")
def evidence_view():
    evidence = get_evidence_data()
    return render_template("evidence_viewer.html", evidence_items=evidence.get("evidence_items", []))

@app.route("/reports/<path:filename>")
def serve_reports(filename):
    reports_dir = os.path.join(PROJECT_ROOT, "reports")
    return send_from_directory(reports_dir, filename)

@app.route("/api/run-retests", methods=["POST"])
def api_run_retests():
    data = run_retest_suite()
    return jsonify(data)

if __name__ == "__main__":
    print("[*] Launching Security Operations Dashboard on http://127.0.0.1:5000...")
    app.run(host="127.0.0.1", port=5000, debug=False)
