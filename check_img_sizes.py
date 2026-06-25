# -*- coding: utf-8 -*-
"""Find all images with large width/height attributes."""
from bs4 import BeautifulSoup
import os

ROOT = 'site'
big_imgs = []

for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html') and not f.endswith('.zh.html'):
            p = os.path.join(dp, f)
            soup = BeautifulSoup(open(p, encoding='utf-8').read(), 'html.parser')
            for img in soup.find_all('img'):
                w = img.get('width', '')
                h = img.get('height', '')
                src = img.get('src', '')
                # Check if width/height are absolute pixel values (not percentages)
                if w and not str(w).endswith('%'):
                    try:
                        wval = int(w)
                        if wval > 1000:
                            rel = os.path.relpath(p, ROOT).replace('\\', '/')
                            big_imgs.append((rel, src, w, h))
                    except ValueError:
                        pass

print(f'Images with width > 1000px: {len(big_imgs)}')
for rel, src, w, h in big_imgs:
    print(f'  {rel}: {src} width={w} height={h}')
