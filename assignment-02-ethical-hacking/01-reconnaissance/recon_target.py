#!/usr/bin/env python3
"""
Reconnaissance & Footprinting Automation Script.
Collects passive/active metadata, header fingerprints, DNS/Host resolution, and web technologies.
"""

import socket
import urllib.request
import urllib.error
import json
import os
import sys

def perform_recon(target_host: str = "127.0.0.1", target_port: int = 5000) -> dict:
    """Performs non-intrusive footprinting against target host/port."""
    print(f"[*] Initiating Reconnaissance Phase against {target_host}:{target_port}...")
    
    recon_data = {
        "target_host": target_host,
        "target_port": target_port,
        "dns_resolution": {},
        "server_headers": {},
        "detected_technologies": [],
        "status": "completed"
    }

    # 1. DNS & Host Resolution
    try:
        ip_addr = socket.gethostbyname(target_host)
        fqdn = socket.getfqdn(target_host)
        recon_data["dns_resolution"] = {
            "resolved_ip": ip_addr,
            "fqdn": fqdn,
            "is_loopback": ip_addr.startswith("127.") or ip_addr == "::1"
        }
        print(f"[+] Host resolved: {fqdn} -> {ip_addr}")
    except Exception as e:
        recon_data["dns_resolution"] = {"error": str(e)}

    # 2. HTTP Banner & Header Inspection
    target_url = f"http://{target_host}:{target_port}"
    try:
        req = urllib.request.Request(target_url, headers={"User-Agent": "SecurityAssessmentRecon/1.0"})
        with urllib.request.urlopen(req, timeout=3) as resp:
            headers = dict(resp.info())
            recon_data["server_headers"] = headers
            
            # Technology heuristics
            server_header = headers.get("Server", "Unknown")
            recon_data["detected_technologies"].append(f"Web Server: {server_header}")
            
            if "Werkzeug" in server_header or "Python" in server_header:
                recon_data["detected_technologies"].append("Backend Runtime: Python / WSGI")
            if "X-Powered-By" in headers:
                recon_data["detected_technologies"].append(f"Framework: {headers['X-Powered-By']}")
                
            print(f"[+] HTTP Headers retrieved successfully. Server banner: {server_header}")
    except Exception as e:
        recon_data["server_headers"] = {"status": "Offline / Unreachable on HTTP", "note": str(e)}
        recon_data["detected_technologies"].append("Target Web Daemon not currently active")

    return recon_data

def save_recon_results(data: dict, output_path: str = None):
    if not output_path:
        out_dir = os.path.dirname(os.path.abspath(__file__))
        output_path = os.path.join(out_dir, "recon_output.json")
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Reconnaissance results saved to {output_path}")

if __name__ == "__main__":
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 5000
    results = perform_recon(host, port)
    save_recon_results(results)
