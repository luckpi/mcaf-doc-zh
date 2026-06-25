# -*- coding: utf-8 -*-
import txutil

rel = "architecture/numerics"
title_zh = "3.8. 数值算法处理"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "Treatment of Numerical Algorithms": "数值算法处理",
    "Numerical Representation": "数值表示",
    "Normalization Factors": "归一化因子",
    "Constants in Code": "代码中的常量",
    "State Machine": "状态机",
    "Components": "组件",
    # TOC entries
    "3.8. Treatment of Numerical Algorithms": "3.8. 数值算法处理",
    "3.8.1. Numerical Representation": "3.8.1. 数值表示",
    "3.8.1.1. Normalization Factors": "3.8.1.1. 归一化因子",
    "3.8.2. Constants in Code": "3.8.2. 代码中的常量",
    # Numerical Representation
    "The MCAF at present utilizes only fixed-point (and not floating-point) computation. The majority of state variables and parameters are represented as Q15 fixed-point stored in a signed 16-bit number (":
        "MCAF 目前仅使用定点（而非浮点）计算。大多数状态变量和参数表示为 Q15 定点数，存储在有符号 16 位整数（",
    ")": "）",
    ", with a handful of 32-bit values (usually in integrators or filter state) and a few unsigned Q15 16-bit values. Some gains use other scaling factors like Q11 or variable shifts, where appropriate.":
        "）中，还有少量 32 位值（通常在积分器或滤波器状态中）和少数无符号 Q15 16 位值。某些增益在适当时使用其他缩放因子（如 Q11 或可变移位）。",
    "The primary normalization factors used since MCAF R3 are shown below.":
        "自 MCAF R3 起使用的主要归一化因子如下所示。",
    # table headers
    "quantity": "量",
    "factor (in general)": "因子（通用）",
    "factor used with MCLV-2": "MCLV-2 使用的因子",
    "factor used with MCHV (MCHV-2 and MCHV-3)": "MCHV（MCHV-2 和 MCHV-3）使用的因子",
    # table cells
    "Voltage": "电压",
    "Maximum": "最大",
    "input for DC link": "直流母线输入",
    "Current": "电流",
    "Twice the maximum phase current measurement, which allows room for gain calibration and avoids overflow in Park and Clarke transforms, at the cost of reduced resolution on the low end.":
        "最大相电流测量值的两倍，这为增益校准留出了空间，并避免了 Park 和 Clarke 变换中的溢出，代价是低端分辨率降低。",
    "Velocity": "速度",
    "As of MCAF R6, the": "自 MCAF R6 起，",
    "full-scale velocity": "满量程速度",
    "normalization factor is set on the Customize page of motorBench":
        "归一化因子在 motorBench",
    "Development Suite.": "Development Suite 的 Customize 页面上设置。",
    # Constants in Code
    'Constants found in code are sometimes considered "magic numbers" if the reason for choosing their value is unclear. We try to avoid this situation in the Motor Control Application Framework.':
        '如果选择常量值的原因不明确，代码中的常量有时被认为是"魔数"。我们尽量避免在电机控制应用框架中出现这种情况。',
    "Constants used in the Motor Control Application Framework generally fall into one of five categories.":
        "电机控制应用框架中使用的常量通常分为五类之一。",
    "Automatically calculated values": "自动计算的值",
    ": In the": "：在",
    "directory, in header files or in C run-time initialization functions — these are calculated by motorBench":
        "目录中，在头文件或 C 运行时初始化函数中——这些值由 motorBench",
    "Development Suite during the autotuning and code generation steps. We do not recommend changing these values manually. Where they are fixed-point integer constants, a comment generally accompanies them indicating the floating-point equivalent and the corresponding engineering value, along with quantization accuracy, for example:":
        "Development Suite 在自动整定和代码生成步骤中计算。我们不建议手动更改这些值。对于定点整数常量，通常会附带注释，指示浮点等效值和相应的工程值，以及量化精度，例如：",
    "Among many other tasks, we are working on improving the documentation within our code to clarify how these constants are calculated, or at least what factors they depend on. In some cases the calculations are proprietary formulas within motorBench":
        "在许多其他任务中，我们正在努力改进代码中的文档，以阐明这些常量是如何计算的，或者至少它们依赖于哪些因子。在某些情况下，这些计算是 motorBench",
    "Part of the Hardware Abstraction Layer": "硬件抽象层的一部分",
    "directory. These are intended to be consistent with, and eventually replaced by, automatically-generated output from MCC.":
        "目录中。这些旨在与 MCC 自动生成的输出保持一致，并最终被其替换。",
    '"Obvious" values in the C source files': '"显而易见"的值（位于 C 源文件中）',
    "outside the": "在",
    "directory, including some examples shown below. In these cases, hiding them behind an abstracted symbolic constant obscures rather than clarifies their usage. If you see an example where they seem inappropriate, please bring them to our attention, and we will consider alternatives.":
        "目录之外的 C 源文件中，包括下面的一些示例。在这些情况下，将它们隐藏在抽象的符号常量后面反而会模糊而非澄清其用法。如果您发现某个示例中它们似乎不合适，请告知我们，我们将考虑替代方案。",
    "+1 or -1 as a sign/direction value": "+1 或 -1 作为符号/方向值",
    "maximum representative values like 0xFFFF or 0x7FFF": "最大表示值，如 0xFFFF 或 0x7FFF",
    "shift counts, e.g.": "移位计数，例如",
    "when converting from": "当从",
    "to": "转换为",
    ", or": "，或",
    "where multiplying a QN fixed-point number, and the value of N is clarified in code comments":
        "其中乘以 QN 定点数时，N 的值在代码注释中说明",
    "array indices for unrolled loops": "循环展开的数组索引",
    '(used to output a "short pulse" as mentioned in an accompanying comment)':
        '（用于输出"短脉冲"，如随附注释中所述）',
    "Hand-calculated constants with accompanying comment explaining how they were derived":
        "手工计算的常量，附带注释解释其推导过程",
    "— these are uncommon; if any are unclear, please bring these to our attention.":
        "——这些不常见；如果有任何不明确之处，请告知我们。",
    "Legacy code constants": "遗留代码常量",
    "— if for some reason you notice a constant in code that does not fall into one of the above categories, it is probably an oversight, in which case please bring it to our attention.":
        "——如果由于某种原因您注意到代码中的常量不属于上述任何类别，那可能是疏忽，在这种情况下请告知我们。",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
