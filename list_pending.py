# -*- coding: utf-8 -*-
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")
done = set()
# already translated pages (by .zh.html existence and known tx scripts)
translated = {
    'index', 'introduction', 'getting-started',
    'architecture/index',
    'algorithms/foc/index', 'algorithms/foc/overview', 'algorithms/foc/fundamentals',
    'algorithms/foc/current_measure', 'algorithms/foc/overmodulation',
    'algorithms/foc/dclink-comp', 'algorithms/foc/tuning', 'algorithms/foc/comparison-6step',
}
pending = []
for dp, _, fs in os.walk(ROOT):
    for f in fs:
        if f.endswith('.html') and not f.endswith('.zh.html') and f != 'genindex.html' and f != 'search.html':
            rel = os.path.relpath(os.path.join(dp, f), ROOT).replace('\\', '/').replace('.html', '')
            if rel in translated:
                continue
            pending.append(rel)
pending.sort()
with open('pending.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(pending))
print('pending', len(pending))
for p in pending:
    print(p)
