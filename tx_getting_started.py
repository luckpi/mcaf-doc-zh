# -*- coding: utf-8 -*-
import txutil

rel = "getting-started"
title_zh = "2. 快速入门"

m = {
    "Getting Started": "快速入门",
    "Introduction": "简介",
    "Architecture": "架构",
    "To get started with the Motor Control Application Framework, follow the directions given in the release notes for":
        "要开始使用电机控制应用框架，请按照",
    "Development Suite": "Development Suite",  # keep (part of product name)
    ". This will walk you through these steps:": "的发行说明中的指引操作。它将引导您完成以下步骤：",
    "entering configuration information": "输入配置信息",
    "self-commissioning to identify motor parameters": "自整定（self-commissioning）以识别电机参数",
    "autotuning to compute controller gains": "自动整定（autotuning）以计算控制器增益",
    "file generation to produce source code": "生成文件以产生源代码",
    "At this point, your MPLAB": "此时，您的 MPLAB",
    "X project will now contain code generated from the Motor Control Application Framework, and you can browse these files in the Header Files and Source Files folders in the project:":
        "X 项目中将包含由电机控制应用框架生成的代码，您可以在项目的“Header Files”和“Source Files”文件夹中浏览这些文件：",
    "You can now click on the “Run Main Project” (play) button on the MPLAB":
        "现在您可以点击 MPLAB",
    "X toolbar to build the project and program the device:":
        "X 工具栏上的“Run Main Project”（运行主项目，播放按钮）来构建项目并对器件编程：",
    "© Copyright 2017-2026, Microchip Technology, Inc..": "© 版权所有 2017-2026，Microchip Technology, Inc..",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
