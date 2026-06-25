# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/overmodulation"
title_zh = "5.1.4. 过调制"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Overmodulation": "过调制",
    "Current measurement": "电流测量",
    "DC link compensation": "母线电压补偿",
    "Modulation index": "调制指数",
    "Overmodulation behavior in the stationary frame": "静止坐标系中的过调制行为",
    "Overmodulation behavior in the synchronous frame": "同步坐标系中的过调制行为",
    "Coordinating overmodulation and controller limits": "协调过调制与控制器限幅",
    "Implementation Notes": "实现说明",
    "Feature support": "功能支持",
    "References": "参考文献",
    "Overmodulation example": "过调制示例",
    "Synchronous frame behavior of overmodulation": "过调制在同步坐标系中的行为",
    "Metrics of overmodulation in the synchronous frame, as a function of modulation index":
        "同步坐标系中过调制的指标随调制指数的变化",
    "Interacting limits in overmodulation": "过调制中的相互制约限幅",
    "Overmodulation is a method of increasing the output voltage capability of a motor drive using three-phase modulation. This is achieved by allowing distortion in the output voltages for modulation indices above 1.0. Benefits include a slight increase in potential speed range, as well as slightly faster current control capability because of the increased output voltage range.":
        "过调制是一种利用三相调制提高电机驱动输出电压能力的方法。其实现方式是允许调制指数大于 1.0 时输出电压出现畸变。其收益包括潜在调速范围的轻微扩大，以及由于输出电压范围增大而带来的电流控制能力的略微提升。",
    "shows three-phase modulation waveforms for five increasing values of modulation index.":
        "展示了五个递增调制指数下的三相调制波形。",
    "— the upper row of subplots illustrates voltage trajectories in the stationary (":
        "——上方一行子图绘制的是静止（",
    ") reference frame, while the lower row illustrates voltage trajectories plotted vs. time. The dashed circle in the stationary frame represents a modulation index of 1.0 (maximum output voltage capability without distortion); the dashed hexagon in the stationary frame and dashed lines in the timeseries plots represent maximum voltage capability including distortion. Five different values of modulation index":
        "）坐标系中的电压轨迹，下方一行则是电压轨迹随时间的变化。静止坐标系中的虚线圆表示调制指数 1.0（无畸变时的最大输出电压能力）；静止坐标系中的虚线六边形和时间序列图中的虚线表示包含畸变在内的最大电压能力。图中展示了五个不同的调制指数",
    "are shown, one in each column. Line-to-neutral timeseries waveforms are shown in faint colors.":
        "，每列一个。相电压（线至中性点）时间序列波形以浅色显示。",
    "The modulation index represents output amplitudes normalized to the": "调制指数表示输出幅值相对于",
    "full voltage span": "满电压跨度",
    ". This is the DC link voltage, multiplied by the difference between the maximum and minimum allowable duty cycles applied to each half bridge; for example, in the following situation the full voltage span is 23 V = 25 V × (95% − 3%):":
        "的归一化值。它是母线电压乘以每个半桥所施加的最大与最小允许占空比之差；例如，在以下情形中满电压跨度为 23 V = 25 V ×（95% − 3%）：",
    "DC link voltage of 25 V": "母线电压 25 V",
    "Dead time of 1% (for example 500 ns with a period of 50 μs)": "死区 1%（例如周期 50 μs 时为 500 ns）",
    "Minimum half-bridge duty cycle of 3% (upper transistors at 2%, lower transistors at 96%)":
        "半桥最小占空比 3%（上桥臂晶体管 2%，下桥臂晶体管 96%）",
    "Maximum half-bridge duty cycle of 95% (upper transistors at 94%, lower transistors at 4%)":
        "半桥最大占空比 95%（上桥臂晶体管 94%，下桥臂晶体管 4%）",
    "This definition may be different in this context than in other situations. In this analysis of three-phase modulation, the modulation index represents voltages relative to the full voltage capability":
        "在本语境中，该定义可能与其他场合不同。在本三相调制分析中，调制指数表示相对于满电压能力的电压",
    "subject to duty cycle limitations": "（受占空比限制）",
    "A modulation index of 1.0 represents the maximum possible voltage amplitude for which a set of three-phase line-to-line sine waves can be achieved without distortion, and is shown in":
        "调制指数 1.0 表示能够无畸变地获得一组三相线电压正弦波的最大可能电压幅值，如",
    "as the dotted circle. Output timeseries waveforms using": "中的点线圆所示。使用",
    "zero-sequence modulation": "零序调制",
    "(aka space-vector modulation) below this point have a characteristic “double-humped” shape when shown as line-to-negative-link, but the line-to-line voltages are sinusoidal.":
        "（即空间矢量调制）在此点以下时的输出时间序列波形，在以线至母线负端表示时呈现特征性的“双驼峰”形状，但线电压是正弦的。",
    "Above a modulation index of 1.0, we must do something to limit the output waveforms on each phase within the range of allowable duty cycles. There are several methods of doing this:":
        "当调制指数超过 1.0 时，必须采取某种方法将每相的输出波形限制在允许的占空比范围内。有几种方法可以做到这一点：",
    "The simplest is just to operate on each phase’s duty cycle individually, constraining within limits. This produces a realizable point in the":
        "最简单的方法是分别对每相占空比进行限幅。这会在",
    "reference frame that is the closest distance to the ideal unconstrained value.":
        "坐标系中产生一个距理想无约束值最近的可实现点。",
    "This clipping approaches a trapezoidal waveform when plotted as a timeseries; in the":
        "这种限幅在时间序列上趋近于梯形波；在",
    "reference frame, the voltage trajectory becomes “squished” against the hexagonal limit.":
        "坐标系中，电压轨迹被“挤压”到六边形限幅边界上。",
    "Another approach is to scale the three-phase set of duty cycles by some identical scaling factor":
        "另一种方法是用某个相同的比例因子对三相占空比组进行缩放",
    ", where": "，其中",
    "is the difference between the highest and lowest duty cycle in the 3-phase set;": "为三相组中最高与最低占空比之差；",
    "is 1.0 below overmodulation, and less than 1.0 when operating in overmodulation. In this case, the realizable and ideal points in the":
        "在过调制以下时为 1.0，过调制运行时小于 1.0。此时",
    "reference frame maintain identical commutation angle. Drawbacks are that the computation is slightly more expensive (involving a divide), and less distortion is possible.":
        "坐标系中的可实现点与理想点保持相同的换相角。缺点是计算开销略大（涉及一次除法），且可达到的畸变程度较小。",
    "There is also an algorithmic approach described in": "还有一种算法方法描述于",
    "an article by Peng et al": "Peng 等人的文章",
    "called the method of": "中，称为",
    "realizable references": "可实现参考法",
    ". This has been applied to three-phase modulation in": "。该方法已被应用于",
    "an article by Briz et al": "Briz 等人的文章",
    ". It involves close coordination between the current controller and the saturation logic that restricts the output duty cycle.":
        "中的三相调制。它需要电流控制器与限制输出占空比的饱和逻辑之间紧密协调。",
    "The method of realizable references appears promising, but its complexity in both analysis and implementation precluded using it within the MCAF. The implementation used in the MCAF and shown in":
        "可实现参考法看起来很有前景，但其在分析和实现上的复杂度使其未能在 MCAF 中采用。MCAF 中采用并展示于",
    "utilizes the simple per-phase clipping.": "的实现使用的是简单的逐相限幅。",
    "shows these voltage trajectories transformed into the synchronous (dq) reference frame. Below overmodulation, each is a single point: if we wanted some constant modulation index":
        "展示了变换到同步（dq）坐标系后的这些电压轨迹。在过调制以下，每条轨迹都是一个点：如果我们想要某个恒定调制指数",
    ", we can get exactly that. Upon entering overmodulation, the voltage trajectories no longer have constant values in the dq-frame. This represents voltage harmonics that appear as d- and q-axis distortion. These harmonics are at multiples of 6 times the electrical frequency; for example, if we are producing a 100Hz carrier frequency, then overmodulation harmonics appear at 600Hz, 1200Hz, 1800Hz, and so on. Because overmodulation is used primarily to run at higher speeds, where back-emf requirements are greater, these harmonics are usually above the current controller bandwidth, where the controller is not able to attenuate them, so they do appear in the current waveforms as well as voltage waveforms, although motor inductance usually keeps them at a fairly low level.":
        "，就能精确得到。一旦进入过调制，电压轨迹在 dq 坐标系中不再保持恒定值。这代表了以 d 轴和 q 轴畸变形式出现的电压谐波。这些谐波频率为电频率的 6 倍数的整数倍；例如，若产生 100Hz 的载波频率，则过调制谐波出现在 600Hz、1200Hz、1800Hz 等。由于过调制主要用于在更高转速下运行（此时反电动势要求更大），这些谐波通常高于电流控制器带宽，控制器无法将其衰减，因此它们确实会出现在电流波形和电压波形中，不过电机电感通常将其保持在相当低的水平。",
    "— trajectories plotted for increments of 0.1 in modulation index, and each is labeled with the corresponding modulation index. The d- and q-axes have been normalized so that 1.0 represents a modulation index of 1.0. Colors have no inherent significance other than to distinguish each of the trajectories.":
        "——以 0.1 为调制指数增量绘制的轨迹，每条标注了对应的调制指数。d 轴和 q 轴已归一化，使 1.0 表示调制指数 1.0。颜色仅用于区分各条轨迹，无内在含义。",
    "We can also gain some insight by graphing average behavior over a full commutation cycle as a function of modulation index, shown in":
        "我们还可以通过绘制一个完整换相周期内的平均行为随调制指数的变化来获得一些认识，如",
    "— here we show the mean value of the resulting trajectory in the dq reference frame, as well as its incremental gain (":
        "所示——这里展示了 dq 坐标系中所得轨迹的平均值及其增量增益（",
    "), along with the root-mean-square (RMS) value of d- and q-axis voltage over the commutation cycle. This shows the magnitude of distortion along each axis, as a function of modulation index.":
        "），以及一个换相周期内 d 轴和 q 轴电压的方均根（RMS）值。这展示了沿各轴畸变的大小随调制指数的变化。",
    "A few things to note here, as modulation index increases past 1.0:": "当调制指数超过 1.0 时，有几点需要注意：",
    "The mean value of": "的平均值",
    "is a nonlinear function of modulation index; it does increase beyond 1.0 (that’s the whole point of overmodulation) but it asymptotically approaches a maximum value of":
        "是调制指数的非线性函数；它确实会超过 1.0（这正是过调制的意义所在），但渐近地趋于一个最大值",
    "(the factor of": "（其中",
    "is the distance between the origin and each point of the hexagon, and the": "为原点到六边形各点的距离，",
    "factor represents the mean value of": "因子表示",
    "within the range": "在范围内的平均值",
    "The incremental gain quickly drops, from 1 at m = 1.0, down to below 0.1 at m = 1.15.":
        "增量增益迅速下降，从 m = 1.0 时的 1 降至 m = 1.15 时的 0.1 以下。",
    "The d-axis distortion and q-axis distortion both asymptotically approach values that reflect the extreme case of six-step operation (with active switching on all three half-bridges; this is different than most implementations of six-step control that only operate two half-bridges at a time) where the trajectory forms a 60° arc in the d-q plane:":
        "d 轴畸变和 q 轴畸变都渐近地趋近于反映六步运行极端情形（三个半桥同时有源切换；这与大多数六步控制实现每次只操作两个半桥不同）的值，此时轨迹在 d-q 平面内形成一段 60° 的圆弧：",
    "The RMS q-axis distortion rises quickly, reaching approximately 0.0467 by": "q 轴 RMS 畸变迅速上升，在",
    ", hitting a maximum of approximately 0.0588 near": "时达到约 0.0467，在",
    ", and then decreasing asymptotically towards 0.04627 at very large modulation indices.":
        "附近达到约 0.0588 的最大值，随后在调制指数很大时渐近下降至 0.04627。",
    "The RMS d-axis distortion rises slowly, reaching only approximately 0.0208 by": "d 轴 RMS 畸变上升缓慢，在",
    "All of these factors make overmodulation attractive at moderate modulation indices, but unattractive at extreme modulation indices. We can get that theoretical maximum voltage increase of 10.27%, but to do this requires extreme modulation indices, so in practical terms we are limited to somewhere around 3% – 7% “extra” voltage capability, by limiting the maximum modulation index to somewhere in the 1.05 – 1.25 range.":
        "所有这些因素使过调制在中等调制指数下具有吸引力，而在极端调制指数下则不然。理论上可获得 10.27% 的最大电压提升，但为此需要极端的调制指数，因此在实际中，通过将最大调制指数限制在 1.05–1.25 范围内，我们大约只能获得 3%–7% 的“额外”电压能力。",
    "The nonlinear dependency of mean": "平均值的非线性依赖",
    "on modulation index makes applying overmodulation to a vector current controller somewhat interesting.":
        "于调制指数，使得将过调制应用于矢量电流控制器变得有些有趣。",
    "shows the limits in the dq frame attainable by overmodulation (essentially a hexagon rotating along with the commutation angle) and the limits applied by the MCAF current controller, namely a rectangular region with independent limits for each axis.":
        "展示了过调制在 dq 坐标系中可达到的限幅（本质上是一个随换相角旋转的六边形）以及 MCAF 电流控制器施加的限幅，即对各轴独立限幅的矩形区域。",
    "— the rectangle R1 in the dq frame represents the output voltage limits of the current controller. The hexagon rotates with commutation angle":
        "——dq 坐标系中的矩形 R1 表示电流控制器的输出电压限幅。六边形随换相角",
    "and indicate physical limits attainable through three-phase modulation. Circle C1 represents a modulation index of 1, and circle C2 represents a modulation index of":
        "旋转，表示通过三相调制可达到的物理限幅。圆 C1 表示调制指数 1，圆 C2 表示调制指数",
    "showing the outer locus of the hexagonal limit.": "，即六边形限幅的外边界。",
    "The selection of d- and q-axis controller limits is important; see the implementation notes below for particular recommendations. The “corner” operation (high values in both axes) is important; both axes are competing for voltage and the effective modulation index adds in quadrature. Operation in this corner is rare and usually confined to transients in the current controller. The reason for requiring more voltage along the q-axis is to accommodate the back-emf at high speeds; static values of d-axis voltage are required only by the inductive voltage drop":
        "d 轴和 q 轴控制器限幅的选择很重要；具体建议见下文的实现说明。“角落”运行（两轴都取高值）很重要：两轴争夺电压，有效调制指数按正交相加。在该角落的运行很少见，通常仅限于电流控制器的暂态过程。要求 q 轴方向有更多电压是为了适应高速下的反电动势；d 轴电压的静态值仅由电感压降",
    "and a resistive voltage drop": "和电阻压降",
    "present only with non-zero d-axis current (used in flux weakening operation, or in maximum-torque-per-ampere control with salient-pole rotors — neither of which the MCAF supports at this time).":
        "（仅在 d 轴电流非零时存在，用于弱磁运行或凸极转子的最大转矩/电流比控制——MCAF 目前均不支持）所需。",
    "The MCAF implementation of the forward path (in": "MCAF 的前向通路实现（见",
    ", the top row of blocks, including current controller, inverse Park and Clarke transforms, DC link voltage compensation, and zero-sequence modulation) relies only on the current controller and ZSM blocks to provide limiting and guard against overflow. As long as the current controller limits its outputs below a vector magnitude of":
        "，最上方一行模块，包括电流控制器、逆 Park 和 Clarke 变换、母线电压补偿以及零序调制）仅依靠电流控制器和 ZSM 模块来提供限幅并防止溢出。只要电流控制器将其输出限制在矢量幅值",
    ", subsequent blocks will not overflow. The output limits for each axis are a fixed constant for each axis (":
        "以下，后续模块就不会溢出。各轴的输出限幅是该轴的一个固定常数（",
    "and": "和",
    ") multiplied by the DC link voltage, so this means that": "）乘以母线电压，因此这意味着",
    "In the MCAF software, current controller voltages are expressed in terms of line-to-neutral voltages, so a modulation index of 1.0 corresponds to a line-to-neutral voltage of":
        "在 MCAF 软件中，电流控制器电压以相电压（线至中性点）表示，因此调制指数 1.0 对应的相电压为",
    ". If the d-axis and q-axis limits are expressed as modulation index limits": "。如果 d 轴和 q 轴限幅以调制指数限幅表示",
    ", then": "，则",
    "and the requirement is that": "，且要求",
    ". The default values of these limits in the MCAF is": "。MCAF 中这些限幅的默认值为",
    ". (Software values are": "。（软件值为",
    "and appear as": "，并以",
    "MCAF_CURRENT_CTRL_D_OUT_LIMIT": "MCAF_CURRENT_CTRL_D_OUT_LIMIT",
    "in parameters/foc_params.h.) We recommend a d-axis modulation index limit of 1.0, and a q-axis modulation index limit kept in the 1.05 – 1.25 range. This leaves some design margin (":
        "的形式出现在 parameters/foc_params.h 中。）我们建议 d 轴调制指数限幅取 1.0，q 轴调制指数限幅保持在 1.05–1.25 范围内。这既留出了一定的设计裕量（",
    ") and still provides significant voltage capability through overmodulation.": "），又能通过过调制提供显著的电压能力。",
    "Overmodulation was not present in MCAF R1 but has been added in MCAF R2.":
        "过调制在 MCAF R1 中不存在，已在 MCAF R2 中加入。",
    "Youbin Peng, D. Vrancic and R. Hanus,": "Youbin Peng, D. Vrancic and R. Hanus,",
    "“Anti-windup, bumpless, and conditioned transfer techniques for PID controllers”":
        "“Anti-windup, bumpless, and conditioned transfer techniques for PID controllers”",
    "IEEE Control Systems": "IEEE Control Systems",
    ", vol. 16, no. 4, pp. 48-57, Aug 1996.": ", vol. 16, no. 4, pp. 48-57, Aug 1996.",
    "F. Briz, A. Diez, M. W. Degner and R. D. Lorenz,": "F. Briz, A. Diez, M. W. Degner and R. D. Lorenz,",
    "“Current and flux regulation in field-weakening operation”": "“Current and flux regulation in field-weakening operation”",
    "IEEE Transactions on Industry Applications": "IEEE Transactions on Industry Applications",
    ", vol. 37, no. 1, pp. 42-50, Jan/Feb 2001.": ", vol. 37, no. 1, pp. 42-50, Jan/Feb 2001.",
    "5.1.4. Overmodulation": "5.1.4. 过调制",
    "5.1.4.1. Modulation index": "5.1.4.1. 调制指数",
    "5.1.4.2. Overmodulation behavior in the stationary frame": "5.1.4.2. 静止坐标系中的过调制行为",
    "5.1.4.3. Overmodulation behavior in the synchronous frame": "5.1.4.3. 同步坐标系中的过调制行为",
    "5.1.4.4. Coordinating overmodulation and controller limits": "5.1.4.4. 协调过调制与控制器限幅",
    "5.1.4.5. Implementation Notes": "5.1.4.5. 实现说明",
    "5.1.4.5.1. Feature support": "5.1.4.5.1. 功能支持",
    "5.1.4.6. References": "5.1.4.6. 参考文献",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
