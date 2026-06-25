# -*- coding: utf-8 -*-
import sys, re
from bs4 import BeautifulSoup, NavigableString, Tag

rel = sys.argv[1]
soup = BeautifulSoup(open(rel, encoding='utf-8').read(), 'html.parser')
b = soup.find('div', class_='body')
if not b:
    b = soup
SKIP_TAGS = {"math", "pre", "code", "kbd", "samp", "var", "script", "style", "textarea", "a"}
SKIP_CLASSES = {"section-number", "headerlink", "eqno", "math", "notranslate", "nav-logo", "caption-number"}
EN_WORDS = re.compile(r'\b(the|and|with|for|that|this|from|using|used|which|when|where|into|over|under|between|through|during|after|before|each|both|all|some|more|most|such|also|only|very|can|will|shall|should|would|could|may|might|must|been|have|has|had|does|did|done|made|make|makes|making|get|gets|getting|set|sets|setting|put|puts|putting|take|takes|taking|give|gives|giving|use|uses|using|provide|provides|providing|contain|contains|containing|include|includes|including|consist|consists|consisting|represent|represents|representing|correspond|corresponds|corresponding|describe|describes|describing|explain|explains|explaining|show|shows|showing|indicate|indicates|indicating|note|notes|noting|allow|allows|allowing|require|requires|requiring|support|supports|supporting|implement|implements|implementing|perform|performs|performing|generate|generates|generating|produce|produces|producing|create|creates|creating|maintain|maintains|maintaining|control|controls|controlling|compute|computes|computing|calculate|calculates|calculating|measure|measures|measuring|detect|detects|detecting|determine|determines|determining|update|updates|updating|convert|converts|converting|transform|transforms|transforming|operate|operates|operating|function|functions|functioning|apply|applies|applying|based|called|known|given|shown|located|defined|described|contained|included|provided|represented|corresponding|following|above|below|figure|table|section|chapter|equation|see|refer|reference)\b', re.IGNORECASE)
PUNCT = r'^[\d\s\.\,\;\:\-\(\)\[\]\{\}\/\\\+\=\*\&\%\#\@\!\?\<\>\|~`\'"]+$'
for s in b.descendants:
    if not isinstance(s, NavigableString):
        continue
    p = s.parent
    if not isinstance(p, Tag):
        continue
    if p.name in SKIP_TAGS:
        continue
    classes = p.get('class') or []
    if any(c in SKIP_CLASSES for c in classes):
        continue
    text = str(s).strip()
    if not text or len(text) < 3:
        continue
    if re.match(PUNCT, text):
        continue
    cc = len(re.findall(r'[\u4e00-\u9fff]', text))
    if cc > 0 and cc / len(text) > 0.3:
        continue
    if EN_WORDS.search(text):
        print(f'PARENT=<{p.name} class={classes}>')
        print(f'  TEXT={str(s)[:300]!r}')
        print()
