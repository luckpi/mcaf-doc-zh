# -*- coding: utf-8 -*-
import txutil

rel = "architecture/naming"
title_zh = "3.2. 命名约定"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "Naming Conventions": "命名约定",
    "Additional Naming Guidelines": "附加命名指南",
    "Architectural Overview": "架构概述",
    "State management": "状态管理",
    # TOC entries
    "3.2. Naming Conventions": "3.2. 命名约定",
    "3.2.1. Additional Naming Guidelines": "3.2.1. 附加命名指南",
    # intro
    "The MCAF uses the following naming conventions:": "MCAF 使用以下命名约定：",
    "prefix": "前缀",
    "is used for all functions and types, so that these functions are less likely to conflict with user-defined code. The major prefixes are":
        "用于所有函数和类型，以降低这些函数与用户自定义代码冲突的可能性。主要前缀有",
    "— Motor Control Library": "——电机控制库",
    "— Motor Control Application Framework": "——电机控制应用框架",
    "— Hardware Abstraction Layer": "——硬件抽象层",
    "— Board Support Package": "——板级支持包",
    "— Motion Control API": "——运动控制 API",
    # Functions
    "Functions": "函数",
    "use a prefix and UpperCamelCase, i.e. one or more words with each word capitalized including the first one. These generally fall into one of two types:":
        "使用前缀和 UpperCamelCase（大驼峰命名），即一个或多个单词，每个单词首字母大写（包括第一个单词）。这些通常分为两种类型：",
    "Actions:": "动作类：",
    "<noun-phrase>": "<名词短语>",
    "<action>": "<动作>",
    "Getters:": "获取器类：",
    "<adjective-phrase>": "<形容词短语>",
    "or": "或",
    "<property>": "<属性>",
    # Types
    "Types": "类型",
    "are defined in all capital letters with underscores between words:":
        "以全大写字母定义，单词之间用下划线分隔：",
    # Enum
    "Enum": "枚举",
    "constants are defined in all capital letters with underscores between words. Enum constants in the same type should have a common prefix that is specific to that type, for instance the":
        "常量以全大写字母定义，单词之间用下划线分隔。同一类型中的枚举常量应具有特定于该类型的公共前缀，例如本例中的",
    "prefix in this example:": "前缀：",
    # Variables
    "Variables": "变量",
    "and struct/union": "和结构体/联合体的",
    "members": "成员",
    "are declared in lowerCamelCase, i.e. one or more words with each word capitalized except the first one:":
        "以 lowerCamelCase（小驼峰命名）声明，即一个或多个单词，除第一个单词外每个单词首字母大写：",
    "Underscore characters in variable names and structure members are discouraged.":
        "不鼓励在变量名和结构体成员中使用下划线字符。",
    "Prefixes are not used in global variables, because the number of global variables is minimal. In addition, their names may be changed by customers without impact to the MCAF, since the framework's modules do not access them directly.":
        "全局变量不使用前缀，因为全局变量的数量很少。此外，客户可以更改它们的名称而不会影响 MCAF，因为框架的模块不直接访问它们。",
    # stdint
    "The MCAF uses the standard C types defined in": "MCAF 使用",
    "and": "和",
    ", such as": "中定义的标准 C 类型，例如",
    ", to denote integers of specific bit widths. Earlier application note code included lines such as the following:":
        "，来表示特定位宽的整数。早期应用笔记代码包含如下代码行：",
    "These have since been converted to use": "这些后来已转换为使用",
    # Additional Naming Guidelines
    "The MCAF sometimes uses variable names which are symbolic in nature (for example":
        "MCAF 有时使用具有符号性质的变量名（例如",
    ") because these have specific meanings in motor control theory.":
        "），因为它们在电机控制理论中具有特定含义。",
    "The camelCase convention in symbolic names should not change the capitalization of subscripts, for example we use":
        "符号名中的 camelCase 约定不应改变下标的大小写，例如我们使用",
    "rather than": "而不是",
    "In general, variable names should start off with a general description of the quantity they represent and should be followed by more specific qualifiers. This allows related sibling variables or structure members to be alphabetically adjacent, and allows readers to narrow down the topic of interest as they read from left to right. Thus":
        "通常，变量名应以所表示量的概括描述开头，后跟更具体的限定词。这使得相关的同级变量或结构体成员在字母顺序上相邻，并允许读者在从左到右阅读时逐步缩小感兴趣的主题。因此",
    "is better than": "优于",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
