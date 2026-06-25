# -*- coding: utf-8 -*-
import txutil

pages = [
    "algorithms/startup",
    "algorithms/stopping",
    "algorithms/estimator-interface",
    "algorithms/estimators",
    "algorithms/atpll",
    "algorithms/pll",
    "algorithms/qei",
    "algorithms/qei_sync/align",
    "algorithms/qei_sync/align-sweep",
    "algorithms/qei_sync/common",
    "algorithms/qei_sync/pullout",
    "algorithms/smo",
    "algorithms/zsmt",
    "algorithms/flux_control/flux_weakening",
    "algorithms/flux_control/flux_weakening_mtpa_integration",
    "algorithms/flux_control/fw_types/fw_eq_based",
    "algorithms/flux_control/mtpa",
    "algorithms/current-limit",
    "algorithms/dead-time-comp",
    "algorithms/dynlimit-simple",
    "algorithms/voltage-control",
    "algorithms/temperature-measure",
]

for rel in pages:
    try:
        soup, path = txutil.load(rel + '.zh.html')
    except Exception as e:
        print("ERR", rel, e)
        continue
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
