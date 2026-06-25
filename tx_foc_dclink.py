# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/dclink-comp"
title_zh = "5.1.5. 母线电压补偿"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "DC link compensation": "母线电压补偿",
    "Overmodulation": "过调制",
    "Current loop tuning": "电流环整定",
    "Transients": "暂态过程",
    "Implementation Notes": "实现说明",
    "Feature support": "功能支持",
    "Variability in the DC link voltage manifests itself as a time-varying gain of the power electronics block; if the DC link voltage increases by 10%, then for the same duty cycles applied to a three-phase bridge, the voltage output will also be increased by 10%.":
        "母线电压的变化表现为功率电子模块一个随时间变化的增益；如果母线电压升高 10%，那么在向三相桥施加相同占空比的情况下，输出电压也会升高 10%。",
    "This affects the behavior of a FOC motor controller in a few significant ways:":
        "这会从几个重要方面影响 FOC 电机控制器的行为：",
    "Current controller loop gain changes proportionally to DC link voltage. This variation can degrade the stability of the current controller.":
        "电流控制器的环路增益随母线电压成正比变化。这种变化会降低电流控制器的稳定性。",
    "Voltage transients in the DC link cause a disturbance to the current loop.":
        "母线上的电压暂态会对电流环造成扰动。",
    "Sensorless estimators that rely only on duty cycle signals will also see a gain shift proportional to DC link voltage.":
        "仅依赖占空比信号的无传感器估计器也会看到一个与母线电压成正比的增益偏移。",
    "We can compensate for DC link voltage by converting from voltage to duty cycle in the forward path, as shown in":
        "我们可以通过在前向通路中将电压转换为占空比来补偿母线电压，如",
    "Block diagram of MCAF Field Oriented Control, forward path": "MCAF 磁场定向控制前向通路框图",
    "Essentially the": "本质上，",
    "voltages coming out of the Inverse Clarke blocks are multiplied by the reciprocal of the DC link voltage and then used as the input of the zero sequence modulation (ZSM) block:":
        "从逆 Clarke 变换模块输出的电压被乘以母线电压的倒数，然后作为零序调制（ZSM）模块的输入：",
    "where the subscript": "其中下标",
    "represents the unmodified three-phase output of the Inverse Clarke transform, prior to shifting and clipping by the ZSM block.":
        "表示逆 Clarke 变换未经修改的三相输出，即在 ZSM 模块进行平移和限幅之前的结果。",
    "In addition, we need to make the output limits of the current controller scale proportionally to":
        "此外，我们需要让电流控制器的输出限幅与",
    ", in order to reflect the physical limits of the three-phase bridge.": "成正比地变化，以反映三相桥的物理限制。",
    "DC link compensation will work correctly in the presence of transients if the dynamics of sensing":
        "如果检测",
    "are much faster than the dynamics of the voltage transient itself.": "的动态比电压暂态本身的动态快得多，那么母线电压补偿在暂态下也能正确工作。",
    "On the": "在",
    "dsPICDEM": "dsPICDEM",
    "MCLV‑2 Development Board": "MCLV‑2 开发板",
    ", for example, there is a 188 μs RC filter (see": "上，例如，有一个 188 μs 的 RC 滤波器（见",
    ") that dominates the dynamic behavior of sensing. This has a 3 dB bandwidth of about 847 Hz, so DC link compensation should be able to reject transients with frequency content significantly lower than this, and cannot reject transient content around or above this frequency. In general, motor drive designs should use RC filters with shorter time constants, typically on the order of 1 – 10 μs; antialiasing concerns are usually less important than avoiding excessive phase lag, because the DC link capacitors already limit high frequency content.":
        "），它主导了检测的动态行为。其 3 dB 带宽约为 847 Hz，因此母线电压补偿应能抑制频率成分明显低于此值的暂态，而无法抑制处于或高于此频率的暂态成分。一般而言，电机驱动设计应使用时间常数更短的 RC 滤波器，通常在 1–10 μs 量级；由于母线电容已经限制了高频成分，抗混叠问题通常不如避免过大相位滞后重要。",
    "RC filter in MCLV-2": "MCLV-2 中的 RC 滤波器",
    "The reciprocal step of computing": "计算",
    "in fixed-point relies on choosing a reasonable scaling factor. In the MCAF, we use Q12 representation with a scaling factor of":
        "倒数的定点运算依赖于选择合理的比例因子。在 MCAF 中，我们采用 Q12 表示，比例因子为",
    ", which allows accurate computation of": "，这使得在电压范围",
    "over the voltage range": "内能够准确计算",
    ". For the MCLV-2 board’s maximum input voltage range of 52.8 V, this allows accurate reciprocal calculations between 6.6 V and 52.8 V. For the MCHV-2 and MCHV-3 boards’ maximum input voltage range of 453.3 V, this allows accurate reciprocal calculations between 56.7 V and 453.3 V.":
        "的倒数。对于 MCLV-2 板最大输入电压范围 52.8 V，这允许在 6.6 V 至 52.8 V 之间进行准确的倒数计算。对于 MCHV-2 和 MCHV-3 板最大输入电压范围 453.3 V，这允许在 56.7 V 至 453.3 V 之间进行准确的倒数计算。",
    "If": "如果",
    "the reciprocal is clamped at its maximum value (32767 counts =": "，倒数被限幅至其最大值（32767 个计数 =",
    ") and the DC link compensation will not be perfect; in this case the overall open-loop gain (including the gain of the three-phase bridge in hardware, and DC link compensation in software) will be less than one.":
        "），此时母线电压补偿将不完美；这种情况下总开环增益（包括硬件中三相桥的增益和软件中的母线电压补偿）将小于 1。",
    "DC link compensation was not present in MCAF R1 but has been added in MCAF R2.":
        "母线电压补偿在 MCAF R1 中不存在，已在 MCAF R2 中加入。",
    "5.1.5. DC link compensation": "5.1.5. 母线电压补偿",
    "5.1.5.1. Transients": "5.1.5.1. 暂态过程",
    "5.1.5.2. Implementation Notes": "5.1.5.2. 实现说明",
    "5.1.5.2.1. Feature support": "5.1.5.2.1. 功能支持",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
