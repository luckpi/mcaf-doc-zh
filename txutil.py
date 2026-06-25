# -*- coding: utf-8 -*-
"""Utilities for page-specific translation of .zh.html files.

Approach: translate by replacing English text fragments inside NavigableString
text nodes. This preserves all inline tags (math, code, links, sub/sup, etc.)
and only changes visible prose.
"""
import os
import re
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
_WS = re.compile(r"\s+")

# Tags whose text content must NOT be translated.
SKIP_TAGS = {"math", "pre", "code", "kbd", "samp", "var", "script", "style", "textarea"}
# CSS classes whose element text must NOT be translated (section numbers, permalinks, eq numbers).
SKIP_CLASSES = {"section-number", "headerlink", "eqno", "math", "notranslate", "nav-logo"}


def _skip(el):
    if el is None:
        return True
    if isinstance(el, NavigableString):
        return _skip(el.parent)
    if not isinstance(el, Tag):
        return True
    if el.name in SKIP_TAGS:
        return True
    classes = el.get("class") or []
    if any(c in SKIP_CLASSES for c in classes):
        return True
    return False


def replace_text(soup, pairs, root=None, whole=False):
    """Replace English fragments with Chinese in text nodes under `root`.

    pairs: list of (en, zh). Applied in order to each text node.
    whole: if True, only replace when the stripped text node equals `en`;
           otherwise substring replacement.
    """
    if root is None:
        root = soup
    changed = 0
    # collect text nodes first to avoid mutation issues
    nodes = []
    for s in root.descendants:
        if isinstance(s, NavigableString) and not _skip(s):
            if s.strip():
                nodes.append(s)
    for s in nodes:
        original = str(s)
        # normalize whitespace so fragment matching is predictable
        new = _WS.sub(" ", original)
        for en, zh in pairs:
            if not en:
                continue
            en_norm = _WS.sub(" ", en)
            if whole:
                if new.strip() == en_norm.strip():
                    lead = len(new) - len(new.lstrip())
                    trail = len(new) - len(new.rstrip())
                    new = (" " * lead) + zh + (" " * trail)
            else:
                if en_norm in new:
                    new = new.replace(en_norm, zh)
        if new != original:
            s.replace_with(NavigableString(new))
            changed += 1
    return changed


def set_title(soup, zh_title):
    t = soup.find("title")
    if t:
        # keep the " — MCAF R9 RC31 documentation (docver 9.0.1)" suffix
        txt = t.get_text()
        # strip existing main title before the em-dash
        if "—" in txt:
            suffix = txt.split("—", 1)[1]
            t.string = "{} —{}".format(zh_title, suffix)
        else:
            t.string = zh_title


def set_html_title_attr(soup, zh):
    """Translate the <title> tag fully if needed (rare)."""
    set_title(soup, zh)


def load(rel):
    path = os.path.join(ROOT, rel.replace("/", os.sep))
    with open(path, "r", encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser"), path


def save(path, soup):
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def body(soup):
    return soup.find("div", class_="body")


def collect_nodes(root):
    """Return list of NavigableString text nodes (translatable) under root, in order."""
    nodes = []
    for s in root.descendants:
        if isinstance(s, NavigableString) and not _skip(s):
            if s.strip():
                nodes.append(s)
    return nodes


def extract_strings(root, min_len=2):
    """Print numbered unique normalized strings of translatable text nodes under root."""
    nodes = collect_nodes(root)
    seen = {}
    for i, s in enumerate(nodes):
        norm = _WS.sub(" ", str(s)).strip()
        if len(norm) < min_len:
            continue
        if norm not in seen:
            seen[norm] = i
            print("[{}] {}".format(i, norm))


def apply_dict(root, mapping):
    """Replace text nodes whose normalized text matches a key in `mapping`.

    mapping: {normalized_en: zh}. Preserves a single leading/trailing space.
    """
    changed = 0
    for s in collect_nodes(root):
        original = str(s)
        norm = _WS.sub(" ", original)
        key = norm.strip()
        if key in mapping:
            zh = mapping[key]
            lead = len(norm) - len(norm.lstrip())
            trail = len(norm) - len(norm.rstrip())
            new = (" " * lead) + zh + (" " * trail)
            if new != original:
                s.replace_with(NavigableString(new))
                changed += 1
    return changed


# Standalone Western punctuation -> Chinese punctuation, only for nodes that are
# exactly one punctuation char (these occur between inline math/links).
_PUNCT = {".": "。", ",": "，", ";": "；", ":": "：", "(": "（", ")": "）"}


def apply_punctuation(root):
    changed = 0
    for s in collect_nodes(root):
        val = str(s)
        key = val.strip()
        if key in _PUNCT and len(key) == 1:
            lead = len(val) - len(val.lstrip())
            trail = len(val) - len(val.rstrip())
            new = (" " * lead) + _PUNCT[key] + (" " * trail)
            if new != val:
                s.replace_with(NavigableString(new))
                changed += 1
    return changed


def translate_page(rel, title_zh, pairs, whole_pairs=None, root_only_body=False):
    """Convenience: load a zh page, set its <title>, apply fragment pairs, save.

    By default pairs are applied to the whole document so that breadcrumbs and
    sidebar TOC entries are translated too. Set root_only_body=True to restrict
    to the main body (useful when a fragment might collide with nav text)."""
    soup, path = load(rel + ".zh.html" if not rel.endswith(".zh.html") else rel)
    if title_zh:
        set_title(soup, title_zh)
    root = body(soup) if root_only_body else soup
    if root is not None:
        replace_text(soup, pairs, root=root)
        if whole_pairs:
            replace_text(soup, whole_pairs, root=root, whole=True)
        apply_punctuation(root)
    save(path, soup)
    return path


def translate_dict_page(rel, title_zh, mapping, root_only_body=False):
    """Load a zh page, set <title>, apply a {en:zh} dict to text nodes, save.

    By default applied to the whole document (so breadcrumbs/sidebar titles are
    translated too). mapping keys are matched against normalized node text."""
    soup, path = load(rel + ".zh.html" if not rel.endswith(".zh.html") else rel)
    if title_zh:
        set_title(soup, title_zh)
    root = body(soup) if root_only_body else soup
    if root is not None:
        apply_dict(root, mapping)
        apply_punctuation(root)
    save(path, soup)
    return path
