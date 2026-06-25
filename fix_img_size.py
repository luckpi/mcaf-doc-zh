# -*- coding: utf-8 -*-
"""Fix oversized image in architecture/overview pages."""
import re

for fname in ['site/architecture/overview.html', 'site/architecture/overview.zh.html']:
    content = open(fname, encoding='utf-8').read()
    # Remove height="4576" and replace width="6351" with width="100%"
    new_content = content
    # Handle both orderings: height before width, or width before height
    new_content = re.sub(r'height="4576"\s+width="6351"', 'width="100%"', new_content)
    new_content = re.sub(r'width="6351"\s+height="4576"', 'width="100%"', new_content)
    # Also handle if they're not adjacent
    new_content = new_content.replace('height="4576"', '')
    new_content = new_content.replace('width="6351"', 'width="100%"')
    # Clean up any double spaces left behind
    new_content = re.sub(r'  +', ' ', new_content)
    if new_content != content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Fixed: {fname}')
    else:
        print(f'No change: {fname}')

# Verify
for fname in ['site/architecture/overview.html', 'site/architecture/overview.zh.html']:
    content = open(fname, encoding='utf-8').read()
    m = re.search(r'<img[^>]*app-framework-components[^>]*>', content)
    if m:
        print(f'  {fname}: {m.group(0)}')
