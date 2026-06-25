# -*- coding: utf-8 -*-
"""Fix remaining curly quote / apostrophe mismatches in schedopt - round 4."""
import txutil

rel = "architecture/schedopt"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "The linker can only relocate addresses; it can\u2019t change the sequence of instructions (some newer compilers can, but we don\u2019t want to depend on that)":
        "链接器只能重新定位地址；它无法更改指令序列（一些较新的编译器可以做到，但我们不想依赖于此）",
    "\u201cLocal\u201d function definitions":
        "\u201c本地\u201d函数定义",
    "\u201cShared\u201d function definitions":
        "\u201c共享\u201d函数定义",
    "in a .h file causes transitive dependencies. See the following table: (the \u2192 symbol means \u201cdepends on\u201d)":
        "放在 .h 文件中会导致传递依赖。请参见下表：（\u2192 符号表示\u201c依赖于\u201d）",
    "The function cannot be put into a precompiled library, which means, for example, that if you are creating a motor control library, you\u2019ll need to include the source code for these functions.":
        "该函数不能放入预编译库中，这意味着，例如，如果您正在创建电机控制库，则需要包含这些函数的源代码。",
    "More code space is typically needed, in order to support multiple call sites. For example, don\u2019t do this:":
        "通常需要更多的代码空间，以支持多个调用点。例如，不要这样做：",
    "Inlined functions \u201close their identity\u201d":
        "内联函数\u201c失去其身份\u201d",
    "Debugging may be harder (you don\u2019t see an entry in the call stack, and breakpoints may not work)":
        "调试可能更困难（您看不到调用栈中的条目，断点可能不起作用）",
    "They don\u2019t appear separately in the linker map":
        "它们不会单独出现在链接器映射中",
    "Language lawyers will say you can\u2019t depend on it":
        "语言专家会说您不能依赖它",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)
