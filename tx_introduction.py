# -*- coding: utf-8 -*-
import txutil

rel = "introduction"
title_zh = "1. 简介"

m = {
    "Introduction": "简介",
    "Getting Started": "快速入门",
    "The Motor Control Application Framework (or MCAF) is Microchip’s next-generation application firmware for motor control on dsPIC":
        "电机控制应用框架（简称 MCAF）是 Microchip 面向 dsPIC",
    "DSC devices. This differs from the firmware for previously-published application notes such as":
        "DSC 器件的下一代电机控制应用固件。它与此前发布的应用笔记（如",
    "and": "与",
    ", in a few significant aspects, most notably that the MCAF is integrated with":
        "）存在若干重要差异，最显著之处在于 MCAF 与",
    "Essentially there is a": "本质上，",
    "firmware package": "固件包",
    "included with motorBench": "随 motorBench",
    "Development Suite that contains the": "Development Suite 一起提供，其中包含",
    "Motor Control Application Framework": "电机控制应用框架",
    ". This package consists of files used to generate code into any desired MPLAB":
        "。该包包含若干文件，用于将代码生成到任意目标 MPLAB",
    "X project. Think of it as a motor control code factory, or as a “prepackaged meal” — but for firmware code instead of dinner — that includes both recipes and ingredients. The application framework is “rendered” into a particular instance of application source code by motorBench":
        "X 项目。可以把它想象成一个电机控制代码工厂，或者一份“预制餐”——只是对象是固件代码而非晚餐——其中既包含配方也包含配料。应用框架被“渲染”为一份具体的应用源代码实例，这一过程由 motorBench",
    "Development Suite, based on configuration information, automated motor parameter measurements, and the resulting calculations to tune motor control loops.":
        "Development Suite 根据配置信息、自动化的电机参数测量，以及由此得到的用于整定电机控制环路的计算结果来完成。",
    "This approach provides two major advantages:": "这种方式带来两大优势：",
    "Management of multiple hardware configurations": "管理多种硬件配置",
    "— by using code generation, the MCAF can support the many combinations of processor, board,":
        "——通过代码生成，MCAF 能够用单一的固件包支持处理器、开发板、",
    ", motor, and load with a single firmware package.": "、电机和负载的多种组合。",
    "Automation of the tuning process": "自动化整定流程",
    "— motorBench": "—— motorBench",
    "Development Suite includes algorithms that will automatically tune the current and velocity controllers.":
        "Development Suite 包含的算法可自动整定电流和速度控制器。",
    "In addition, Microchip has made many improvements in code quality, to make the firmware more readable and modular, and reduce barriers in applying this firmware to use in customer applications. We hope you benefit from these improvements in your next motor control project.":
        "此外，Microchip 在代码质量方面做了许多改进，使固件更具可读性、更加模块化，并降低了将本固件应用于客户产品的门槛。希望这些改进能助力您的下一个电机控制项目。",
    "© Copyright 2017-2026, Microchip Technology, Inc..": "© 版权所有 2017-2026，Microchip Technology, Inc..",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
