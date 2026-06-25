# -*- coding: utf-8 -*-
"""Compare full DOM tree structure between EN and ZH pages."""
from bs4 import BeautifulSoup, NavigableString
import os

ROOT = 'site'

def dom_signature(el, depth=0):
    """Generate a structural signature of an element, ignoring text content."""
    if isinstance(el, NavigableString):
        return ''  # ignore text nodes
    if not el.name:
        return ''
    cls = tuple(sorted(el.get('class', [])))
    sig = el.name + ':' + str(cls)
    children = [c for c in el.children if c.name]
    if children:
        child_sigs = [dom_signature(c, depth+1) for c in children]
        sig += '{' + '|'.join(child_sigs) + '}'
    return sig

issues = []
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.zh.html'):
            zh_path = os.path.join(dp, f)
            en_path = zh_path.replace('.zh.html', '.html')
            if not os.path.exists(en_path):
                continue
            en_soup = BeautifulSoup(open(en_path, encoding='utf-8').read(), 'html.parser')
            zh_soup = BeautifulSoup(open(zh_path, encoding='utf-8').read(), 'html.parser')

            # Compare body structure
            en_body = en_soup.find('div', class_='body')
            zh_body = zh_soup.find('div', class_='body')
            if not en_body or not zh_body:
                if bool(en_body) != bool(zh_body):
                    rel = os.path.relpath(zh_path, ROOT).replace('\\', '/')
                    issues.append((rel, 'missing body div'))
                continue

            en_sig = dom_signature(en_body)
            zh_sig = dom_signature(zh_body)
            if en_sig != zh_sig:
                rel = os.path.relpath(zh_path, ROOT).replace('\\', '/')
                # Find where they differ
                issues.append((rel, 'DOM structure differs'))

print('Pages with DOM structure differences:', len(issues))
for rel, issue in issues:
    print(f'  {rel}: {issue}')
