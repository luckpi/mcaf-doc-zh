# -*- coding: utf-8 -*-
"""Download the MCAF doc site for offline use, preserving directory structure."""
import os
import re
import sys
import time
from urllib.parse import urljoin, urlparse, unquote
import requests
from bs4 import BeautifulSoup

BASE = "https://microchiptech.github.io/mcaf-doc/9.0.1/"
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(ROOT, "site")

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0 (compatible; MCAF-mirror/1.0)"})

visited = set()
asset_urls = set()


def local_path_for(url):
    p = urlparse(url)
    path = unquote(p.path)
    if path.endswith("/"):
        path += "index.html"
    if not path:
        path = "index.html"
    # strip leading slash
    rel = path.lstrip("/")
    return os.path.join(SITE_DIR, rel.replace("/", os.sep))


def save(url, content_bytes):
    dst = local_path_for(url)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with open(dst, "wb") as f:
        f.write(content_bytes)


def fetch(url):
    for attempt in range(3):
        try:
            r = session.get(url, timeout=30)
            if r.status_code == 200:
                return r.content
            if r.status_code == 404:
                return None
        except Exception as e:
            print("  retry", url, e)
            time.sleep(1)
    return None


def is_internal(url):
    p = urlparse(url)
    return p.netloc == "" or p.netloc == "microchiptech.github.io"


def normalize(url, base):
    full = urljoin(base, url)
    # strip fragment
    full = full.split("#")[0]
    return full


def crawl_html(url):
    url = url.split("#")[0]
    if url in visited:
        return
    visited.add(url)
    print("HTML:", url)
    content = fetch(url)
    if content is None:
        return
    save(url, content)
    soup = BeautifulSoup(content, "html.parser")

    # collect linked html pages
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("mailto:") or href.startswith("javascript:"):
            continue
        full = normalize(href, url)
        if not is_internal(full):
            continue
        # only follow .html or directory links within our base
        if full.startswith(BASE) or full.startswith(BASE.rstrip("/")):
            p = urlparse(full)
            if p.path.endswith(".html") or p.path.endswith("/") or "." not in os.path.basename(p.path):
                crawl_html(full)

    # collect assets (css, js, images)
    for tag, attr in [("link", "href"), ("script", "src"), ("img", "src"), ("img", "srcset")]:
        for el in soup.find_all(tag, **{attr: True}):
            val = el[attr]
            if attr == "srcset":
                for part in val.split(","):
                    part = part.strip().split(" ")[0]
                    if part:
                        asset_urls.add(normalize(part, url))
            else:
                if val.startswith("mailto:") or val.startswith("javascript:") or val.startswith("data:"):
                    continue
                asset_urls.add(normalize(val, url))


def download_assets():
    for u in sorted(asset_urls):
        if not is_internal(u):
            continue
        if not u.startswith(BASE) and not u.startswith(BASE.rstrip("/")):
            continue
        dst = local_path_for(u)
        if os.path.exists(dst):
            continue
        print("ASSET:", u)
        c = fetch(u)
        if c is not None:
            save(u, c)


if __name__ == "__main__":
    os.makedirs(SITE_DIR, exist_ok=True)
    crawl_html(BASE)
    download_assets()
    print("DONE. HTML pages:", len(visited), "assets:", len(asset_urls))
