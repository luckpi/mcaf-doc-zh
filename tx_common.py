# -*- coding: utf-8 -*-
"""Apply common template translations to all .zh.html pages.
Operates on raw HTML strings with safe, context-specific replacements.
"""
import os
import re
from bs4 import BeautifulSoup, NavigableString

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

# (old, new) pairs applied to every .zh.html file.
# Order matters: longer/more-specific patterns first.
COMMON = [
    # headerlink titles
    ('title="Permalink to this heading"', 'title="本标题的永久链接"'),
    ('title="Permalink to this equation"', 'title="本公式的永久链接"'),
    ('title="Permalink to this code"', 'title="本代码块的永久链接"'),
    ('title="Permalink to this image"', 'title="本图片的永久链接"'),
    ('title="Permalink to this table"', 'title="本表格的永久链接"'),
    ('title="Permalink to this section"', 'title="本节的永久链接"'),
    # search box
    ('<h3 id="searchlabel">Quick search</h3>', '<h3 id="searchlabel">快速搜索</h3>'),
    ('<input type="submit" value="Go" />', '<input type="submit" value="搜索" />'),
    # sidebar
    ('<h3><a href="#">Table of Contents</a></h3>', '<h3><a href="#">目录</a></h3>'),
    ('<h4>Next topic</h4>', '<h4>下一主题</h4>'),
    ('<h4>Previous topic</h4>', '<h4>上一主题</h4>'),
    # navigation headings
    ('<h3>Navigation</h3>', '<h3>导航</h3>'),
    # nav link titles + text
    ('title="General Index"', 'title="总索引"'),
    ('title="next chapter"', 'title="下一章"'),
    ('title="previous chapter"', 'title="上一章"'),
    # nav link visible text (appear in accesskey nav)
    ('accesskey="I">index</a>', 'accesskey="I">索引</a>'),
    ('accesskey="N">next</a> |', 'accesskey="N">下一页</a> |'),
    ('accesskey="P">previous</a> |', 'accesskey="P">上一页</a> |'),
    # bottom nav (no accesskey variant)
    ('>index</a></li>', '>索引</a></li>'),
    ('>next</a> |</li>', '>下一页</a> |</li>'),
    ('>previous</a> |</li>', '>上一页</a> |</li>'),
    # title suffix
    ('MCAF R9 RC31 documentation', 'MCAF R9 RC31 文档'),
    # footer copyright (both entity and decoded forms)
    ('&#169; Copyright 2017-2026, Microchip Technology, Inc..',
     '&#169; 版权所有 2017-2026，Microchip Technology, Inc..'),
    ('© Copyright 2017-2026, Microchip Technology, Inc..',
     '© 版权所有 2017-2026，Microchip Technology, Inc..'),
    # "Quick search" label fallback
    ('Quick search', '快速搜索'),
    # cross-references (raw replace is safe: capital + space, no class/attr matches)
    # NOTE: "Table of Contents" must come before "Table " -> "表 ".
    ('Table of Contents', '目录'),
    ('表 of Contents', '目录'),  # repair pages already mangled by a previous run
    ('Figure ', '图 '),
    ('Table ', '表 '),
    ('Equation ', '公式 '),
    ('Section ', '节 '),
]


def apply_common(path):
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    orig = s
    for old, new in COMMON:
        s = s.replace(old, new)
    if s != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        return True
    return False


def main():
    n = 0
    for dp, _, fs in os.walk(ROOT):
        for f in fs:
            if f.endswith(".zh.html"):
                if apply_common(os.path.join(dp, f)):
                    n += 1
    print("Common template applied to", n, "zh pages")


if __name__ == "__main__":
    main()
