# -*- coding: utf-8 -*-
import txutil

pages = [
    'architecture/codegen',
    'architecture/config-params',
    'architecture/naming',
    'architecture/numerics',
    'architecture/schedopt',
    'architecture/statemach',
    'architecture/statevar',
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
