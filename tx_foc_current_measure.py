# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/current_measure"
title_zh = "5.1.3. 电流测量"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Current measurement": "电流测量",
    "Fundamentals of FOC": "FOC 基础",
    "Overmodulation": "过调制",
    "Overview": "概述",
    "Gain and offset compensation": "增益与偏置补偿",
    "Current measurement channels": "电流测量通道",
    "Current polarity conventions": "电流极性约定",
    "Validity of lower-leg shunt resistors": "下桥臂分流电阻的有效性",
    "Triple-channel current measurement": "三通道电流测量",
    "Dual-channel current measurement": "双通道电流测量",
    "Single-channel current measurement": "单通道电流测量",
    "Microchip development board support": "Microchip 开发板支持",
    "Implementation notes": "实现说明",
    "ADC Calibration and Compensation": "ADC 校准与补偿",
    "Simplified FOC diagram": "简化 FOC 框图",
    "Typical current sense resistors in a three-phase bridge": "三相桥中典型的电流采样电阻",
    "Current measurement algorithms take individual current measurements (phase currents, low-side transistor currents, or DC link currents) and adapt them for use in the feedback path of field-oriented control. This feedback processing step is shown as “gain/ofs compensation” in":
        "电流测量算法获取各个电流测量值（相电流、下桥臂晶体管电流或母线电流），并将其适配为磁场定向控制反馈通路中可用的量。该反馈处理步骤在",
    "Current measurement includes several aspects:": "电流测量包括以下几个方面：",
    "run-time compensation of current offset error": "运行时对电流偏置误差进行补偿",
    "compile-time compensation of current gain error, for cases such as the": "编译时对电流增益误差进行补偿，例如",
    "MCLV-2": "MCLV-2",
    "use of single/dual/triple-channel current measurement": "使用单/双/三通道电流测量",
    "Gain and offset errors in current measurement are undesirable in a motor drive for several reasons. They cause unwanted torque ripple. Motor drives must be derated in current capacity to cover uncertainty in current-sense gain and offset, so that the components are kept within their safe operating area.":
        "电机驱动中不希望出现电流测量的增益和偏置误差，原因有几方面：它们会引起不希望的转矩脉动；电机驱动必须在工作电流上降额使用，以覆盖电流采样增益与偏置的不确定性，从而保证器件处于安全工作区之内。",
    "See": "参见",
    "for more information.": "以获取更多信息。",
    "MCAF supports flexibility in the number of channels (“shunts”) that can be used. Typical current sensing for low-current":
        "MCAF 在可使用的通道数（“分流电阻/shunt”）方面具有灵活性。小电流",
    "motor control uses shunt resistors placed in the lower leg(s) of the power stage, as shown in":
        "电机控制通常使用放置在功率级下桥臂的分流电阻来检测电流，如",
    "In": "在",
    "dual-channel": "双通道",
    "and": "和",
    "triple-channel": "三通道",
    "measurement, phase currents are sensed through current sense resistors": "测量中，相电流通过电流采样电阻",
    ", and": "、和",
    ". Dual-channel requires two current sense channels, whereas triple-channel measurement requires all three.":
        "来检测。双通道需要两个电流采样通道，而三通道测量需要全部三个通道。",
    "In some cases,": "在某些情况下，",
    "single-channel": "单通道",
    "measurement (“single-shunt”) can be used, where one current sense resistor": "测量（“单分流电阻/single-shunt”）可以使用，此时一个电流采样电阻",
    "measuring the DC link current is enough to reconstruct phase currents.":
        "测量母线电流即可重建相电流。",
    "Shunt resistors are typically used with currents that can be safely handled on a printed circuit board, on the order of 25 – 50 A depending on the duration of the current and on the design and thermal management techniques. At higher currents, galvanically isolated current sensors are typically used, with higher cost and complexity, but with the advantage that they can be placed to measure the output currents directly.":
        "分流电阻通常用于可在印制电路板上安全处理的电流，量级约为 25–50 A，具体取决于电流持续时间以及设计和热管理方式。在更高电流下，通常使用电气隔离的电流传感器，其成本和复杂度更高，但优点是可以直接布置以测量输出电流。",
    "MCAF uses the following convention for current polarity, as shown in": "MCAF 对电流极性采用如下约定，如",
    "Phase currents": "相电流",
    "are positive when current flows out of the bridge output terminals into the motor.":
        "在电流从桥的输出端子流入电机时为正。",
    "DC link current": "母线电流",
    "is positive when current flows into the positive DC link terminal and out the negative DC link terminal of the bridge.":
        "在电流从桥的正母线端子流入、从负母线端子流出时为正。",
    "As shown in": "如",
    ", positive phase currents correspond to negative values of phase shunt currents": "所示，正的相电流对应于相分流电流",
    "should be near zero when all low-side switches are turned on.":
        "在所有下桥臂开关都导通时应接近零。",
    "This configuration is recommended for the most noise-sensitive applications.":
        "建议在对噪声最敏感的应用中使用此配置。",
    "When all three phase currents are measured, this maximizes the signal-to-noise ratio. It also adds some redundancy:":
        "当测量全部三相电流时，信噪比达到最大。这还增加了一定的冗余：",
    "In this case, a full 3×2": "此时使用完整的 3×2",
    "Clarke transform": "Clarke 变换",
    "is used.": "。",
    "Two phase currents are enough to reconstruct the third current, assuming that": "在假设",
    ". This does give up redundancy, and the overall noise level is increased.":
        "的前提下，两个相电流足以重建第三个相电流。这确实放弃了冗余，且总体噪声水平会升高。",
    "In this case, a reduced 2×2": "此时使用降阶的 2×2",
    "With dual-channel measurement, gain errors between the current sense channels manifest themselves as a cross-coupling effect in the phase that is sensed directly; suppose":
        "在双通道测量中，电流采样通道之间的增益误差会表现为被直接采样那一相的交叉耦合效应；假设",
    "is 10 A,": "为 10 A，",
    "is -10 A, and": "为 -10 A，",
    "is zero, but phase A’s gain is +5%, phase B’s gain is -5%, and phase C not measured. Then the sensed values of current are 10.5 A, -9.5 A, and -1 A.":
        "为零，但 A 相增益为 +5%、B 相增益为 -5%、C 相未测量。则检测到的电流值为 10.5 A、-9.5 A 和 -1 A。",
    "The single channel current algorithm is used to reconstruct the three phase currents by measuring the DC link current. With the knowledge of switching states and the DC link current, the three phase motor currents are reconstructed as shown in":
        "单通道电流算法通过测量母线电流来重建三相电流。借助开关状态和母线电流，可以重建三相电机电流，如",
    ". Based on the switching state, either the upper transistors or the lower transistors must include only one phase’s transistor that is turned on, which allows estimation of that phase current from the DC link current.":
        "所示。根据开关状态，上桥臂晶体管或下桥臂晶体管中必须只有某一相的一个晶体管导通，从而可由母线电流估计该相电流。",
    "Instances of current reconstruction: Left image:": "电流重建示例：左图：",
    "(DC link current flows out of motor and through lower leg of phase B). Right image:": "（母线电流从电机流出并流过 B 相下桥臂）。右图：",
    "(DC link flows through upper leg of phase A and into motor).": "（母线电流流过 A 相上桥臂并流入电机）。",
    "If the phase currents are reconstructured using single channel without adjusting the duty cycles, the outputs from Zero Sequence Modulation (ZSM) can result in three-phase currents which are distorted and poses a challenge to perform FOC. This happens due to less time to sample currents using single shunt in the low-modulation index region, and sections of mid-to-high modulation index regions.":
        "如果在单通道方式下重建相电流时不调整占空比，零序调制（ZSM）的输出可能导致三相电流畸变，从而给 FOC 的执行带来挑战。这发生在低调制指数区域以及中高调制指数区域的部分区段，因为在这些区域单分流电阻可用于采样电流的时间较少。",
    "This is resolved by adjusting the ZSM outputs to meet the minimum time window requirements, resulting in better (sinusoidal) current information. Here, we need to ensure sufficient time for each active vector to sample current through the single channel. To achieve this, we check for active vector against a minimum time window":
        "通过调整 ZSM 输出以满足最小时间窗口要求可解决此问题，从而获得更好的（正弦的）电流信息。这里我们需要确保每个有效矢量有足够的时间通过单通道采样电流。为此，我们将有效矢量与一个最小时间窗口",
    ", and compensate if required. The": "进行比较，并在需要时进行补偿。该",
    "minimum time window": "最小时间窗口",
    "can be adjusted in the Customize page of motorBench": "可在 motorBench",
    "Development Suite.": "Development Suite 的 Customize（定制）页面中调整。",
    "In the use case shown below in": "在下方",
    ", the time window T2 is not wide enough to sample current through the single channel. In order to allow a minimum time window for current measurement, we modify this time. The active vector time T2 is increased to meet the minimum time window, and the same is compensated in the falling edge (second half of PWM cycle).":
        "所示的使用场景中，时间窗口 T2 不足以通过单通道采样电流。为了给电流测量留出最小时间窗口，我们对该时间进行修改：增大有效矢量时间 T2 以满足最小时间窗口，并在下降沿（PWM 周期的后半段）进行相应补偿。",
    "This adjustment is not needed if the active vector time T2 is wide enough for the current measurement to be valid and accurate.":
        "如果有效矢量时间 T2 已足够宽，使电流测量有效且准确，则无需此调整。",
    "Duty cycle time T2 being adjusted": "占空比时间 T2 的调整",
    "When the outputs (duty cycles) are modified in the first half of PWM cycle, they are also compensated on the falling edge during its second half of the PWM cycle. This ensures the average voltage vectors (duty cycles) remain the same.":
        "当在 PWM 周期的前半段修改输出（占空比）时，也会在 PWM 周期后半段的下降沿进行补偿，以确保平均电压矢量（占空比）保持不变。",
    "On some boards where the delays due to gate driver propagation and opamp slew rate are larger, the ADC trigger delay": "在栅极驱动器传播延迟和运放压摆率导致的延迟较大的某些板卡上，ADC 触发延迟",
    "will need to be adjusted to meet the delay requirements. The": "需要调整以满足延迟要求。该",
    "ADC trigger delay": "ADC 触发延迟",
    "For more information on implementation details of single channel based current reconstruction for FOC, see Microchip’s application note":
        "关于 FOC 中基于单通道的电流重建实现细节的更多信息，请参见 Microchip 的应用笔记",
    "AN1299": "AN1299",
    "Microchip motor control development boards supported by motorBench are listed in the following table, with current polarities (as seen by the ADC) shown: a green plus indicates positive polarity, and a blue minus indicates negative polarity. Blank table cells mean the specified current input is not sensed.":
        "motorBench 支持的 Microchip 电机控制开发板如下表所列，并标注了电流极性（ADC 所见）：绿色加号表示正极性，蓝色减号表示负极性。空白单元格表示未检测相应的电流输入。",
    "Board": "开发板",
    "Comments": "说明",
    "dsPICDEM": "dsPICDEM",
    "MCLV‑2 Development Board": "MCLV‑2 开发板",
    "MCHV‑2 Development Board": "MCHV‑2 开发板",
    "dsPIC33CK Low Voltage Motor Control (LVMC) Development Board": "dsPIC33CK 低压电机控制（LVMC）开发板",
    "MCS MCLV‑48V‑300W Development Board": "MCS MCLV‑48V‑300W 开发板",
    "MCHV‑230VAC‑1.5kW Motor Control High-Voltage Development Board": "MCHV‑230VAC‑1.5kW 电机控制高压开发板",
    "Support history:": "支持历史：",
    "Number of channels": "通道数",
    "single": "单",
    "dual": "双",
    "triple": "三",
    "MCAF R1 – R6": "MCAF R1 – R6",
    "Dual includes phases A and B only.": "双通道仅包含 A 相和 B 相。",
    "MCAF R7": "MCAF R7",
    "5.1.3. Current measurement": "5.1.3. 电流测量",
    "5.1.3.1. Overview": "5.1.3.1. 概述",
    "5.1.3.2. Gain and offset compensation": "5.1.3.2. 增益与偏置补偿",
    "5.1.3.3. Current measurement channels": "5.1.3.3. 电流测量通道",
    "5.1.3.3.1. Current polarity conventions": "5.1.3.3.1. 电流极性约定",
    "5.1.3.3.2. Validity of lower-leg shunt resistors": "5.1.3.3.2. 下桥臂分流电阻的有效性",
    "5.1.3.3.3. Triple-channel current measurement": "5.1.3.3.3. 三通道电流测量",
    "5.1.3.3.4. Dual-channel current measurement": "5.1.3.3.4. 双通道电流测量",
    "5.1.3.3.5. Single-channel current measurement": "5.1.3.3.5. 单通道电流测量",
    "5.1.3.3.6. Microchip development board support": "5.1.3.3.6. Microchip 开发板支持",
    "5.1.3.3.7. Implementation notes": "5.1.3.3.7. 实现说明",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
