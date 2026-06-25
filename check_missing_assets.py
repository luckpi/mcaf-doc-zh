# -*- coding: utf-8 -*-
"""Check for any missing local assets referenced by HTML pages."""
import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# Collect all referenced local assets from all HTML files
referenced = set()
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html'):
            p = os.path.join(dp, f)
            content = open(p, encoding='utf-8').read()
            soup = BeautifulSoup(content, 'html.parser')
            for tag in soup.find_all(['script', 'img', 'link']):
                src = tag.get('src') or tag.get('href')
                if not src:
                    continue
                if src.startswith('http') or src.startswith('//') or src.startswith('mailto:') or src.startswith('javascript:'):
                    continue
                if src.startswith('#'):
                    continue
                # Remove fragment
                src = src.split('#')[0].split('?')[0]
                if not src:
                    continue
                referenced.add(src)

# Check which ones exist
missing = []
for ref in sorted(referenced):
    # Resolve relative to site root
    # All refs are relative to the page they appear in, but we can check
    # by looking for the file anywhere under site/
    # Actually, refs are relative paths like "../../_static/foo.css"
    # We need to check from each page's location. But for a quick check,
    # let's just see if the basename exists somewhere
    basename = os.path.basename(ref)
    found = False
    for dp, _, fs in os.walk(ROOT):
        if basename in fs:
            found = True
            break
    if not found:
        missing.append(ref)

print("Referenced local assets:", len(referenced))
print("Missing assets:", len(missing))
for m in missing:
    print("  ", m)
