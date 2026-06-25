# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/index"
title_zh = "5.1. 磁场定向电流控制"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Field-oriented control (FOC): an overview": "磁场定向控制（FOC）：概述",
    "5.1.1. Field-oriented control (FOC): an overview": "5.1.1. 磁场定向控制（FOC）：概述",
    "5.1.2. Fundamentals of FOC": "5.1.2. FOC 基础",
    "5.1.2.1. Torque production and reference frames": "5.1.2.1. 转矩产生与参考坐标系",
    "5.1.2.2. Stator voltage and flux equations": "5.1.2.2. 定子电压与磁通方程",
    "5.1.2.3. FOC block diagram": "5.1.2.3. FOC 框图",
    "5.1.2.4. Implementation notes": "5.1.2.4. 实现说明",
    "5.1.2.5. Miscellaneous topics": "5.1.2.5. 其他主题",
    "5.1.2.6. References": "5.1.2.6. 参考文献",
    "5.1.3. Current measurement": "5.1.3. 电流测量",
    "5.1.3.1. Overview": "5.1.3.1. 概述",
    "5.1.3.2. Gain and offset compensation": "5.1.3.2. 增益与偏置补偿",
    "5.1.3.3. Current measurement channels": "5.1.3.3. 电流测量通道",
    "5.1.4. Overmodulation": "5.1.4. 过调制",
    "5.1.4.1. Modulation index": "5.1.4.1. 调制指数",
    "5.1.4.2. Overmodulation behavior in the stationary frame": "5.1.4.2. 静止坐标系中的过调制行为",
    "5.1.4.3. Overmodulation behavior in the synchronous frame": "5.1.4.3. 同步坐标系中的过调制行为",
    "5.1.4.4. Coordinating overmodulation and controller limits": "5.1.4.4. 协调过调制与控制器限幅",
    "5.1.4.5. Implementation Notes": "5.1.4.5. 实现说明",
    "5.1.4.6. References": "5.1.4.6. 参考文献",
    "5.1.5. DC link compensation": "5.1.5. 母线电压补偿",
    "5.1.5.1. Transients": "5.1.5.1. 暂态过程",
    "5.1.5.2. Implementation Notes": "5.1.5.2. 实现说明",
    "5.1.6. Current loop tuning": "5.1.6. 电流环整定",
    "5.1.6.1. Background": "5.1.6.1. 背景",
    "5.1.6.2. Evaluating control performance": "5.1.6.2. 评估控制性能",
    "5.1.6.3. Examples of poorly-tuned and well-tuned current loops": "5.1.6.3. 整定不良与整定良好的电流环示例",
    "5.1.6.4. Tuning criteria and motorBench": "5.1.6.4. 整定准则与 motorBench",
    "5.1.6.5. Adjusting current control gains in MCAF": "5.1.6.5. 在 MCAF 中调整电流控制增益",
    "5.1.6.6. Commutation angle issues during current loop tuning": "5.1.6.6. 电流环整定过程中的换相角问题",
    "5.1.6.7. References": "5.1.6.7. 参考文献",
    "5.1.7. Comparison between FOC and six-step control": "5.1.7. FOC 与六步控制的比较",
    "5.1.7.1. Torque capability": "5.1.7.1. 转矩能力",
    "5.1.7.2. Torque ripple": "5.1.7.2. 转矩脉动",
    "5.1.7.3. Efficiency": "5.1.7.3. 效率",
    "5.1.7.4. Switching loss": "5.1.7.4. 开关损耗",
    "5.1.7.5. Current management": "5.1.7.5. 电流管理",
    "5.1.7.6. Cost optimization": "5.1.7.6. 成本优化",
    "5.1.7.7. Control complexity": "5.1.7.7. 控制复杂度",
    "© Copyright 2017-2026, Microchip Technology, Inc..": "© 版权所有 2017-2026，Microchip Technology, Inc..",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
