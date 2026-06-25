# -*- coding: utf-8 -*-
import txutil

rel = "architecture/config-params"
title_zh = "3.5. 配置参数"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "Configuration Parameters": "配置参数",
    "Classic Application Notes": "经典应用笔记",
    "Motor Control Application Framework": "电机控制应用框架",
    "Code Generation": "代码生成",
    "Scheduling and Optimization": "调度与优化",
    # TOC entries
    "3.5. Configuration Parameters": "3.5. 配置参数",
    "3.5.1. Classic Application Notes": "3.5.1. 经典应用笔记",
    "3.5.2. Motor Control Application Framework": "3.5.2. 电机控制应用框架",
    # intro
    "There are many configurable parameters in the MCAF:": "MCAF 中有许多可配置参数：",
    "control gains": "控制增益",
    "time delays": "时间延迟",
    "ramp rates": "斜坡速率",
    "filter time constants": "滤波器时间常数",
    "full-scale values (current, voltage, duty cycle, etc.)": "满量程值（电流、电压、占空比等）",
    "limits (current, voltage, duty cycle, etc.)": "限值（电流、电压、占空比等）",
    "and so on. The velocity control loop is a good example. Algebraically it looks like this:":
        "等等。速度控制环就是一个很好的例子。从代数上看，它如下所示：",
    "The question becomes: how can we manage parameters such as": "问题变成了：我们如何管理诸如",
    "and": "和",
    "for each control loop and take advantage of fixed-point mathematics?":
        "这样的参数，并利用定点数学？",
    # Classic Application Notes
    "Microchip's classic application notes, such as AN1292 and AN1078 used calculations expressed via the C preprocessor. For example:":
        "Microchip 的经典应用笔记（如 AN1292 和 AN1078）使用通过 C 预处理器表达的计算。例如：",
    "Listing 3.7": "代码清单 3.7",
    "from AN1078": "来自 AN1078",
    "Advantages of this approach are that the formula used to derive each value is visible.":
        "这种方法的优点是用于推导每个值的公式是可见的。",
    "Disadvantages of this approach revolve around the way the C preprocessor works. The":
        "这种方法的缺点在于 C 预处理器的工作方式。",
    "approach is purely a text substitution, and the preprocessor does not actually do any calculations; the compiler optimizes by computing any calculations it can do at compile-time (also known as":
        "方法纯粹是文本替换，预处理器实际上并不执行任何计算；编译器通过在编译时计算它能完成的任何计算来优化（也称为",
    "constant folding": "常量折叠",
    ") but does not see the original code prior to preprocessing. Specific disadvantages are":
        "），但看不到预处理之前的原始代码。具体的缺点包括",
    "Potential for cryptic or invisible errors due to overflow, type mismatch, or unsafe calculations (lack of parentheses to control precedence, no checking of values out of range). For example:":
        "由于溢出、类型不匹配或不安全的计算（缺少括号来控制优先级、不检查值是否超出范围），可能导致难以理解或不可见的错误。例如：",
    "This code has an error; the substituted code looks like": "此代码有错误；替换后的代码如下所示",
    "which is missing parentheses around": "缺少",
    "No visibility of the intermediate or final computed values": "无法看到中间或最终的计算值",
    "No debugging of preprocessor calculations is possible": "无法调试预处理器计算",
    'Can cover "built-in" function calls (standard math) but not more complicated calculations (e.g. requiring loops, advanced math functions like':
        '可以覆盖"内置"函数调用（标准数学），但无法处理更复杂的计算（例如需要循环、高级数学函数如',
    "or Bessel functions, or other numerical analysis)": "或贝塞尔函数，或其他数值分析）",
    # Motor Control Application Framework
    "The MCAF approach takes advantage of the": "MCAF 方法利用了",
    "code generation": "代码生成",
    "features in motorBench": "功能，这些功能在 motorBench",
    "Development Suite. These features use a templating engine; in the MCAF firmware package are files containing parameterized code with placeholder expressions:":
        "Development Suite 中。这些功能使用模板引擎；在 MCAF 固件包中，包含带有占位符表达式的参数化代码文件：",
    "Listing 3.8": "代码清单 3.8",
    "which will get values substituted into the": "其中",
    "blocks and end up looking like": "块中的值将被替换，最终如下所示",
    "Listing 3.9": "代码清单 3.9",
    "This provides a couple of advantages:": "这提供了几个优点：",
    "Calculations can be made at code generation time using mechanisms that can be debugged":
        "可以在代码生成时使用可调试的机制进行计算",
    "Intermediate and final results can be made visible": "中间和最终结果可以可视化",
    "Reporting of floating-point / engineering equivalents can be added": "可以添加浮点/工程等效值的报告",
    "Almost any computable equation can be used": "几乎可以使用任何可计算的方程",
    "The sample code above is an example of floating-point parameters; since we tend to use fixed-point calculations, the firmware package templates could look more like":
        "上面的示例代码是浮点参数的示例；由于我们倾向于使用定点计算，固件包模板可能更像",
    "Listing 3.10": "代码清单 3.10",
    "using templating macros that produce both integer counts and an equivalent floating-point value in a comment:":
        "使用模板宏，在注释中同时生成整数值和等效的浮点值：",
    "Listing 3.11": "代码清单 3.11",
    "Then we can apply the defined constants in code:": "然后我们可以在代码中使用定义的常量：",
    "Listing 3.12": "代码清单 3.12",
    "This approach of": "这种",
    "compile-time separation": "编译时分离",
    "(splitting configurable parameters into a definition in a template-generated C header file, and usage in one or more C source files) is essentially the one used in the MCAF. In general it has some important characteristics:":
        "方法（将可配置参数拆分为模板生成的 C 头文件中的定义，以及在一个或多个 C 源文件中的使用）本质上是 MCAF 中使用的方法。一般来说，它具有一些重要特征：",
    "Good for optimization — the compiler sees the constant value, might be able to speed up the calculation.":
        "有利于优化——编译器能看到常量值，可能能够加速计算。",
    "Bad for modularity — What if we have software driving two motors with different gains? Then we need":
        "不利于模块化——如果我们有驱动两个不同增益的电机的软件怎么办？那么我们需要",
    "and somehow in our C code we need to determine when to apply each.":
        "，并且在 C 代码中我们需要以某种方式确定何时使用哪个。",
    "Bad for development — We can't use run-time diagnostic tools to try out different gains.":
        "不利于开发——我们无法使用运行时诊断工具来尝试不同的增益。",
    "Definition and point of use are separated — this is an inevitable casualty of modular design.":
        "定义和使用点分离——这是模块化设计的必然代价。",
    "We are addressing some of these concerns by taking a slightly different approach, using":
        "我们通过采用稍微不同的方法来解决其中一些问题，使用",
    "run-time separation": "运行时分离",
    ", storing configuration parameters in state variables:":
        "，将配置参数存储在状态变量中：",
    "Listing 3.13": "代码清单 3.13",
    "Listing 3.14": "代码清单 3.14",
    "(dynamically generated)": "(动态生成)",
    "This allows a code architecture so that": "这允许一种代码架构，使得",
    "more than one motor can be used with different gains for each":
        "可以使用多个电机，每个电机有不同的增益",
    "variable shift counts can be used, to support a dynamic range that is optimized for each motor.":
        "可以使用可变的移位计数，以支持为每个电机优化的动态范围。",
    "parameters can be changed at run-time during development and testing":
        "参数可以在开发和测试期间在运行时更改",
    "The run-time cost is slightly higher than in the case where each line of C code uses a constant fixed at compile-time, rather than a run-time parameter, but is a better approach for the MCAF.":
        "运行时开销略高于每行 C 代码使用编译时固定常量而非运行时参数的情况，但对 MCAF 来说是更好的方法。",
    "As of MCAF version 1.0, there is a mix of compile-time and run-time separation; we are migrating to use purely run-time separation in future versions. All generated code relating to configurable parameters is located in the":
        "截至 MCAF 版本 1.0，编译时分离和运行时分离混合使用；我们正在迁移到在将来版本中纯粹使用运行时分离。所有与可配置参数相关的生成代码位于",
    "files.": "文件中。",
    'One drawback of the code generation approach is that it is not very easy to be "transparent"; that is, to show equations of where the calculated values came from. We are working to address this issue in the future.':
        '代码生成方法的一个缺点是不太容易做到"透明"；也就是说，不容易展示计算值的来源方程。我们正在努力在未来解决这个问题。',
    "Sample generated parameters of the MCAF:": "MCAF 的示例生成参数：",
    "Listing 3.15": "代码清单 3.15",
    "Listing 3.16": "代码清单 3.16",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
