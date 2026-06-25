# -*- coding: utf-8 -*-
import re, os, glob

for f in glob.glob('site/algorithms/*.zh.html'):
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    matches = re.findall(r'href="([^"]*\.html)"', content)
    bad = [m for m in matches if '.zh.html' not in m and 'http' not in m]
    if bad:
        print(f'{os.path.basename(f)}: {len(bad)} non-zh html links')
        for b in bad[:5]:
            print(f'  {b}')
