#!/usr/bin/env python3
"""
Web Content & Endpoint Enumeration Tool.
Performs directory brute-forcing, sensitive file discovery, and route mapping.
"""

import urllib.request
import urllib.error
import json
import os
import sys

WORDLIST = [
    "",
    "api",
    "api/vulnerable/login",
    "api/vulnerable/search",
    "api/vulnerable/user/1",
    "api/secure/login",
    "api/secure/search",
    "api/secure/user/1",
    "admin",
    "dashboard",
    "config",
    ".env",
    "robots.txt",
    "server-status",
    "backup.sql",
    "static/css/style.css"
]

def enumerate_endpoints(base_url: str = "http://127.0.0.1:5000", wordlist: list = None) -> dict:
    if wordlist is None:
        wordlist = WORDLIST

    print(f"[*] Starting Web Enumeration against {base_url} ({len(wordlist)} wordlist items)...")
    results = {
        "base_url": base_url,
        "discovered_routes": []
    }

    for path in wordlist:
        url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "SecAssessmentCrawler/1.0"})
            with urllib.request.urlopen(req, timeout=2) as resp:
                status = resp.getcode()
                content_len = len(resp.read())
                entry = {
                    "path": f"/{path}",
                    "url": url,
                    "status_code": status,
                    "content_length": content_len,
                    "classification": "Accessible Endpoint"
                }
                results["discovered_routes"].append(entry)
                print(f"  [+] Discovered: {url} [HTTP {status}] ({content_len} bytes)")
        except urllib.error.HTTPError as e:
            if e.code in [401, 403, 405]:
                entry = {
                    "path": f"/{path}",
                    "url": url,
                    "status_code": e.code,
                    "content_length": 0,
                    "classification": "Restricted / Auth Required"
                }
                results["discovered_routes"].append(entry)
                print(f"  [!] Restricted: {url} [HTTP {e.code}]")
        except Exception:
            pass

    return results

def save_enum_results(data: dict, out_file: str = None):
    if not out_file:
        out_dir = os.path.dirname(os.path.abspath(__file__))
        out_file = os.path.join(out_dir, "enumeration_output.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"[+] Web enumeration complete. Results saved to {out_file}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:5000"
    res = enumerate_endpoints(target)
    save_enum_results(res)
