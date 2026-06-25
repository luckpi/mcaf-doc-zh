# -*- coding: utf-8 -*-
import txutil

rel = "components/miscellaneous"
title_zh = "4.11. 杂项"

m = {
    "Components": "组件",
    "Miscellaneous": "杂项",
    "4.11. Miscellaneous": "4.11. 杂项",
    "A few other modules don\u2019t have anything directly to do with the behavior of the MCAF but contribute to areas like math routines.": "其他一些模块与 MCAF 的行为没有直接关系，但对数学例程等领域有所贡献。",
    "Implementation Notes": "实现说明",
    "4.11.1. Implementation Notes": "4.11.1. 实现说明",
    "Modules": "模块",
    "4.11.1.1. Modules": "4.11.1.1. 模块",
    "Module": "模块",
    "Files": "文件",
    "Description": "描述",
    "Comments": "说明",
    "C-callable CORDIC implementation of arctangent,": "C 可调用的反正切 CORDIC 实现，",
    "This contains an assembly implementation of a Q15": "这包含 Q15",
    "based arctangent, and may be abandoned or replaced by a C implementation.": "的汇编实现，可能被放弃或替换为 C 实现。",
    "First order low-pass and high-pass filters": "一阶低通和高通滤波器",
    "Utility math routines": "实用数学例程",
    "This contains an assembly implementation of a Q15 fixed-point square root": "这包含 Q15 定点平方根的汇编实现",
    "which is likely to be replaced by one of two alternatives:": "可能被以下两种替代方案之一替换：",
    "not using a square root at all (at present it is involved in saturation-handling logic in the vector current loop)": "完全不使用平方根（目前它涉及矢量电流环中的饱和处理逻辑）",
    "using the": "使用",
    "function found in the standard": "函数，该函数位于标准",
    "library in the": "库的",
    "Utility routines for timing": "时序实用例程",
    "C typedef indirections indicating engineering unit types (voltage, current, etc.)": "指示工程单位类型（电压、电流等）的 C typedef 间接定义",
    "Miscellaneous utility and math functions": "杂项实用和数学函数",
    "Contains numerous inline utility functions with the prefix": "包含大量带有前缀",
    "for things like squaring of Q15 numbers with a fixup for -32768, limiting a value between a minimum and maximum, etc.": "的内联实用函数，用于 Q15 数的平方（对 -32768 的修正）、将值限制在最小值和最大值之间等。",
    "Essentially all small functions that had potential for reuse were refactored and placed in this module.": "基本上所有有复用潜力的小函数都被重构并放置在此模块中。",
    "Motor parameters (including R, L, Ke, J, etc.)": "电机参数（包括 R、L、Ke、J 等）",
    "Operating parameters such as speed ranges and slew rates": "运行参数，如速度范围和压摆率",
    "Various timing parameters": "各种时序参数",
    "Motion Control API (MCAPI)": "运动控制 API（MCAPI）",
    "Detailed Algorithm Notes": "详细算法说明",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
