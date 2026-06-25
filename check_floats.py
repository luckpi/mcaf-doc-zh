# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
ROOT = 'site'
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html') and not f.endswith('.zh.html'):
            p = os.path.join(dp, f)
            soup = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')
            for el in soup.find_all(class_=lambda x: x and any(c in ('align-left', 'align-right') for c in x)):
                rel = os.path.relpath(p, ROOT).replace('\\', '/')
                print(rel, el.name, el.get('class'))
