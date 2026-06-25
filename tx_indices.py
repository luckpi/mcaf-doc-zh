# -*- coding: utf-8 -*-
"""Translate all index/overview pages in batch."""
import txutil

# Common section titles used across the algorithms chapter
TITLES = {
    # Ch 5 algorithms index
    "5. Detailed Algorithm Notes": "5. 详细算法说明",
    "5.1. Field-oriented Current Control": "5.1. 磁场定向电流控制",
    "5.1.1. Field-oriented control (FOC): an overview": "5.1.1. 磁场定向控制（FOC）：概述",
    "5.1.2. Fundamentals of FOC": "5.1.2. FOC 基础",
    "5.1.3. Current measurement": "5.1.3. 电流测量",
    "5.1.4. Overmodulation": "5.1.4. 过调制",
    "5.1.5. DC link compensation": "5.1.5. 母线电压补偿",
    "5.1.6. Current loop tuning": "5.1.6. 电流环整定",
    "5.1.7. Comparison between FOC and six-step control": "5.1.7. FOC 与六步控制的比较",
    "5.2. Startup": "5.2. 启动",
    "5.2.1. Overview": "5.2.1. 概述",
    "5.2.2. Startup sequence and common elements": "5.2.2. 启动序列与公共要素",
    "5.2.3. Classic startup (current decay)": "5.2.3. 经典启动（电流衰减）",
    "5.2.4. Weathervane startup": "5.2.4. 风向标启动",
    "5.2.5. ZS/MT + IPC startup": "5.2.5. ZS/MT + IPC 启动",
    "5.2.6. Active damping": "5.2.6. 主动阻尼",
    "5.2.7. Slow and fast acceleration": "5.2.7. 慢加速与快加速",
    "5.3. Stopping": "5.3. 停机",
    "5.3.1. Overview": "5.3.1. 概述",
    "5.3.2. Minimal-impact PWM": "5.3.2. 最小影响 PWM",
    "5.3.3. Closed-loop methods": "5.3.3. 闭环方法",
    "5.3.4. Implementation notes": "5.3.4. 实现说明",
    "5.4. Position and Velocity Estimation": "5.4. 位置与速度估计",
    "5.4.1. Firmware Interface": "5.4.1. 固件接口",
    "5.4.2. AN1292 Phase-locked Loop (PLL)": "5.4.2. AN1292 锁相环（PLL）",
    "5.4.3. Quadrature encoder support": "5.4.3. 正交编码器支持",
    "5.4.4. Angle-tracking Phase-locked Loop (ATPLL)": "5.4.4. 角度跟踪锁相环（ATPLL）",
    "5.4.5. Zero-Speed / Maximum Torque (ZS/MT)": "5.4.5. 零速/最大转矩（ZS/MT）",
    "5.4.6. Sliding Mode Observer (SMO)": "5.4.6. 滑模观测器（SMO）",
    "5.4.7. Overview": "5.4.7. 概述",
    "5.4.8. Comparative analysis": "5.4.8. 比较分析",
    "5.5. Flux control": "5.5. 磁通控制",
    "5.5.1. Flux weakening": "5.5.1. 弱磁",
    "5.5.2. Maximum Torque Per Ampere (MTPA)": "5.5.2. 最大转矩/电流比（MTPA）",
    "5.5.3. D-axis current reference generation": "5.5.3. d 轴电流参考生成",
    "5.5.4. Overview": "5.5.4. 概述",
    "5.5.5. Flow chart and details": "5.5.5. 流程图与细节",
    "5.6. Current limit": "5.6. 电流限制",
    "5.6.1. Overview": "5.6.1. 概述",
    "5.6.2. Implications of operating at the current limit": "5.6.2. 在电流限值下运行的含义",
    "5.6.3. Dynamic current limit": "5.6.3. 动态电流限制",
    "5.6.4. Thermal modeling background": "5.6.4. 热建模背景",
    "5.6.5. Available current limit algorithms in MCAF": "5.6.5. MCAF 中可用的电流限制算法",
    "5.6.6. Peak and continuous limits": "5.6.6. 峰值与连续限值",
    "5.6.7. Implementation notes": "5.6.7. 实现说明",
    "5.7. Dead-time Compensation": "5.7. 死区补偿",
    "5.7.1. Overview": "5.7.1. 概述",
    "5.7.2. Definition and origin of dead time": "5.7.2. 死区的定义与来源",
    "5.7.3. Dead-time distortion": "5.7.3. 死区畸变",
    "5.7.4. Practical effects of dead-time distortion": "5.7.4. 死区畸变的实际影响",
    "5.7.5. Dead-time compensation": "5.7.5. 死区补偿",
    "5.7.6. References": "5.7.6. 参考文献",
    "5.8. Voltage Control": "5.8. 电压控制",
    "5.8.1. Overview": "5.8.1. 概述",
    "5.8.2. Effects of motor parameters on mechanical compliance": "5.8.2. 电机参数对机械柔性的影响",
    "5.8.3. Choosing algorithm parameters": "5.8.3. 选择算法参数",
    "5.9. Temperature measurement": "5.9. 温度测量",
    "5.9.1. Filtering": "5.9.1. 滤波",
    "5.9.2. Implementation notes": "5.9.2. 实现说明",
    "Miscellaneous": "其他",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Detailed Algorithm Notes": "详细算法说明",
}

PAGES = [
    ("algorithms/index", "5. 详细算法说明", TITLES),
]

for rel, title_zh, m in PAGES:
    path = txutil.translate_dict_page(rel, title_zh, m)
    print("translated", path)
