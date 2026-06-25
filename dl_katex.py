# -*- coding: utf-8 -*-
"""Download KaTeX (0.16.4 and 0.11.1) for offline use and rewrite CDN refs."""
import os
import re
import requests

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
S = requests.Session()
S.headers.update({"User-Agent": "Mozilla/5.0"})

VERSIONS = ["0.16.4", "0.11.1"]
CDN = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/"

# KaTeX font files (woff2 is enough for modern browsers; also grab ttf + woff for safety)
FONT_BASES = [
    "KaTeX_AMS-Regular", "KaTeX_Caligraphic-Bold", "KaTeX_Caligraphic-Regular",
    "KaTeX_Fraktur-Bold", "KaTeX_Fraktur-Regular", "KaTeX_Main-Bold",
    "KaTeX_Main-BoldItalic", "KaTeX_Main-Italic", "KaTeX_Main-Regular",
    "KaTeX_Math-BoldItalic", "KaTeX_Math-Italic", "KaTeX_SansSerif-Bold",
    "KaTeX_SansSerif-Italic", "KaTeX_SansSerif-Regular", "KaTeX_Script-Regular",
    "KaTeX_Size1-Regular", "KaTeX_Size2-Regular", "KaTeX_Size3-Regular",
    "KaTeX_Size4-Regular", "KaTeX_Typewriter-Regular",
]
FONT_FMTS = ["woff2", "ttf", "woff"]


def fetch(url):
    r = S.get(url, timeout=60)
    if r.status_code == 200:
        return r.content
    print("  FAIL", r.status_code, url)
    return None


def main():
    for v in VERSIONS:
        dest = os.path.join(ROOT, "_static", "katex", v)
        os.makedirs(os.path.join(dest, "fonts"), exist_ok=True)
        os.makedirs(os.path.join(dest, "contrib"), exist_ok=True)
        files = [
            ("katex.min.css", os.path.join(dest, "katex.min.css")),
            ("katex.min.js", os.path.join(dest, "katex.min.js")),
            ("contrib/auto-render.min.js", os.path.join(dest, "contrib", "auto-render.min.js")),
        ]
        for name, path in files:
            if os.path.exists(path):
                continue
            url = CDN + v + "/" + name
            print("GET", url)
            c = fetch(url)
            if c is not None:
                with open(path, "wb") as f:
                    f.write(c)
        for base in FONT_BASES:
            for fmt in FONT_FMTS:
                fname = base + "." + fmt
                fpath = os.path.join(dest, "fonts", fname)
                if os.path.exists(fpath):
                    continue
                url = CDN + v + "/fonts/" + fname
                c = fetch(url)
                if c is not None:
                    with open(fpath, "wb") as f:
                        f.write(c)
    # rewrite CDN references in all html files to local paths
    n = 0
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            orig = s
            # compute relative prefix from this file to _static
            rel = os.path.relpath(os.path.join(ROOT, "_static"), dp).replace("\\", "/")
            for v in VERSIONS:
                s = s.replace(CDN + v + "/katex.min.css", rel + "/katex/" + v + "/katex.min.css")
                s = s.replace(CDN + v + "/katex.min.js", rel + "/katex/" + v + "/katex.min.js")
                s = s.replace(CDN + v + "/contrib/auto-render.min.js", rel + "/katex/" + v + "/contrib/auto-render.min.js")
            if s != orig:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(s)
                n += 1
    print("rewrote references in", n, "html files")


if __name__ == "__main__":
    main()
