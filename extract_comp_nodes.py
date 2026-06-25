# -*- coding: utf-8 -*-
import txutil

pages = [
    'components/main',
    'components/adc',
    'components/statemach',
    'components/foc',
    'components/testharness',
    'components/supervisory',
    'components/ext-interface',
    'components/diagnostics',
    'components/hal',
    'components/mcapi',
    'components/miscellaneous',
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
