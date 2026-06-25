# -*- coding: utf-8 -*-
import txutil

pages = [
    'implementation/source-tree-structure',
    'implementation/codegen',
    'implementation/custom-board-support/configuration',
    'implementation/custom-board-support/custom_board_definitions',
    'implementation/custom-board-support/verification',
    'implementation/integration',
    'implementation/resource-usage',
    'implementation/sampling-rate',
    'implementation/ui-customization',
    'dataflow-diagram/dataflow-diagrams',
    'appendix/glossary',
    'appendix/error_codes',
    'appendix/mclv2',
    'appendix/otherdocs',
    'appendix/rev_history',
    'faq',
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
