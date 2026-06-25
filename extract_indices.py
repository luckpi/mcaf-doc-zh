# -*- coding: utf-8 -*-
"""Extract text nodes from all index/overview pages for batch translation."""
import txutil
import os

pages = [
    'algorithms/index', 'algorithms/flux_control/index',
    'components/index', 'implementation/index',
    'implementation/custom-board-support/index',
    'appendix/index',
    'architecture/overview',
    'implementation/custom-board-support/overview',
]

for rel in pages:
    soup, path = txutil.load(rel + '.zh.html')
    nodes = txutil.collect_nodes(soup)
    seen = set()
    out = []
    for i, s in enumerate(nodes):
        norm = txutil._WS.sub(' ', str(s)).strip()
        if len(norm) < 2 or norm in seen:
            continue
        seen.add(norm)
        out.append('[%d] %s' % (i, norm))
    fname = rel.replace('/', '_') + '_nodes.txt'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('\n'.join(out))
    print(rel, len(out))
