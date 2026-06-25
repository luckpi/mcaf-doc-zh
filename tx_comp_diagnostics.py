# -*- coding: utf-8 -*-
import txutil

rel = "components/diagnostics"
title_zh = "4.8. 诊断内核"

m = {
    "Components": "组件",
    "Diagnostic Kernel": "诊断内核",
    "4.8. Diagnostic Kernel": "4.8. 诊断内核",
    "The diagnostic kernel allows real-time diagnostics and testing through interaction with an external host PC. At this time, there are two options, selectable in the": "诊断内核允许通过与外部主机 PC 交互来进行实时诊断和测试。目前有两个选项，可在",
    "Customize page": "自定义页面",
    "of motorBench": "的 motorBench",
    "Development Suite:": "开发套件中选择：",
    "from the Linz Center of Mechatronics GmbH, for use with the X2Cscope plugin for MPLAB": "来自林茨机电一体化中心，用于 MPLAB",
    "X. This is the default option.": "X 的 X2Cscope 插件。这是默认选项。",
    "\u201cNone\u201d is for board configurations without a UART for diagnostics or to reduce": "\u201c无\u201d用于没有诊断 UART 的电路板配置或为了减少",
    "CPU usage": "CPU 使用率",
    "is configured to sample data at the control": "被配置为在控制",
    "(nominally 20 kHz) and use a UART channel for communication with the host PC.": "（标称 20 kHz）时采样数据，并使用 UART 通道与主机 PC 通信。",
    "Implementation Notes": "实现说明",
    "4.8.1. Implementation Notes": "4.8.1. 实现说明",
    "Modules": "模块",
    "4.8.1.1. Modules": "4.8.1.1. 模块",
    "Module": "模块",
    "Files": "文件",
    "Description": "描述",
    "Comments": "说明",
    "Top-level diagnostics": "顶层诊断",
    "External Interface": "外部接口",
    "Hardware Abstraction Layer (HAL)": "硬件抽象层（HAL）",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
