# -*- coding: utf-8 -*-
"""Fix remaining curly quote / apostrophe mismatches - round 3."""
import txutil

# Fix schedopt
rel = "architecture/schedopt"
soup, path = txutil.load(rel + '.zh.html')
m = {
    'Development Suite for the customizable parameter \u201cUi service period\u201d. This function does not have a hard real-time requirement.':
        ' Development Suite 的 Customize 页面中为可定制参数\u201cUi service period\u201d输入。此函数没有硬实时要求。',
    "The compiler can\u2019t see the source of other compilation units":
        "编译器无法看到其他编译单元的源代码",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)
