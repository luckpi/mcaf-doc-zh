# -*- coding: utf-8 -*-
"""Prepare bilingual structure:
- Inject lang-switch.js into every existing (English) .html page.
- Create a .zh.html mirror for each .html page, with:
    * <html lang="zh">
    * internal .html links rewritten to .zh.html
    * lang-switch.js injected
The body text remains English at this stage; translation is applied separately.
"""
import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
LANG_JS = "lang-switch.js"


def list_html():
    out = []
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(".html"):
                out.append(os.path.join(dp, f))
    return out


def static_prefix(content):
    """Derive the relative prefix used to reference _static/ in this page."""
    m = re.search(r'(?:href|src)="([^"]*?)_static/', content)
    if m:
        return m.group(1)
    # fall back to depth-based prefix
    return ""


def inject_script(content, prefix):
    snippet = '<script src="{}_static/{}"></script>\n  </body>'.format(prefix, LANG_JS)
    if 'lang-switch.js' in content:
        return content
    if "</body>" in content:
        return content.replace("</body>", snippet, 1)
    return content + snippet


def rewrite_links_for_zh(soup):
    """Rewrite internal .html links to .zh.html inside a zh page."""
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if h.startswith("#") or h.startswith("http") or h.startswith("mailto:") or h.startswith("javascript:"):
            continue
        # only rewrite links ending with .html (preserve query/fragment)
        m = re.match(r"^(.*?)(\.html)([?#].*)?$", h)
        if m:
            a["href"] = m.group(1) + ".zh.html" + (m.group(3) or "")
    for link in soup.find_all("link", href=True):
        h = link["href"]
        if h.startswith("#") or h.startswith("http") or h.startswith("mailto:"):
            continue
        m = re.match(r"^(.*?)(\.html)([?#].*)?$", h)
        if m:
            link["href"] = m.group(1) + ".zh.html" + (m.group(3) or "")


def process(en_path):
    with open(en_path, "r", encoding="utf-8") as f:
        content = f.read()
    prefix = static_prefix(content)

    # 1. inject into English page
    new_en = inject_script(content, prefix)
    if new_en != content:
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(new_en)

    # 2. build zh mirror
    zh_path = re.sub(r"\.html$", ".zh.html", en_path)
    soup = BeautifulSoup(content, "html.parser")
    if soup.html:
        soup.html["lang"] = "zh"
    rewrite_links_for_zh(soup)
    zh_content = str(soup)
    zh_content = inject_script(zh_content, prefix)
    with open(zh_path, "w", encoding="utf-8") as f:
        f.write(zh_content)


def main():
    pages = list_html()
    for p in pages:
        process(p)
    print("Processed", len(pages), "pages")


if __name__ == "__main__":
    main()
