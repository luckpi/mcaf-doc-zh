# -*- coding: utf-8 -*-
import sys

fname = sys.argv[1]
content = open(fname, 'r', encoding='utf-8').read()
# Replace ASCII double quotes inside strings with smart quotes where needed
replacements = [
    ('"Weathervane"', '\u201cWeathervane\u201d'),
    ('"alignment"', '\u201calignment\u201d'),
    ('"acceleration"', '\u201cacceleration\u201d'),
    ('"spin"', '\u201cspin\u201d'),
    ('"spring"', '\u201cspring\u201d'),
    ('"active damping"', '\u201cactive damping\u201d'),
]
for old, new in replacements:
    content = content.replace(old, new)
open(fname, 'w', encoding='utf-8').write(content)
print('fixed', fname)
