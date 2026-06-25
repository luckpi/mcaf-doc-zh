# -*- coding: utf-8 -*-
import re, os
for f in ['basic.css', 'classic.css', 'microchip.css', 'mcaf_doc.css', 'pygments.css']:
    p = os.path.join('site/_static', f)
    c = open(p, encoding='utf-8').read()
    refs = re.findall(r'url\(["\']?(.*?)["\']?\)', c)
    if refs:
        print(f'{f} url refs: {refs}')
