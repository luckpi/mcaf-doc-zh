# -*- coding: utf-8 -*-
import txutil

rel = "appendix/otherdocs"
title_zh = "7.4. 相关文档"

m = {
    "7.4. Related Documents — MCAF R9 RC31 文档 (docver 9.0.1)": "7.4. 相关文档 — MCAF R9 RC31 文档 (docver 9.0.1)",
    "Appendix": "附录",
    "Related Documents": "相关文档",
    "More information is available in these other documents, available from Microchip MCU16 Applications on request.": "更多信息可从这些其他文档中获取，可向 Microchip MCU16 Applications 索取。",
    "Hardware Abstraction Layer": "硬件抽象层",
    "\u2014 This document provides a detailed description of the Hardware Abstraction Layer (HAL), its architecture, components, and usage model. The HAL allows decoupling of the hardware-dependent firmware from the rest of the Motor Control Application Framework, and minimizes the amount of work needed to support additional hardware designs.": "\u2014 本文档详细描述了硬件抽象层（HAL）的架构、组件和使用模型。HAL 使硬件相关固件与电机控制应用框架的其余部分解耦，并最小化支持额外硬件设计所需的工作量。",
    "MCC Peripheral Settings": "MCC 外设设置",
    "\u2014 To use MCAF, setup MCC or use the sample projects provided. This document gives detailed instructions on how to setup MCC for use with motorBench": "\u2014 要使用 MCAF，请设置 MCC 或使用提供的示例项目。本文档提供了如何设置 MCC 以与 motorBench",
    "Development Suite. It also gives details on what is required of MCC and what is user configurable.": "Development Suite 配合使用的详细说明。还详细说明了 MCC 的要求以及用户可配置的内容。",
    "Monitoring module design": "监控模块设计",
    "(fault detection) \u2014 The complexity needed to achieve a field-oriented": "（故障检测）——实现磁场定向",
    "motor control system requires a similar level of complexity in fault monitoring, to be able to detect malfunctions in a reliable manner, and determine the underlying cause.": "电机控制系统所需的复杂度要求故障监控具有类似的复杂度，以可靠地检测故障并确定根本原因。",
    "Mechanical system perturbations are among the most unpredictable, due to their total exposure to the environment, and may be associated with safety hazards to surrounding people or property. Therefore the more accurate and more quickly a mechanical fault can be detected and handled, the more reliably the system can be kept in a safe state. In addition, usually the electronics and mechanical components of a motor-driven system are expensive, so that fault monitoring ultimately has economic advantages.": "机械系统扰动是最不可预测的，因为它们完全暴露在环境中，可能对周围人员或财产造成安全隐患。因此，机械故障检测和处理越准确、越快速，系统就越能可靠地保持在安全状态。此外，电机驱动系统的电子和机械组件通常昂贵，因此故障监控最终具有经济优势。",
    "This document describes the up-to-date implementation of fault monitoring in the motor control system, capable to distinguish between hazardous and benign situations encountered by either mechanical or electrical systems related to the control of a": "本文档描述了电机控制系统中故障监控的最新实现，能够区分与",
    "Saturation treatment module design": "饱和处理模块设计",
    "(saturation and antiwindup) \u2014 A good design of the motor control system requires prediction and management of boundaries of control linearity, in order to achieve performance targets. Saturation of control output can cause inefficient, suboptimum, or unstable operation, and must be managed carefully in order to avoid these problems.": "（饱和与抗积分饱和）——良好的电机控制系统设计需要预测和管理控制线性边界，以实现性能目标。控制输出饱和可能导致低效、次优或不稳定的运行，必须仔细管理以避免这些问题。",
    "Saturation handling covered in this document describes the methods designed to detect saturation of the controller outputs, such as current, voltage, or speed, and the way in which the controllers must be modified or functionally enhanced to counteract unwanted effects.": "本文档涵盖的饱和处理描述了用于检测控制器输出（如电流、电压或速度）饱和的方法，以及控制器必须如何修改或功能增强以抵消不良影响。",
    "Recovery module design": "恢复模块设计",
    "\u2014 Fault management in a motor control system needs to be designed assuming that faults will eventually occur. When this happens, one important decision is how they will be handled.": "\u2014 电机控制系统中的故障管理需要假设故障最终会发生来设计。当故障发生时，一个重要的决定是如何处理它们。",
    "Unfortunately, malfunctions frequently affect electromechanical systems, and in some cases the best response is for the motor to be brought to a stop. Fortunately there are system malfunctions that can be predicted and sometimes treated depending on the degree of severity, and whether sufficient input signals are available.": "遗憾的是，故障经常影响机电系统，在某些情况下最佳响应是使电机停止。幸运的是，有些系统故障是可以预测的，有时可以根据严重程度以及是否有足够的输入信号进行处理。",
    "There is a strong relationship between the recovery and monitoring system. The monitoring system provides the recovery system with information about detected faults. The recovery system is meant to bring the motor back to its previous operation, in the case of a motor stall or fault.": "恢复系统与监控系统之间有密切关系。监控系统向恢复系统提供检测到的故障信息。恢复系统旨在电机堵转或故障时使电机恢复到之前的运行状态。",
    "Comparison of AN1292 and MC Application Framework": "AN1292 与 MC 应用框架的比较",
    "\u2014 This document provides an analysis into differences between AN1292 software and the Motor Control Application Framework supplied with motorBench": "\u2014 本文档分析了 AN1292 软件与 motorBench",
    "Development Suite. The intention here is to retrospectively review the improvements and limitations of the new Application Framework source code relative to the reference application note software from AN1292.": "Development Suite 提供的电机控制应用框架之间的差异。目的是回顾性地审查新应用框架源代码相对于 AN1292 参考应用笔记软件的改进和局限性。",
    "MCLV-2 Sense Resistors": "MCLV-2 采样电阻",
    "Revision History": "修订历史",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
