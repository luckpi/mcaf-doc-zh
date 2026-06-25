# -*- coding: utf-8 -*-
import sys

fname = sys.argv[1]
content = open(fname, 'r', encoding='utf-8').read()
# Fix Chinese translations that use ASCII double quotes for emphasis
# Replace patterns like: ""风向标" -> "\u201c风向标\u201d
# These are in the value (Chinese) side of the dict
fixes = [
    ('""风向标"', '\u201c风向标\u201d'),
    ('""对齐"', '\u201c对齐\u201d'),
    ('""加速"', '\u201c加速\u201d'),
    ('""稳速"', '\u201c稳速\u201d'),
    ('""弹簧"', '\u201c弹簧\u201d'),
    ('""有源阻尼"', '\u201c有源阻尼\u201d'),
]
for old, new in fixes:
    content = content.replace(old, new)
open(fname, 'w', encoding='utf-8').write(content)
print('fixed2', fname)
