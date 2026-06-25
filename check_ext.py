# -*- coding: utf-8 -*-
import os, re
root = 'site'
ext = set()
for dp, _, fs in os.walk(root):
    for f in fs:
        if f.endswith('.html'):
            s = open(os.path.join(dp, f), encoding='utf-8').read()
            for m in re.finditer(r'(?:href|src)="(https?://[^"]+)"', s):
                ext.add(m.group(1))
with open('ext_urls.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(sorted(ext)))
print('count', len(ext))
