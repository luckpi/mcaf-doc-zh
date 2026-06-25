# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/tuning"
title_zh = "5.1.6. 电流环整定"

m = {
    # nav / sidebar
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Current loop tuning": "电流环整定",
    "DC link compensation": "母线电压补偿",
    "Comparison between FOC and six-step control": "FOC 与六步控制的比较",
    "Background": "背景",
    "Evaluating control performance": "评估控制性能",
    "Examples of poorly-tuned and well-tuned current loops": "整定不良与整定良好电流环的示例",
    "Current loop tuning at zero velocity": "零速下的电流环整定",
    "Current loop tuning at nonzero velocity": "非零速下的电流环整定",
    "Effects of sample-to-update delay": "采样到更新延迟的影响",
    "Tuning criteria and motorBench": "整定准则与 motorBench",
    "Performance criteria definitions": "性能准则定义",
    "Bode plots of example cases": "示例情形的伯德图",
    "Default values of performance criteria": "性能准则的默认值",
    "Adjusting current control gains in MCAF": "在 MCAF 中调整电流控制增益",
    "Example": "示例",
    "Commutation angle issues during current loop tuning": "电流环整定过程中的换相角问题",
    "Example using the AN1292 PLL": "使用 AN1292 PLL 的示例",
    "References": "参考文献",
    "Reference tracking": "参考值跟踪",
    "Overshoot management": "超调管理",
    "Disturbance rejection": "扰动抑制",
    "Stability": "稳定性",
    "FOC component": "FOC 组件",
    "current control": "电流控制",
    "MIMO": "MIMO",
    "PMSM": "PMSM",
    "rotor saliency": "转子凸极",
    "flux weakening": "弱磁",
    "SPM": "SPM",
    "IPM": "IPM",
    "MTPA": "MTPA",
    "quadrature encoder": "正交编码器",
    "commutation issues": "换相问题",
    "square-wave perturbation of the test harness": "测试框架的方波扰动",
    "Square wave velocity command disturbances to a velocity controller with fixed velocity command":
        "对固定速度指令的速度控制器施加方波速度指令扰动",
    "motor.testing.sqwave.halfPeriod": "motor.testing.sqwave.halfPeriod",
    "the normal MCAF startup sequence": "正常的 MCAF 启动序列",
    "section on performance criteria": "性能准则一节",
    "Nidec Hurst DMA0204024B101": "Nidec Hurst DMA0204024B101",
    "dsPICDEM": "dsPICDEM",
    "MCLV‑2 Development Board": "MCLV‑2 开发板",
    "double-update PWM": "双更新 PWM",
    "Phase margin": "相位裕量",
    "PI phase lag at crossover": "交叉频率处的 PI 相位滞后",
    "Bode plot of selected PI phase lags at crossover, with a phase margin of 75°.":
        "在 75° 相位裕量下，若干交叉频率处 PI 相位滞后的伯德图。",
    "Bode plot of current loop transfer functions for example cases discussed in this section":
        "本节所讨论示例情形的电流环传递函数伯德图",
    "Tuning parameters for six different cases.": "六种不同情形的整定参数。",
    "Example of time-domain metrics for the step response of the mildly interesting transfer function":
        "一个尚算有趣的传递函数阶跃响应的时域指标示例",
    "contact Microchip": "联系 Microchip",
    "AN1292 PLL estimator": "AN1292 PLL 估计器",
    "commutation override": "换相覆盖",
    "motor.testing.overrideOmegaElectrical": "motor.testing.overrideOmegaElectrical",
    "foc_params.h": "foc_params.h",
    "Listing 5.1": "代码清单 5.1",
    "Listing 5.2": "代码清单 5.2",
    "case": "情形",
    "Development Suite": "Development Suite",
    # intro
    "This section provides guidance on the following aspects of tuning the current loop in FOC:":
        "本节就 FOC 中电流环整定的以下几个方面提供指导：",
    "What constitutes a well-tuned current controller?": "什么构成一个整定良好的电流控制器？",
    "How do I adjust the current control loop gains in MCAF?": "如何在 MCAF 中调整电流控制环增益？",
    "How can I use autotuning in the Tune page of motorBench": "如何使用 motorBench 的 Tune（整定）页面中的自动整定",
    "Development Suite to make gain tuning easier?": "Development Suite 来简化增益整定？",
    "Are the default current control loop tuning criteria in motorBench": "motorBench 中默认的电流控制环整定准则",
    "Development Suite good enough to meet the requirements of most systems?": "Development Suite 是否足以满足大多数系统的要求？",
    # background
    "As mentioned in the": "如",
    "section on": "一节中关于",
    ", MCAF uses a pair of PI controllers with saturation and antiwindup. The PI control gains are proportional gain":
        "所述，MCAF 使用一对带饱和与抗积分饱和的 PI 控制器。PI 控制增益为比例增益",
    "and integral gain": "和积分增益",
    "Current loop tuning in FOC can be a challenging task, for a number of related reasons:":
        "FOC 中的电流环整定可能是一项具有挑战性的任务，原因有若干且相互关联：",
    "Control variables of interest (d-axis and q-axis currents) are not directly measurable with test equipment, and exist only as software variables within the microcontroller":
        "所关注的控制变量（d 轴和 q 轴电流）无法用测试设备直接测量，仅作为微控制器内的软件变量存在",
    "Aside from directly assessing step responses of dq-frame currents, evaluating control performance is an unclear task":
        "除了直接评估 dq 坐标系电流的阶跃响应外，评估控制性能是一项不甚明确的任务",
    "Control problems are not readily apparent": "控制问题不易察觉",
    "a motor may be rotating very smoothly but still exhibiting poor current control behavior":
        "电机可能转动得非常平稳，但仍表现出糟糕的电流控制行为",
    "observable effects are usually audible but are unclear indicators such as clicks, clunks, chatter, hiss, or screeching":
        "可观察到的效果通常是可听见的，但指示不明确，如滴答声、闷响、颤振声、嘶嘶声或尖啸声",
    "sinusoidal distortion when measuring phase currents may be viewed as a disproportionate concern":
        "测量相电流时看到的正弦畸变可能被过度关注",
    "FOC is a 2 × 2": "FOC 是一个 2 × 2 的",
    "control system with some subtleties (inductive cross-coupling and saturation behavior for all":
        "控制系统，存在一些微妙之处（所有",
    ", with anisotropic behavior for motors with": "都存在电感交叉耦合和饱和行为，对于具有",
    "or fast mechanical time constants)": "或快速机械时间常数的电机还存在各向异性行为）",
    "The good news is that tuning a current controller with FOC is usually forgiving and does not have to be optimal, and the control gains calculated in motorBench":
        "好消息是，FOC 的电流控制器整定通常比较宽容，不必达到最优，且 motorBench",
    "Development Suite are usually acceptable and conservative.": "Development Suite 计算出的控制增益通常是可接受且偏保守的。",
    # evaluating control performance
    "Several goals of the current controller are listed below:": "电流控制器有以下几个目标：",
    "— make the measured current follow the current reference input with zero steady-state error.":
        "——使测得的电流以零稳态误差跟随电流参考输入。",
    "Torque generated by the motor is proportional to the Q-axis current": "电机产生的转矩与 q 轴电流",
    ", so controlling": "成正比，因此控制",
    "controls the torque.": "即控制转矩。",
    "D-axis current": "d 轴电流",
    "modulates the airgap flux. For": "调制气隙磁通。对于",
    "motors, the torque per ampere is maximized by": "电机，通过",
    "motors, a nonzero value of": "电机，可以使用非零的",
    "can be used to increase efficiency, as calculated by the": "来提高效率，其值由",
    "equations. Any PMSM can also utilize": "方程计算。任何 PMSM 也可利用",
    "to counteract part of the back-emf and extend the operating velocity range, when required, through":
        "来抵消部分反电动势，并在需要时通过",
    "An important quantity for reference tracking is the control bandwidth, along with time-domain metrics such as rise time and settling time, shown in":
        "参考值跟踪的一个重要指标是控制带宽，以及上升时间和调节时间等时域指标，如",
    "— we don’t want undesirable transient behavior following a step change in reference current; we want it to settle quickly and avoid reaching excessive values. Overshoot can be described quantitatively as a normalized fraction; for example, if a reference current step from -1 A to 1 A (a change of 2 A) leads to a maximum current during the transient of 1.3A, then the overshoot is equal to":
        "——我们不希望在参考电流阶跃变化后出现不希望的暂态行为；我们希望它快速稳定并避免达到过大的值。超调可以用归一化比例定量描述；例如，如果参考电流从 -1 A 阶跃到 1 A（变化 2 A），暂态期间最大电流为 1.3 A，则超调等于",
    "An example of overshoot is shown in": "一个超调示例如",
    ". Rise time measures the time needed to transition from 10% of the step change to 90% of the step change. Settling time measures the time until the step response stays within a given bound, here ±5%.":
        "所示。上升时间衡量从阶跃变化的 10% 过渡到 90% 所需的时间。调节时间衡量阶跃响应保持在给定范围内（此处为 ±5%）所需的时间。",
    "— noise, back-emf harmonics, and dead-time distortion are effects that perturb the motor current. A well-tuned current control loop will keep the current error small. Disturbance rejection can be characterized quantitatively by a stiffness transfer function":
        "——噪声、反电动势谐波和死区畸变都是扰动电机电流的效应。整定良好的电流控制环会将电流误差保持在较小水平。扰动抑制可以用刚度传递函数",
    "that represents the voltage disturbance required to make a particular change in current.":
        "定量描述，它表示产生特定电流变化所需的电压扰动。",
    "In closed loop at frequencies much lower than the current loop bandwidth, this stiffness can be very large, but in open loop and at high frequencies it is the per-phase impedance":
        "在闭环下、频率远低于电流环带宽时，该刚度可以非常大；但在开环和 high frequency 下，它就是定子的每相阻抗",
    "of the stator.": "。",
    "— we want oscillations in current to decay and not persist or grow. An important quantity for stability is phase margin":
        "——我们希望电流振荡能衰减而非持续或增长。稳定性的一个重要指标是相位裕量",
    "More specifically, the tuning goals are to": "更具体地说，整定目标是",
    "constrain error": "限制误差",
    "constrain overshoot": "限制超调",
    "maximize bandwidth": "最大化带宽",
    "Current control error can cause vibration and audible noise within the motor. In extreme cases it can add excess thermal dissipation, damage components (if the overcurrent is not detected), or cause nuisance faults (if the overcurrent is detected).":
        "电流控制误差会在电机内引起振动和可听噪声。在极端情况下，它会增加额外功耗、损坏器件（若过流未被检测到）或引起误报故障（若过流被检测到）。",
    "Phase margin should be selected to keep overshoot small. Acceptable values of overshoot are typically in the 0-10% range. This depends on the application as well as the frequency content of the current reference. The worst-case step of full negative current to full positive current is not necessarily something that occurs in a real application, but if it is, causing false overcurrent faults should be avoided. For example, a motor drive that can accept reference currents up to 10 A that undergoes a worst-case step from -10 A to +10 A and has a 10% overshoot would reach a maximum current of +12 A. There should be enough design margin between this maximum current and the minimum overcurrent threshold to allow room for noise while still avoiding false overcurrent faults.":
        "应选择合适的相位裕量以保持较小的超调。可接受的超调通常在 0–10% 范围内。这取决于应用以及电流参考的频率成分。从满负向电流到满正向电流的最坏阶跃未必在实际应用中出现，但如果出现，应避免引起误过流故障。例如，一个可接受高达 10 A 参考电流的电机驱动，若经历从 -10 A 到 +10 A 的最坏阶跃且有 10% 超调，将达到 +12 A 的最大电流。该最大电流与最低过流阈值之间应有足够的设计裕量，以容纳噪声同时仍避免误过流故障。",
    "Current control bandwidth should generally be maximized as long as it does not degrade stability or introduce excessive noise into the motor current. Typical 3dB current bandwidth of industrial motor drives are 5% – 15% of the PWM frequency, or 1 – 3 kHz for a 20 kHz PWM. This is desirable even if the overall motor control bandwidth of position or velocity is slow, for example a pump or fan operating at constant velocity. It improves disturbance rejection and reduces the duration of overcurrent events.":
        "电流控制带宽一般应最大化，只要不降低稳定性或给电机电流引入过多噪声。工业电机驱动的典型 3dB 电流带宽为 PWM 频率的 5%–15%，即 20 kHz PWM 时为 1–3 kHz。即使位置或速度的整体电机控制带宽较慢（例如恒速运行的水泵或风机），这也是可取的。它能改善扰动抑制并缩短过流事件的持续时间。",
    "Applications that do require fast acceleration (robotics and e-mobility, for example) are constrained by the performance of the current loop; the velocity loop bandwidth is generally 5 – 10 times lower than the current loop bandwidth.":
        "确实需要快速加速的应用（例如机器人和电动出行）受电流环性能约束；速度环带宽一般比电流环带宽低 5–10 倍。",
    # examples
    "The best way to evaluate current loop performance is with a step response test at constant velocity. The easiest way of doing this with MCAF is to use the":
        "评估电流环性能的最佳方法是在恒定速度下进行阶跃响应测试。在 MCAF 中最简单的方法是使用",
    "(see": "（见",
    ") with one of the following:": "）并采用以下方式之一：",
    "clamping the rotor to prevent movement": "夹紧转子以阻止运动",
    "running the motor with open-loop commutation, using a fixed commutation angle (see section on":
        "以开环换相运行电机，使用固定换相角（参见关于",
    "controlling the motor to run at constant velocity, with a low-bandwidth velocity loop. (This lets the motor accelerate or decelerate slightly; rotor inertia will smooth out velocity.)":
        "控制电机恒速运行，使用低带宽速度环。（这允许电机轻微加速或减速；转子惯性会平滑速度。）",
    "A square wave perturbation in the 20 Hz – 200 Hz range is recommended: for 20 kHz control rate, this corresponds to values of":
        "建议使用 20 Hz–200 Hz 范围内的方波扰动：对于 20 kHz 控制速率，这对应",
    "between 500 and 50. In general the period of the square wave should be just long enough for transients to complete.":
        "在 500 到 50 之间的值。一般而言，方波周期应刚好让暂态完成即可。",
    "Note:": "注：",
    "Pay special attention to motor commutation. Sensorless position estimators add their own sources of error to commutation angle, and may not be practical to use at zero speed to test current loop tuning. Except where noted, all graphs in this section show data from a motor using a":
        "请特别注意电机换相。无传感器位置估计器会给换相角带来自身的误差源，在零速下用于测试电流环整定可能不实用。除特别说明外，本节所有图中的数据均来自使用",
    "for commutation. See the last section on": "进行换相的电机。请参见最后一节关于",
    "for more information.": "以获取更多信息。",
    "Operation with open-loop commutation may also be required for current loop tuning if": "如果",
    "fails to run or transition properly into closed-loop commutation.": "无法正常运行或无法正确过渡到闭环换相，则电流环整定也可能需要开环换相运行。",
    # zero velocity
    "shows an example of the current loop step response of the": "展示了",
    "motor operated with MCAF on the": "电机在 MCAF 上、使用",
    ", with default tuning in motorBench": "运行时的电流环阶跃响应示例，采用 motorBench",
    "Case 0: Current loop step response with phase margin": "情形 0：电流环阶跃响应，相位裕量",
    "and PI phase lag at crossover": "，交叉频率处 PI 相位滞后",
    "0.414 V/A,": "0.414 V/A，",
    "613 V/As). All cases in this section have dead time reduced from 2 μs to 1.2 μs to minimize the effects of dead-time distortion. Step-response graphs included in this section all contain values for phase margin, PI phase lag at crossover (see":
        "613 V/As）。本节所有情形均将死区从 2 μs 减小到 1.2 μs，以最小化死区畸变的影响。本节所含的阶跃响应图均在标题中包含相位裕量、交叉频率处 PI 相位滞后（定义见",
    "for a definition), and crossover frequency": "）以及交叉频率",
    "in the graph title.": "的值。",
    "This current loop has a low bandwidth — so low that current does not reach its steady-state value because the velocity is allowed to vary, and the changing back-emf, which results from changes in velocity, acts as a disturbance to the current loop. To avoid this effect, the product of mechanical time constant":
        "该电流环带宽较低——低到电流无法达到稳态值，因为允许速度变化，而速度变化引起的反电动势变化作为扰动作用于电流环。为避免此效应，机械时间常数",
    "and current loop bandwidth should be much greater than 1. For the Nidec Hurst DMA0204024B101, the mechanical time constant":
        "与电流环带宽的乘积应远大于 1。对于 Nidec Hurst DMA0204024B101，机械时间常数",
    "3.25 ms, and in this particular instance (Case 0) the product": "为 3.25 ms，在本例（情形 0）中乘积",
    "= 4.8, not high enough to mitigate the effect of changing back-emf.": "= 4.8，不足以消除反电动势变化的影响。",
    "Several other cases, with the same motor and board, are summarized in": "使用同一电机和板卡的若干其他情形汇总于",
    # table headers
    "(rad/s)": "(rad/s)",
    "(Hz)": "(Hz)",
    "(V/A)": "(V/A)",
    "(V/As)": "(V/As)",
    # cases
    "The next case (1), shown in": "下一个情形（1）如",
    ", has slightly lower phase margin and PI phase at crossover, which results in higher bandwidth and a better step response. This looks similar to Case 0 in shape, but the time scale here is 2.5× faster.":
        "所示，相位裕量和交叉频率处 PI 相位略低，从而带宽更高、阶跃响应更好。其形状与情形 0 类似，但时间尺度快了 2.5 倍。",
    "Case 1: Current loop step response with": "情形 1：电流环阶跃响应，",
    "1.226 V/A,": "1.226 V/A，",
    "2121 V/As).": "2121 V/As）。",
    "The early part of the step response (during the first 100 μs or so) is dominated by the proportional gain":
        "阶跃响应的早期部分（约前 100 μs）由比例增益",
    ". This causes a rapid pulse in voltage. As the current approaches its reference value and the error decreases, the response becomes dominated by the integral term; the integral gain":
        "主导。这会引起一个快速的电压脉冲。当电流接近其参考值且误差减小时，响应转由积分项主导；积分增益",
    "determines how fast this transition occurs.": "决定该过渡发生的快慢。",
    "The response of Case 1 can still be improved.": "情形 1 的响应仍可改进。",
    "Case 2, in": "情形 2 如",
    ", shows a well-tuned current loop. This has fast bandwidth of about": "所示，展示了一个整定良好的电流环。其快速带宽约为",
    "(where": "（其中",
    "is the sampling and control rate) and a reasonably good step response without overshoot. Improving bandwidth beyond":
        "为采样和控制速率），阶跃响应相当好且无超调。将带宽提升到",
    "can be done, but is tricky and requires careful attention to discrete-time design as well as the sample-to-output delay.":
        "以上是可以做到的，但比较棘手，需要仔细处理离散时间设计以及采样到输出延迟。",
    "Again, note the initial voltage impulse beyond the final value required to maintain current at its reference value.":
        "再次注意，初始电压脉冲超出了维持电流在参考值所需的最终值。",
    "Case 2: Well-tuned current loop step response with": "情形 2：整定良好的电流环阶跃响应，",
    "4.487 V/A,": "4.487 V/A，",
    "12168 V/As).": "12168 V/As）。",
    "Case 3, in": "情形 3 如",
    ", shows a current loop with gains that are too high, causing excessive overshoot. Here the overshoot is only about 12%, but if we operate at":
        "所示，展示了一个增益过高的电流环，导致过大超调。此处超调仅约 12%，但若在",
    "nonzero velocities": "非零速度",
    "the overshoot will get worse.": "下运行，超调会恶化。",
    "Case 3: High-gain current loop step response with": "情形 3：高增益电流环阶跃响应，",
    "7.038 V/A,": "7.038 V/A，",
    "12107 V/As).": "12107 V/As）。",
    "Case 4, in": "情形 4 如",
    ", shows a current loop with about the same proportional gain": "所示，展示了一个比例增益大致相同",
    "but a much lower integral gain. The proportional gain yields a very good short-term response, but the low integral gain causes a much slower settling time towards the final value.":
        "但积分增益低得多的电流环。比例增益带来非常好的短期响应，但低积分增益导致趋向最终值的调节时间慢得多。",
    "Case 4: Current loop step response with": "情形 4：电流环阶跃响应，",
    "4.473 V/A,": "4.473 V/A，",
    "2920 V/As).": "2920 V/As）。",
    "Finally, Case 5, in": "最后，情形 5 如",
    ", shows the same phase margin and PI phase lag at crossover as Case 0, but with an external inertial load added to increase the rotor inertia by about a factor of 3. Current loop tuning doesn’t change much, but note the improved settling of the current loop caused by the reduction in velocity fluctuation.":
        "所示，其相位裕量和交叉频率处 PI 相位滞后与情形 0 相同，但增加了外部惯性负载，使转子惯量约增大 3 倍。电流环整定变化不大，但请注意速度波动减小带来的电流环调节改善。",
    "Case 5: Current loop step response with": "情形 5：电流环阶跃响应，",
    "but with": "但带有",
    "0.418 V/A,": "0.418 V/A，",
    "566 V/As)": "566 V/As）",
    # nonzero velocity
    "At low velocities, the current loop step response does not change much.":
        "在低速下，电流环阶跃响应变化不大。",
    "As the rotor velocity increases, there are cross-axis coupling effects between the d- and q-axes that change the step response somewhat.":
        "随着转子速度升高，d 轴和 q 轴之间存在交叉轴耦合效应，会使阶跃响应有所变化。",
    "For this reason, it is important to verify current loop tuning at the upper end of the velocity range.":
        "因此，在速度范围的上限验证电流环整定很重要。",
    "Avoiding voltage saturation is important for the purposes of tuning, so either use an elevated DC link voltage, or choose a velocity that is about 80-90% of maximum velocity.":
        "为整定目的，避免电压饱和很重要，因此可使用升高的母线电压，或选择约为最大速度 80–90% 的速度。",
    "Below are the step responses of cases 1 – 3 at 1200 RPM and 2400 RPM.":
        "下面是情形 1–3 在 1200 RPM 和 2400 RPM 下的阶跃响应。",
    "In the low-gain controller cases of": "在低增益控制器的情形",
    "and": "和",
    ", the voltage disturbances of dead-time distortion and back-emf harmonics can cause moderate error, compared to the step response seen at zero velocity.":
        "中，与零速下看到的阶跃响应相比，死区畸变和反电动势谐波造成的电压扰动会引起中等程度的误差。",
    "Case 1: Current loop step response of low-gain controller with": "情形 1：低增益控制器的电流环阶跃响应，",
    "at 1200 RPM.": "，1200 RPM。",
    "at 2400 RPM.": "，2400 RPM。",
    "In the well-tuned case of": "在整定良好的情形",
    ", the increased gain improves disturbance rejection, reducing the error from the current reference.":
        "中，增大的增益改善了扰动抑制，减小了相对于电流参考的误差。",
    "In the high-gain case of": "在高增益的情形",
    ", the current overshoot increases with increasing velocity, reaching 20% overshoot at 2400 RPM. This is undesirable and may become worse than shown here due to several causes:":
        "中，电流超调随速度升高而增大，在 2400 RPM 时达到 20% 超调。这是不希望的，且可能因以下几种原因变得比此处所示更糟：",
    "part-to-part variations in the motor parameters": "电机参数的个体差异",
    "part-to-part variations in current sense circuitry in the drive electronics": "驱动电子设备中电流检测电路的个体差异",
    "resistance and back-emf changes with temperature": "电阻和反电动势随温度变化",
    "inductance changes with iron saturation": "电感随铁芯饱和变化",
    "In short: if at all possible, avoid overshoot and leave design margin for parameter tolerances.":
        "简而言之：尽可能避免超调，并为参数容差留出设计裕量。",
    # sample-to-update delay
    "A critical bottleneck in providing stable high-bandwidth current loops is the sample-to-update delay":
        "提供稳定高带宽电流环的一个关键瓶颈是采样到更新延迟",
    ". This is the delay between the instant the ADC inputs are sampled, and the instant the duty cycle of the transistors changes based on the values of those sampled inputs.":
        "。它是 ADC 输入被采样的时刻与晶体管占空比基于这些采样值发生变化的时刻之间的延迟。",
    "Reducing the delay": "减小该延迟",
    "allows for a more stable current loop at a given bandwidth, or a higher bandwidth for equivalent stability. The difference is most pronounced at high bandwidths (5% or more of the sampling frequency, e.g. 1 kHz and greater for a 20 kHz sampling-and-update rate)":
        "能在给定带宽下获得更稳定的电流环，或在同等稳定性下获得更高带宽。这种差异在高带宽（采样频率的 5% 或更高，例如 20 kHz 采样和更新速率下 1 kHz 及以上）时最为显著",
    "Use of": "使用",
    "is recommended, to help reduce sample-to-update delay.": "有助于减小采样到更新延迟，推荐使用。",
    # tuning criteria
    "The autotuning feature of motorBench": "motorBench",
    "Development Suite allows adjustment of two performance criteria for both the current and velocity loops:":
        "Development Suite 的自动整定功能允许对电流环和速度环各调整两个性能准则：",
    "is the difference between -180° and the phase of open-loop gain transfer function at the crossover frequency":
        "是 -180° 与开环增益传递函数在交叉频率",
    ", where the open-loop gain has magnitude 1. This represents design margin from the point of instability. Decreased phase margin generally raises both proportional gain":
        "处相位的差值，此处开环增益幅值为 1。它代表距失稳点的设计裕量。减小相位裕量通常会同时提高比例增益",
    ". This can increase the maximum achievable bandwidth and improve the performance of reference tracking and disturbance rejection, but at the cost of decreased stability.":
        "。这可以提高最大可实现带宽并改善参考值跟踪和扰动抑制性能，但代价是稳定性下降。",
    "is the phase lag of the PI controller at the crossover frequency. Decreased PI phase lag at crossover decreases the corner frequency (or “zero”) of the PI controller, decreasing integral gain":
        "是 PI 控制器在交叉频率处的相位滞后。减小交叉频率处 PI 相位滞后会降低 PI 控制器的转折频率（或“零点”），从而减小积分增益",
    "and increasing proportional gain": "并增大比例增益",
    ". With a fixed phase margin, this generally increases the current loop bandwidth, but at the cost of decreased gain at low frequencies, which reduces the controller’s disturbance rejection.":
        "。在相位裕量固定时，这通常会提高电流环带宽，但代价是低频增益下降，从而降低控制器的扰动抑制能力。",
    "While phase margin may be familiar to engineers with a rudimentary knowledge of control systems, PI phase lag at crossover may not.":
        "相位裕量对具备控制系统基础知识的工程师可能很熟悉，但交叉频率处 PI 相位滞后可能不然。",
    "shows a Bode plot of the current loop transfer functions for the Nidec Hurst DMA0204024B101, with the following elements:":
        "展示了 Nidec Hurst DMA0204024B101 电流环传递函数的伯德图，包含以下元素：",
    "The plant transfer function G(s), representing voltage-to-current gain, is drawn in a thin dash-dot line":
        "被控对象传递函数 G(s)（表示电压到电流增益）以细点划线绘制",
    "PI controller transfer functions K(s), representing current-to-voltage gain, are drawn in dashed lines":
        "PI 控制器传递函数 K(s)（表示电流到电压增益）以虚线绘制",
    "Open-loop gain transfer functions G(s)K(s) are drawn in solid lines": "开环增益传递函数 G(s)K(s) 以实线绘制",
    "The transfer functions are evaluated and marked with a small dot at the crossover frequency. Note that in":
        "这些传递函数在交叉频率处求值并用小圆点标记。注意在",
    ", the open-loop gain transfer function has a phase of -105°, in order to meet the phase margin constraint of 75°.":
        "中，开环增益传递函数的相位为 -105°，以满足 75° 的相位裕量约束。",
    "The PI controller zero, which is the frequency where proportional and integral gain are equal and the phase is -45°, is marked with an open circle. The ratio of the PI controller zero to the crossover frequency is":
        "PI 控制器零点（即比例增益与积分增益相等、相位为 -45° 的频率）以空心圆标记。PI 控制器零点与交叉频率之比为",
    ", so that low values of PI phase lag at crossover push the controller zero to very low frequencies.":
        "，因此交叉频率处 PI 相位滞后值越小，控制器零点就被推到越低的频率。",
    "shows a Bode plot of the examples for cases 0 – 4 discussed earlier in this section.":
        "展示了本节前面讨论的情形 0–4 的示例伯德图。",
    "Cases 2 (": "情形 2（",
    ") and 3 (": "）和情形 3（",
    ") have the highest low-frequency open-loop gain, but the the lower phase margin of case 3 renders it undesirable.":
        "）的低频开环增益最高，但情形 3 较低的相位裕量使其不可取。",
    "The default values chosen for the current loop in motorBench": "motorBench 中为电流环选择的默认值",
    "Development Suite versions 1.15 – 2.35, namely": "Development Suite 1.15–2.35 版本，即",
    ", are stable for a very wide range of motors. They are also extremely conservative, and result in a current loop bandwidth that is rather low.":
        "，对非常宽范围的电机都是稳定的。但它们也极其保守，导致电流环带宽相当低。",
    "Microchip staff is re-evaluating these default values for a higher-performance recommendation. In the interim, if careful step-response testing is possible, consider reducing phase margin to the 50° – 70° range and reducing PI phase lag at crossover to the 8° – 20° range.":
        "Microchip 人员正在重新评估这些默认值以给出更高性能的建议。在此期间，如果可以进行仔细的阶跃响应测试，可考虑将相位裕量降至 50°–70° 范围，并将交叉频率处 PI 相位滞后降至 8°–20° 范围。",
    "Do not decrease these values below the defaults without testing.":
        "未经测试，不要将这些值降到默认值以下。",
    "PI phase lags below 5° are not recommended without careful study.":
        "未经仔细研究，不建议将 PI 相位滞后降到 5° 以下。",
    "Autotuning uses these performance criteria, rather than PI gains or loop bandwidth, as a normalized specification that is somewhat applicable across a wide range of motor and drive combinations. Are the exact values for phase margin and PI phase lag at crossover for the Nidec Hurst DMA0204024B101 shown here in the well-tuned case (":
        "自动整定使用这些性能准则，而非 PI 增益或环路带宽，作为一种归一化指标，它在较宽范围的电机和驱动组合中具有一定的适用性。此处整定良好情形（",
    ") applicable to all motors? No. Each motor and drive combination has different characteristics, and there are often subtle second-order effects that may warrant higher or lower settings.":
        "）中所示的 Nidec Hurst DMA0204024B101 的相位裕量和交叉频率处 PI 相位滞后的确切值是否适用于所有电机？否。每个电机和驱动组合都有不同的特性，且常常存在可能需要更高或更低设置的微妙二阶效应。",
    "If you have a motor that seems difficult to tune, please": "如果您的电机似乎难以整定，请",
    "so that we can improve our recommendations.": "以便我们改进建议。",
    # adjusting gains
    "The best way to adjust current control gains in MCAF is to change the performance criteria (phase margin":
        "在 MCAF 中调整电流控制增益的最佳方式是在 motorBench",
    ") in the Tune page of motorBench": "的 Tune（整定）页面中更改性能准则（相位裕量",
    "Development Suite. This may require repeated iterations of code generation, however.":
        "Development Suite）。但这可能需要反复迭代生成代码。",
    "To fine-tune the current loop more quickly, it is possible to change the current loop gains at runtime directly, by changing the proportional and integral gains of both d-axis and q-axis current loops, using a real-time diagnostic tool to adjust the MCAF variables shown in":
        "要更快地细调电流环，可在运行时直接更改电流环增益，即使用实时诊断工具调整 d 轴和 q 轴电流环的比例和积分增益，所调整的 MCAF 变量如",
    "(Note that there are also runtime shift counts with the same variable names as the gains, preceded by an": "（注意还有与增益同名的运行时移位计数，前面带一个",
    ", for example": "，例如",
    "motor.idCtrl.nkp": "motor.idCtrl.nkp",
    "for the shift count corresponding to": "为对应于",
    ".kp": ".kp",
    ". If the desired gain would overflow (above 32767 counts), then subtract one from the shift count and divide the gain counts by two.":
        "的移位计数。如果所需增益会溢出（超过 32767 个计数），则将移位计数减一并将增益计数除以 2。",
    "38000,": "38000，",
    ".nkp": ".nkp",
    "15": "15",
    ", which is not representable, is equivalent to": "（无法表示）等价于",
    "19000,": "19000，",
    "14": "14",
    ", which is representable.)": "（可表示）。",
    "The recommended approach is as follows:": "推荐方法如下：",
    "Make a copy of the initial gains generated by motorBench": "复制 motorBench",
    "Development Suite, found in": "Development Suite 生成的初始增益，位于",
    "Adjust current loop gains at runtime, using a real-time diagnostic tool to perform step-response testing. The most important software variables to watch are":
        "在运行时调整电流环增益，使用实时诊断工具进行阶跃响应测试。需要观察的最重要的软件变量是",
    "motor.idq.q": "motor.idq.q",
    "— Q-axis current": "——q 轴电流",
    "motor.idqCmd.q": "motor.idqCmd.q",
    "— Q-axis current reference": "——q 轴电流参考",
    "motor.vdq.q": "motor.vdq.q",
    "— Q-axis voltage output from PI controller": "——PI 控制器输出的 q 轴电压",
    "Determine desired software gains empirically": "通过实验确定所需的软件增益",
    "Compute real-world gains corresponding to the software gains": "计算与软件增益对应的实际工程增益",
    "Adjust": "调整",
    "in the Tune page of motorBench": "在 motorBench 的 Tune（整定）页面中",
    "Development Suite to produce gains that are close to the desired real-world gains. (At this time, entry of PI gains in the Tune page is not possible, but it may be considered in future versions.)":
        "Development Suite，以产生接近所需实际工程增益的值。（目前 Tune 页面尚不支持直接输入 PI 增益，但未来版本可能会考虑。）",
    "shows an example set of gains in": "展示了",
    "generated by motorBench": "中由 motorBench",
    "//************** PI Coefficients **************": "//************** PI 系数 **************",
    "//// Current loop": "//// 电流环",
    "// phase margin = 80 deg": "// 相位裕量 = 80 度",
    "// PI phase at crossover = 45.000 deg": "// 交叉频率处 PI 相位 = 45.000 度",
    "// crossover frequency = 1.478 k rad/s (235.238 Hz)": "// 交叉频率 = 1.478 k rad/s (235.238 Hz)",
    "/* Current loop proportional gain */": "/* 电流环比例增益 */",
    "#define KIP 2263": "#define KIP 2263",
    "// Q15( 0.06906) = +414.36768 mV/A = +414.42006 mV/A - 0.0126%": "// Q15( 0.06906) = +414.36768 mV/A = +414.42006 mV/A - 0.0126%",
    "#define KIP_Q 15": "#define KIP_Q 15",
    "/* Current loop integral gain */": "/* 电流环积分增益 */",
    "#define KII 167": "#define KII 167",
    "// Q15( 0.00510) = +611.57227 V/A/s = +612.53173 V/A/s - 0.1566%": "// Q15( 0.00510) = +611.57227 V/A/s = +612.53173 V/A/s - 0.1566%",
    "#define KII_Q 15": "#define KII_Q 15",
    "Suppose that a well-tuned current loop response can be obtained using a real-time diagnostic tool with the following software gains:":
        "假设使用实时诊断工具，通过以下软件增益可获得整定良好的电流环响应：",
    "motor.idCtrl.kp": "motor.idCtrl.kp",
    "motor.iqCtrl.kp": "motor.iqCtrl.kp",
    "24500": "24500",
    "motor.idCtrl.ki": "motor.idCtrl.ki",
    "motor.iqCtrl.ki": "motor.iqCtrl.ki",
    "3300": "3300",
    "The engineering units can be computed by adjusting the original gain in engineering units by the ratio of new to old software values:":
        "工程单位可通过将原始工程单位增益乘以新软件值与旧软件值之比来计算：",
    "= (24500/2263) × 0.41437 = 4.4861 V/A": "= (24500/2263) × 0.41437 = 4.4861 V/A",
    "= (3300/167) × 611.57 = 12085 V/As": "= (3300/167) × 611.57 = 12085 V/As",
    "Then adjust phase margin": "然后在 motorBench",
    "of the current loop in the Tune page of motorBench": "的 Tune（整定）页面中调整电流环的相位裕量",
    "Development Suite to get close to these values. (Again, decreasing phase margin should increase both":
        "Development Suite，以接近这些值。（同样，减小相位裕量应同时增大",
    "; decreasing PI phase lag at crossover increases": "；减小交叉频率处 PI 相位滞后会增大",
    "and decreases": "并减小",
    # commutation angle issues
    "Commutation angle accuracy is not particularly critical during current loop tuning, as long as the total error is manageable. Typically a commutation angle error of 15° electrical is acceptable for field-oriented control. High-frequency content (oscillation in the commutation angle) will show up as a disturbance orthogonal to the current vector; in the normal case where D-axis current is approximately zero and the current vector is primarily along the Q-axis, then the D-axis current will show oscillations from commutation angle errors, whereas similar oscillations in the Q-axis current will be much smaller.":
        "电流环整定期间换相角精度并非特别关键，只要总误差可控即可。通常 15° 电角度的换相角误差对磁场定向控制是可接受的。高频成分（换相角振荡）会表现为与电流矢量正交的扰动；在 d 轴电流近似为零、电流矢量主要沿 q 轴的正常情况下，d 轴电流会显示来自换相角误差的振荡，而 q 轴电流中的类似振荡则小得多。",
    "If possible, perform step-response tuning using a quadrature encoder for commutation. Use a tracking loop time constant that is relatively slow: 5 ms is a good default choice.":
        "如果可能，请使用正交编码器进行换相来完成阶跃响应整定。使用相对较慢的跟踪环路时间常数：5 ms 是一个不错的默认选择。",
    "If a quadrature encoder is not available, then operation at zero speed may not be possible with closed-loop commutation. (The":
        "如果无法使用正交编码器，则零速下可能无法进行闭环换相运行。（",
    "is generally stable at zero speed, but cannot provide useful torque, whereas the ATPLL has stability issues around zero speed.) If this is the case, use open-loop commutation instead, by taking the following steps using the test harness and a real-time diagnostic tool:":
        "在零速下通常稳定，但无法提供有用转矩，而 ATPLL 在零速附近存在稳定性问题。）如果是这种情况，请改用开环换相，使用测试框架和实时诊断工具采取以下步骤：",
    "turn on the": "开启",
    "use a fixed commutation angle by setting": "通过设置",
    ", which controls the commutation frequency.": "来使用固定换相角，该变量控制换相频率。",
    "At zero speed, mechanically clamping the rotor can be helpful, but is not necessary, and will not suppress small high-frequency vibrations.":
        "在零速下，机械夹紧转子可能有帮助，但并非必需，且无法抑制小幅高频振动。",
    "Operation at nonzero speed to check current loop tuning should be done with closed-loop commutation. Again, a quadrature encoder is recommended, but a sensorless estimator may be used for commutation as long as the velocity is large enough for good performance.":
        "在非零速下检查电流环整定应使用闭环换相。再次建议使用正交编码器，但只要速度足够大以获得良好性能，也可使用无传感器估计器进行换相。",
    "Similar current loop evaluation can be done using the AN1292 PLL at zero speed in closed-loop commutation.":
        "可在零速下使用 AN1292 PLL 进行闭环换相，完成类似的电流环评估。",
    "show current loop evaluation of the Nidec Hurst DMA0204024B101 motor with the well-tuned current loop gains (":
        "展示了 Nidec Hurst DMA0204024B101 电机使用本节前面所用整定良好电流环增益（",
    ") that were used earlier in this section. To keep the current reference from changing quickly, the velocity loop bandwidth was lowered to around 2.2 Hz from the default tuning, by choosing":
        "）的电流环评估。为避免电流参考变化过快，通过选择",
    ". (This is not necessary in general — it just makes current loop tuning easier to avoid unnecessary distractions, and a higher-bandwidth velocity loop can be used after current loop tuning is complete.)":
        "，将速度环带宽从默认整定降至约 2.2 Hz。（这通常并非必要——只是让电流环整定更容易，避免不必要的干扰；电流环整定完成后可使用更高带宽的速度环。）",
    "Steps in the current reference at 1 ms intervals are visible due to angle and velocity uncertainty from the estimator, but otherwise the current loop tuning behaves almost identically to the case where a quadrature encoder is used for commutation angle.":
        "由于估计器的角度和速度不确定性，可见电流参考以 1 ms 间隔出现的阶跃，但除此之外，电流环整定的表现与使用正交编码器作为换相角的情形几乎完全相同。",
    "Case 2 with PLL: Well-tuned current loop step response with": "使用 PLL 的情形 2：整定良好的电流环阶跃响应，",
    "at 0 RPM. Velocity tuning has": "，0 RPM。速度整定为",
    "at 1200 RPM. Velocity tuning has": "，1200 RPM。速度整定为",
    "at 2400 RPM. Velocity tuning has": "，2400 RPM。速度整定为",
    # references
    "F. B. del Blanco, M. W. Degner and R. D. Lorenz,": "F. B. del Blanco, M. W. Degner and R. D. Lorenz,",
    "“Dynamic analysis of current regulators for AC motors using complex vectors”": "“Dynamic analysis of current regulators for AC motors using complex vectors”",
    "IEEE Transactions on Industry Applications": "IEEE Transactions on Industry Applications",
    ", vol. 35, no. 6, pp. 1424-1432, Nov/Dec. 1999.": ", vol. 35, no. 6, pp. 1424-1432, Nov/Dec. 1999.",
    "F. Briz, M. W. Degner and R. D. Lorenz,": "F. Briz, M. W. Degner and R. D. Lorenz,",
    "“Analysis and design of current regulators using complex vectors”": "“Analysis and design of current regulators using complex vectors”",
    ", vol. 36, no. 3, pp. 817-825, May/June 2000.": ", vol. 36, no. 3, pp. 817-825, May/June 2000.",
    # toc
    "5.1.6. Current loop tuning": "5.1.6. 电流环整定",
    "5.1.6.1. Background": "5.1.6.1. 背景",
    "5.1.6.2. Evaluating control performance": "5.1.6.2. 评估控制性能",
    "5.1.6.3. Examples of poorly-tuned and well-tuned current loops": "5.1.6.3. 整定不良与整定良好电流环的示例",
    "5.1.6.3.1. Current loop tuning at zero velocity": "5.1.6.3.1. 零速下的电流环整定",
    "5.1.6.3.2. Current loop tuning at nonzero velocity": "5.1.6.3.2. 非零速下的电流环整定",
    "5.1.6.3.3. Effects of sample-to-update delay": "5.1.6.3.3. 采样到更新延迟的影响",
    "5.1.6.4. Tuning criteria and motorBench": "5.1.6.4. 整定准则与 motorBench",
    "5.1.6.4.1. Performance criteria definitions": "5.1.6.4.1. 性能准则定义",
    "5.1.6.4.2. Bode plots of example cases": "5.1.6.4.2. 示例情形的伯德图",
    "5.1.6.4.3. Default values of performance criteria": "5.1.6.4.3. 性能准则的默认值",
    "5.1.6.5. Adjusting current control gains in MCAF": "5.1.6.5. 在 MCAF 中调整电流控制增益",
    "5.1.6.5.1. Example": "5.1.6.5.1. 示例",
    "5.1.6.6. Commutation angle issues during current loop tuning": "5.1.6.6. 电流环整定过程中的换相角问题",
    "5.1.6.6.1. Example using the AN1292 PLL": "5.1.6.6.1. 使用 AN1292 PLL 的示例",
    "5.1.6.7. References": "5.1.6.7. 参考文献",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
