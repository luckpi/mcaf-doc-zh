# -*- coding: utf-8 -*-
"""Find untranslated English text in .zh.html pages."""
import os
import re
from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = 'site'
SKIP_TAGS = {"math", "pre", "code", "kbd", "samp", "var", "script", "style", "textarea", "a"}
SKIP_CLASSES = {"section-number", "headerlink", "eqno", "math", "notranslate", "nav-logo", "caption-number"}

# Common English words to look for
EN_WORDS = re.compile(r'\b(the|and|with|for|that|this|from|using|used|which|when|where|into|over|under|between|through|during|after|before|each|both|all|some|more|most|such|also|only|very|can|will|shall|should|would|could|may|might|must|been|have|has|had|does|did|done|made|make|makes|making|get|gets|getting|set|sets|setting|put|puts|putting|take|takes|taking|give|gives|giving|use|uses|using|provide|provides|providing|contain|contains|containing|include|includes|including|consist|consists|consisting|represent|represents|representing|correspond|corresponds|corresponding|describe|describes|describing|explain|explains|explaining|show|shows|showing|indicate|indicates|indicating|note|notes|noting|allow|allows|allowing|require|requires|requiring|support|supports|supporting|implement|implements|implementing|perform|performs|performing|generate|generates|generating|produce|produces|producing|create|creates|creating|maintain|maintains|maintaining|control|controls|controlling|compute|computes|computing|calculate|calculates|calculating|measure|measures|measuring|detect|detects|detecting|determine|determines|determining|update|updates|updating|convert|converts|converting|transform|transforms|transforming|operate|operates|operating|function|functions|functioning|apply|applies|applying|based|called|known|given|shown|located|defined|described|contained|included|provided|represented|corresponding|following|above|below|figure|table|section|chapter|equation|see|refer|reference)\b', re.IGNORECASE)

results = {}

for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith('.zh.html'):
            continue
        zh_path = os.path.join(dp, f)
        soup = BeautifulSoup(open(zh_path, encoding='utf-8').read(), 'html.parser')
        body = soup.find('div', class_='body')
        if not body:
            continue

        untranslated = []
        for s in body.descendants:
            if not isinstance(s, NavigableString):
                continue
            parent = s.parent
            if not isinstance(parent, Tag):
                continue
            if parent.name in SKIP_TAGS:
                continue
            classes = parent.get('class') or []
            if any(c in SKIP_CLASSES for c in classes):
                continue
            text = str(s).strip()
            if not text or len(text) < 3:
                continue
            # Skip pure numbers, punctuation, code-like text
            if re.match(r'^[\d\s\.\,\;\:\-\(\)\[\]\{\}\/\\\+\=\*\&\%\#\@\!\?\<\>\|~`\'"]+$', text):
                continue
            # Skip if mostly Chinese
            chinese_chars = len(re.findall(r'[\u4e00-\u9fff]', text))
            if chinese_chars > 0 and chinese_chars / len(text) > 0.3:
                continue
            # Check for common English words
            if EN_WORDS.search(text):
                untranslated.append(text[:120])

        if untranslated:
            rel = os.path.relpath(zh_path, ROOT).replace('\\', '/')
            results[rel] = untranslated

print(f'Pages with untranslated text: {len(results)}')
for rel, texts in sorted(results.items()):
    print(f'\n=== {rel} ({len(texts)} fragments) ===')
    for t in texts[:10]:
        print(f'  - {t}')
    if len(texts) > 10:
        print(f'  ... and {len(texts)-10} more')
