# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/fundamentals"
title_zh = "5.1.2. FOC 基础"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Fundamentals of FOC": "FOC 基础",
    "Torque production and reference frames": "转矩产生与参考坐标系",
    "MCAF utilizes field-oriented control (FOC) of motor current. This section describes the theory of FOC in general, with some specific notes on MCAF implementation.":
        "MCAF 对电机电流采用磁场定向控制（FOC）。本节一般性地介绍 FOC 的理论，并给出一些针对 MCAF 实现的具体说明。",
    "The goal of": "的目标",
    "field-oriented control (FOC)": "磁场定向控制（FOC）",
    "is to control instantaneous electromagnetic torque with high bandwidth. This is possible — although not obvious for newcomers to field-oriented control — by managing two orthogonal components of current in a reference frame at some electrical angle":
        "是以高带宽控制瞬时电磁转矩。这可以通过在某个电角度的参考坐标系中管理两个正交的电流分量来实现——尽管对初学者而言这并不直观。",
    ". The electrical frequency": "。电频率",
    "is the rate at which the electrical angle changes.": "是电角度的变化率。",
    "Electrical angles and frequencies are proportional to mechanical angles and frequencies as expressed in Equation":
        "电角度和电频率与机械角度和机械频率成正比，如公式",
    ", where": "所示，其中",
    "is the number of pole pairs. For example, a six-pole machine, with": "为极对数。例如，一台六极电机，",
    ", undergoes three electrical cycles for each mechanical revolution.": "，每旋转一圈（机械旋转）经历三个电周期。",
    "Electromagnetic torque": "电磁转矩",
    "in three-phase rotating machinery is proportional to the cross product of stator currents and rotor flux linkage, as shown in Equation":
        "在三相旋转电机中与定子电流和转子磁链的叉积成正比，如公式",
    ". Here": "所示。这里",
    "is a unit vector along the axis of rotation, x and y are components of a two-dimensional plane perpendicular to":
        "是沿旋转轴的单位矢量，x 和 y 是垂直于",
    ", and the current vector is an equivalent vector sum of currents based on how the resulting fields are aligned with these x and y axes.":
        "的二维平面上的分量，而电流矢量是根据合成磁场与这些 x、y 轴的对齐关系得到的电流等效矢量和。",
    "The angle": "角度",
    "between flux linkage and current vectors, illustrated in": "（磁链矢量与电流矢量之间的夹角），如",
    ", plays an important role in determining electromagnetic torque. If the two vectors are aligned, this angle":
        "所示，在决定电磁转矩时起重要作用。如果两个矢量同向，该角度",
    "is zero, and no torque is produced. Maximum torque occurs when the flux linkage and current vectors are perpendicular, and the term":
        "为零，不产生转矩。当磁链矢量与电流矢量垂直时转矩最大，此时",
    "in Equation": "在公式",
    "is ±1.": "中为 ±1。",
    "Flux linkage vector, current vector, and the angle": "磁链矢量、电流矢量及其夹角",
    "between them, in an arbitrary": "，位于一个任意",
    "-coordinate frame.": "坐标系中。",
    "It is important to note that these x and y axes are": "需要注意的是，这些 x 和 y 轴是",
    "arbitrary": "任意的",
    "— we can pick any unit basis vectors": "——我们可以选取任意一组单位基矢量",
    "and": "和",
    "that form a mutually perpendicular set with the axis of rotation": "，使它们与旋转轴",
    ", such that their cross product": "构成相互垂直的集合，使其叉积",
    "There are two common choices for these basis vectors. One is the stationary frame, commonly aligned with one of the stator phases. Pictured on the left of":
        "对这些基矢量有两种常见选择。其一是静止坐标系，通常与某一定子相对齐。图中左侧",
    "is a three-phase stator with windings positioned 120° apart. This is equivalent — at least in terms of magnetic flux linkage — to a two-phase stator with orthogonal windings α and β, pictured on the right. For any combination of currents":
        "是一个三相定子，其绕组相隔 120° 分布。这在磁链意义上等价于右侧所示、具有正交绕组 α 和 β 的两相定子。对于三相定子绕组中的任意电流组合",
    "in the three-phase stator winding, the same magnetic field seen by the rotor can be produced by an appropriate combination of currents":
        "，转子所看到的同一磁场可以通过适当的电流组合",
    "through two “virtual” coils used to create the horizontal and vertical components of the stator field. The mathematical conversion of projecting three-phase quantities onto these virtual orthogonal coils is called the Clarke transform, after one of its originators, Edith Clarke.":
        "流过两个用于产生定子磁场水平与垂直分量的“虚拟”线圈来获得。将三相量投影到这些虚拟正交线圈上的数学转换称为 Clarke 变换（克拉克变换），以它的提出者之一 Edith Clarke 命名。",
    "Use of Clarke transform to convert between per-phase quantities and the αβ frame The angle reference is commonly aligned with the first motor phase (phase A in an ABC-labeled set, or phase U in a UVW-labeled set) and the α winding. The rotor’s position is some electrical angle":
        "利用 Clarke 变换在每相量与 αβ 坐标系之间转换 角度参考通常与电机的第一相（在 ABC 标记中为 A 相，在 UVW 标记中为 U 相）以及 α 绕组对齐。转子的位置为某个电角度",
    "relative to these angle references.": "，相对于这些角度参考。",
    "The Clarke transform is a linear transformation, shown in Equation": "Clarke 变换是一种线性变换，如公式",
    ", which can apply to any vector quantity": "所示，它可以作用于任意矢量",
    ", although typical examples are voltage": "，典型示例为电压",
    ", current": "、电流",
    ", or flux linkage": "或磁链",
    "This is usually expressed in the equivalent matrix form, as in Equation": "通常也用等价的矩阵形式表示，如公式",
    ", with the transformation matrix": "所示，其变换矩阵为",
    "The inverse Clarke transform, Equation": "逆 Clarke 变换（公式",
    ", converts from αβ to ABC, using the transformation matrix": "）将 αβ 转换回 ABC，所用变换矩阵为",
    "We can substitute": "我们可以代入",
    "to obtain Equation": "得到公式",
    ", describing torque based on stationary-frame quantities:": "，即用静止坐标系中的量来描述转矩：",
    "In the stationary reference frame, the flux vector": "在静止参考坐标系中，磁链矢量",
    "and current vector": "与电流矢量",
    "are not fixed, but rotate along with the rotor’s magnetic field.": "并不固定，而是随转子磁场一同旋转。",
    "The other common choice of basis vectors is the rotating reference frame, aligned with the electrical angle of excitation":
        "另一种常见的基矢量选择是旋转参考坐标系，它与励磁的电角度",
    "as it increases with electrical frequency": "对齐，并随电频率",
    ". This reference frame has components denoted": "的增加而增长。该参考坐标系的分量记为",
    "(“direct”) and": "（“直轴”，direct）和",
    "(“quadrature”). The transformation from αβ to dq axes is a rotation by an angle":
        "（“交轴”，quadrature）。从 αβ 到 dq 轴的变换是绕角度",
    ", shown in Equation": "的旋转，如公式",
    ". This is known as the Park transform, named for Robert Park, who developed it in the late 1920s, while working at General Electric to analyze the dynamics of synchronous motors.":
        "所示。这被称为 Park 变换（帕克变换），以 Robert Park 命名，他在 1920 年代末于通用电气工作时为分析同步电机的动态而提出了该方法。",
    "With permanent-magnet synchronous motors, this reference frame is known as the synchronous reference frame. Correct alignment for a PMSM occurs when the d-axis is aligned with the rotor flux, and the electrical angle":
        "对于永磁同步电机，该参考坐标系称为同步参考坐标系。PMSM 的正确对齐发生在 d 轴与转子磁通对齐时，此时电角度",
    "is identical to the rotor’s electrical angle": "与转子的电角度",
    "The inverse Park transform, Equation": "逆 Park 变换（公式",
    ", rotates in the opposite direction to convert from dq to αβ axes.": "）沿相反方向旋转，将 dq 轴转换回 αβ 轴。",
    ", describing torque based on synchronous-frame quantities:": "，即用同步坐标系中的量来描述转矩：",
    "The advantage of using the synchronous frame is that for steady-state rotation, to produce constant electromagnetic torque":
        "使用同步坐标系的优势在于：在稳态旋转下，为产生恒定电磁转矩",
    ", the flux linkage vector": "，磁链矢量",
    "and the current vector": "与电流矢量",
    "are constants. This allows current controllers with an integrator term to operate with zero steady-state error. It also allows for independent torque and flux control.":
        "均为常量。这使得带积分项的电流控制器能够实现零稳态误差运行，同时也允许对转矩和磁通进行独立控制。",
    "It is worth noting that for different motor types, the angle of the reference frame":
        "值得注意的是，对于不同类型的电机，参考坐标系的角度",
    "and the electrical angle of the rotor": "与转子的电角度",
    "may or may not be identical. For permanent-magnet synchronous motors, the reference frame should be aligned with the permanent magnet flux of the rotor, so that":
        "不一定相同。对于永磁同步电机，参考坐标系应与转子的永磁体磁通对齐，因此",
    ". For induction motors": "。对于感应电机",
    "; the electrical frequency": "；电频率",
    "where": "其中",
    "is the rotor speed expressed as an alectrical frequency, and": "是以电频率表示的转子转速，",
    "is the slip frequency needed to produce rotor current.": "是产生转子电流所需的转差频率。",
    "Stator voltage and flux equations": "定子电压与磁通方程",
    "General stator voltage equation": "通用定子电压方程",
    "The equations so far in this section on FOC have involved torque, angle, and the vector components of flux linkage and current. The stator voltage, which is the voltage across the stator coils, is a more relevant quantity than flux linkage, since we can measure and control voltage more directly.":
        "本节到目前为止的 FOC 公式涉及转矩、角度以及磁链和电流的矢量分量。定子电压（即定子线圈两端的电压）是比磁链更相关的量，因为我们可以更直接地测量和控制电压。",
    "Motor control engineers working with FOC often talk about a voltage vector":
        "从事 FOC 的电机控制工程师常谈论电压矢量",
    "in a rotating reference frame, and even though this voltage vector is not directly measurable — there are no actual “d” and “q” coils — it can be derived mathematically through the Park and Clarke transforms from per-phase measurements of the actual motor coils. The stator voltage equations relating voltage, flux, and current, in a reference frame rotating with electrical frequency":
        "（位于旋转参考坐标系中）；尽管该电压矢量无法直接测量——并不存在实际的“d”和“q”线圈——但可以通过 Park 和 Clarke 变换从实际电机线圈的每相测量值中经数学推导得到。将电压、磁链和电流联系起来的定子电压方程，在以电频率",
    ", are shown below in equation": "旋转的参考坐标系中如下式",
    ". This equation is valid for both induction motors and permanent-magnet synchronous motors.":
        "所示。该方程对感应电机和永磁同步电机均成立。",
    "Here the": "这里",
    "coefficient is the stator resistance.": "系数为定子电阻。",
    "The": "其中",
    "terms are known as": "项被称为",
    "speed voltage": "速度电压",
    "and are artifacts of the rotating reference frame; they have nothing to do with the motor construction, and are present even with other loads such as a three-phase inductor or transformer when operated in FOC with a reference frame rotating at frequency":
        "，是旋转参考坐标系的产物；它们与电机的结构无关，即使对三相电感或变压器等其他负载，在以频率",
    ". They also represent an interesting cross-coupling behavior between the d- and q-axes.":
        "旋转的参考坐标系下进行 FOC 时也会存在。它们还代表了 d 轴与 q 轴之间一种有趣的交叉耦合行为。",
    "PMSM voltage equations": "PMSM 电压方程",
    "For the PMSM, the flux equations are listed in Equation": "对于 PMSM，磁链方程如公式",
    "and relate the flux linkage vector": "所示，将磁链矢量",
    "to the current vector": "与电流矢量",
    "The terms": "项",
    "are the d- and q-axis stator inductances, which are generally identical for":
        "是 d 轴和 q 轴的定子电感，对于",
    "surface permanent magnet motors (SPMSM)": "表贴式永磁电机（SPMSM）",
    "but different for": "通常二者相等，而对于",
    "interior permanent-magnet motors (IPMSM)": "内置式永磁电机（IPMSM）",
    ", where usually": "则通常不同，",
    "due to intentional differences in construction. For the IPMSM, inductances in the synchronous frame are independent of rotor position, but the inductances measured in the stationary frame (either per-phase or in the αβ frame) change with rotor position.":
        "这是由结构上的有意差异造成的。对于 IPMSM，同步坐标系中的电感与转子位置无关，但在静止坐标系（每相或 αβ 坐标系）中测得的电感会随转子位置变化。",
    "The term": "项",
    "is the permanent magnet flux linkage.": "为永磁体磁链。",
    "The flux equations can be substituted into the stator voltage equations to produce stator voltage equations expressed in terms of circuit voltages and currents, shown below in Equation":
        "将磁链方程代入定子电压方程，可得到以电路电压和电流表示的定子电压方程，如公式",
    "From left to right, these terms represent the resistive voltage drop": "从左到右，这些项依次代表电阻压降",
    ", cross-coupling speed voltage, the voltage": "、交叉耦合速度电压、改变电流所需的电压",
    "needed to change current, and the back-emf": "以及反电动势",
    "is commonly known as the back-emf constant or voltage constant.": "通常称为反电动势常数或电压常数。",
    "PMSM torque equation": "PMSM 转矩方程",
    "The PMSM flux equation can also be substituted into the torque equation (Equation":
        "PMSM 的磁链方程也可代入转矩方程（公式",
    ") to derive Equation": "）以推导出公式",
    "showing the two torque terms found in a PMSM:": "，展示 PMSM 中的两个转矩项：",
    "alignment torque": "对齐转矩",
    "or": "或",
    "permanent magnet torque": "永磁转矩",
    ", resulting from the alignment between the rotor’s permanent magnet and the field caused by the stator current":
        "，由转子永磁体与定子电流产生的磁场之间的对齐作用产生",
    "reluctance torque": "磁阻转矩",
    ", resulting from the tendency of the rotor iron to rotate towards the field caused by the stator current":
        "，由转子铁芯趋向于转向定子电流产生的磁场的趋势产生",
    "For a SPMSM,": "对于 SPMSM，",
    ", so there is no reluctance torque, and the electromagnetic torque is produced only by the q-axis component of current. In this case, d-axis current is driven towards zero (except in":
        "，因此没有磁阻转矩，电磁转矩仅由电流的 q 轴分量产生。此时 d 轴电流被驱动至零（除",
    "flux weakening": "弱磁",
    ") to reduce": "外），以降低",
    "losses in the stator.": "定子中的损耗。",
    "For an IPMSM,": "对于 IPMSM，",
    ", and the reluctance torque can help increase efficiency by controlling": "，磁阻转矩可通过控制",
    ". The optimum choice of": "来帮助提高效率。其最优选择",
    "is the aim of": "是",
    "Maximum Torque Per Ampere (MTPA)": "最大转矩/电流比（MTPA）",
    "algorithms.": "算法的目标。",
    "Per-phase equivalent circuit": "每相等效电路",
    "It is important to note that the equations in this section are derived from the per-phase equivalent circuit model, shown in":
        "需要注意的是，本节的方程都是由每相等效电路模型推导得到的，如",
    ". This model treats each winding of a three-phase wye-connected PMSM as a winding resistance": "所示。该模型将三相星形连接 PMSM 的每个绕组视为绕组电阻",
    ", winding inductance": "、绕组电感",
    ", and back-emf": "和反电动势",
    "in series, between the neutral and one of the three line terminals A, B, or C.":
        "串联在中性点与三个端子 A、B、C 之一之间。",
    "The per-phase equivalent for each of the stator windings in a PMSM with wye (star) connection":
        "星形连接 PMSM 中每个定子绕组的每相等效电路",
    "In this model, the back-emf components are sinusoidal voltages with the phase sequence A, B, C, separated by 120°.":
        "在该模型中，反电动势分量为正弦电压，相序为 A、B、C，彼此相差 120°。",
    "The line-to-line resistance measurable at any pair of the terminals is": "在任意两端子间测得的线电阻为",
    ", and the line-to-line inductance measurable at any pair of terminals is":
        "，在任意两端子间测得的线电感为",
    "for SPMSM. (For IPMSM, remember that inductance varies with rotor angle.) The line-to-line back-emf measurable at any pair of terminals has amplitude":
        "（对 SPMSM 而言；对 IPMSM，请记住电感随转子角度变化）。在任意两端子间测得的线反电动势幅值为",
    "is the line-to-neutral back-emf constant in V/(rad/s).": "为相（线至中性点）反电动势常数，单位为 V/(rad/s)。",
    "Wye and delta connections": "星形与三角形连接",
    "The per-phase model also applies equally to the delta-connected PMSM. A delta-connected stator, shown in":
        "每相模型同样适用于三角形连接的 PMSM。三角形连接的定子，如",
    "can be modeled by an equivalent wye-connected stator with": "所示，可以用一个等效的星形连接定子来建模，其",
    ", and": "、和",
    ". Delta-connected windings also involve a phase shift of 30° because of the change in connections.":
        "。由于连接方式的改变，三角形连接的绕组还涉及 30° 的相移。",
    "Per-phase equivalence between wye (star) connection, shown at left, and delta connection, shown at right.":
        "星形连接（左）与三角形连接（右）之间的每相等效关系。",
    "Knowing the wye-to-delta conversion is important for those motors which have individual phase windings that can be connected either as a wye or delta configuration, which is more common in larger electric machines. These motors have six terminals — A1, A2, B1, B2, C1, C2, or more commonly U1, U2, V1, V2, W1, W2 — which can be connected appropriately in a terminal box, as shown in":
        "了解星形—三角形转换对于具有可接成星形或三角形的独立相绕组的电机很重要，这在较大型电机中更为常见。这些电机有六个端子——A1、A2、B1、B2、C1、C2，或更常见的 U1、U2、V1、V2、W1、W2——可在接线盒中适当连接，如",
    ", in either wye or delta configuration depending on the installation of terminal jumpers.":
        "所示，根据端子短接片的安装方式接成星形或三角形。",
    "Terminal box connections (top) and resulting motor topologies (bottom) for wye (star) connection, shown at left, and delta connection, shown at right, on an electric machine with three independent windings. Terminal jumpers are shown in light gray.":
        "具有三个独立绕组的电机的接线盒连接（上）及所得电机拓扑（下）：左侧为星形连接，右侧为三角形连接。端子短接片以浅灰色显示。",
    "Very large motors may have more than six winding terminals that can be reconnected in multiple ways; see for example Annex A2 of":
        "非常大的电机可能有超过六个绕组端子，并能以多种方式重新连接；参见",
    "IEC 60034-8": "IEC 60034-8",
    "As long as the motor is supplied as a three-terminal black box from the manufacturer, however, the internal construction of the motor (wye or delta) doesn’t matter, and the theory of three-phase electric machines applies equally to either configuration.":
        "的附录 A2。不过，只要电机由制造商以三端子“黑盒”形式提供，其内部结构（星形或三角形）就无关紧要，三相电机的理论对两种连接方式同样适用。",
    "Steady-state and phasor analysis": "稳态与相量分析",
    "At steady state, the": "在稳态下，",
    "terms of Equation": "（公式",
    "are zero, and the voltage equations reduce to Equation": "中的）项为零，电压方程简化为公式",
    "These can be pictured graphically in a voltage phasor diagram, as shown in":
        "这些关系可以用电压相量图直观表示，如",
    ". The dark green arrows show back-emf, resistive, and inductive components of the resulting terminal voltage":
        "所示。深绿色箭头表示在 d 轴电流为零时，合成端电压",
    ", with zero d-axis current. This is typical operation for a PMSM in field-oriented control. The light blue arrows show additional resistive and inductive components caused by controlling d-axis current to":
        "的反电动势、电阻和电感分量。这是 PMSM 在磁场定向控制下的典型工作状态。浅蓝色箭头表示将 d 轴电流控制为",
    ". This is done during": "时产生的附加电阻和电感分量。这发生在",
    "flux-weakening operation": "弱磁运行",
    ", to reduce the magnitude of the terminal voltage by using the inductive voltage drop":
        "期间，目的是利用电感压降",
    "to counteract part of the back-emf voltage.": "来抵消部分反电动势电压，从而降低端电压的幅值。",
    "PMSM phasor diagram": "PMSM 相量图",
    "Phasor analysis is a valuable yet extremely simple approach to determine the voltage requirements of a PMSM. Some care is necessary in the units used for the different motor parameters, so that Equation":
        "相量分析是确定 PMSM 电压需求的一种非常有价值且极其简单的方法。在使用各电机参数的单位时需要稍加留意，以使公式",
    "is valid:": "成立：",
    "The per-phase equivalent model is stated in terms of line-to-neutral voltage.":
        "每相等效模型以相电压（线至中性点）表示。",
    "Resistance and inductances should be line-to-neutral (half of the line-to-line value)":
        "电阻和电感应使用相值（线值的一半）",
    "Back-emf should be calculated as line-to-neutral voltage (":
        "反电动势应按相电压计算（",
    "0.5774 of the line-to-line voltage)": "线电压的 0.5774 倍）",
    "Be aware of temperature coefficients, if operating the motor near its rated maximum temperature:":
        "如果电机在其额定最高温度附近运行，请注意温度系数：",
    "The resistance of copper stator windings will increase roughly linearly with temperature over normal operating temperature ranges (-55 °C to +200 °C). Relative to its value at 20 °C, copper’s resistance has a temperature coefficient of ≈0.4%/°C.":
        "在正常工作温度范围（-55 °C 至 +200 °C）内，铜定子绕组的电阻随温度近似线性增加。相对于 20 °C 时的值，铜电阻的温度系数约为 0.4%/°C。",
    "Both": "无论",
    "neodymium and samarium-cobalt magnets have a slight negative temperature coefficient of remanence":
        "钕铁硼还是钐钴磁体，其剩磁都呈微弱的负温度系数",
    ", which means that the back-emf decreases slightly with increasing temperature.":
        "，这意味着反电动势随温度升高而略有下降。",
    "The units for computing the product of": "在计算",
    "(or": "（或",
    ") should be consistent, so if": "）的乘积时，单位应保持一致：如果",
    "is available in V/(rad/s), then velocity": "的单位为 V/(rad/s)，则速度",
    "should be converted to rad/s; if": "应转换为 rad/s；如果",
    "is available in V/kRPM, then velocity": "的单位为 V/kRPM，则速度",
    "should be converted to kRPM. (1 RPM =": "应转换为 kRPM。（1 RPM =",
    "rad/s)": "rad/s）",
    "Use peak amplitude rather than RMS for all voltages and currents. (1V RMS =":
        "所有电压和电流应使用峰值而非有效值（RMS）。（1V RMS =",
    "V amplitude)": "V 峰值）",
    "Motor manufacturers are notorious for specifying back-emf constant":
        "电机制造商在规定反电动势常数",
    "inconsistently and ambiguously. It can be stated in terms of RMS or peak amplitude; line-to-line or line-to-neutral; and in terms of voltage per rad/s or RPM or kRPM.":
        "时常常不一致且含糊。它可能以有效值或峰值、线电压或相电压、以及每 rad/s 或每 RPM 或每 kRPM 的电压来给出。",
    "The resulting components": "所得各分量",
    "should be added in quadrature, as shown in Equation": "应按正交相加，如公式",
    ", to compute the required amplitude of line-to-neutral terminal voltage.":
        "所示，以计算所需相端电压的幅值。",
    "Compute required line-to-line terminal voltage by multiplying line-to-neutral terminal voltage by":
        "将相端电压乘以",
    "The motor and drive are well-matched if the maximum required line-to-line voltage is below the DC link voltage, but both are the same order of magnitude. (Typically, the maximum line-to-line terminal voltage":
        "即得到所需线端电压。如果所需最大线电压低于母线电压且二者数量级相当，则电机与驱动器匹配良好。（通常，最大线端电压",
    "is 70-95% of the minimum DC link voltage, to leave enough engineering margin so current can still change quickly —":
        "为最小母线电压的 70%–95%，以留出足够的工程裕量，使电流仍能快速变化——",
    "terms require voltage — even considering other voltage losses such as":
        "项需要电压——即便考虑其他电压损耗，如",
    "dead-time distortion": "死区畸变",
    "and on-state voltage across the transistors.)": "以及晶体管的导通压降。）",
    "FOC block diagram": "FOC 框图",
    "The general structure of an FOC controller is an inner vector current loop, and an outer velocity loop, as shown in":
        "FOC 控制器的一般结构是一个内部矢量电流环和一个外部速度环，如",
    "Generalized FOC block diagram structure": "通用 FOC 框图结构",
    "The inner vector current loop has a current controller that operates in the synchronous (dq) frame. Park and Clarke transforms are used in the feedback path to convert measured phase currents to the synchronous frame as inputs to the current controller, and in the forward path to convert desired synchronous-frame voltages":
        "内部矢量电流环包含一个在同步（dq）坐标系中工作的电流控制器。Park 和 Clarke 变换用于反馈通路，将测得的相电流转换到同步坐标系作为电流控制器的输入；同时用于前向通路，将期望的同步坐标系电压",
    "to realizable PWM duty cycles in a three-phase bridge.": "转换为三相桥中可实现的 PWM 占空比。",
    "In its linear range, there is nothing particularly special about the vector current loop, and it is often realized as two PI controllers, one for the d axis and the other for the q axis. Saturation and antiwindup should be designed carefully, keeping in mind the overall vector controller, rather than as two independent axis controllers.":
        "在其线性范围内，矢量电流环并无特别之处，通常由两个 PI 控制器实现，一个用于 d 轴，一个用于 q 轴。饱和与抗积分饱和应仔细设计，要从整体矢量控制器的角度考虑，而不是当作两个独立的单轴控制器。",
    "Implementation notes": "实现说明",
    "The Components section has more information on the implementation details of": "“组件”一章提供了关于",
    "field-oriented-control": "磁场定向控制",
    "in MCAF.": "在 MCAF 中实现细节的更多信息。",
    "Voltages in the αβ or dq frames are represented as line-to-neutral voltages. Per-phase voltages are relative to the negative terminal of the DC link.":
        "αβ 或 dq 坐标系中的电压以相电压（线至中性点）表示。每相电压相对于母线的负端。",
    "Miscellaneous topics": "其他主题",
    "Alternate reference frame transforms": "其他参考坐标系变换",
    "There are two other common forms of reference transforms used, in addition to the forms of the Park transform (":
        "除了上文所述的 Park 变换（",
    ", Equation": "、公式",
    ") and Clarke transform (": "）和 Clarke 变换（",
    ") described above.": "）形式外，还有两种常用的参考变换形式。",
    "One is the full 3×3 Clarke transform (": "其一是完整的 3×3 Clarke 变换（",
    ", using the transformation matrix": "，所用变换矩阵为",
    "Here, the zero-sequence component": "这里，零序分量",
    "is the common-mode voltage. For motors without an accessible neutral connection, this voltage is arbitrary and does not affect operation of the motor. (The zero-sequence component does matter in some cases, where parasitic capacitance between windings and motor housing can cause what are known as":
        "为共模电压。对于没有可访问中性点连接的电机，该电压是任意的，不影响电机运行。（在某些情况下零序分量确实有影响：绕组与电机外壳之间的寄生电容会导致所谓的",
    "bearing currents": "轴承电流",
    "to flow through the motor bearings, gradually damaging them through electrical discharge. This is known as electrical fluting, and reduces the operating life of the motor.":
        "流过电机轴承，通过电放电逐渐损坏轴承。这被称为电蚀（electrical fluting），会缩短电机的使用寿命。",
    "It is worth noting that the common form of the Clarke transform (Equation": "值得注意的是，常见形式的 Clarke 变换（公式",
    ") and the Inverse Clarke transform (Equation": "）和逆 Clarke 变换（公式",
    ") are not truly inverses, since their transformation matrices are not square, but rather": "）并非真正的互逆，因为它们的变换矩阵不是方阵，而是",
    "pseudoinverses": "伪逆",
    ". It is possible to go make a full round trip from": "。可以从",
    "since one product of the two matrices is the identity:": "完成一次完整往返，因为这两个矩阵的乘积之一为单位矩阵：",
    ". But in the other direction,": "。但在另一方向上则不行，",
    "since the matrix product": "因为矩阵乘积",
    "does not have full rank. In plain terms, the zero-sequence component is lost as soon as the 2×3 Clarke transform is applied, and cannot be recovered.":
        "不满秩。通俗地说，零序分量一旦经过 2×3 Clarke 变换就会丢失，且无法恢复。",
    "The full 3×3 Clarke transform is invertible, on the other hand; the 3×3 Inverse Clarke transform is shown in Equation":
        "另一方面，完整的 3×3 Clarke 变换是可逆的；3×3 逆 Clarke 变换如公式",
    "using the transformation matrix": "所示，所用变换矩阵为",
    "The other common reference frame transform is the 2×2 Reduced Clarke transform (":
        "另一种常用的参考坐标系变换是 2×2 降阶 Clarke 变换（",
    ", which allows conversion of only two currents": "），它允许仅由两个电流",
    "into αβ coordinates through the assumption": "在假设",
    "This is used in MCAF for calculating": "下转换到 αβ 坐标系。MCAF 利用它由 A、B 相电流计算",
    "from phase currents A and B, with C unmeasured. It is possible to construct similar matrices":
        "（C 相未测量）。当未测量的相为 A 或 B 时，可以构造类似的矩阵",
    "when the unmeasured phase is A or B.": "。",
    "References": "参考文献",
    "Some of the material in this section was adapted from the section “FOC in Fifteen Minutes” from the 2016 MASTERS presentation":
        "本节的部分内容改编自 2016 年 MASTERS 技术研讨会演讲",
    "How to Succeed in Motor Control": "如何在电机控制中取得成功",
    "R. H. Park,": "R. H. Park,",
    "“Two-reaction theory of synchronous machines generalized method of analysis-part I,”":
        "“Two-reaction theory of synchronous machines generalized method of analysis-part I,”",
    "Transactions of the American Institute of Electrical Engineers": "Transactions of the American Institute of Electrical Engineers",
    ", vol. 48, no. 3, pp. 716-727, July 1929.": ", vol. 48, no. 3, pp. 716-727, July 1929.",
    "W. C. Duesterhoeft, M. W. Schulz and E. Clarke,": "W. C. Duesterhoeft, M. W. Schulz and E. Clarke,",
    "“Determination of Instantaneous Currents and Voltages by Means of Alpha, Beta, and Zero Components,”":
        "“Determination of Instantaneous Currents and Voltages by Means of Alpha, Beta, and Zero Components,”",
    ", vol. 70, no. 2, pp. 1248-1255, July 1951.": ", vol. 70, no. 2, pp. 1248-1255, July 1951.",
    "C. J. O’Rourke, M. M. Qasim, M. R. Overlin and J. L. Kirtley,": "C. J. O’Rourke, M. M. Qasim, M. R. Overlin and J. L. Kirtley,",
    "“A Geometric Interpretation of Reference Frames and Transformations: dq0, Clarke, and Park,”":
        "“A Geometric Interpretation of Reference Frames and Transformations: dq0, Clarke, and Park,”",
    "IEEE Transactions on Energy Conversion": "IEEE Transactions on Energy Conversion",
    ", vol. 34, no. 4, pp. 2070-2083, Dec. 2019. Also available via":
        ", vol. 34, no. 4, pp. 2070-2083, Dec. 2019. Also available via",
    "MIT Open Access": "MIT Open Access",
    "D. Busse, J. Erdman, R. J. Kerkman, D. Schlegel and G. Skibinski,": "D. Busse, J. Erdman, R. J. Kerkman, D. Schlegel and G. Skibinski,",
    # standalone connectors / punctuation
    ".": "。",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
