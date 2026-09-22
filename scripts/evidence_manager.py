#!/usr/bin/env python3
"""
Standardized Evidence Management & Cryptographic Hashing Engine.
Discovers, indexes, hashes (SHA-256), and catalogs all evidence artifacts across both assignments.
"""

import os
import hashlib
import json
from datetime import datetime, timezone

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")

def calculate_sha256(filepath: str) -> str:
    """Computes standard SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return "ERROR_COMPUTING_HASH"

def index_all_evidence() -> dict:
    print("[*] Initiating Evidence Discovery & Cryptographic Verification...")
    evidence_index = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "assessor_id": "2311CS040137-EH",
        "evidence_count": 0,
        "evidence_items": []
    }

    evidence_dirs = [
        (os.path.join(PROJECT_ROOT, "assignment-01-sqli", "evidence"), "Assignment-01-SQLi"),
        (os.path.join(PROJECT_ROOT, "assignment-02-ethical-hacking", "evidence"), "Assignment-02-EthicalHacking")
    ]

    for dir_path, module_name in evidence_dirs:
        if not os.path.exists(dir_path):
            continue
        
        for root, _, files in os.walk(dir_path):
            for file in files:
                if file.endswith((".md", ".json", ".txt", ".png")):
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, PROJECT_ROOT).replace("\\", "/")
                    sha256 = calculate_sha256(full_path)
                    
                    evidence_id = file.split("_")[0] if file.startswith("EV-") else f"EV-{file}"
                    
                    entry = {
                        "evidence_id": evidence_id,
                        "filename": file,
                        "relative_path": rel_path,
                        "module": module_name,
                        "sha256_checksum": sha256,
                        "last_modified": datetime.fromtimestamp(os.path.getmtime(full_path), timezone.utc).isoformat()
                    }
                    evidence_index["evidence_items"].append(entry)
                    print(f"  [+] Indexed {evidence_id:<12} | {rel_path} | SHA-256: {sha256[:12]}...")

    evidence_index["evidence_count"] = len(evidence_index["evidence_items"])
    
    os.makedirs(REPORTS_DIR, exist_ok=True)
    index_json_path = os.path.join(REPORTS_DIR, "evidence_index.json")
    with open(index_json_path, "w", encoding="utf-8") as f:
        json.dump(evidence_index, f, indent=2)
        
    print(f"\n[+] Centralized Evidence Registry written to: {index_json_path}")
    return evidence_index

if __name__ == "__main__":
    index_all_evidence()
