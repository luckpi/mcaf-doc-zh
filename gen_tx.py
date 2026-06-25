# -*- coding: utf-8 -*-
"""Helper to generate translation scripts without quote conflicts.
Usage: python -X utf8 gen_tx.py <rel> <title_zh> <pairs_file>
pairs_file format: one pair per line, tab-separated: english<TAB>chinese
Lines starting with # are comments.
"""
import sys
import os

rel = sys.argv[1]
title_zh = sys.argv[2]
pairs_file = sys.argv[3]

pairs = []
with open(pairs_file, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if not line or line.startswith('#'):
            continue
        parts = line.split('\t', 1)
        if len(parts) == 2:
            pairs.append((parts[0], parts[1]))

# Generate the script content
lines = []
lines.append('# -*- coding: utf-8 -*-')
lines.append('import txutil')
lines.append('')
lines.append('rel = %r' % rel)
lines.append('title_zh = %r' % title_zh)
lines.append('')
lines.append('m = {')
for en, zh in pairs:
    lines.append('    %r: %r,' % (en, zh))
lines.append('}')
lines.append('')
lines.append('path = txutil.translate_dict_page(rel, title_zh, m)')
lines.append('print("translated", path)')

# Write the script
script_name = 'tx_algo_' + rel.replace('/', '_').replace('algorithms_', '') + '.py'
with open(script_name, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('generated', script_name, 'with', len(pairs), 'pairs')
