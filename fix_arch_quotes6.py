# -*- coding: utf-8 -*-
"""Fix remaining untranslated nodes in schedopt - round 6."""
import txutil

rel = "architecture/schedopt"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "The linker can only relocate addresses; it can\u2019t change the sequence of instructions (some newer compiler toolchains have link-time / \u201cwhole program\u201d optimization which get around this restriction \u2014 if you have such a toolchain you should probably rethink your use of":
        "链接器只能重新定位地址；它无法更改指令序列（一些较新的编译器工具链具有链接时/\u201c全程序\u201d优化功能可以绕过此限制——如果您有这样的工具链，您可能应该重新考虑对",
    "The function cannot be put into a precompiled library, which means, for example, that if you are creating a library and you have access to the premium version of XC16, you can\u2019t compile it with":
        "该函数不能放入预编译库中，这意味着，例如，如果您正在创建一个库并且可以访问 XC16 的高级版本，您无法用",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)
