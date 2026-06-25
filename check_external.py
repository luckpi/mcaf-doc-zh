# -*- coding: utf-8 -*-
"""Check for any remaining external/CDN references in all HTML and CSS files."""
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

external_refs = set()

# Check HTML files
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html'):
            p = os.path.join(dp, f)
            content = open(p, encoding='utf-8').read()
            # Find http/https URLs
            urls = re.findall(r'(?:src|href)\s*=\s*["\']?(https?://[^"\'>\s]+)', content)
            for u in urls:
                external_refs.add(('HTML', f, u))

# Check CSS files
css_dir = os.path.join(ROOT, '_static')
for f in os.listdir(css_dir):
    if f.endswith('.css'):
        p = os.path.join(css_dir, f)
        content = open(p, encoding='utf-8').read()
        urls = re.findall(r'url\((https?://[^)]+)\)', content)
        for u in urls:
            external_refs.add(('CSS', f, u))

print("External references found:", len(external_refs))
for typ, fname, url in sorted(external_refs):
    print(f"  [{typ}] {fname}: {url}")
