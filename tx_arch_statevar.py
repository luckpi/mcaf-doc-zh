# -*- coding: utf-8 -*-
import txutil

rel = "architecture/statevar"
title_zh = "3.3. 状态管理"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "State management": "状态管理",
    "Miscellaneous Guidelines": "杂项指南",
    "Naming Conventions": "命名约定",
    "Code Generation": "代码生成",
    # TOC entries
    "3.3. State management": "3.3. 状态管理",
    "3.3.1. Miscellaneous Guidelines": "3.3.1. 杂项指南",
    # intro
    "Motor control algorithms require maintenance of numerous state variables, for things like control loops and estimators (integrator and filter state), state machines (the state of the state machine), schedulers (countdown timers), configuration parameters, and so on.":
        "电机控制算法需要维护大量状态变量，用于控制环和估计器（积分器和滤波器状态）、状态机（状态机的状态）、调度器（倒计时定时器）、配置参数等。",
    "The motor control application framework defines several data structures for managing this state data. The two top-level data structures are":
        "电机控制应用框架定义了若干数据结构来管理这些状态数据。两个顶层数据结构是",
    "and": "和",
    ", used for storing per-system and per-motor state variables, respectively.":
        "，分别用于存储系统级和电机级状态变量。",
    "We used an approach consisting of three major aspects:":
        "我们使用了一种包含三个主要方面的方法：",
    "Structure": "结构",
    "— how are state variables organized?": "——状态变量如何组织？",
    "Group data in appropriate C structures": "将数据分组到适当的 C 结构体中",
    "Follow the Goldilocks principle: not too big or too small": "遵循 Goldilocks 原则：不要太大也不要太小",
    "Allocation": "分配",
    "— how are state variables allocated?": "——状态变量如何分配？",
    "Minimize the number of independent global variables": "最小化独立全局变量的数量",
    "Put them in easy-to-find places (no easter egg hunts)": "将它们放在易于查找的位置（不需要找彩蛋）",
    "Access": "访问",
    "— how are state variables accessed by functions?": "——函数如何访问状态变量？",
    "Functions (with limited exceptions, such as": "函数（有少数例外，如",
    ", ISRs and the HAL) do not directly access global variables":
        "、ISR 和 HAL）不直接访问全局变量",
    "Primitive types are passed in directly as arguments": "基本类型直接作为参数传递",
    "Structures are passed in via a pointer or": "结构体通过指针或",
    "pointer, and the smallest applicable structure is used.":
        "指针传递，并使用最小的适用结构体。",
    "Our goal is to follow the principle of least knowledge in the design of our system state; the top-level module functions get access to the entire data structure, whereas lower-level functions get access to appropriate pieces.":
        "我们的目标是在系统状态设计中遵循最小知识原则；顶层模块函数可以访问整个数据结构，而底层函数只能访问适当的部分。",
    "A simplified example may help explain this.":
        "一个简化的示例可能有助于解释这一点。",
    # code example explanation
    "The top-level module functions look like the following. Note that the function":
        "顶层模块函数如下所示。注意，函数",
    "does have access to the entire": "确实可以访问整个",
    "structure, but it calls other functions, such as":
        "结构体，但它调用的其他函数，如",
    "which only have access to appropriate information within that structure.":
        "只能访问该结构体内的适当信息。",
    "This frees many of the modules from having to": "这使许多模块不必",
    "the main system state and reduces inter-module dependency. Changes in overall application behavior do not generally affect individual module behavior, so recompilation and testing are required less often.":
        "主系统状态，并减少了模块间依赖。整体应用行为的变化通常不会影响单个模块的行为，因此需要重新编译和测试的频率更低。",
    'Note that the module functions with this approach do not "own" their data. They do not allocate any global variables, do not access any global variables, and do not maintain any permanent pointers to external data. Instead, data is passed in as an argument. The module functions will operate on any data passed in. They don\'t care whether they operate on data from one motor or another, or whether it\'s mock data from a testing program or real data from an':
        '请注意，采用此方法的模块函数不"拥有"其数据。它们不分配任何全局变量，不访问任何全局变量，也不维护任何指向外部数据的永久指针。相反，数据作为参数传入。模块函数将对任何传入的数据进行操作。它们不关心操作的是来自一个电机还是另一个电机的数据，也不关心是来自测试程序的模拟数据还是来自',
    "As a result, the module functions are easily covered by unit tests. We just create sample inputs, call the appropriate function, and examine the outputs.":
        "因此，模块函数很容易被单元测试覆盖。我们只需创建示例输入，调用相应的函数，然后检查输出。",
    "The main application is responsible for allocating program state variables for the entire system, and for each motor.":
        "主应用负责为整个系统和每个电机分配程序状态变量。",
    "One consequence of this philosophy is that many of the motor control parameters cannot be hard-coded in the application; instead, they must be":
        "这种理念的一个后果是，许多电机控制参数不能在应用中硬编码；相反，它们必须是",
    "configurable parameters": "可配置参数",
    ". The reason is that we wish to support control of two different motors at once using the same module functions, and each motor may have different software parameters, so these parameters need to be removed from the code and kept in state variables.":
        "。原因是我们希望使用相同的模块函数同时支持控制两个不同的电机，而每个电机可能有不同的软件参数，因此这些参数需要从代码中移除并保存在状态变量中。",
    # Miscellaneous Guidelines
    "Related state variables belong together. If a group of variables are always found and used together, they are probably best off if declared as members in a structure.":
        "相关的状态变量应该放在一起。如果一组变量总是同时出现和使用，那么将它们声明为结构体的成员可能是最好的选择。",
    "Hierarchy can assist and simplify naming: if there are 5 counters e.g.":
        "层次结构可以帮助并简化命名：如果有 5 个计数器，例如",
    ", these could be combined into a": "，这些可以合并到一个",
    "structure with the members not needing the word": "结构体中，成员不需要",
    "because they are now contained in a context that implies they are counters:":
        "这个词，因为它们现在处于一个暗示它们是计数器的上下文中：",
    "Embedded structures (structures which contain other structures) indicate ownership: the contained structure is owned by, and is an inherent part of, the containing structure.":
        "嵌入结构体（包含其他结构体的结构体）表示所有权：被包含的结构体由包含它的结构体所拥有，并且是其固有部分。",
    "Referenced structures (structures which contain a pointer to other structures) indicate association and non-exclusivity: a contained pointer allows access to other data.":
        "引用结构体（包含指向其他结构体的指针的结构体）表示关联和非排他性：包含的指针允许访问其他数据。",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
