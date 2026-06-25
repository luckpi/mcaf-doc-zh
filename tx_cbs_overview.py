# -*- coding: utf-8 -*-
import txutil

rel = "implementation/custom-board-support/overview"
title_zh = "6.6.1. motorBench Development Suite 中的板卡支持概述"

m = {
    "General Implementation Issues": "通用实现问题",
    "Custom Board Support": "定制板卡支持",
    "Overview of board support in motorBench": "motorBench 中的板卡支持概述",
    "Development Suite": "Development Suite",
    "Creating a custom board configuration": "创建定制板卡配置",
    "motorBench User’s Guide": "motorBench 用户指南",
    "Scope of hardware support": "硬件支持范围",
    "Board configuration features": "板卡配置功能",
    "Assumptions": "假设",
    "Current measurement": "电流测量",
    "Voltage measurement": "电压测量",
    "Board definition file structure": "板卡定义文件结构",
    "System parameters": "系统参数",
    "Hardware components supported by MCAF": "MCAF 支持的硬件组件",
    "ADC input to measured phase / DC link current specification": "ADC 输入与被测相/母线电流的规格关系",
    "ADC input to measured phase / DC link voltage specification": "ADC 输入与被测相/母线电压的规格关系",
    "Current polarity conventions": "电流极性约定",
    "current sense channels": "电流检测通道",
    "Custom board definition format": "定制板卡定义格式",
    "Custom board schema": "定制板卡架构",
    "Modifying the starter board definition": "修改起始板卡定义",
    "three current measurement methods": "三种电流测量方法",
    "Digital Signal Controller": "数字信号控制器",
    "MCAF supports custom boards as of MCAF R8. Users may now configure motorBench":
        "MCAF 自 MCAF R8 起支持定制板卡。用户现在可以配置 motorBench",
    "Development Suite for use with a wide range of motor control boards with a variety of features. To configure a custom board, users can define a board configuration in the form of a board definition file. From there, motorBench can automatically configure MCC peripherals and then generate code based on the board configuration and other parameters set in the motorBench Configure, Tuning, and Customize pages.":
        "Development Suite，以适配具有各种功能的广泛电机控制板卡。要配置定制板卡，用户可以以板卡定义文件的形式定义板卡配置。然后，motorBench 可以自动配置 MCC 外设，并根据板卡配置和 motorBench 的 Configure（配置）、Tuning（整定）和 Customize（定制）页面中设置的其他参数生成代码。",
    "See the": "详见",
    "for more information.": "以获取更多信息。",
    "illustrates the typical components of a motor drive hardware design that are within the scope of MCAF’s board support functionality.":
        "展示了电机驱动硬件设计中属于 MCAF 板卡支持功能范围的典型组件。",
    "Note": "注",
    "Motor terminals are shown above as A, B, and C. MCAF firmware reflects this naming choice. Some drive designs or motors may have terminals named U, V, and W; if this is the case, use A, B, and C, to substitute for U, V, and W, respectively.":
        "上图中的电机端子以 A、B、C 表示。MCAF 固件反映了这一命名选择。某些驱动设计或电机可能使用 U、V、W 命名端子；在这种情况下，请分别用 A、B、C 替代 U、V、W。",
    "The following table details the features that can be configured for a custom board.":
        "下表详列了可为定制板卡配置的功能。",
    "Note that at least one of the": "请注意，",
    "(single-, dual- or triple-channel) is required in order for a board to be compatible with motorBench.":
        "（单通道、双通道或三通道）中至少需要一种，板卡才能与 motorBench 兼容。",
    "Category": "类别",
    "Supported board feature": "支持的板卡功能",
    "Required": "是否必需",
    "Comments": "说明",
    "Device": "器件",
    "dsPIC": "dsPIC",
    "Devices from the following device families:": "支持以下器件系列：",
    "dsPIC33CK": "dsPIC33CK",
    "dsPIC33CDV, dsPIC33CDVC and dsPIC33CDVL": "dsPIC33CDV、dsPIC33CDVC 和 dsPIC33CDVL",
    "dsPIC33E (custom board feature is not supported, peripherals must be configured manually in MCC)":
        "dsPIC33E（不支持定制板卡功能，外设必须在 MCC 中手动配置）",
    "MCP802x gate driver": "MCP802x 栅极驱动器",
    "MCP8021/MCP8022/MCP8027 supported by the MCC library": "MCC 库支持的 MCP8021/MCP8022/MCP8027",
    "Analog": "模拟",
    "DC link voltage measurement": "母线电压测量",
    "Needed for DC link compensation in MCAF": "MCAF 母线电压补偿所需",
    "Phase current — two phases": "相电流——两相",
    "Phases A and B are required for dual-channel and triple-channel measurement (which also needs phase C).":
        "双通道和三通道测量需要 A 相和 B 相（三通道还需要 C 相）。",
    "DC link measurement is required for single-channel measurement.":
        "单通道测量需要母线电流测量。",
    "Phase current — three phases": "相电流——三相",
    "DC link current": "母线电流",
    "Phase voltage — three phases": "相电压——三相",
    "Op amps for current measurement": "用于电流测量的运放",
    "Op amps that are internal to the dsPIC, or external/discrete devices":
        "dsPIC 内部运放，或外部/分立器件",
    "Potentiometer": "电位器",
    "Used by MCAF sample application to control motor speed": "MCAF 示例应用用于控制电机速度",
    "Inverter bridge temperature sensor": "逆变桥温度传感器",
    "Absolute voltage reference": "绝对电压基准",
    "Custom analog channels": "定制模拟通道",
    "These channels will be queued for sequential sampling in every MCAF ADC interrupt cycle.":
        "这些通道将在每个 MCAF ADC 中断周期中排队进行顺序采样。",
    "Digital": "数字",
    "PWM fault": "PWM 故障",
    "Overcurrent fault, for example. This can be set to": "例如过流故障。可设置为",
    "none": "none",
    "if not available.": "（若无）。",
    "UART": "UART",
    "Required for real-time diagnostic kernel support. High baud rate UART support circuitry is suggested (at least 115.2Kbaud, but 921.6K or higher recommended).":
        "实时诊断内核支持所需。建议使用高波特率 UART 支持电路（至少 115.2K 波特，推荐 921.6K 或更高）。",
    "Programmer/debugger": "编程器/调试器",
    "Need to specify the programming pin pair (PGD/PGCx)": "需指定编程引脚对（PGD/PGCx）",
    "Oscillator": "振荡器",
    "Internal FRC / external clock / crystal": "内部 FRC/外部时钟/晶振",
    "Internal comparator": "内部比较器",
    "Only one instance is supported in this release of motorBench": "本版 motorBench 仅支持一个实例",
    "Pushbuttons": "按钮",
    "Up to two pushbuttons are supported for use with MCAF. Application may define additional pushbuttons using custom GPIOs. The GPIO names":
        "MCAF 最多支持两个按钮。应用可使用定制 GPIO 定义额外按钮。GPIO 名称",
    "MCAF_BUTTON1": "MCAF_BUTTON1",
    "and": "和",
    "MCAF_BUTTON2": "MCAF_BUTTON2",
    "are reserved for the MCAF pushbuttons.": "为 MCAF 按钮保留。",
    "LEDs": "LED",
    "Up to two LEDs are supported for use with MCAF. Application may defined additional LEDs using custom GPIOs. The GPIO names":
        "MCAF 最多支持两个 LED。应用可使用定制 GPIO 定义额外 LED。GPIO 名称",
    "MCAF_LED1": "MCAF_LED1",
    "MCAF_LED2": "MCAF_LED2",
    "are reserved for the MCAF LEDs.": "为 MCAF LED 保留。",
    "Test point": "测试点",
    "One test point is supported for use with MCAF. Probing the test point will show a pulse at PWM switching frequency, representing the time interval when the MCAF ADC ISR is executing. The GPIO name":
        "MCAF 支持一个测试点。探测该测试点会显示一个 PWM 开关频率的脉冲，表示 MCAF ADC ISR 正在执行的时间间隔。GPIO 名称",
    "MCAF_TESTPOINT1": "MCAF_TESTPOINT1",
    "is reserved for the MCAF test point.": "为 MCAF 测试点保留。",
    "QEI": "QEI",
    "Only one instance is supported in this release of motorBench for use with MCAF.":
        "本版 motorBench 用于 MCAF 时仅支持一个实例。",
    "Custom GPIOs": "定制 GPIO",
    "Application-specific digital inputs and outputs": "应用特定的数字输入和输出",
    "Guidance for adding MCAF features to a custom board is provided in": "关于向定制板卡添加 MCAF 功能的指导见",
    ". See the": "。完整的可添加到定制板卡的功能分解见",
    "for a full breakdown of the features that can be added to a custom board.":
        "。",
    "MCAF requires the phase and DC link current measurement circuits to provide analog input to the ADC with a DC bias of":
        "MCAF 要求相电流和母线电流测量电路向 ADC 提供具有",
    "in order to be able to measure current across a range from negative full-scale (":
        "直流偏置的模拟输入，以便能测量从负满量程（",
    ") to positive full-scale (": "）到正满量程（",
    ") as shown in": "）范围内的电流，如",
    "Depending on the circuit design, the sign of some of the current channels may need to be inverted. (See":
        "根据电路设计的不同，某些电流通道的符号可能需要反转。（参见",
    "for more information.)": "以获取更多信息。）",
    "MCAF will automatically handle this sign inversion as long as it is configured in the appropriate":
        "只要在板卡定义文件的相应",
    "of the board definition file.": "中进行了配置，MCAF 将自动处理此符号反转。",
    "MCAF determines the current scaling of the board based on the full-scale phase current given in the board definition file. The full-scale DC link current in the board definition file has no impact on any part of the code generation process.":
        "MCAF 根据板卡定义文件中给出的满量程相电流来确定板卡的电流比例。板卡定义文件中的满量程母线电流对代码生成过程的任何部分都没有影响。",
    "MCAF requires the DC link voltage measurement circuit to provide analog input to the ADC with zero DC bias to be able to measure voltage from 0V to positive full-scale (":
        "MCAF 要求母线电压测量电路向 ADC 提供零直流偏置的模拟输入，以便能测量从 0V 到正满量程（",
    "The same specification applies for phase voltage measurement, which is optionally supported by MCAF.":
        "相同的规格也适用于相电压测量（MCAF 可选支持）。",
    "The board definition file is a hierarchical data model that describes various configuration settings. The serialization format used in motorBench is YAML; we may expand this to include support for JSON and/or TOML in future revisions of motorBench":
        "板卡定义文件是一个描述各种配置设置的层次化数据模型。motorBench 使用的序列化格式为 YAML；未来版本的 motorBench",
    "Development Suite.": "Development Suite 可能扩展为支持 JSON 和/或 TOML。",
    "For more information, see": "更多信息请参见",
    "System parameters are application-specific properties that can be viewed and edited in the Configure page of motorBench":
        "系统参数是应用特定的属性，可在 motorBench",
    "Development Suite. They include parameters such as PWM frequency and dead time, which are application choices, rather than inherent, fixed properties of a board. For this reason they are not part of a board definition — but they do need to meet the constraints of the board, for example maximum PWM frequency or minimum dead time.":
        "Development Suite 的 Configure（配置）页面中查看和编辑。它们包括 PWM 频率和死区等参数，这些是应用选择，而非板卡的固有固定属性。因此它们不是板卡定义的一部分——但确实需要满足板卡的约束条件，例如最大 PWM 频率或最小死区。",
    "The overall concept is analogous to getting some food in a buffet.":
        "整体概念类似于在自助餐厅取食物。",
    "Meal = project at hand": "餐食 = 手头的项目",
    "Food = project properties / system parameters": "食物 = 项目属性/系统参数",
    "Plate = board": "盘子 = 板卡",
    "The system parameters are “on top of” the board and need to fit within the constraints of the board.":
        "系统参数“在板卡之上”，需要符合板卡的约束。",
    "System parameters configurable in motorBench are:": "可在 motorBench 中配置的系统参数为：",
    "System parameter": "系统参数",
    "Type": "类型",
    "Unit": "单位",
    "Editable": "可编辑",
    "Use maximum supported system clock frequency (Fosc)": "使用最大支持的系统时钟频率（Fosc）",
    "Boolean": "布尔",
    "System clock frequency (Fosc)": "系统时钟频率（Fosc）",
    "Integer": "整数",
    "MHz": "MHz",
    "Editable only if the maximum supported system clock frequency is not being used.":
        "仅在不使用最大支持系统时钟频率时可编辑。",
    "PWM frequency": "PWM 频率",
    "Float": "浮点",
    "kHz": "kHz",
    "Initialized to default": "初始化为默认值",
    "PWM dead time": "PWM 死区",
    "ns": "ns",
    "Current control loop sampling time factor": "电流控制环采样时间系数",
    "Tpwm": "Tpwm",
    "Sampling time of current control loop as a multiple of PWM periods.":
        "电流控制环采样时间，以 PWM 周期的倍数表示。",
    "Velocity control loop sampling time factor": "速度控制环采样时间系数",
    "Sampling time of voltage control loop as a multiple of PWM periods.":
        "电压控制环采样时间，以 PWM 周期的倍数表示。",
    "ADC sampling time": "ADC 采样时间",
    "Nominal DC link voltage": "标称母线电压",
    "System parameters should be configured to meet application requirements after a board configuration file is imported.":
        "导入板卡配置文件后，应配置系统参数以满足应用需求。",
    "MCAF reserves two hardware timers, which are configured by MCC and not part of the custom board definition file:":
        "MCAF 保留了两个硬件定时器，由 MCC 配置，不属于定制板卡定义文件：",
    "Tick timer": "Tick 定时器",
    ": used for the internal": "：用于内部",
    "board service": "板卡服务",
    "timer ISR; the timer period is set via the": "定时器 ISR；定时器周期通过 motorBench",
    "UI service period": "UI 服务周期",
    "parameter on the Customize page of motorBench": "的 Customize（定制）页面上的",
    "Profiling timer": "性能分析定时器",
    ": used for": "：用于",
    "profiling timestamps": "性能分析时间戳",
    "Avoid using these hardware timers for any purpose outside of MCAF.":
        "避免将这两个硬件定时器用于 MCAF 之外的任何目的。",
    "Some of the system parameters are initialized to the default values given in the board configuration file.":
        "部分系统参数会初始化为板卡配置文件中给出的默认值。",
    "6.6.1. Overview of board support in motorBench": "6.6.1. motorBench 中的板卡支持概述",
    "6.6.2. Scope of hardware support": "6.6.2. 硬件支持范围",
    "6.6.2.1. Board configuration features": "6.6.2.1. 板卡配置功能",
    "6.6.2.2. Assumptions": "6.6.2.2. 假设",
    "6.6.2.2.1. Current measurement": "6.6.2.2.1. 电流测量",
    "6.6.2.2.2. Voltage measurement": "6.6.2.2.2. 电压测量",
    "6.6.3. Board definition file structure": "6.6.3. 板卡定义文件结构",
    "6.6.4. System parameters": "6.6.4. 系统参数",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
