# -*- coding: utf-8 -*-
"""Final comprehensive verification of the bilingual site."""
import os
import re
from bs4 import BeautifulSoup

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

zh_pages = []
en_pages = []
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.zh.html'):
            zh_pages.append(os.path.relpath(os.path.join(dp, f), ROOT).replace('\\', '/'))
        elif f.endswith('.html'):
            en_pages.append(os.path.relpath(os.path.join(dp, f), ROOT).replace('\\', '/'))

zh_pages.sort()
en_pages.sort()

print("=== 页面统计 ===")
print("中文页面:", len(zh_pages))
print("英文页面:", len(en_pages))

# check every zh page has a corresponding en page
missing_en = [p for p in zh_pages if p.replace('.zh.html', '.html') not in en_pages]
print("缺少对应英文页的中文页:", missing_en if missing_en else "无")

# check every en page has a corresponding zh page
missing_zh = [p for p in en_pages if p.replace('.html', '.zh.html') not in zh_pages]
print("缺少对应中文页的英文页:", missing_zh if missing_zh else "无")

# verify offline integrity: check all zh pages for broken local resources
issues = []
cdn_refs = 0
for p in zh_pages:
    fp = os.path.join(ROOT, p.replace('/', os.sep))
    s = open(fp, encoding='utf-8').read()
    # check for remaining CDN references
    if 'cdnjs.cloudflare.com' in s:
        cdn_refs += s.count('cdnjs.cloudflare.com')
    # check lang-switch.js
    if 'lang-switch.js' not in s:
        issues.append(p + ": missing lang-switch.js")

print("\n=== 离线完整性 ===")
print("CDN 引用残留:", cdn_refs)
print("缺少切换脚本的页面:", len(issues))
if issues:
    for i in issues[:5]:
        print("  ", i)

# spot-check a few pages for content
print("\n=== 内容抽查 ===")
spot = [
    'index.zh.html',
    'algorithms/foc/fundamentals.zh.html',
    'architecture/overview.zh.html',
    'components/index.zh.html',
    'algorithms/startup.zh.html',
    'appendix/glossary.zh.html',
    'faq.zh.html',
]
for p in spot:
    fp = os.path.join(ROOT, p.replace('/', os.sep))
    if not os.path.exists(fp):
        print(p, "-> 文件不存在!")
        continue
    s = open(fp, encoding='utf-8').read()
    soup = BeautifulSoup(s, 'html.parser')
    body = soup.find('div', class_='body')
    if body:
        text = body.get_text(separator=' ')
        # check if there's substantial Chinese content
        chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
        total_chars = len(text)
        ratio = chinese_chars / max(total_chars, 1) * 100
        print(f"{p}: {chinese_chars} 中文字符 / {total_chars} 总字符 ({ratio:.1f}%)")
    else:
        print(p, "-> 无 body div")

print("\n=== 验证完成 ===")
