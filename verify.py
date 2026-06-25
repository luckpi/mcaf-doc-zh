# -*- coding: utf-8 -*-
"""Verify offline integrity of the bilingual site."""
import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")


def check_page(rel):
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    s = open(p, encoding="utf-8").read()
    soup = BeautifulSoup(s, "html.parser")
    dp = os.path.dirname(p)
    issues = []
    # 1. lang-switch.js referenced and exists
    refs = [x.get("src") for x in soup.find_all("script", src=True) if "lang-switch.js" in (x.get("src") or "")]
    if not refs:
        issues.append("missing lang-switch.js reference")
    else:
        for r in refs:
            rp = os.path.normpath(os.path.join(dp, r))
            if not os.path.exists(rp):
                issues.append("lang-switch.js missing on disk: " + r)
    # 2. images resolve
    for img in soup.find_all("img", src=True):
        src = img["src"]
        if src.startswith("data:") or src.startswith("http"):
            continue
        rp = os.path.normpath(os.path.join(dp, src))
        if not os.path.exists(rp):
            issues.append("img missing: " + src)
    # 3. css resolve
    for link in soup.find_all("link", href=True):
        h = link["href"]
        if h.startswith("http") or h.startswith("#"):
            continue
        rp = os.path.normpath(os.path.join(dp, h))
        if not os.path.exists(rp):
            issues.append("css/link missing: " + h)
    return issues


def check_zh_links(rel):
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    s = open(p, encoding="utf-8").read()
    soup = BeautifulSoup(s, "html.parser")
    bad = []
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if h.startswith("http") or h.startswith("#") or h.startswith("mailto:"):
            continue
        if h.endswith(".html") and ".zh.html" not in h:
            # internal nav link should point to zh version
            bad.append(h)
    return bad


pages = [
    "index.html", "index.zh.html",
    "introduction.html", "introduction.zh.html",
    "algorithms/foc/fundamentals.html", "algorithms/foc/fundamentals.zh.html",
    "algorithms/foc/dclink-comp.zh.html",
]
ok = True
for pg in pages:
    issues = check_page(pg)
    print(pg, "->", "OK" if not issues else issues)
    if issues:
        ok = False
for pg in ["index.zh.html", "algorithms/foc/fundamentals.zh.html"]:
    bad = check_zh_links(pg)
    print("zh-link", pg, "->", "OK" if not bad else ("non-zh links: " + str(bad[:5])))

# count zh pages
zh = sum(1 for dp, _, fs in os.walk(ROOT) for f in fs if f.endswith(".zh.html"))
en = sum(1 for dp, _, fs in os.walk(ROOT) for f in fs if f.endswith(".html") and not f.endswith(".zh.html"))
print("zh pages:", zh, "en pages:", en)
print("ALL OK" if ok else "HAS ISSUES")
