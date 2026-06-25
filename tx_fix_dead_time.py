# -*- coding: utf-8 -*-
"""Fix remaining untranslated English text in dead-time-comp.zh.html."""
import txutil
from bs4 import BeautifulSoup

rel = "algorithms/dead-time-comp"
soup, path = txutil.load(rel + ".zh.html")
root = txutil.body(soup)

# Substring replacement pairs (longer fragments first to avoid conflicts)
pairs = [
    # ---- Section 5.7.2: Definition and origin of dead time ----
    ("Drive electronics for a three-phase", "三相"),
    ("includes a three-phase bridge shown in", "的驱动电子电路包括如"),

    ("The dead time is shown in", "死区如"),
    (", expressed as a fraction", "所示，表示为"),
    ("of the total PWM period", "占整个 PWM 周期的比例"),
    (". It is used to accommodate the time needed for switching transitions, and allow one transistor to turn off completely before the other starts turning on. This avoids shoot-through, where a temporary short-circuit occurs across the DC link and causes",
     "。它用于适应开关转换所需的时间，并允许一个晶体管在另一个开始导通之前完全关断。这避免了直通，即直流母线两端发生暂时短路并在两个晶体管中引起"),

    ("The signals in", "中的信号"),
    ("are described below.", "如下所述。"),

    ("Signal G is a raw generated pulse waveform with duty cycle", "信号 G 是原始生成的脉冲波形，占空比为"),
    ("Signal H is the gate drive signal for the high-side transistor, which is active for duty cycle",
     "信号 H 是高侧晶体管的栅极驱动信号，其有效占空比为"),
    ("Signal L is the gate drive signal for the low-side transistor, which is active for duty cycle",
     "信号 L 是低侧晶体管的栅极驱动信号，其有效占空比为"),

    ("When G turns on, the low-side gate drive L turns off instantly, but the high-side gate drive H is turned on after a delay of dead time",
     "当 G 导通时，低侧栅极驱动 L 立即关断，但高侧栅极驱动 H 在死区时间"),
    (". When G turns off, the high-side gate drive H turns off instantly, but the low-side gate drive L is turned on after a delay of dead time",
     "的延迟后导通。当 G 关断时，高侧栅极驱动 H 立即关断，但低侧栅极驱动 L 在死区时间"),

    # ---- Section 5.7.3.1: Output voltage during dead time ----
    ("Field-oriented control in MCAF uses average-value modeling. The control variables can be represented by the mean value over the sampling time, and the sampling time consists of a discrete number of half-periods. MCAF R1 – R9 all use a sampling time of 1 full PWM period. The mean output voltage of the half bridge during a PWM cycle is",
     "MCAF 中的矢量控制使用平均值建模。控制变量可以用采样时间内的平均值表示，采样时间由离散数量的半周期组成。MCAF R1 – R9 均使用 1 个完整 PWM 周期作为采样时间。PWM 周期内半桥的平均输出电压为"),

    ("During dead time, each half-bridge output is effectively in a high-impedance state, with voltage clamps at the DC link voltage rails from the freewheeling diodes of the power stage. (MOSFETs have intrinsic body diodes; IGBTs do not, and require anti-",
     "在死区期间，每个半桥输出实际上处于高阻状态，由功率级的续流二极管在直流母线电压轨处钳位。（MOSFET 具有固有体二极管；IGBT 没有，需要反并联二极管）"),

    ("This causes the output voltage during dead time to vary, depending on the output current. In a motor drive, the half-bridge load is inductive, so the output voltage is one of the following, as shown in",
     "这导致死区期间的输出电压随输出电流而变化。在电机驱动中，半桥负载是感性的，因此输出电压为以下之一，如"),

    ("If the output current is strictly positive (flowing out of the half bridge) during dead time, then the low-side free-wheeling diode turns on, and the output voltage is",
     "如果死区期间输出电流严格为正（从半桥流出），则低侧续流二极管导通，输出电压为"),
    (", namely a diode drop below the negative terminal of the DC link, as shown by the green curve in",
     "，即低于直流母线负端一个二极管压降，如"),

    ("If the output current is strictly negative (flowing into of the half bridge) during dead time, then the high-side free-wheeling diode turns on, and the output voltage is",
     "如果死区期间输出电流严格为负（流入半桥），则高侧续流二极管导通，输出电压为"),
    (", namely a diode drop above the positive terminal of the DC link, as shown by the black curve in",
     "，即高于直流母线正端一个二极管压降，如"),

    ("If the output current reaches zero during the dead time, then the half-bridge undergoes discontinuous conduction, and the voltage is determined by interaction of the inductive load with the parasitic capacitance",
     "如果死区期间输出电流达到零，则半桥进入断续导通，电压由感性负载与半桥的寄生电容"),
    ("and leakage resistance", "和漏电阻"),
    ("of the half-bridge. This can lead to voltage oscillations at frequency",
     "的相互作用决定。这可能导致频率为"),
    (", as shown by the red and orange curves in",
     "的电压振荡，如"),
    (". The exact waveform is hard to predict, and very sensitive to slight changes in output current.",
     "的红色和橙色曲线所示。精确波形难以预测，且对输出电流的微小变化非常敏感。"),

    ("show oscilloscope traces captured to illustrate the effect of dead time on the dsPICDEM",
     "展示了示波器捕获的波形，用于说明死区对 dsPICDEM"),
    ("MCLV\u20112 Development Board running at 24Vdc, at 1 \u03bcs/division timebase and 10 V/division on the phase voltage measurement.",
     "MCLV-2 开发板的影响，该板运行在 24Vdc，时间基为 1 μs/格，相电压测量为 10 V/格。"),

    # ---- Section 5.7.3.2: Analysis of error bounds ----
    ("The mean voltage over the sampling time can be bounded by looking at the upper and lower bounds caused by high positive and high negative currents during dead time. These are the green and black curves in",
     "采样时间内的平均电压可以通过观察死区期间大正电流和大负电流引起的上下界来限定。这些是"),
    ("; similar curves are shown in", "中的绿色和黑色曲线；类似的曲线如"),
    ("labeled with effective duty cycles", "所示，标注了有效占空比"),

    ("The major term in effective duty cycle error is just", "有效占空比误差的主要项仅为"),
    ("caused directly by dead time at currents which are not near zero. There are a few secondary effects:",
     "，由电流不在零附近时的死区直接引起。还有一些次要效应："),

    ("during dead time — the resulting error tends to be very small: for example, a 1-volt drop on a 24-volt system during a total dead time of 4% of the entire PWM cycle represents an effective duty cycle error of 4% / 24 = 0.17%. It affects very low voltage systems most severely, but these are also cases where dead time can usually be reduced. Furthermore, since its effect is proportional to dead time, it can be lumped into an effective dead time",
     "在死区期间的二极管压降——由此产生的误差往往非常小：例如，在 24 伏系统中 1 伏压降，在整个 PWM 周期总死区时间为 4% 时，代表有效占空比误差为 4% / 24 = 0.17%。它对极低电压系统影响最严重，但这些情况下死区通常可以减小。此外，由于其效应与死区时间成正比，可以合并到有效死区时间"),

    ("Asymmetry in turn-on and turn-off times — this is shown in",
     "导通和关断时间的不对称——这如"),
    (". It effectively lengthens the dead time by the difference between turn-on and turn-off times, since turn-off in a well-designed motor drive is usually faster than turn-on — although it could also reduce the effective dead-time if turn-off is slower than turn-on.",
     "所示。它通过导通和关断时间之差有效地延长了死区时间，因为在设计良好的电机驱动中，关断通常比导通快——尽管如果关断比导通慢，它也可能减小有效死区时间。"),
    ("This appears to be the case in the oscilloscope traces captured in",
     "在示波器波形中似乎就是这种情况，这些波形捕获于"),
    (": the time span of output voltage transitions is smaller than the dead time. This effect can also be lumped into an effective dead time",
     "：输出电压转换的时间跨度小于死区时间。此效应也可合并到有效死区时间"),

    ("Discontinuous conduction — this is discussed in the next section.",
     "断续导通——这在下一节中讨论。"),

    # ---- Section 5.7.3.3: Behavior during discontinuous conduction ----
    ("When currents are near zero and the half-bridge enters discontinuous conduction, the effective duty cycle error",
     "当电流接近零且半桥进入断续导通时，有效占空比误差"),
    ("is between the upper and lower bounds", "介于上下界之间"),
    (", and is a function of current that is difficult to model.",
     "，且是电流的函数，难以建模。"),

    ("isolates the interesting behavior for currents", "分离了电流在"),
    ("near zero, in a nonlinear function", "附近零时的有趣行为，用非线性函数"),
    (", which is some difficult-to-model empirical nonlinear function that maps the input range [-1,1] into the output range [-1,1]. In most cases, there is no need to know what it really is; some examples of nonlinear functions",
     "表示，它是一个难以建模的经验非线性函数，将输入范围 [-1,1] 映射到输出范围 [-1,1]。在大多数情况下，不需要知道它究竟是什么；一些非线性函数"),
    ("are shown in", "的示例如"),
    (". The dead-time compensation in MCAF just assumes a linear function",
     "所示。MCAF 中的死区补偿仅假设线性函数"),

    ("varying in their behavior within the range", "在其行为范围内变化"),
    (", including the sign function, the identity, a", "，包括符号函数、恒等函数、"),
    (", and a constant.", "和常数。"),

    ("The magnitude of current", "电流幅值"),
    ("under which discontinuous conduction is possible is approximately equal to the current ripple. Its behavior is within the discontinuous conduction zone is dependent on the relative magnitudes of",
     "以下可能发生断续导通的值约等于电流纹波。其在断续导通区内的行为取决于"),
    ("and characteristic current", "和特征电流"),
    ("required to charge the parasitic capacitance", "的相对大小，后者是充电寄生电容"),
    (". Reference", "所需的。参考文献"),
    ("discusses both effects in detail.", "详细讨论了这两种效应。"),

    # ---- Section 5.7.3.4: Dead-time distortion voltage in field-oriented current control ----
    ("shows the unit voltage disturbance", "展示了单位电压扰动"),
    ("in various reference frames, assuming sinusoidal currents and smooth angular rotation, and neglecting the discontinuous conduction zone.",
     "在各种参考坐标系中的情况，假设正弦电流和平滑角旋转，并忽略断续导通区。"),

    ("— phase currents with some amplitude", "——相电流，幅值为"),
    ("— sign of the corresponding current, with amplitude", "——对应电流的符号，幅值为"),
    (". This represents a constant amplitude of", "。这表示恒定幅值"),
    ("and an angle that jumps by 60° at each zero-crossing of current.",
     "和每次电流过零时跳变 60° 的角度。"),
    ("in the synchronous reference frame.", "在同步参考坐标系中。"),

    ("Both d- and q-axis disturbances follow sinusoidal waveforms every 60° electrical angle. If the current vector is along the q-axis, then the unit d-axis disturbance",
     "d 轴和 q 轴扰动每 60° 电气角度遵循正弦波形。如果电流矢量沿 q 轴方向，则单位 d 轴扰动"),
    ("is centered around an angular disturbance of zero, with no DC offset. The unit q-axis disturbance",
     "以零角度扰动为中心，无直流偏移。单位 q 轴扰动"),
    ("is centered around 90°, with smaller variation and a nonzero offset. For a unit dead-time distortion amplitude on each half-bridge, relevant characteristics of these waveforms are listed in",
     "以 90° 为中心，变化较小且有非零偏移。对于每个半桥上的单位死区畸变幅值，这些波形的相关特性列于"),

    ("If the current vector contains a d-axis component, as in the", "如果电流矢量包含 d 轴分量，如"),
    (", then the dead-time disturbance will be centered around the direction of the current vector, instead of around the q-axis.",
     "中那样，则死区扰动将以电流矢量方向为中心，而不是以 q 轴为中心。"),

    ("These are the effects of unit voltage disturbances. In a real system, the voltage disturbance when the current magnitude is large (avoiding discontinuous conduction) are",
     "这些是单位电压扰动的效应。在实际系统中，当电流幅值较大（避免断续导通）时，电压扰动为"),
    ("in each reference frame. In other words:", "在每个参考坐标系中。换言之："),

    ("In the stationary frame, the dead-time voltage disturbance is", "在静止坐标系中，死区电压扰动为"),
    ("In the synchronous frame, the dead-time voltage disturbance is", "在同步坐标系中，死区电压扰动为"),
    (", also with amplitude", "，幅值也为"),
    (", but sweeping across an arc within ±30° of the current vector. Peak, mean, and RMS disturbances in the dq reference frame can also be computed proportionally, so that a 4% dead time (2 μs for each transition in a 50 μs PWM period) with a 24V DC link",
     "，但在电流矢量 ±30° 范围内扫过一个弧。dq 参考坐标系中的峰值、均值和有效值扰动也可按比例计算，因此 4% 的死区（50 μs PWM 周期中每次转换 2 μs）在 24V 直流母线下"),
    ("and a current vector along the q-axis should experience a mean q-axis disturbance of approximately",
     "和沿 q 轴的电流矢量应经历约"),

    ("The voltage disturbances from dead-time distortion may also be visualized as an x-y plot (α-β or d-q).",
     "死区畸变的电压扰动也可以可视化为 x-y 图（α-β 或 d-q）。"),
    ("shows such plots in the case of a PMSM in the motoring quadrant. In the stationary frame, dead-time distortion maps a circular voltage trajectory into 6 disconnected arcs that look something like a sawblade. In the synchronous frame, dead-time distortion maps a single point, representing constant dq voltage, to a small arc with a mean DC offset along the q-axis that subtracts from the desired voltage.",
     "展示了 PMSM 在电动象限中的此类图。在静止坐标系中，死区畸变将圆形电压轨迹映射为 6 段不连续弧，看起来像锯齿。在同步坐标系中，死区畸变将代表恒定 dq 电压的单个点映射为一个小弧，沿 q 轴有均值直流偏移，从期望电压中减去。"),

    ("In the generating quadrant, the direction of voltage disturbance would be reversed and would cause a mean DC offset along the q-axis that adds to the desired voltage.",
     "在发电象限中，电压扰动方向将反转，并导致沿 q 轴的均值直流偏移叠加到期望电压上。"),

    ("that leads the current by 30° electrical, and a product", "超前电流 30° 电气角度，乘积"),
    ("(product of dead time fraction and DC link voltage) that is", "（死区比例与直流母线电压的乘积）为"),
    (". In this case, the disturbance in the αβ and dq frames has amplitude",
     "。在此情况下，αβ 和 dq 坐标系中的扰动幅值为"),

    # ---- Section 5.7.4.1: Dead-time distortion and field-oriented current control ----
    ("shows measured and predicted voltage requirements for the Nidec Hurst DMA0204024B101 at low velocity (about 240RPM) and various dead times, driven with the dsPICDEM",
     "展示了 Nidec Hurst DMA0204024B101 在低速（约 240RPM）和不同死区下的测量和预测电压需求，由 dsPICDEM"),
    ("MCLV‑2 Development Board, and running with a smooth, light load that requires",
     "MCLV-2 开发板驱动，运行在平滑轻载条件下，需要"),
    ("0.5 A. The left-hand graph shows the stationary-frame output voltage",
     "0.5 A。左图显示静止坐标系输出电压"),
    (". The red circle is the back-emf magnitude. The blue, orange, and green scatter plots show measured samples of αβ-frame voltage at 1, 2, and 3 microsecond dead-times. Black dots mark the predicted output voltage based on a pure signum function",
     "。红色圆圈是反电动势幅值。蓝色、橙色和绿色散点图显示 1、2 和 3 微秒死区下 αβ 坐标系电压的测量样本。黑点标记基于纯符号函数"),
    (") and essentially show the six 60° sectors of the back-emf circle \u201cexploding\u201d outwards due to the extra voltage required to counteract dead-time distortion. These match the measured data fairly well, at least when not in discontinuous conduction. The",
     "）的预测输出电压，本质上显示了反电动势圆的六个 60° 扇区由于抵消死区畸变所需额外电压而向外\u201c爆炸\u201d。这些与测量数据匹配良好，至少在非断续导通时如此。"),
    ("gain of the dead-time distortion in the measured data is slightly greater than predicted (note that the blue, orange, and green hexagonal scatter plots lie slightly outside the black arcs) and may be due to the diode voltage drops mentioned in",
     "测量数据中死区畸变的增益略大于预测值（注意蓝色、橙色和绿色六边形散点图略在黑色弧线之外），可能是由于"),
    ("The right-hand graph of", "的右图"),
    ("shows the same information in the synchronous (dq) frame, where the back-emf is a tight cluster, varying very slightly along the q-axis due to small velocity fluctuations. The measured and predicted data for",
     "在同步（dq）坐标系中显示相同信息，其中反电动势是一个紧密簇，沿 q 轴变化很小，由微小速度波动引起。"),
    ("approximately follow arcs showing the increase in q-axis voltage and the sweep in d-axis voltage.",
     "的测量和预测数据近似遵循弧线，显示 q 轴电压的增加和 d 轴电压的扫掠。"),

    ("shows the same measured voltages, but with a change in the predicted voltage that takes discontinuous conduction into account, by using a linear model",
     "展示了相同的测量电压，但预测电压考虑了断续导通的影响，通过使用线性模型"),
    ("within the range", "在范围内"),
    ("to handle behavior near the zero crossings (see", "以处理过零附近的行为（参见"),
    ("). The zero-crossing range used in this graph is", "）。此图中使用的过零范围为"),
    ("(see", "（参见"),

    ("Note the improved match in both stationary and synchronous frames, compared with",
     "注意与"),
    ("The current itself is shown in", "电流本身如"),
    (". Measured current tracks the intended circular trajectory in the stationary frame (constant current",
     "所示。测量电流在静止坐标系中相当好地跟踪预期的圆形轨迹（同步坐标系中恒定电流"),
    ("in the synchronous frame) fairly well, degrading slightly as the dead time is increased.",
     "），随死区增大而略有退化。"),

    ("The faint concentric gray ellipses in the dq frame are error ellipses, based on the covariance of the measured currents, at 1, 2, 3, and 4 standard deviations from the mean. (For purely random noise from a normal distribution, the expected fraction of data enclosed by error ellipses follows the cumulative distribution function (CDF) of a",
     "dq 坐标系中淡同心灰色椭圆是误差椭圆，基于测量电流的协方差，在均值的 1、2、3 和 4 个标准差处。（对于正态分布的纯随机噪声，误差椭圆所包围的数据期望比例遵循"),
    (". Approximately 39.35% of samples are expected to lie within 1 standard deviation; 86.47% within 2 standard deviations, 98.89% within 3 standard deviations, and 99.96% within 4 standard deviations.)",
     "的累积分布函数（CDF），自由度为 2。约 39.35% 的样本预期在 1 个标准差以内；86.47% 在 2 个标准差以内，98.89% 在 3 个标准差以内，99.96% 在 4 个标准差以内。）"),

    ("show the same 10-pole motor and current control tuning at 1200 RPM and 1800 RPM.",
     "展示了同一 10 极电机和电流控制调谐在 1200 RPM 和 1800 RPM 下的情况。"),
    ("At these velocities, the sixth-harmonic frequency is 600 Hz and 900 Hz, respectively. Both are below the current control bandwidth (2031 Hz in this case), but not by much, and the result is an increase in current distortion.",
     "在这些速度下，六次谐波频率分别为 600 Hz 和 900 Hz。两者都低于电流控制带宽（本例中为 2031 Hz），但差距不大，结果是电流畸变增加。"),

    ("The DC voltage offset in", "中的直流电压偏移"),
    ("(the shift between predicted and measured voltage) is probably due to these three effects:",
     "（预测电压和测量电压之间的偏移）可能由以下三个效应引起："),
    ("0.19V along the q axis", "沿 q 轴 0.19V"),
    ("0.11V at 1200 RPM, 0.17V at 1800 RPM, along the d axis",
     "1200 RPM 时 0.11V，1800 RPM 时 0.17V，沿 d 轴"),
    ("75 μs is about 2.7° at 1200 RPM and 4.1° at 1800 RPM. At 1200 RPM, with a 2.7° rotation of a 6 V signal along the q axis we can expect a d-axis shift of ≈ 0.28 V. At 1800 RPM, with a 4.1° rotation of an 8.2 V signal along the q axis, we can expect a",
     "75 μs 在 1200 RPM 时约 2.7°，1800 RPM 时约 4.1°。在 1200 RPM 时，沿 q 轴 6 V 信号旋转 2.7° 可预期 d 轴偏移约 0.28 V。在 1800 RPM 时，沿 q 轴 8.2 V 信号旋转 4.1°，可预期"),

    # ---- Section 5.7.4.1.1: Low-bandwidth current controllers ----
    ("are with the same motor (Nidec Hurst DMA0204024B101) using the default current loop tuning in motorBench",
     "使用同一电机（Nidec Hurst DMA0204024B101），采用 motorBench"),
    ("Development Suite. With this tuning, the current loop bandwidth is around 235 Hz. These tests show operation at 240 RPM with a smooth light load of ≈ 0.5 A.",
     "Development Suite 中的默认电流环调谐。在此调谐下，电流环带宽约为 235 Hz。这些测试显示在 240 RPM 下运行，平滑轻载约 0.5 A。"),

    ("The result is a much higher current distortion even at the low electrical frequency of 20 Hz; The dead-time distortion frequency",
     "即使在 20 Hz 的低电气频率下，电流畸变也更大；死区畸变频率"),
    ("120Hz is about half the current loop bandwidth.",
     "120Hz 约为电流环带宽的一半。"),

    ("show operation at 600 RPM (50 Hz electrical frequency,", "展示了 600 RPM（50 Hz 电气频率，"),
    ("300 Hz) with a smooth light load of ≈ 0.5 A. In this case, the disturbance frequency is above the current loop bandwidth, and the current loop can barely react to the dead-time distortion — note that the voltage outputs in the synchronous frame are fairly tightly-clustered spots in the graphs, and in the stationary frame are almost circular.",
     "300 Hz）下的运行，平滑轻载约 0.5 A。在此情况下，扰动频率高于电流环带宽，电流环几乎无法对死区畸变作出反应——注意同步坐标系中的电压输出在图中是相当紧密的簇点，而静止坐标系中几乎是圆形。"),

    ("show operation at 1200 RPM (100 Hz electrical frequency,", "展示了 1200 RPM（100 Hz 电气频率，"),
    ("600 Hz) with a smooth light load of ≈ 0.5 A. In this case, the disturbance frequency is even further above the current loop bandwidth. Again, the current loop can barely react to the dead-time distortion — note that the voltage outputs in the stationary frame are almost circular, and in the synchronous frame are fairly tightly-clustered, although with some fluctuations mostly along the d-axis, which is indicative of angle jitter, perhaps due to the torque ripple causing velocity fluctuations.",
     "600 Hz）下的运行，平滑轻载约 0.5 A。在此情况下，扰动频率更高于电流环带宽。同样，电流环几乎无法对死区畸变作出反应——注意静止坐标系中的电压输出几乎是圆形，同步坐标系中相当紧密，尽管有一些主要沿 d 轴的波动，这表明存在角度抖动，可能是由于转矩纹波引起的速度波动。"),

    ("There are a number of reasons for", "有多种原因需要"),
    ("tuning a current loop with a more aggressive bandwidth", "以更激进的带宽调谐电流环"),
    (", and improving otherwise poor performance in the presence of dead-time distortion is one of them.",
     "，改善死区畸变存在时的不良性能是其中之一。"),

    # ---- Section 5.7.4.2: Dead-time distortion and sensorless estimation ----
    ("based solely on voltage and current measurements are sensitive to errors in the voltage and currents. These typically try to estimate a back-emf voltage vector and track its angle. Since dead-time distortion causes voltage errors between the current controller outputs and the actual voltage present on the motor terminals, these estimators tend to produce significant errors when the back-emf voltage is below the dead-time distortion voltage amplitude",
     "仅基于电压和电流测量的估计器对电压和电流误差敏感。它们通常试图估计反电动势电压矢量并跟踪其角度。由于死区畸变在电流控制器输出和电机端子上的实际电压之间引起电压误差，当反电动势电压低于死区畸变电压幅值"),
    ("also relies on the amplitude of the estimated back-emf, so it is likely more sensitive to dead-time distortion than other estimators.",
     "还依赖于估计反电动势的幅值，因此它可能比其他估计器对死区畸变更敏感。"),

    # ---- Section 5.7.5.1: MCAF per-phase dead-time compensation algorithm ----
    ("is shown in", "如"),
    (", and in context in", "所示，上下文如"),
    (". The inputs to this block are phase currents", "所示。此模块的输入为相电流"),
    ("and duty cycles", "和占空比"),
    ("that are outputs of the ZSM block.", "，它们是 ZSM 模块的输出。"),

    ("The upper half of the dead-time compensation block, above the dashed line shown in",
     "死区补偿模块的上半部分，即"),
    (", handles the feedback voltage for use by position and velocity estimators. The duty cycles are converted to the stationary (αβ) frame using a Clarke transform, and then delayed by two cycles to match the current sampling delay (TBD add link here).",
     "中虚线上方部分，处理用于位置和速度估计器的反馈电压。占空比通过 Clarke 变换转换为静止（αβ）坐标系，然后延迟两个周期以匹配电流采样延迟（待补链接）。"),
    (", which is a duty cycle vector in the stationary frame, is added to the delay-matched duty cycle and then multiplied by DC link voltage",
     "，它是静止坐标系中的占空比矢量，被加到延迟匹配的占空比上，然后乘以直流母线电压"),
    ("to compute the estimator feedback voltage", "以计算估计器反馈电压"),

    ("The lower half of the dead-time compensation block shows the core of the dead-time compensation algorithm, which has three portions:",
     "死区补偿模块的下半部分展示了死区补偿算法的核心，分为三个部分："),

    ("The per-phase unit disturbance signals are calculated as shown in",
     "逐相单位扰动信号的计算如"),
    ("using a saturation block with linear gain", "所示，使用饱和模块，线性增益为"),
    ("for a chosen current amplitude", "对于选定的电流幅值"),
    ("and fixed scaling factor", "和固定缩放因子"),
    (", and limits", "，限幅为"),

    ("This effectively computes the nonlinear function", "这实际上计算了非线性函数"),
    ("and applied as", "并应用为"),

    ("Development Suite, then the upper part of", "Development Suite \u7684\u81ea\u5b9a\u4e49\u9875\u9762\u4e2d\u9009\u62e9\u4e86\u6b7b\u533a\u8865\u507f\u7684\u201c\u65e0\u201d\u53d8\u4f53\uff0c\u5219"),

    # ---- Section 5.7.5.3.1: Current linearity range ----
    ("Empirical work with the Nidec Hurst DMA0204024B101 motor and dsPICDEM",
     "使用 Nidec Hurst DMA0204024B101 电机和 dsPICDEM"),
    ("MCLV‑2 Development Board showed improved stability in the range of",
     "MCLV-2 开发板的实验工作表明在以下范围内稳定性提高："),
    ("133 – 200, corresponding to", "133 – 200，对应"),

    # ---- Section 5.7.5.3.2: Forward-path gain ----
    ("Forward-path dead-time compensation was not particularly successful. Use of nonzero forward-path gain is not recommended without performing detailed testing on the intended motor and load, to determine a desirable value.",
     "前向通道死区补偿并不特别成功。不建议在未对目标电机和负载进行详细测试以确定合适值的情况下使用非零前向通道增益。"),
    ("An unloaded motor, which experiences very low q-axis currents, is a difficult subject to reduce the effects of dead-time distortion.",
     "空载电机承受非常低的 q 轴电流，是减小死区畸变效应的困难对象。"),
    ("With the Nidec Hurst DMA0204024B101 motor, a forward-path gain of only",
     "对于 Nidec Hurst DMA0204024B101 电机，仅"),
    ("produced the least distortion; increasing gain much beyond that point caused the distortion to increase again.",
     "的前向通道增益产生最小畸变；增益超过该点太多会导致畸变再次增加。"),
    ("For the motor loaded with about 0.5 A q-axis current, the dead-time compensation was more effective, with",
     "对于加载约 0.5 A q 轴电流的电机，死区补偿更有效，"),
    ("producing the least distortion.", "产生最小畸变。"),

    # ---- Section 5.7.5.3.3: Feedback-path gain ----
    ("Nonzero feedback-path gain was successful at improving estimator performance of the",
     "非零反馈通道增益成功改善了"),
    ("at very low velocities. Values of", "在极低速下的估计器性能。"),
    ("were generally successful on several motors tested, and lowered the minimum operating speed by a factor of anywhere from 2 to 4.",
     "的值在多台测试电机上普遍成功，将最低运行速度降低了 2 到 4 倍。"),
    ("is too high, the motor controller tended to \u201cclench\u201d and apply full current. (This effect seems to be reduced if the motor resistance is underestimated intentionally by a few percent.)",
     "过高时，电机控制器倾向于\u201c锁死\u201d并施加满电流。（如果故意低估电机电阻几个百分点，此效应似乎会减小。）"),
    ("Use of nonzero feedback-path gain with the AN1292 PLL is recommended, starting with a gain of 0.4 – 0.5. The gain may be increased, with careful experimentation to avoid the \u201cclenching\u201d behavior, to improve torque performance at low speed.",
     "建议在 AN1292 PLL 中使用非零反馈通道增益，从 0.4 – 0.5 的增益开始。增益可以增加，但需仔细实验以避免\u201c锁死\u201d行为，以改善低速转矩性能。"),

    # ---- Section 5.7.5.4: Experimental results ----
    ("In this case, the Nidec Hurst DMA0204024B101 and dsPICDEM",
     "在此情况下，使用 Nidec Hurst DMA0204024B101 和 dsPICDEM"),
    ("MCLV‑2 Development Board were used to show an increase in tolerable load current at lower speeds. The current loop was tuned to a high bandwidth (≈ 2 kHz) and the velocity loop was tuned to a low bandwidth (≈ 1.8Hz) to allow slowly-changing current. The ",
     "MCLV-2 开发板，展示在低速下可容忍负载电流的增加。电流环调谐为高带宽（≈ 2 kHz），速度环调谐为低带宽（≈ 1.8Hz），以允许缓慢变化的电流。"),
    ("estimator was used for commutation with quadrature encoder as an angle reference.",
     "估计器用于换相，正交编码器作为角度参考。"),
    ("This was run at a variety of motor velocities for three different values of",
     "在多种电机速度下运行，使用三个不同的"),
    (", and a manually-applied load torque gradually increased until the encoder and estimators diverged by more than 60° electrical. As the commutation error approaches 90° electrical, torque production drops off rapidly and the motor undergoes cycle slip",
     "值，手动施加的负载转矩逐渐增加，直到编码器和估计器偏差超过 60° 电气角度。当换相误差接近 90° 电气角度时，转矩产生迅速下降，电机出现周期滑转"),
    ("shows an increase in motor current as", "显示随着"),
    ("is increased, for a given velocity, before approaching a cycle slip. This increased motor current means the motor controller can apply a larger current with less commutation angle error, providing an improved torque response at low speeds.",
     "的增加，在给定速度下接近周期滑转前电机电流增加。增加的电机电流意味着电机控制器可以施加更大的电流而换相角度误差更小，从而在低速下提供改善的转矩响应。"),

    # ---- Section 5.7.5.5: Implementation notes ----
    ("since in MCAF, currents are represented with numerical full-scale of twice the ADC full-scale values to leave design margin for avoiding overflow. For example, on dsPICDEM",
     "因为在 MCAF 中，电流以两倍 ADC 满量程值的数值满量程表示，以留出设计裕量避免溢出。例如，在 dsPICDEM"),
    ("MCLV‑2 Development Board the full-scale ADC current is 4.4 A but the numerical full-scale range of currents is 8.8 A.",
     "MCLV-2 开发板上，满量程 ADC 电流为 4.4 A，但电流的数值满量程范围为 8.8 A。"),

    # ---- Shorter fragments with enough context to be safe ----
    ("are shown in", "如"),
    ("shown in", "如"),
]

changed = txutil.replace_text(soup, pairs, root=root)
print("replace_text changed {} nodes".format(changed))

# Use apply_dict for short standalone text nodes (whole-node match is safe)
short_map = {
    "The": "",
    "for": "用于",
    ", and": "，以及",
    "and": "以及",
    "a": "一个",
}
dict_changed = txutil.apply_dict(root, short_map)
print("apply_dict (short) changed {} nodes".format(dict_changed))

# Apply punctuation conversion for standalone Western punctuation
punct_changed = txutil.apply_punctuation(root)
print("apply_punctuation changed {} nodes".format(punct_changed))

# Fix nav link title attributes (not handled by replace_text)
for a_tag in soup.find_all('a'):
    title = a_tag.get('title', '')
    if title:
        new_title = title
        new_title = new_title.replace("5.8. Voltage Control", "5.8. 电压控制")
        new_title = new_title.replace("5.6.5.1. Simple dynamic current limit", "5.6.5.1. 简单动态电流限制")
        if new_title != title:
            a_tag['title'] = new_title

txutil.save(path, soup)
print("saved", path)
