# -*- coding: utf-8 -*-
"""Fix remaining curly quote / apostrophe mismatches - round 2."""
import txutil

# Fix config-params
rel = "architecture/config-params"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "Bad for development \u2014 We can\u2019t use run-time diagnostic tools to try out different gains.":
        "不利于开发——我们无法使用运行时诊断工具来尝试不同的增益。",
    "One drawback of the code generation approach is that it is not very easy to be \u201ctransparent\u201d; that is, to show equations of where the calculated values came from. We are working to address this issue in the future.":
        "代码生成方法的一个缺点是不太容易做到\u201c透明\u201d；也就是说，不容易展示计算值的来源方程。我们正在努力在未来解决这个问题。",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)

# Fix schedopt
rel = "architecture/schedopt"
soup, path = txutil.load(rel + '.zh.html')
m = {
    "register setup to comply with function call conventions (":
        "符合函数调用约定的寄存器设置（",
    "Good candidates for inlining are functions that are less than \u224870 cycles, whether that is the total time, or the time excluding 2nd-level calls, as in \u201cadapter\u201d functions like the one shown below:":
        "内联的良好候选者是少于约 70 个周期的函数，无论是总时间，还是排除二级调用的时间，如以下所示的\u201c适配器\u201d函数：",
    "Desperation can lead to poor decision-making, so don\u2019t do it lightly.":
        "迫切感可能导致糟糕的决策，所以不要轻率行事。",
    "If you ignore Rule #1, don\u2019t inline blindly.":
        "如果您忽略规则 #1，不要盲目内联。",
}
txutil.apply_dict(txutil.body(soup), m)
txutil.save(path, soup)
print("fixed", rel)
