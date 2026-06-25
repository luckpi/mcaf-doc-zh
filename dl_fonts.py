# -*- coding: utf-8 -*-
"""Download Google Fonts (Open Sans) for offline use."""
import os
import re
import requests

STATIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site", "_static")
FONT_DIR = os.path.join(STATIC, "fonts")
os.makedirs(FONT_DIR, exist_ok=True)

UA = {"User-Agent": "Mozilla/5.0"}

# 1. Download the CSS
css_url = "https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800"
r = requests.get(css_url, headers=UA)
css_text = r.text
print("Downloaded CSS:", len(css_text), "bytes")

# 2. Find all font URLs
font_urls = re.findall(r"url\((https://fonts\.gstatic\.com/[^)]+)\)", css_text)
print("Font files to download:", len(font_urls))

# 3. Download each font
for i, furl in enumerate(font_urls):
    fname = os.path.basename(furl)
    fpath = os.path.join(FONT_DIR, fname)
    if not os.path.exists(fpath):
        r2 = requests.get(furl, headers=UA)
        with open(fpath, "wb") as f:
            f.write(r2.content)
        print(f"  [{i+1}/{len(font_urls)}] {fname}: {len(r2.content)} bytes")
    else:
        print(f"  [{i+1}/{len(font_urls)}] {fname}: already exists")

# 4. Rewrite CSS to use local paths
local_css = css_text
for furl in font_urls:
    fname = os.path.basename(furl)
    local_css = local_css.replace(furl, "fonts/" + fname)

# 5. Save local font CSS
font_css_path = os.path.join(STATIC, "open-sans.css")
with open(font_css_path, "w", encoding="utf-8") as f:
    f.write(local_css)
print("Saved local font CSS:", font_css_path)

# 6. Update microchip.css to use local font CSS instead of Google Fonts URL
micro_path = os.path.join(STATIC, "microchip.css")
micro = open(micro_path, encoding="utf-8").read()
micro_new = micro.replace(
    "@import url(https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800);",
    "@import url(open-sans.css);"
)
if micro_new != micro:
    with open(micro_path, "w", encoding="utf-8") as f:
        f.write(micro_new)
    print("Updated microchip.css to use local fonts")
else:
    print("WARNING: microchip.css not updated - URL not found")
