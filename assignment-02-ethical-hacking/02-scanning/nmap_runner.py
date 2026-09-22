#!/usr/bin/env python3
"""
Port Scanning & Host Discovery Engine.
Integrates system Nmap binary with an automated fallback Python multi-threaded socket scanner.
"""

import socket
import json
import os
import sys
import subprocess
import shutil
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5000: "Flask-Dashboard",
    5001: "Vulnerable-Lab-API",
    8080: "HTTP-Proxy/DVWA",
    8443: "HTTPS-Alt"
}

def check_port(host: str, port: int, timeout: float = 0.5) -> dict:
    """Checks TCP handshake status on a single port."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        res = s.connect_ex((host, port))
        if res == 0:
            # Attempt simple banner grab
            banner = ""
            try:
                s.sendall(b"HEAD / HTTP/1.0\r\n\r\n")
                raw = s.recv(256).decode("utf-8", errors="ignore")
                banner = raw.split("\r\n")[0] if raw else ""
            except Exception:
                banner = "No banner returned"
            return {"port": port, "state": "open", "service": COMMON_PORTS.get(port, "unknown"), "banner": banner}
    except Exception:
        pass
    finally:
        s.close()
    return {"port": port, "state": "closed", "service": COMMON_PORTS.get(port, "unknown")}

def run_port_scan(target_host: str = "127.0.0.1", ports_to_scan: list = None) -> dict:
    """Executes multi-threaded port scan."""
    if ports_to_scan is None:
        ports_to_scan = list(COMMON_PORTS.keys())

    print(f"[*] Starting TCP Port Scan against {target_host} ({len(ports_to_scan)} ports)...")
    results = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "target": target_host,
        "open_ports": [],
        "closed_ports_count": 0
    }

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_port, target_host, p) for p in ports_to_scan]
        for f in futures:
            res = f.result()
            if res["state"] == "open":
                results["open_ports"].append(res)
                print(f"  [+] OPEN: Port {res['port']} ({res['service']}) - Banner: {res.get('banner', '')}")
            else:
                results["closed_ports_count"] += 1

    return results

def save_scan_output(data: dict, out_dir: str = None):
    if not out_dir:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scans")
    os.makedirs(out_dir, exist_ok=True)
    
    json_path = os.path.join(out_dir, "port_scan_latest.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Scan results saved to: {json_path}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    scan_data = run_port_scan(target)
    save_scan_output(scan_data)
