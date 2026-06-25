# -*- coding: utf-8 -*-
"""Fix remaining untranslated nodes due to curly quote / apostrophe mismatches."""
import txutil

# Fix config-params
rel = "architecture/config-params"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "Microchip\u2019s classic application notes, such as AN1292 and AN1078 used calculations expressed via the C preprocessor. For example:":
        "Microchip 的经典应用笔记（如 AN1292 和 AN1078）使用通过 C 预处理器表达的计算。例如：",
    "Can cover \u201cbuilt-in\u201d function calls (standard math) but not more complicated calculations (e.g. requiring loops, advanced math functions like":
        "可以覆盖\u201c内置\u201d函数调用（标准数学），但无法处理更复杂的计算（例如需要循环、高级数学函数如",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)

# Fix numerics
rel = "architecture/numerics"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "), with a handful of 32-bit values (usually in integrators or filter state) and a few unsigned Q15 16-bit values. Some gains use other scaling factors like Q11 or variable shifts, where appropriate.":
        "），还有少量 32 位值（通常在积分器或滤波器状态中）和少数无符号 Q15 16 位值。某些增益在适当时使用其他缩放因子（如 Q11 或可变移位）。",
    "Constants found in code are sometimes considered \u201cmagic numbers\u201d if the reason for choosing their value is unclear. We try to avoid this situation in the Motor Control Application Framework.":
        "如果选择常量值的原因不明确，代码中的常量有时被认为是\u201c魔数\u201d。我们尽量避免在电机控制应用框架中出现这种情况。",
    "\u201cObvious\u201d values in the C source files":
        "\u201c显而易见\u201d的值（位于 C 源文件中）",
    "(used to output a \u201cshort pulse\u201d as mentioned in an accompanying comment)":
        "（用于输出\u201c短脉冲\u201d，如随附注释中所述）",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)

# Fix naming
rel = "architecture/naming"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "Prefixes are not used in global variables, because the number of global variables is minimal. In addition, their names may be changed by customers without impact to the MCAF, since the framework\u2019s modules do not access them directly.":
        "全局变量不使用前缀，因为全局变量的数量很少。此外，客户可以更改它们的名称而不会影响 MCAF，因为框架的模块不直接访问它们。",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)

# Fix schedopt
rel = "architecture/schedopt"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "The term \u201ccooperative scheduling\u201d means that each task runs to completion without blocking, before the next one executes; there is not an operating system which preemptively switches threads of execution before a task has completed.":
        "\u201c协作调度\u201d一词意味着每个任务在下一次执行之前运行至完成而不阻塞；不存在一个操作系统在任务完成之前抢占式地切换执行线程。",
    ", where the interaction between main and control ISR threads is simple and not prone to concurrency errors (main thread sets count to zero and does not read the count; control ISR increments count and isn\u2019t interrupted by the main thread)":
        "，其中主线程与控制 ISR 线程之间的交互简单且不易出现并发错误（主线程将计数置零且不读取计数；控制 ISR 递增计数且不被主线程中断）",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)

# Fix statevar
rel = "architecture/statevar"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "Note that the module functions with this approach do not \u201cown\u201d their data. They do not allocate any global variables, do not access any global variables, and do not maintain any permanent pointers to external data. Instead, data is passed in as an argument. The module functions will operate on any data passed in. They don\u2019t care whether they operate on data from one motor or another, or whether it\u2019s mock data from a testing program or real data from an":
        "请注意，采用此方法的模块函数不\u201c拥有\u201d其数据。它们不分配任何全局变量，不访问任何全局变量，也不维护任何指向外部数据的永久指针。相反，数据作为参数传入。模块函数将对任何传入的数据进行操作。它们不关心操作的是来自一个电机还是另一个电机的数据，也不关心是来自测试程序的模拟数据还是来自",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)
