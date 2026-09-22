#!/usr/bin/env python3
"""
Nmap & Port Scan Output Parser Utility.
Parses raw JSON or XML port scan logs and formats them into structured Markdown tables.
"""

import json
import os
import sys

def parse_scan_json(json_path: str) -> str:
    if not os.path.exists(json_path):
        return "Error: Specified scan file does not exist."

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    target = data.get("target", "Unknown")
    timestamp = data.get("timestamp", "Unknown")
    open_ports = data.get("open_ports", [])

    md = f"### Scan Summary for Target: `{target}`\n"
    md += f"- **Scan Timestamp:** `{timestamp}`\n"
    md += f"- **Open Ports Discovered:** {len(open_ports)}\n\n"
    md += "| Port | Protocol | State | Service | Banner / Version |\n"
    md += "| :--- | :--- | :--- | :--- | :--- |\n"

    for p in open_ports:
        md += f"| **{p.get('port')}** | TCP | `{p.get('state')}` | {p.get('service')} | {p.get('banner', 'N/A')} |\n"

    return md

if __name__ == "__main__":
    default_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assignment-02-ethical-hacking", "02-scanning", "scans", "port_scan_latest.json")
    target_file = sys.argv[1] if len(sys.argv) > 1 else default_path
    print(parse_scan_json(target_file))
