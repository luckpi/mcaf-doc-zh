# -*- coding: utf-8 -*-
import txutil

rel = "architecture/index"
title_zh = "3. 架构"

m = {
    "Architecture": "架构",
    "Getting Started": "快速入门",
    "Architectural Overview": "架构概览",
    "3.1. Architectural Overview": "3.1. 架构概览",
    "3.1.1. How to Spin a Motor (In Brief)": "3.1.1. 如何驱动电机（简述）",
    "3.1.2. Modules and Components": "3.1.2. 模块与组件",
    "3.1.3. Software Design Principles for Modular and Maintainable Code": "3.1.3. 面向模块化与可维护代码的软件设计原则",
    "3.2. Naming Conventions": "3.2. 命名约定",
    "3.2.1. Additional Naming Guidelines": "3.2.1. 补充命名指南",
    "3.3. State management": "3.3. 状态管理",
    "3.3.1. Miscellaneous Guidelines": "3.3.1. 其他指南",
    "3.4. Code Generation": "3.4. 代码生成",
    "3.4.1. Why Code Generation?": "3.4.1. 为什么使用代码生成？",
    "3.4.2. How Does Code Generation Work?": "3.4.2. 代码生成是如何工作的？",
    "3.5. Configuration Parameters": "3.5. 配置参数",
    "3.5.1. Classic Application Notes": "3.5.1. 经典应用笔记",
    "3.5.2. Motor Control Application Framework": "3.5.2. 电机控制应用框架",
    "3.6. Scheduling and Optimization": "3.6. 调度与优化",
    "3.6.1. Scheduling": "3.6.1. 调度",
    "3.6.2. Optimization": "3.6.2. 优化",
    "3.7. State Machine": "3.7. 状态机",
    "3.7.1. States": "3.7.1. 状态",
    "3.8. Treatment of Numerical Algorithms": "3.8. 数值算法处理",
    "3.8.1. Numerical Representation": "3.8.1. 数值表示",
    "3.8.2. Constants in Code": "3.8.2. 代码中的常量",
    "© Copyright 2017-2026, Microchip Technology, Inc..": "© 版权所有 2017-2026，Microchip Technology, Inc..",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
