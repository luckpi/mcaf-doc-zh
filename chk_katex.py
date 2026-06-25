# -*- coding: utf-8 -*-
import re
s = open('site/algorithms/foc/fundamentals.zh.html', encoding='utf-8').read()
for m in re.findall(r'(?:href|src)="[^"]*katex[^"]*"', s):
    print(m)
print('--- remaining cdnjs refs:', s.count('cdnjs.cloudflare.com'))
