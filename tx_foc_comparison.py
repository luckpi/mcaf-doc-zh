# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/comparison-6step"
title_zh = "5.1.7. FOC 与六步控制的比较"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Comparison between FOC and six-step control": "FOC 与六步控制的比较",
    "Current loop tuning": "电流环整定",
    "Startup": "启动",
    "overview section": "概述一节",
    "Performance benefits": "性能收益",
    "Costs": "代价",
    "Torque capability": "转矩能力",
    "Torque degradation from angle error": "由角度误差引起的转矩下降",
    "Torque degradation from dynamics of commutation": "由换相动态引起的转矩下降",
    "Torque ripple": "转矩脉动",
    "Efficiency": "效率",
    "Switching loss": "开关损耗",
    "Current management": "电流管理",
    "Current sensing": "电流检测",
    "Current range": "电流范围",
    "Cost optimization": "成本优化",
    "Control complexity": "控制复杂度",
    "Six-step sectors": "六步控制的扇区",
    "Torque vs. angle error in six-step control with perfect knowledge of sector edges": "在精确获知扇区边界时六步控制中转矩随角度误差的变化",
    "Torque vs. angle error in six-step control with imperfect knowledge of sector edges": "在未精确获知扇区边界时六步控制中转矩随角度误差的变化",
    "Notes": "注",
    "phasor analysis": "相量分析",
    "Nidec Hurst DMA0204024B101": "Nidec Hurst DMA0204024B101",
    "dsPIC33CK Low Voltage Motor Control (LVMC) Development Board": "dsPIC33CK 低压电机控制（LVMC）开发板",
    "code from Microchip’s AN957": "Microchip AN957 的代码",
    "Six-step switching patterns, assuming phase C is open-circuited during one commutation sector.":
        "六步开关模式（假设在某换相扇区内 C 相开路）。",
    "FOC switching patterns": "FOC 开关模式",
    "Single-channel current measurement": "单通道电流测量",
    "Note:": "注：",
    "cost optimization": "成本优化",
    "There are several tradeoffs between FOC and six-step control of permanent magnet synchronous motors. As mentioned in the":
        "永磁同步电机的 FOC 与六步控制之间存在若干折中。如",
    ", FOC adds several improvements in performance, with minor drawbacks, at the cost of some design and implementation complexity:":
        "所述，FOC 在性能上带来若干改进，缺点较小，但代价是设计和实现复杂度的增加：",
    "full torque independent of angle": "与角度无关的满转矩",
    "full torque unaffected by commutation dynamics": "不受换相动态影响的满转矩",
    "lower torque ripple": "更低的转矩脉动",
    "better efficiency, reduced power dissipation": "更高的效率、更低的功耗",
    "higher switching loss": "更高的开关损耗",
    "higher range of phase current required": "所需相电流范围更大",
    "(possibly)": "（可能）",
    "current sense requirements": "电流检测要求",
    "more complex control": "更复杂的控制",
    "Perfect FOC maintains the stator field perpendicular to the rotor flux.":
        "理想的 FOC 使定子磁场与转子磁通保持垂直。",
    "An estimate of rotor angle is required (along with rotor flux, in the case of an induction motor). Torque in FOC is proportional":
        "需要估计转子角度（对于感应电机，还包括转子磁通）。FOC 中的转矩正比于",
    ", where": "，其中",
    "is the angle error from perfect perpendicularity.": "为相对于理想垂直的角度误差。",
    "In FOC, the": "在 FOC 中，",
    "term is generally very close to 1.": "项通常非常接近 1。",
    "In six-step control,": "在六步控制中，",
    "cannot be guaranteed any better than 30°. This is because the current vector in six-step control is fixed at the center of each 60° sector, as shown in":
        "无法保证优于 30°。这是因为六步控制中的电流矢量固定在每个 60° 扇区的中心，如",
    "and": "和",
    ", and the angle error of at least one of the edges of each sector is 30° or more.":
        "所示，且每个扇区至少有一条边界处的角度误差为 30° 或更大。",
    "This torque dropoff near the edges of the six-step sector is significant. At high speeds, inertia smooths out high-frequency components of torque, and only the average of":
        "六步扇区边缘附近的这种转矩下降是显著的。在高速下，惯性会平滑转矩的高频分量，只有",
    "affects the system: with perfectly-aligned sectors, the average torque of six-step control is 95.5% of perfect FOC torque for the same current limit: six-step torque is about 4.5% lower.":
        "的平均值影响系统：在扇区完全对齐时，对于相同的电流限幅，六步控制的平均转矩为理想 FOC 转矩的 95.5%：六步转矩约低 4.5%。",
    "At low speeds, this averaging is not present, and the best case for six-step control is that torque at the edges of sectors is 86.6% of FOC torque for the same current limit. Errors in angle sensing (misaligned Hall sensors, for instance) can lower this value further, and the torque falls off very quickly with higher angle error. When the load torque is high, this can cause the motor to become “stuck” at the edge of a sector, unable to overcome load torque.":
        "在低速下，这种平均效应不存在，六步控制的最佳情形是扇区边缘处的转矩为相同电流限幅下 FOC 转矩的 86.6%。角度检测的误差（例如霍尔传感器未对齐）会进一步降低该值，且转矩随角度误差增大而迅速下降。当负载转矩较高时，这可能使电机“卡”在扇区边缘，无法克服负载转矩。",
    "FOC is also prone to angle error, but errors are not as significant. It would take about 17.3° angle error to reduce FOC torque by the same 4.5%.":
        "FOC 也会出现角度误差，但误差的影响不那么显著。需要约 17.3° 的角度误差才能使 FOC 转矩下降相同的 4.5%。",
    "shows the impact of a 4° electrical error in the two cases:": "展示了两种情况下 4° 电角度误差的影响：",
    "FOC loses about 0.24% torque": "FOC 损失约 0.24% 的转矩",
    "Six-step loses about 0.24% torque (in addition to the 4.5% loss with perfect sector alignment) on average, but another few percent at one end of the sector.":
        "六步平均损失约 0.24% 的转矩（在扇区完全对齐时 4.5% 损失之外），但在扇区一端还会再多损失几个百分点。",
    "Fine print: some component of the stator field may be parallel to the rotor flux in order to control rotor flux.":
        "细则：为了控制转子磁通，定子磁场的某个分量可能与转子磁通平行。",
    "As the commutation angle changes, FOC provides voltages that change continuously with electrical angle, and compensates automatically for the phase lag of stator inductance. (at steady state, a component of voltage is required to change current through the stator windings; see":
        "随着换相角变化，FOC 提供的电压随电角度连续变化，并自动补偿定子电感造成的相位滞后。（在稳态下，需要一定的电压分量来改变定子绕组中的电流；参见",
    "for more information)": "以获取更多信息）",
    "Six-step commutation has the drawback that it must move the current vector in discrete jumps, by 60° at each transition between commutation sectors. At low speeds, this leads to a very short torque transient at each sector transition, usually accompanied by a faint “tick” sound.":
        "六步换相的缺点是必须以离散跳变的方式移动电流矢量，每次在换相扇区之间切换时跳变 60°。在低速下，这会在每次扇区切换时产生一个非常短暂的转矩暂态，通常伴随轻微的“滴答”声。",
    "At higher speeds, there are two major disadvantages of six-step commutation:":
        "在更高转速下，六步换相有两个主要缺点：",
    "commutation instants occur more frequently (higher electrical frequency)": "换相时刻出现得更频繁（电频率更高）",
    "available voltage for commutation is reduced (back-emf uses up more of the voltage)": "可用于换相的电压减少（反电动势消耗了更多电压）",
    "Commutation transients are no longer negligible; a significant fraction of each sector is spent making the current vector move. The total time during each sector is reduced, because the motor is operating at an increased electrical frequency. Peak current requirements increase slightly, to make up for lost torque at the beginning of each sector, which increases torque ripple. As back-emf requirements increase, the available voltage headroom is less, meaning that current transients take longer. At some point, it takes the entire commutation sector to work towards increasing current, and six-step control limits the available current.":
        "换相暂态不再可忽略；每个扇区有相当一部分时间用于使电流矢量移动。由于电机在更高的电频率下运行，每个扇区的总时间减少。峰值电流需求略有增加，以补偿每个扇区开始时损失的转矩，这会增大转矩脉动。随着反电动势需求增加，可用电压裕量减小，意味着电流暂态耗时更长。到某一时刻，整个换相扇区都用于提升电流，六步控制便限制了可用电流。",
    "show this trend in a simulation of the": "通过一个",
    "with increasing commutation frequency.": "在换相频率递增时的仿真展示了这一趋势。",
    "Simulation at 200 RPM — the commutation transient is very short": "200 RPM 时的仿真——换相暂态非常短",
    "Simulation at 1000 RPM — the commutation transient is short but visible": "1000 RPM 时的仿真——换相暂态较短但可见",
    "Simulation at 2500 RPM — the commutation transient takes more than one third of the total sector time, and steady-state current must be slightly higher to make up for the PI control transient":
        "2500 RPM 时的仿真——换相暂态占整个扇区时间的三分之一以上，稳态电流必须略高以补偿 PI 控制的暂态",
    "Simulation at 3100 RPM — due to voltage limits, the entire commutation sector is needed to increase motor current, and it never quite gets to the commanded current":
        "3100 RPM 时的仿真——由于电压限制，整个换相扇区都用于提升电机电流，且始终无法完全达到指令电流",
    "show measured current waveforms from a Nidec Hurst DMA0204024B101 operated in six-step from the":
        "展示了由",
    "using": "驱动、以六步方式运行的 Nidec Hurst DMA0204024B101 的实测电流波形。该",
    ". This particular six-step motor controller does not use a current loop, and instead wraps a slower PI loop around estimated speed, so commutation transitions take longer than their counterparts in the simulations shown above. In these tests the mechanical load on the motor was approximately constant, so at higher speeds, the required current is higher to overcome six-step transient effects and deliver the same mechanical torque.":
        "是一款不使用电流环的六步电机控制器，而是在估计速度外围绕一个较慢的 PI 环，因此其换相切换比上文仿真中的对应过程耗时更长。在这些测试中，电机的机械负载近似恒定，因此在更高转速下需要更大的电流来克服六步暂态效应并输出相同的机械转矩。",
    "Measured currents at approximately 100 RPM — six-step currents are held fairly steady": "约 100 RPM 时的实测电流——六步电流保持得相当平稳",
    "Measured currents at approximately 1000 RPM — a substantial fraction of the sector time is required to bring current to its steady-state value":
        "约 1000 RPM 时的实测电流——需要相当一部分扇区时间才能使电流达到稳态值",
    "Measured currents at approximately 2500 RPM — commanded currents rise, and the control loop utilizes all the available voltage but cannot reach a steady-state value by the end of each sector.":
        "约 2500 RPM 时的实测电流——指令电流上升，控制环路用尽所有可用电压，但在每个扇区结束时仍无法达到稳态值。",
    "FOC’s continuous commutation can achieve higher current at high speeds, making better use of available voltage, and minimizes torque ripple.":
        "FOC 的连续换相能在高速下实现更高的电流，更好地利用可用电压，并将转矩脉动降至最低。",
    "At steady state in FOC (constant speed and load torque), as long as the current controller can maintain a constant current vector I": "在 FOC 稳态下（恒定转速和负载转矩），只要电流控制器能维持恒定的电流矢量 I",
    ", motor torque ripple is zero.": "，电机转矩脉动即为零。",
    "Six-step torque ripple is affected by two factors:": "六步转矩脉动受两个因素影响：",
    "the": "即",
    "torque dependency for constant current": "恒定电流下的转矩依赖关系",
    "commutation transients that make torque ripple worse at increasing speeds": "使转矩脉动随转速升高而恶化的换相暂态",
    "The angle error of six-step causes excess I²R loss in the motor windings. Averaged over an electrical cycle — and neglecting the dynamics of commutation transients, which will increase the power dissipation further — for the same load torque, the I²R power dissipation in the windings is about 10% higher in six-step than in FOC:":
        "六步的角度误差会在电机绕组中造成额外的 I²R 损耗。在一个电周期内平均——并忽略会使功耗进一步增加的换相暂态动态——对于相同的负载转矩，六步绕组中的 I²R 功耗比 FOC 高约 10%：",
    "under assumptions of constant current — if the motor speed or inertia is high enough or velocity control is slow enough that the commanded current does not change much within each commutation sector, then I²R loss in six-step is 9.7% higher than in FOC. Currents in this case are shown in":
        "在恒定电流假设下——如果电机转速或惯性足够高，或速度控制足够慢，使得指令电流在每个换相扇区内变化不大，则六步的 I²R 损耗比 FOC 高 9.7%。这种情况下的电流如",
    "under assumptions of constant torque — if the motor speed or inertia is low enough, or velocity control is fast enough, that the commanded current varies within each commutation sector to keep torque constant. (":
        "在恒定转矩假设下——如果电机转速或惯性足够低，或速度控制足够快，使得指令电流在每个换相扇区内变化以保持转矩恒定。（",
    "where angle error": "其中角度误差",
    "varies from -30° to +30°) Currents in this case are shown in": "在 -30° 到 +30° 之间变化）这种情况下的电流如",
    "Comparison of FOC and six-step currents at equivalent average torque": "在等效平均转矩下 FOC 与六步电流的比较",
    "Comparison of FOC and six-step currents at equivalent instantaneous torque": "在等效瞬时转矩下 FOC 与六步电流的比较",
    "Note: this does": "注：这并",
    "not": "不",
    "mean that six-step is 10% less efficient; the exact decrease in efficiency depends on the motor construction and how much of the efficiency losses are resistive, meaning proportional to I². An oversized motor operating under some load condition in FOC where the mechanical power out is 98 W, and 2 W is dissipated in the windings, with negligible losses from other sources, would be 98% efficient; operating under the same conditions in six-step would raise winding dissipation by about 10% to 2.2W, making it 97.8% efficient.":
        "意味着六步效率低 10%；效率的确切下降取决于电机结构以及效率损耗中阻性（即与 I² 成正比）损耗所占的比例。一台在 FOC 下某种负载工况运行的过大电机，若机械输出功率为 98 W、绕组损耗为 2 W、其他损耗可忽略，则效率为 98%；在相同工况下以六步运行，绕组损耗约增加 10% 至 2.2 W，效率变为 97.8%。",
    "Switching loss under PWM operation can be reduced in six-step compared to FOC, by reducing the number of actively-switching transistors.":
        "与 FOC 相比，六步在 PWM 工作下可通过减少有源切换的晶体管数量来降低开关损耗。",
    "Six-step requires either 1, 2, or 4 transistors to be actively switching, depending on the switching pattern used, as shown in":
        "根据所用开关模式的不同，六步需要 1、2 或 4 个晶体管进行有源切换，如",
    ". One phase in each sector is unused, leaving two transistors completely off.":
        "所示。每个扇区中有一相未使用，使两个晶体管完全关断。",
    "1 or 2 actively-switching transistors: take the lowest-voltage motor terminal, turn on the lower transistor on that phase at 100% duty cycle. (See top row in": "1 或 2 个有源切换晶体管：取电压最低的电机端子，以 100% 占空比导通该相的下桥臂晶体管。（见",
    ".)": "顶行。）",
    "1 transistor: take the highest-voltage motor terminal, and actively switch the upper transistor. (relying on the lower transistor’s diode to carry free-wheeling current)":
        "1 个晶体管：取电压最高的电机端子，对上桥臂晶体管进行有源切换。（依靠下桥臂晶体管的二极管承载续流电流）",
    "2 transistors: actively switch both transistors of the highest-voltage motor terminal.":
        "2 个晶体管：对电压最高电机端子的两个晶体管都进行有源切换。",
    "2 or 4 actively-switching transistors: choose complementary PWM duty cycles of the upper switches for the two active phases: for example, phase A at 15% duty cycle, phase B at 85% duty cycle. Two transistors are enough if relying on diodes to carry free-wheeling current. (See bottom row in":
        "2 或 4 个有源切换晶体管：为两个有源相的上桥臂开关选择互补的 PWM 占空比，例如 A 相 15% 占空比、B 相 85% 占空比。若依靠二极管承载续流电流，两个晶体管即足够。（见",
    "The corresponding situations for FOC are either 2, 3, 4, or 6 actively-switching transistors, as shown in":
        "FOC 的对应情形为 2、3、4 或 6 个有源切换晶体管，如",
    ". (Two transistors can be kept out of active switching by choosing the lowest-voltage motor phase and turning on its low-side transistor; the number of actively-switching transistors remaining depends on whether synchronous rectification is used in a given half-bridge.)":
        "所示。（通过选取电压最低的电机相并导通其下桥臂晶体管，可使两个晶体管不参与有源切换；剩余有源切换晶体管的数量取决于特定半桥是否使用同步整流。）",
    "There are trade-offs in that reducing the number of actively-switching transistors usually increases the ripple current in the motor at the switching frequency, or will cause more conduction loss in the power stage diodes.":
        "这里存在折中：减少有源切换晶体管数量通常会增加电机在开关频率处的纹波电流，或导致功率级二极管导通损耗增大。",
    "In low-voltage motor drives where MOSFETs are used in the power stage, switching loss is usually small compared to conduction loss, and there’s no reason to try to reduce switching losses.":
        "在功率级使用 MOSFET 的低压电机驱动中，开关损耗通常远小于导通损耗，没有理由去刻意降低开关损耗。",
    "In motor drives that utilize IGBTs for higher voltage operation (powered by AC mains or electric vehicle batteries), switching loss is greater, whereas conduction loss in diodes is a much smaller concern.":
        "在使用 IGBT 进行更高电压运行（由交流市电或电动汽车电池供电）的电机驱动中，开关损耗更大，而二极管导通损耗则相对次要。",
    "Optimization of switching loss is a system-level task: motor control engineers should be discussing with their circuit designer counterparts to find the best solution.":
        "开关损耗的优化是一项系统级任务：电机控制工程师应与电路设计人员讨论以找到最佳方案。",
    "Aside from commutation transients from one sector to the next, six-step can be summarized by a single current:":
        "除从一个扇区到下一个扇区的换相暂态外，六步可用单个电流来概括：",
    "the highest-voltage motor terminal H has current I flowing into the motor terminal": "电压最高的电机端子 H 有电流 I 流入电机端子",
    "the lowest-voltage motor terminal L has the same current I flowing out of the motor terminal": "电压最低的电机端子 L 有相同的电流 I 流出电机端子",
    "the remaining motor terminal M is open-circuited, conducting zero current": "剩余的电机端子 M 开路，流过零电流",
    "FOC requires knowledge of the current vector, which has two degrees of freedom (three phase currents, but they add to zero, so knowing any two can determine the third)":
        "FOC 需要知道电流矢量，它有两个自由度（三个相电流之和为零，因此知道其中任意两个即可确定第三个）",
    "Because six-step control requires sensing one current, a single DC current sensor can be used.":
        "由于六步控制只需检测一个电流，因此可使用单个直流电流传感器。",
    "FOC requires either one, two, or three current sensors, depending on the method:":
        "FOC 需要一个、两个或三个电流传感器，取决于所用方法：",
    "three current sensors provides the highest accuracy and least noise": "三个电流传感器精度最高、噪声最小",
    "two current sensors provides knowledge about all three currents, with more noise and worse gain/offset accuracy than three current sensors, but otherwise no loss of information":
        "两个电流传感器可获知全部三相电流，噪声和增益/偏置精度比三个传感器差，但除此之外无信息损失",
    "a single DC current sensor can be used (": "可使用单个直流电流传感器（",
    ") with some constraints on signal conditioning and PWM duty cycle, and an increase in complexity, by sampling the current at multiple instants within the PWM period":
        "），但对信号调理和 PWM 占空比有一定约束，且复杂度增加，需在 PWM 周期内的多个时刻采样电流",
    "Systems with severe cost constraints may require the use of a single DC current sensor. (": "成本约束严格的系统可能需要使用单个直流电流传感器。（",
    "please see section on": "请参见关于",
    "For the same instantaneous torque, six-step and FOC require the same range of currents. (See": "对于相同的瞬时转矩，六步和 FOC 所需的电流范围相同。（见",
    "If equivalent instantaneous torque is not required, but we want to know how the current ranges compare for the same average torque, then the situation changes. (See":
        "如果不需要等效瞬时转矩，而是想知道在相同平均转矩下电流范围如何比较，则情况发生变化。（见",
    ".) For the same average torque, equivalent current amplitudes can be written for six-step and FOC. In six-step, current I":
        "。）对于相同的平均转矩，可为六步和 FOC 写出等效的电流幅值。在六步中，电流 I",
    "flows into one terminal of the motor and out another. If the FOC current is I": "流入电机的一个端子并从另一个端子流出。如果 FOC 电流幅值为 I",
    "in amplitude, then:": "，则：",
    "FOC requires about 10.3% higher peak current sense range than six-step, for the same motor. This is true even though six-step is less efficient: current I":
        "对于同一电机，FOC 所需的峰值电流检测范围比六步高约 10.3%。即便六步效率较低也是如此：电流 I",
    "into one terminal and out another has the equivalent three-phase vector magnitude of current that is": "流入一个端子并从另一个端子流出，其等效的三相电流矢量幅值为",
    ", so that six-step current sensing sneaks by with a lower peak current requirement.":
        "，因此六步电流检测能以更低的峰值电流要求蒙混过关。",
    "With FOC, the worst-case commutation angle with current amplitude I": "在 FOC 中，电流幅值 I 对应的最坏换相角",
    "is where I": "是 I",
    "flows into (or out of) one motor terminal, and half of this current flows out of (or into) each of the other two terminals. The best-case commutation angle for this current amplitude is where":
        "流入（或流出）一个电机端子，而该电流的一半从另外两个端子流出（或流入）的情况。该电流幅值对应的最佳换相角是",
    "flows into one motor terminal and out of another, and the third terminal carries zero current. Current sensors have to cover the full range of ±I":
        "流入一个电机端子并从另一个端子流出、第三个端子电流为零的情况。然而电流传感器必须覆盖 ±I 的完整范围",
    "See": "参见",
    "for a graphical portrayal; at the 30/90/150/210/270/330 degree points, the FOC current amplitudes are lower by 4.5% (a factor of": "的图形描述；在 30/90/150/210/270/330 度的点处，FOC 电流幅值比等效平均转矩下的六步电流低 4.5%（系数为",
    ") than the six-step current for equivalent average torque, but the FOC waveforms require higher current ranges at the peaks of the sine waves.":
        "），但 FOC 波形在正弦波峰值处需要更高的电流范围。",
    "In practical terms, this means that current sense circuitry, overcurrent circuitry, and (to a lesser extent) gate drives need to be designed to cover the full instantaneous phase current, so the requirements are slightly lower for six-step — if average torque rather than instantaneous torque is the determining factor.":
        "在实际中，这意味着电流检测电路、过流电路以及（在较小程度上）栅极驱动都需要设计成能覆盖完整的瞬时相电流，因此如果决定因素是平均转矩而非瞬时转矩，六步的要求略低。",
    "System components with ratings that depend more on root-mean-square current due to thermal reasons, such as connectors, wires, the power stage, and the motor itself, require higher ratings for six-step than for FOC. (See":
        "由于热原因其额定值更取决于方均根电流的系统部件（如连接器、导线、功率级和电机本身），在六步下比在 FOC 下需要更高的额定值。（见",
    "Cost optimization is a system-level task. Increased performance in current sensing can increase the utilization of the motor and power stage, and actually reduce the overall system cost.":
        "成本优化是一项系统级任务。提升电流检测性能可以提高电机和功率级的利用率，从而真正降低系统总成本。",
    "For example, imagine a digitally-controlled system that contains a $50 motor and $5 of power electronics, capable of carrying 10A continuous current, and $2 current-sensing components that are accurate within ±2%, which require derating the motor to use only 9.6A of its capability in the worst-case. (Digital control limited to 9.8A in firmware, so that if the sensors are underestimating current by 2%, it ensures the real motor current is no more than 10A — but if the sensors overestimate current by 2%, then only 9.6A might be used.)":
        "例如，设想一个数字控制系统，包含一个 50 美元的电机、5 美元的功率电子器件（能承受 10A 连续电流），以及 2 美元、精度在 ±2% 以内的电流检测元件，这要求在最坏情况下将电机降额至仅使用其 9.6A 的能力。（固件中将数字控制限制为 9.8A，这样即使传感器低估电流 2%，也能保证实际电机电流不超过 10A——但如果传感器高估电流 2%，则可能只用到 9.6A。）",
    "If better current-sensing components are used, that cost $2.50 but are accurate within ±0.5%, a slightly smaller motor capable of carrying 9.7A continuous current could be used to ensure that worst-case capability is at least 9.6A. (Digital control limited to 9.65A in firmware, corresponding to between 9.6A and 9.7A of real-world current.) If this 3% reduction in maximum current and torque saves more than $0.50 in the cost of the motor and power stage, then it is worth choosing more expensive current-sensing components.":
        "如果使用更好的电流检测元件，成本 2.50 美元但精度在 ±0.5% 以内，则可使用一个略小、能承受 9.7A 连续电流的电机，以确保最坏情况下的能力至少为 9.6A。（固件中将数字控制限制为 9.65A，对应实际电流在 9.6A 到 9.7A 之间。）如果最大电流和转矩这 3% 的降低能在电机和功率级成本上节省超过 0.50 美元，那么选择更贵的电流检测元件就是值得的。",
    "Techniques that “save money” because they allow less expensive current sensing (higher tolerance, reduced number of sensors) under nominal operation may actually cost more, because the overall system design sees lower worst-case utilization of motor and power electronics that will need to be oversized as a result.":
        "那些因为在标称工况下允许使用更便宜的电流检测（更高容差、更少传感器数量）而“省钱”的技术，实际上可能花费更多，因为系统整体设计会看到电机和功率电子器件最坏情况利用率降低，从而需要将其选得更大。",
    "Six-step controllers can be simpler than FOC, requiring only these components:":
        "六步控制器可以比 FOC 更简单，只需以下组成部分：",
    "sector determination": "扇区判定",
    "a scalar current loop, or no current control loop": "一个标量电流环，或不使用电流控制环",
    "sector application (determining how to apply the current loop output to different PWM phases)":
        "扇区应用（决定如何将电流环输出施加到不同 PWM 相）",
    "FOC requires a vector current loop and coordinate transforms — these are roughly 2 – 3 times the computational equivalent of the components listed above for six-step. The lower CPU usage for six-step can allow the system designer to work with a higher PWM switching frequency and electrical frequency for certain types of motors. (Higher switching frequency reduces current ripple in low-inductance motors; electrical frequency is proportional to motor velocity, so higher electrical frequency is required for high-speed motors.)":
        "FOC 需要矢量电流环和坐标变换——其计算量大约是上述六步各组件总和的 2–3 倍。六步较低的 CPU 占用可使系统设计者对某些类型电机采用更高的 PWM 开关频率和电频率。（更高的开关频率可降低低电感电机的电流纹波；电频率与电机速度成正比，因此高速电机需要更高的电频率。）",
    "In addition, if a sensorless position/velocity estimator is required, the complexity is higher for FOC than for sensorless six-step estimators.":
        "此外，如果需要无传感器位置/速度估计器，FOC 的复杂度高于无传感器六步估计器。",
    "5.1.7. Comparison between FOC and six-step control": "5.1.7. FOC 与六步控制的比较",
    "5.1.7.1. Torque capability": "5.1.7.1. 转矩能力",
    "5.1.7.1.1. Torque degradation from angle error": "5.1.7.1.1. 由角度误差引起的转矩下降",
    "5.1.7.1.2. Torque degradation from dynamics of commutation": "5.1.7.1.2. 由换相动态引起的转矩下降",
    "5.1.7.2. Torque ripple": "5.1.7.2. 转矩脉动",
    "5.1.7.3. Efficiency": "5.1.7.3. 效率",
    "5.1.7.4. Switching loss": "5.1.7.4. 开关损耗",
    "5.1.7.5. Current management": "5.1.7.5. 电流管理",
    "5.1.7.5.1. Current sensing": "5.1.7.5.1. 电流检测",
    "5.1.7.5.2. Current range": "5.1.7.5.2. 电流范围",
    "5.1.7.6. Cost optimization": "5.1.7.6. 成本优化",
    "5.1.7.7. Control complexity": "5.1.7.7. 控制复杂度",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
