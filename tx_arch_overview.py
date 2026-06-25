# -*- coding: utf-8 -*-
import txutil

rel = "architecture/overview"
title_zh = "3.1. 架构概述"

m = {
    "Architecture": "架构",
    "Architectural Overview": "架构概述",
    "Naming Conventions": "命名约定",
    "DSC devices": "DSC 器件",
    "FOC": "FOC",
    "PMSM": "PMSM",
    "ADC": "ADC",
    "PLL": "PLL",
    "SMO": "SMO",
    "Components of Motor Control Application Framework": "电机控制应用框架的组件",
    "How to Spin a Motor (In Brief)": "如何驱动电机（简述）",
    "Modules and Components": "模块与组件",
    "High-level component descriptions": "组件高层描述",
    "Software Design Principles for Modular and Maintainable Code": "面向模块化与可维护代码的软件设计原则",
    "Naming convention": "命名约定",
    "State management": "状态管理",
    "Configuration parameters": "配置参数",
    "Scheduling": "调度",
    "Optimization": "优化",
    "State machines": "状态机",
    "module": "模块",
    "component": "组件",
    "index": "索引",
    "Main Application": "主应用",
    "Motion Control API (MCAPI)": "运动控制 API（MCAPI）",
    "ADC Calibration and Compensation": "ADC 校准与补偿",
    "State Machine": "状态机",
    "Field-Oriented Control": "磁场定向控制",
    "Velocity Control": "速度控制",
    "Current Control": "电流控制",
    "Commutation and Estimation": "换相与估计",
    "Test Harness": "测试框架",
    "Supervisory Algorithms": "监督算法",
    "External Interface": "外部接口",
    "Diagnostic Kernel": "诊断内核",
    "Hardware Abstraction Layer": "硬件抽象层",
    "foc": "foc",
    "— top-level": "——顶层",
    "foc.c": "foc.c",
    "foc.h": "foc.h",
    "foc_types.h": "foc_types.h",
    "sat_PI": "sat_PI",
    "— PI loop saturation management": "——PI 环饱和管理",
    "sat_PI.c": "sat_PI.c",
    "sat_PI.h": "sat_PI.h",
    "sat_PI_types.h": "sat_PI_types.h",
    "parameters/foc_params": "parameters/foc_params",
    "tuning parameters": "整定参数",
    "parameters/foc_params.h": "parameters/foc_params.h",
    "parameters/sat_PI_params": "parameters/sat_PI_params",
    "— saturation parameters": "——饱和参数",
    "parameters/sat_PI_params.h": "parameters/sat_PI_params.h",
    "Hall sensor commutation and estimation": "霍尔传感器换相与估计",
    "Quadrature encoder commutation and estimation": "正交编码器换相与估计",
    "Resolver commutation and estimation": "旋变器换相与估计",
    "Overvoltage/undervoltage detection": "过压/欠压检测",
    "Overcurrent detection": "过流检测",
    "Thermal management": "热管理",
    "Stall detection and recovery": "堵转检测与恢复",
    "Saturation and antiwindup management (if not already present in the velocity and current controllers)": "饱和与抗积分饱和管理（若速度和电流控制器中尚未包含）",
    "Adaptive estimators (e.g. online resistance estimation)": "自适应估计器（如在线电阻估计）",
    "Field weakening": "弱磁",
    "Maximum torque per ampere controllers": "最大转矩/电流比控制器",
    "The overall goals of the MCAF code are": "MCAF 代码的总体目标是",
    "to spin a motor based on simple user inputs": "基于简单的用户输入驱动电机",
    "to detect and report fault conditions": "检测并报告故障状态",
    "to be modular and maintainable": "模块化且可维护",
    "to be a clear example to Microchip customers for a motor control Application using dsPIC": "为 Microchip 客户提供使用 dsPIC",
    "to make efficient use of available CPU time in resource-limited devices": "在资源受限的器件中高效利用可用的 CPU 时间",
    "This section will describe an overview of how these goals are met.":
        "本节将概述如何实现这些目标。",
    "The MCAF spins a motor using a velocity control loop, with an inner current loop using field-oriented control (":
        "MCAF 使用速度控制环驱动电机，内部电流环采用磁场定向控制（",
    ") to manage motor current and torque. Sensorless estimation techniques are used to estimate motor position for commutation and velocity control. User input is provided with a potentiometer and buttons to start and stop the motor, or to reverse direction. A state machine is used to control the transitions between these different modes of operation.":
        "）来管理电机电流和转矩。使用无传感器估计技术来估计电机位置以进行换相和速度控制。用户输入通过电位器和按钮提供，用于启动和停止电机或改变方向。状态机用于控制这些不同工作模式之间的转换。",
    "The motor startup process involves so-called “open-loop” operation. When the motor is at rest or moving very slowly, the sensorless estimator is not accurate enough; instead, a special set of states is provided to manage startup, in which commutation is forced at a desired acceleration rate, and the velocity control loop is disabled.":
        "电机启动过程涉及所谓的“开环”运行。当电机静止或运动非常缓慢时，无传感器估计器不够准确；此时提供一组特殊状态来管理启动，在此期间以期望的加速度强制换相，并禁用速度控制环。",
    "Monitoring algorithms run continuously, to detect a motor stall and other abnormal conditions such as overcurrent or overvoltage. These conditions disable the motor controller. The controller will automatically restart, if possible; otherwise, a fault code will be displayed.":
        "监控算法持续运行，以检测电机堵转及过流或过压等异常情况。这些情况会禁用电机控制器。如果可能，控制器将自动重启；否则将显示故障代码。",
    "More detailed descriptions are provided in appropriate sections.":
        "更详细的描述见相应章节。",
    "The MCAF is based on a modular design, and consists of a number of components that work together. We use the terms":
        "MCAF 基于模块化设计，由若干协同工作的组件组成。我们在 MCAF 中以特定方式使用",
    "and": "和",
    "in specific ways in the MCAF:": "这两个术语：",
    "refers to a specific set of 1 – 3 source code files with a common base name, and a specific responsibility.":
        "指一组具有共同基础名、承担特定职责的 1–3 个源代码文件。",
    "refers to some number of modules that comprise a high-level set of features.":
        "指若干模块，它们共同构成一组高层功能。",
    "For example, the field-oriented control (": "例如，磁场定向控制（",
    ") component, covering velocity and current control, contains these modules:":
        "）组件涵盖速度和电流控制，包含以下模块：",
    "shows the MCAF components, with arrows designating component dependencies:":
        "展示了 MCAF 的各组件，箭头表示组件间的依赖关系：",
    "At a high level, a short description of these components is given below; more details are provided in appropriate subsections.":
        "在高层面上，下面给出这些组件的简要描述；更多细节见相应子节。",
    "Note": "注",
    ": because this is a general motor control framework, most components have more than one implementation option, including some that are intended for the future but which have not yet been implemented.":
        "：由于这是一个通用电机控制框架，大多数组件有不止一种实现选项，包括一些计划在未来实现但尚未实现的部分。",
    "Modules within these components can be found in a description of the components that contain them, and can also be located by name in the":
        "这些组件内的模块可在包含它们的组件描述中找到，也可按名称在",
    "under “modules”.": "的“modules”条目下查找。",
    ": The main application depends on a number of components to do its job. It is the one in charge: with limited exceptions, it handles all scheduling and interactions with the hardware, and takes output from one component for use in another, so that the individual components do not need to have inter-component dependencies.":
        "：主应用依赖若干组件来完成其工作。它是总指挥：除少数例外，它处理所有调度和与硬件的交互，并将一个组件的输出用于另一个组件，使各组件之间无需相互依赖。",
    ": Provides a set of high-level interfaces that can be used by an application to control the motor and obtain feedback information from it.":
        "：提供一组高层接口，应用程序可使用这些接口控制电机并从中获取反馈信息。",
    ": Handles offset and gain compensation for": "：处理",
    "readings. May also include computation of offset and gain coefficients during calibration times.":
        "读数的偏置和增益补偿。也可在校准期间计算偏置和增益系数。",
    ": Controls state-dependent behavior of the application that changes over time because of different conditions. In a motor control application, this usually covers the actions that occur when the motor is disabled, starting up, running, and shutting down.":
        "：控制应用中随时间因不同条件而变化的状态相关行为。在电机控制应用中，这通常涵盖电机禁用、启动、运行和停机时发生的动作。",
    "):": "）：",
    ": Most motor control applications involve a velocity control loop that attempts to control the motor to achieve a given desired speed. (Some use a position control loop, typically as an outer loop around a velocity controller; this is a feature that may be added in the future.)":
        "：大多数电机控制应用包含一个速度控制环，试图控制电机达到给定的期望速度。（有些使用位置控制环，通常作为速度控制器的外环；这是未来可能添加的功能。）",
    ": Most motor control algorithms require a current control loop to manage motor torque and/or current. (Some do not; instead the main velocity controller outputs duty cycle directly. Support for these systems may be added in the future.) The application framework will initially support":
        "：大多数电机控制算法需要电流控制环来管理电机转矩和/或电流。（有些不需要；而是由主速度控制器直接输出占空比。未来可能添加对这类系统的支持。）应用框架最初将支持",
    "of a permanent-magnet synchronous motor, but may also support": "永磁同步电机的，但也可支持",
    "of induction motors, six-step control, direct torque control, etc. as needed.":
        "感应电机的、六步控制、直接转矩控制等（视需要）。",
    ": All permanent-magnet synchronous motors (": "：所有永磁同步电机（",
    "), switched-reluctance motors (SR), AC induction motors (ACIM), and stepper motors require AC waveforms and control of which motor terminals receive current at any given time; the only exception are DC motors with a built-in commutator. The functions of commutation and estimation are to examine the available inputs and come up with estimates of motor position, velocity, and/or commutation angle. The commutation angle determines which phases should receive current. This component may consist of several alternative implementations:":
        "）、开关磁阻电机（SR）、交流感应电机（ACIM）和步进电机都需要交流波形，并控制任意时刻哪些电机端子接收电流；唯一例外是带有内置换向器的直流电机。换相与估计的功能是检查可用输入并得出电机位置、速度和/或换相角的估计值。换相角决定哪些相应接收电流。该组件可由若干替代实现组成：",
    "Sensorless estimators (": "无传感器估计器（",
    ", etc.)": "等）",
    "Forced commutation: this is typically used in startup for a system with a sensorless estimator, and includes the management of transition between forced commutation and closed-loop commutation.":
        "强制换相：通常用于带无传感器估计器的系统的启动，包括管理强制换相与闭环换相之间的过渡。",
    ": this provides the ability to modify the normal modes of operation of the commutation and current controllers, and apply test disturbance signals.":
        "：提供修改换相和电流控制器正常工作模式的能力，并施加测试扰动信号。",
    ": There are a number of additional algorithms that can be used to enhance reliability or performance, including":
        "：有许多附加算法可用于增强可靠性或性能，包括",
    ": Facilitates the interface with the outside world. This includes either a user interface (pushbuttons/knobs) or programmatic control through a communications interface.":
        "：便于与外界交互。这包括用户界面（按钮/旋钮）或通过通信接口的程序化控制。",
    ": Allows real-time diagnostics and testing through interaction with an external host PC. The Motor Control Applications team at Microchip uses this to debug and test motor control algorithms.":
        "：允许通过与外部主机 PC 交互进行实时诊断和测试。Microchip 的电机控制应用团队使用它来调试和测试电机控制算法。",
    ": Handles all hardware-specific functions through a well-defined interface common across multiple processors and platforms. The only components that interact with the HAL are the main (top-level) application and the state machine. Other components are given access to system state variables which are used as a way to exchange data with the HAL.":
        "：通过一个跨多个处理器和平台的通用、定义良好的接口处理所有硬件相关功能。只有主（顶层）应用和状态机与 HAL 交互。其他组件通过访问系统状态变量来与 HAL 交换数据。",
    "In addition to organizing the MCAF code into modules, there are a number of other design principles we followed, in order to increase modularity, maintainability, and readability, which may not be immediately apparent. These are outlined briefly below, and described in later sections. Overall we aimed to be consistent throughout the codebase, so that it is easier for engineers to become familiar with the way it works.":
        "除了将 MCAF 代码组织为模块外，我们还遵循了若干其他设计原则，以提高模块化、可维护性和可读性，这些可能并不显而易见。下面简要列出，并在后续章节中详述。总体而言，我们力求在整个代码库中保持一致，使工程师更容易熟悉其工作方式。",
    "— MCAF follows a consistent naming convention to improve clarity and reduce the possibility of collision with customer code.":
        "——MCAF 遵循一致的命名约定，以提高清晰度并降低与客户代码冲突的可能性。",
    "— the way that state variables are structured, allocated, and accessed facilitates modularity.":
        "——状态变量的结构化、分配和访问方式有助于模块化。",
    "— there are many different configuration parameters in the MCAF, and these are organized to make them accessible to, but separate from, the corresponding modules, so that they can be easily changed but their associated code remains constant":
        "——MCAF 中有许多不同的配置参数，它们被组织成可被对应模块访问但又与模块分离的形式，以便于修改而相关代码保持不变",
    "— MCAF aims to make efficient use of embedded CPU time, but still maintain a modular architecture":
        "——MCAF 旨在高效利用嵌入式 CPU 时间，同时保持模块化架构",
    "— to implement complex behaviors, the MCAF uses intentionally-designed state machines and run-to-completion scheduling to avoid accidental side effects.":
        "——为实现复杂行为，MCAF 使用精心设计的状态机和运行至完成的调度，以避免意外的副作用。",
    "3.1. Architectural Overview": "3.1. 架构概述",
    "3.1.1. How to Spin a Motor (In Brief)": "3.1.1. 如何驱动电机（简述）",
    "3.1.2. Modules and Components": "3.1.2. 模块与组件",
    "3.1.2.1. High-level component descriptions": "3.1.2.1. 组件高层描述",
    "3.1.3. Software Design Principles for Modular and Maintainable Code": "3.1.3. 面向模块化与可维护代码的软件设计原则",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
