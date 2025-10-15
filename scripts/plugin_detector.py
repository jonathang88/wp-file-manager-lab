#!/usr/bin/env python3
"""
plugin_detector.py
Safe script to detect WordPress plugin footprints (non-exploitative).
Usage: python3 plugin_detector.py https://example.test
"""
import sys
import requests
from urllib.parse import urljoin

def check_plugins(base_url):
    candidates = ['wp-content/plugins/wp-file-manager/', 'wp-content/plugins/']
    for c in candidates:
        url = urljoin(base_url, c)
        try:
            r = requests.get(url, timeout=8, allow_redirects=True)
            print(f"[{r.status_code}] {url} (len={len(r.text)})")
            if 'wp-file-manager' in r.text.lower() or 'wpdiscuz' in r.text.lower():
                print("Possible plugin strings found in plugin directory index.")
        except Exception as e:
            print(f"Error accessing {url}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 plugin_detector.py https://target")
        sys.exit(1)
    base = sys.argv[1].rstrip('/') + '/'
    check_plugins(base)

if __name__ == '__main__':
    main()

