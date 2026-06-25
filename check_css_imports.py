# -*- coding: utf-8 -*-
import os, re
css_dir = 'site/_static'
for f in os.listdir(css_dir):
    if f.endswith('.css'):
        content = open(os.path.join(css_dir, f), encoding='utf-8').read()
        imports = re.findall(r'@import\s+url\(["\']?(.*?)["\']?\)', content)
        if imports:
            print(f'{f} imports: {imports}')
            for imp in imports:
                if not imp.startswith('http'):
                    imp_path = os.path.join(css_dir, imp)
                    exists = os.path.exists(imp_path)
                    print(f'  -> {imp}: {"EXISTS" if exists else "MISSING!"}')
