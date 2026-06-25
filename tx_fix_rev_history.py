# -*- coding: utf-8 -*-
"""Fix remaining English text in rev_history.zh.html."""
import re
import txutil
from bs4 import NavigableString

REL = "appendix/rev_history.zh.html"

def fix_dbmc_parens(root):
    """Convert English parentheses around DB_MC references to Chinese parentheses,
    and convert commas between DB_MC refs to Chinese commas."""
    changed = 0
    for s in txutil.collect_nodes(root):
        original = str(s)
        new = original
        # Convert "(DB_MC-" to "（DB_MC-"
        new = new.replace("(DB_MC-", "（DB_MC-")
        # Convert ", DB_MC-" to "、DB_MC-" (between DB_MC refs)
        new = new.replace(", DB_MC-", "、DB_MC-")
        # Convert closing ")" to "）" when it follows a DB_MC reference number
        # Pattern: DB_MC-XXXX) or DB_MC-XXXX, DB_MC-XXXX) etc.
        new = re.sub(r'(DB_MC-\d+)\)', r'\1）', new)
        # Convert ". (" before DB_MC to "。（" 
        new = new.replace(". （DB_MC-", "。（DB_MC-")
        if new != original:
            s.replace_with(NavigableString(new))
            changed += 1
    return changed

def fix_remaining_english(root):
    """Translate remaining English fragments in text nodes."""
    pairs = [
        # Common English words in DB_MC reference fragments
        ("module. (DB_MC-", "模块。（DB_MC-"),
        ("removed. (DB_MC-", "已移除。（DB_MC-"),
        ("motors. (DB_MC-", "电机。（DB_MC-"),
        ("module (DB_MC-", "模块（DB_MC-"),
        ("modules (DB_MC-", "模块（DB_MC-"),
        ("state (DB_MC-", "状态（DB_MC-"),
        ("group (DB_MC-", "组（DB_MC-"),
        ("calculation (DB_MC-", "计算（DB_MC-"),
        ("of zero (DB_MC-", "为零的问题（DB_MC-"),
        ("prefix (DB_MC-", "前缀（DB_MC-"),
        ("in math_asm.s (DB_MC-", "在 math_asm.s 中（DB_MC-"),
        ("in sat_PI.c (DB_MC-", "在 sat_PI.c 中（DB_MC-"),
        (", etc. (DB_MC-", "等。（DB_MC-"),
        ("sensorless estimator. (DB_MC-", "无传感器估计器。（DB_MC-"),
        ("Development Suite. (DB_MC-", "Development Suite。（DB_MC-"),
        ("Development Suite (DB_MC-", "Development Suite（DB_MC-"),
        ('Added \u201cweathervane\u201d startup method (DB_MC-1039)',
         '添加了"weathervane"启动方法（DB_MC-1039）'),
        ('Added \u201cprobe current\u201d parameter (DB_MC-4424)',
         '添加了"probe current"参数（DB_MC-4424）'),
        ('.) (DB_MC-', '。）（DB_MC-'),
    ]
    return txutil.replace_text(None, pairs, root=root)

# (English, Chinese) pairs applied as substring replacements on text nodes.
# Order matters: longer/more specific fragments first to avoid partial matches.
PAIRS = [
    # ---- Fix-up pairs for text corrupted by previous run ----
    ("该re is now an mcaf_main.h as well to include function declarations. (DB_MC-1846)",
     "现在还有一个 mcaf_main.h 用于包含函数声明。（DB_MC-1846）"),
    (". (DB_MC-1164) 该 difference between these state variables is that",
     "。（DB_MC-1164）这些状态变量之间的区别在于"),
    ("based on calculating from PWM duty cycles. 该 two are identical except when the current controller\nenters into",
     "的最佳估计。两者在电流控制器\n进入"),
    ("该 list of derived parameters in aux-files/report.html has been expanded. (DB_MC-1178)",
     "aux-files/report.html 中的派生参数列表已扩展。（DB_MC-1178）"),
    ("Fixed issue involving estimator initialization、 provided initialization hooks for all sensorless estimators (DB_MC-2576)",
     "修复了涉及估计器初始化的问题，并为所有无传感器估计器提供了初始化钩子（DB_MC-2576）"),
    (",\npreventing flux control module from changing it、 allowing it to be changed via real-time diagnostic tools.\n(DB_MC-2855)",
     "，\n防止磁通控制模块更改它，并允许通过实时诊断工具更改它。\n（DB_MC-2855）"),
    ("with MCP8021 gate driver、 MCP802X gate drivers (DB_MC-4564)",
     "带 MCP8021 栅极驱动器和 MCP802X 栅极驱动器的支持（DB_MC-4564）"),
    ("Improved current offset calibration to allow wider maximum range in the Customize page、 cause a fault if outside acceptable limits (DB_MC-5542, DB_MC-4924, DB_MC-4180)",
     "改进了电流偏置校准以允许在 Customize 页面中更宽的最大范围，如果超出可接受的限制则产生故障（DB_MC-5542、DB_MC-4924、DB_MC-4180）"),
    ("Improved current offset calibration to allow wider maximum range in the Customize page,\nand cause a fault if outside acceptable limits\n(DB_MC-5542, DB_MC-4924, DB_MC-4180)",
     "改进了电流偏置校准以允许在 Customize 页面中更宽的最大范围，\n如果超出可接受的限制则产生故障\n（DB_MC-5542、DB_MC-4924、DB_MC-4180）"),

    # ---- Remaining untranslated fragments ----
    ("prefix from ATPLL constants (DB_MC-2712)",
     "前缀从 ATPLL 常量中移除（DB_MC-2712）"),
    ("in the sample application (DB_MC-5838)",
     "在示例应用中（DB_MC-5838）"),
    ("macros for each configurable parameter in generated parameters files (DB_MC-5536)",
     "宏到生成的参数文件中每个可配置参数（DB_MC-5536）"),
    ("Removed remaining RTDM content from firmware package (DB_MC-5664)",
     "从固件包中移除了剩余的 RTDM 内容（DB_MC-5664）"),

    # ---- Additional untranslated fragments (not caught by EN_WORDS regex) ----
    ("该 former", "先前的"),
    ("模块以形成新的", "模块的部分功能合并，形成新的"),
    ("module was rewritten as a simple state machine\nto avoid unintentional behavior.",
     "模块被重写为简单的状态机\n以避免意外行为。"),
    ("module to form a new", "模块以形成新的"),
    ("module written in C. (DB_MC-97, DB_MC-675)",
     "模块（用 C 编写）。（DB_MC-97、DB_MC-675）"),
    ("该 file report.xml 已重命名为 report.xml.txt to avoid triggering an error in MCC. (DB_MC-1868)",
     "文件 report.xml 已重命名为 report.xml.txt 以避免在 MCC 中触发错误。（DB_MC-1868）"),
    ("Development Suite user interface. (DB_MC-2156, DB_MC-2057)",
     "Development Suite 用户界面中调整关键 MCAF 参数的能力。（DB_MC-2156、DB_MC-2057）"),
    ("state at device reset (DB_MC-2094)", "状态的问题（DB_MC-2094）"),
    ("values in Classic startup (DB_MC-2529)", "值的问题（DB_MC-2529）"),
    ("in Weathervane startup (DB_MC-2628)", "在 Weathervane 启动中的赋值问题（DB_MC-2628）"),
    ("Fixed initialization of startup counter in Weathervane startup (DB_MC-2535)",
     "修复了 Weathervane 启动中启动计数器的初始化（DB_MC-2535）"),
    ("to extend velocity range. (DB_MC-2723)", "以扩展速度范围。（DB_MC-2723）"),
    ("Added Binary hard switching hybrid estimator (DB_MC-3140)",
     "添加了二进制硬切换混合估计器（DB_MC-3140）"),
    ("Added new customizable parameters (DB_MC-3687)",
     "添加了新的可定制参数（DB_MC-3687）"),
    ("module to clear latched faults (DB_MC-5227)",
     "模块以清除锁存的故障（DB_MC-5227）"),
    ("PWM bootstrap charging logic", "PWM 自举充电逻辑"),
    ("Sliding Mode Observer", "滑模观测器"),
    ("continuous current limit (DB_MC-5781)", "连续电流限制（DB_MC-5781）"),
    ("to specify initial filter state (DB_MC-6292)",
     "以指定初始滤波器状态（DB_MC-6292）"),
    ("instead of its value of zero (DB_MC-6389)", "而非其零值（DB_MC-6389）"),
    ("Removed blank commutation_params.h file (DB_MC-4867)",
     "移除了空白的 commutation_params.h 文件（DB_MC-4867）"),
    ('Changed software overcurrent \u201cstall\u201d detector to disabled by default (DB_MC-5569)',
     "将软件过流\u201c堵转\u201d检测器更改为默认禁用（DB_MC-5569）"),
    ("in util.h rather than processor-specific builtins (DB_MC-6079)",
     "在 util.h 中而非处理器特定的内建函数中（DB_MC-6079）"),

    # ---- 9.0.1 doc rev history (line 369) ----
    ("Added support for MCHV‑230VAC‑1.5kW Motor Control High-Voltage Development Board",
     "新增对 MCHV‑230VAC‑1.5kW 电机控制高压开发板的支持"),

    # ---- Motor Control Library heading (line 444, 527, 737) ----
    # These appear as standalone text nodes "Motor Control Library" in headings
    # We handle them via whole_pairs below.

    # ---- R3 RC14 modules (line 458-459) ----
    ("module, written in assembly, has been combined with some functionality\nof the",
     "模块（用汇编编写）已与"),
    ("MCAF is now compatible with the MCC system module including oscillator setup. (DB_MC-1679,\nDB_MC-1688, DB_MC-1689, DB_MC-1690)",
     "MCAF 现在与 MCC 系统模块兼容，包括振荡器设置。（DB_MC-1679、\nDB_MC-1688、DB_MC-1689、DB_MC-1690）"),
    ("There is now an mcaf_main.h as well to include function declarations. (DB_MC-1846)",
     "现在还有一个 mcaf_main.h 用于包含函数声明。（DB_MC-1846）"),
    ("MCAF has yielded responsibility to MCC for oscillator configuration (DB_MC-1849)",
     "MCAF 已将振荡器配置的责任交给 MCC（DB_MC-1849）"),

    # ---- R3 scaling factors (line 483-484) ----
    ("Development Suite is now exactly equal to the maximum dq-frame\ncommanded current amplitude. In MCAF R2, there was a 0.824 derating factor applied. (DB_MC-1307)",
     "Development Suite 中输入的连续额定逆变器电流现在精确等于最大 dq 轴\n指令电流幅值。在 MCAF R2 中，应用了 0.824 的降额系数。（DB_MC-1307）"),

    # ---- R3 core FOC (line 493-498) ----
    ("PLL now uses", "PLL 现在使用"),
    (". (DB_MC-1164)\nThe difference between these state variables is that",
     "。（DB_MC-1164）\n这些状态变量之间的区别在于"),
    ("represents the\nintended value of", "表示在"),
    ("represents the best estimate of the actual", "表示基于 PWM 占空比计算的实际"),
    ("based on calculating from PWM duty cycles. The two are identical except when the current controller\nenters into",
     "的最佳估计。两者在电流控制器\n进入"),
    (". See also", "之前是相同的。另请参见"),

    # ---- R3 fault detection (line 504-507) ----
    ("Torque angle stall detection has been disabled by default. (DB_MC-1732)\nSee",
     "转矩角堵转检测默认已禁用。（DB_MC-1732）\n参见"),
    ("has been renamed", "已重命名为"),
    ("for clarity. (DB_MC-846)", "以提高清晰度。（DB_MC-846）"),

    # ---- R3 test harness (line 515) ----
    ("DC link compensation can be disabled by setting the corresponding override bit. (DB_MC-1168)",
     "DC 母线补偿可通过设置相应的覆盖位来禁用。（DB_MC-1168）"),

    # ---- R3 motor control library (line 528-529) ----
    ("has been fixed. (DB_MC-1403)\nThis manifested as a build failure (",
     "中的一个小错误已修复。（DB_MC-1403）\n这表现为构建失败（"),

    # ---- R3 code generation (line 537-540) ----
    ("Improved code generation error messages when an out-of-range error is encountered. (DB_MC-1435)",
     "改进了遇到超出范围错误时的代码生成错误消息。（DB_MC-1435）"),
    ("Improved internal mechanisms for calculating parameters in code generation. (DB_MC-1706, DB_MC-1760)",
     "改进了代码生成中计算参数的内部机制。（DB_MC-1706、DB_MC-1760）"),
    ("Overvoltage and undervoltage margins are now set to 2V for MCLV-2 and 20V for MCHV-2. (DB_MC-1734)\nFuture versions of motorBench",
     "过压和欠压裕量现在设置为 MCLV-2 的 2V 和 MCHV-2 的 20V。（DB_MC-1734）\nmotorBench 的未来版本"),

    # ---- R3 auxiliary reports (line 546-550) ----
    ("The list of derived parameters in aux-files/report.html has been expanded. (DB_MC-1178)",
     "aux-files/report.html 中的派生参数列表已扩展。（DB_MC-1178）"),
    ("Reports in aux-files/ now include traceability to the corresponding MCAF version. (DB_MC-1364)",
     "aux-files/ 中的报告现在包含对相应 MCAF 版本的可追溯性。（DB_MC-1364）"),
    ("Updated KaTeX to a more recent version. (DB_MC-1517)",
     "更新了 KaTeX 到更新的版本。（DB_MC-1517）"),
    ("Fixed a bug in report.xml, specifically a missing close tag (DB_MC-1572)",
     "修复了 report.xml 中的错误，具体为缺少闭合标签（DB_MC-1572）"),
    ("The file report.xml has been renamed report.xml.txt to avoid triggering an error in MCC. (DB_MC-1868)",
     "文件 report.xml 已重命名为 report.xml.txt 以避免在 MCC 中触发错误。（DB_MC-1868）"),

    # ---- R3 miscellaneous (line 557) ----
    ("MCAF copyright date updated to 2018. (DB_MC-1788)",
     "MCAF 版权日期已更新为 2018 年。（DB_MC-1788）"),

    # ---- R4 modules (line 570-573) ----
    ("until a conflict with MCC can be resolved. (DB_MC-2175)",
     "直到与 MCC 的冲突得到解决。（DB_MC-2175）"),
    ("peripheral as this is not supported by MCC yet. (DB_MC-2146)",
     "外设，因为 MCC 尚不支持此功能。（DB_MC-2146）"),

    # ---- R4 MCC compatibility (line 580-581) ----
    ("HAF functions have been added to use new MCC PWM APIs. (DB_MC-2089)",
     "已添加 HAF 函数以使用新的 MCC PWM API。（DB_MC-2089）"),
    ("HAF function for retrieving interrupt vector number has been added.",
     "已添加用于获取中断向量号的 HAF 函数。"),

    # ---- R4 quadrature encoder (line 588, 591) ----
    ("Support quadrature encoders as a primary position and velocity estimator (DB_MC-812)",
     "支持正交编码器作为主要位置和速度估计器（DB_MC-812）"),
    ("index capture support (DB_MC-2078)", "索引捕获支持（DB_MC-2078）"),

    # ---- R4 core FOC (line 610) ----
    ("Refactored commutation module to support multiple estimators (DB_MC-2076)",
     "重构了换相模块以支持多个估计器（DB_MC-2076）"),

    # ---- R4 code generation (line 616) ----
    ("Fixed error in startup hold time calculation so that 32-bit values are now supported (DB_MC-2120)",
     "修复了启动保持时间计算中的错误，现在支持 32 位值（DB_MC-2120）"),

    # ---- R4 test harness (line 623) ----
    ("Corrected state initialization when entering a test mode (DB_MC-2107)",
     "修正了进入测试模式时的状态初始化（DB_MC-2107）"),

    # ---- R4 style (line 630, 636) ----
    ("module have been renamed for clarify (DB_MC-2227):",
     "模块中的启动电流已重命名以澄清（DB_MC-2227）："),
    ("Updated util.h to add assembly comments to inline assembly, for traceability (DB_MC-2011)",
     "更新了 util.h 以在内联汇编中添加汇编注释，用于可追溯性（DB_MC-2011）"),

    # ---- R5 MCC compat (line 657) ----
    ("MCAF R5 now supports dsPIC33CK devices. (DB_MC-2399)\nSee the documentation for the",
     "MCAF R5 现在支持 dsPIC33CK 器件。（DB_MC-2399）\n参见"),

    # ---- R5 HAL (line 664-669) ----
    ("definition out of ui.c and into HAL (DB_MC-436);\nutilized MCC-generated value to reflect actual choice of\noscillator frequency (DB_MC-821)",
     "定义从 ui.c 中移出并移入 HAL（DB_MC-436）；\n利用 MCC 生成的值来反映振荡器频率的实际选择（DB_MC-821）"),
    ("Improved proper encapsulation of device-specific issues\nthrough Hardware Access Functions layer (DB_MC-2368)",
     "改进了通过硬件访问函数层对器件特定问题的适当封装（DB_MC-2368）"),
    ("Other miscellaneous improvements – see", "其他杂项改进——参见"),

    # ---- R5 diagnostics (line 677-678) ----
    ("Added dsPIC33CK support. (DB_MC-2420)", "新增了对 dsPIC33CK 的支持。（DB_MC-2420）"),
    ("Now allows application to specify buffer (DB_MC-801)", "现在允许应用程序指定缓冲区（DB_MC-801）"),

    # ---- R5 quadrature encoder (line 687-689) ----
    ("Improve parameter management of pullout synchronization method\n(DB_MC-2255)",
     "改进了失步同步方法的参数管理\n（DB_MC-2255）"),
    ("Clarified and corrected angle units in QEI tracking loop (DB_MC-2521)",
     "澄清并修正了 QEI 跟踪环中的角度单位（DB_MC-2521）"),

    # ---- R5 misc sensorless (line 701-705) ----
    ("Categorized ATPLL and PLL estimator state variables\nto help distinguish core algorithm state from\nauxiliary state used for logging (DB_MC-2579, DB_MC-2580)",
     "对 ATPLL 和 PLL 估计器的状态变量进行了分类\n以帮助区分核心算法状态和\n用于日志记录的辅助状态（DB_MC-2579、DB_MC-2580）"),
    ("Clarified ATPLL and PLL inductance identifiers and units (DB_MC-2601)",
     "澄清了 ATPLL 和 PLL 的电感标识符和单位（DB_MC-2601）"),
    ("Fixed issue involving estimator initialization, and provided initialization hooks for all sensorless estimators (DB_MC-2576)",
     "修复了涉及估计器初始化的问题，并为所有无传感器估计器提供了初始化钩子（DB_MC-2576）"),

    # ---- R5 startup (line 712, 716) ----
    ("Improve support for slower transitions to closed-loop in Classic startup (DB_MC-2513)",
     "改进了经典启动中对较慢闭环转换的支持（DB_MC-2513）"),
    ("Allow nonzero ALIGN time (DB_MC-2510)", "允许非零 ALIGN 时间（DB_MC-2510）"),

    # ---- R5 customize page (line 730-731) ----
    ("Added “Advice” pane for guidance based on motor and system parameters. (DB_MC-2507)",
     '添加了\u201c建议\u201d面板，用于基于电机和系统参数提供指导。（DB_MC-2507）'),
    ("Added display of normalized values in engineering units. (DB_MC-2519)",
     "添加了以工程单位显示归一化值的功能。（DB_MC-2519）"),

    # ---- R5 auxiliary reports (line 747) ----
    ("Added section “Normalization factors used in fixed-point representation” (DB_MC-2049)",
     '添加了\u201c定点表示中使用的归一化因子\u201d节（DB_MC-2049）'),

    # ---- R6 adjustable PWM (line 764) ----
    ("Added support for adjusting PWM frequency and control frequency as a submultiple of the PWM frequency. (DB_MC-2720, DB_MC-2950)\nPlease refer to",
     "新增了调整 PWM 频率和控制频率作为 PWM 频率子倍数的支持。（DB_MC-2720、DB_MC-2950）\n请参见"),

    # ---- R6 motion control API (line 771) ----
    ("to provide a high-level abstracted interface for custom applications to control and obtain feedback from the motor. (DB_MC-796)",
     "以提供高级抽象接口，供自定义应用程序控制和获取电机反馈。（DB_MC-796）"),

    # ---- R6 flux control (line 780-781) ----
    ("Refactored FOC with structural changes to support flux weakening and MTPA. (DB_MC-2861, DB_MC-2863)\nFor more information, see",
     "重构了 FOC 并进行结构变更以支持弱磁和 MTPA。（DB_MC-2861、DB_MC-2863）\n更多信息请参见"),

    # ---- R6 dsPIC33CK support (line 793) ----
    ("Added support for dsPIC33CK64MP105 and dsPIC33CK64MC105 (DB_MC-2694, DB_MC-2693)",
     "新增了对 dsPIC33CK64MP105 和 dsPIC33CK64MC105 的支持（DB_MC-2694、DB_MC-2693）"),

    # ---- R6 board service (line 799-800) ----
    (".\n(DB_MC-2726, DB_MC-2728, DB_MC-2732) See", "。\n（DB_MC-2726、DB_MC-2728、DB_MC-2732）参见"),
    (",\npreventing flux control module from changing it, and allowing it to be changed via real-time diagnostic tools.\n(DB_MC-2855)",
     "，\n防止磁通控制模块更改它，并允许通过实时诊断工具更改它。\n（DB_MC-2855）"),

    # ---- R6 customize page (line 814-815) ----
    ("Added read-only parameter calculations such as Saliency ratio (DB_MC-2903)",
     "添加了只读参数计算，如凸极比（DB_MC-2903）"),
    ("Included additional customizable parameters. (DB_MC-2689, DB_MC-2750, DB_MC-2838, DB_MC-2879, DB_MC-2882, DB_MC-2905)",
     "包含了额外的可定制参数。（DB_MC-2689、DB_MC-2750、DB_MC-2838、DB_MC-2879、DB_MC-2882、DB_MC-2905）"),

    # ---- R6 modularity (line 821-825) ----
    ("All calls to MCC HAL are now made through HAF (DB_MC-2671)",
     "所有对 MCC HAL 的调用现在都通过 HAF 进行（DB_MC-2671）"),
    ("Removed directly modifying registers to clear status bits (DB_MC-2696)",
     "移除了直接修改寄存器以清除状态位的做法（DB_MC-2696）"),
    ("Refactored data flow interface for estimators and flux control module to reduce tight coupling (DB_MC-2854)",
     "重构了估计器和磁通控制模块的数据流接口以减少紧耦合（DB_MC-2854）"),
    ("Refactored back-emf calculation for use by estimators and flux control module\n(DB_MC-2106)",
     "重构了反电动势计算以供估计器和磁通控制模块使用\n（DB_MC-2106）"),

    # ---- R6 naming (line 831-837) ----
    ("Improved names for PWM generators (DB_MC-2807)", "改进了 PWM 生成器的名称（DB_MC-2807）"),
    ("Replaced inconsistent PI parameters (DB_MC-2857)", "替换了不一致的 PI 参数（DB_MC-2857）"),
    ("Rename test harness functions to use verb “Trigger” for clarification\n(TriggerSeizure, TriggerStackOverflow) (DB_MC-1720)",
     '重命名测试框架函数以使用动词\u201cTrigger\u201d进行澄清\n（TriggerSeizure、TriggerStackOverflow）（DB_MC-1720）'),
    ("Addressed potential naming collision between PLL and ATPLL\n(DB_MC-2602)",
     "解决了 PLL 和 ATPLL 之间潜在的命名冲突\n（DB_MC-2602）"),

    # ---- R6 misc firmware (line 843-846) ----
    ("Improve how velocities are represented in generated code in parameters/* files (DB_MC-2915)",
     "改进了生成的代码中 parameters/* 文件里速度的表示方式（DB_MC-2915）"),
    ("Removed unnecessary and added missing #include statements in several locations (DB_MC-1719)",
     "在多处移除了不必要的并添加了缺失的 #include 语句（DB_MC-1719）"),
    ("Tracking loop Kp value can now vary between a Q8 - Q15 value (DB_MC-2688)",
     "跟踪环 Kp 值现在可以在 Q8 到 Q15 之间变化（DB_MC-2688）"),
    ("Fixed half-PWM-cycle short circuit across motor during entry to STOPPING state (DB_MC-2931)",
     "修复了进入 STOPPING 状态时电机上的半 PWM 周期短路问题（DB_MC-2931）"),

    # ---- R7 modules (line 856, 858) ----
    ("and multi-channel current measurement (DB_MC-3350, DB_MC-3623)",
     "和多通道电流测量（DB_MC-3350、DB_MC-3623）"),
    ("and ZS/MT hybrid estimator modules (DB_MC-3079, DB_MC-3140)",
     "和 ZS/MT 混合估计器模块（DB_MC-3079、DB_MC-3140）"),

    # ---- R7 MCC Melody (line 864-865) ----
    ("Updated motorBench/hal/hardware_access_functions.h to add new methods and update existing methods to work with\nperipheral drivers from",
     "更新了 motorBench/hal/hardware_access_functions.h 以添加新方法并更新现有方法以与"),
    ("to allow short transient\ncurrents above the continuous current limit. (DB_MC-3283)",
     "以允许短时间内\n超过连续电流限制的瞬态电流。（DB_MC-3283）"),

    # ---- R7 ZS/MT (line 879, 887) ----
    ("estimator (DB_MC-3109) with", "估计器（DB_MC-3109），带有"),
    ("methods to restart motion quickly\nwith certain types of estimators (DB_MC-3440)",
     "方法，以便在某些类型的估计器下快速重启运动\n（DB_MC-3440）"),

    # ---- R7 voltage control (line 901-902) ----
    ("in addition to the\nexisting outer velocity loop (DB_MC-3338)",
     "以及\n现有的外环速度环（DB_MC-3338）"),

    # ---- R7 main application (line 915-916) ----
    ("module (DB_MC-3281, DB_MC-3744, DB_MC-3292) to separate MCAF related\ncode from the",
     "模块（DB_MC-3281、DB_MC-3744、DB_MC-3292）以将 MCAF 相关\n代码从"),
    (". See", "中分离出来。参见"),

    # ---- R7 current measurement (line 923-924) ----
    ("component to support one/two/three channel current measurement\nschemes (DB_MC-3350)",
     "组件以支持一/二/三通道电流测量\n方案（DB_MC-3350）"),

    # ---- R7 customize page (line 954) ----
    ("Made minor improvements in overall Customize page user interface behavior (DB_MC-4030, DB_MC-4013, DB_MC-3739)",
     "对整体 Customize 页面用户界面行为进行了小幅改进（DB_MC-4030、DB_MC-4013、DB_MC-3739）"),

    # ---- R7 misc firmware (line 961-978) ----
    ("Compensated for time delays in voltage input of sensorless estimators (DB_MC-3415)",
     "补偿了无传感器估计器电压输入中的时间延迟（DB_MC-3415）"),
    ("Updated DC link voltage scaling to allow a different gain compared to ADC full-scale (DB_MC-3267)",
     "更新了 DC 母线电压缩放以允许与 ADC 满量程不同的增益（DB_MC-3267）"),
    ("to detect motor stall condition only after the\nmotor startup is complete (DB_MC-3244)",
     "以仅在\n电机启动完成后检测电机堵转条件（DB_MC-3244）"),
    ("module in support of updates to other modules\nin MCAF (DB_MC-3749, DB_MC-3750, DB_MC-3751, DB_MC-3752)",
     "模块以支持 MCAF 中其他模块的更新\n（DB_MC-3749、DB_MC-3750、DB_MC-3751、DB_MC-3752）"),
    ("Consolidated low-pass filter implementation variants into one canonical low-pass filter\nimplementation in filter.h  (DB_MC-3590)",
     "将低通滤波器实现的变体整合为 filter.h 中的一个规范低通滤波器\n实现（DB_MC-3590）"),
    ("Fixed an issue with motor startup state machine that caused it to lose synchronization\nwith MCAF state machine at initialization (DB_MC-3332)",
     "修复了电机启动状态机在初始化时与\nMCAF 状态机失去同步的问题（DB_MC-3332）"),
    ("to use a fixed value\nof minimum pulse width on PWMxL channels rather than a ramp of PWMxL duty cycle from zero (DB_MC-978)",
     "以在 PWMxL 通道上使用固定值\n的最小脉冲宽度，而不是从零开始的 PWMxL 占空比斜坡（DB_MC-978）"),

    # ---- R8 modules (line 988-991) ----
    ("Moved PWM fault-related variables out of the ADC compensation module to",
     "将 PWM 故障相关变量从 ADC 补偿模块移至"),
    ("into a dedicated", "到专用的"),

    # ---- R8 custom board (line 998-999) ----
    ("with MCP8021 gate driver, and MCP802X gate drivers (DB_MC-4564)",
     "带 MCP8021 栅极驱动器和 MCP802X 栅极驱动器的支持（DB_MC-4564）"),
    ("to support Custom Board Support (DB_MC-5220)",
     "以支持自定义板级支持（DB_MC-5220）"),

    # ---- R8 customize page (line 1007-1014) ----
    ("Updated generated code to reference the primary estimator consistent with Customize UI (DB_MC-4325)",
     "更新了生成的代码以引用与 Customize UI 一致的主估计器（DB_MC-4325）"),
    ("section to spell out “Zero-Speed / Maximum Torque” consistently (DB_MC-4420)",
     '节以一致地拼写\u201cZero-Speed / Maximum Torque\u201d（DB_MC-4420）'),
    ("Fixed a bug where voltage control gains could cause parameter out-of-range error during code generation, even\nif voltage controller is not selected (DB_MC-4671)",
     "修复了一个错误，即电压控制增益可能在代码生成期间导致参数超出范围错误，即使\n未选择电压控制器（DB_MC-4671）"),
    ("Updated code generation to skip parameter calculations for features that are disabled in Customize page\n(DB_MC-5128)",
     "更新了代码生成以跳过 Customize 页面中已禁用功能的参数计算\n（DB_MC-5128）"),
    ("Made warnings for Single Channel and Triple Channel current measurement consistent in Customize UI (DB_MC-5371)",
     "使 Customize UI 中单通道和三通道电流测量的警告保持一致（DB_MC-5371）"),
    ("Added support for input validation expressions in numeric fields (DB_MC-5406)",
     "新增了对数字字段中输入验证表达式的支持（DB_MC-5406）"),

    # ---- R8 diagnostics (line 1027-1028) ----
    ("firmware library packaged with MCAF to\nv2.1 (DB_MC-5287)",
     "与 MCAF 打包的固件库更新至\nv2.1（DB_MC-5287）"),

    # ---- R8 MCAPI fault (line 1035) ----
    ("is called before reading new faults (DB_MC-4252)",
     "在读取新故障之前被调用（DB_MC-4252）"),

    # ---- R8 misc firmware (line 1041-1056) ----
    ("Added comments explaining empty HAL functions (DB_MC-5175)",
     "添加了说明空 HAL 函数的注释（DB_MC-5175）"),
    ("Renamed ADC value getter functions for DC link voltage and current, so they are more consistent with ADC\nchannel names (DB_MC-4004)",
     "重命名了 DC 母线电压和电流的 ADC 值获取函数，使其与 ADC\n通道名称更加一致（DB_MC-4004）"),
    ("Clarified intentional use of overflow in qei.h (DB_MC-4277)",
     "澄清了 qei.h 中溢出的有意使用（DB_MC-4277）"),
    ("Fixed bug in current calibration with single-channel current sense (DB_MC-4738)",
     "修复了单通道电流检测的电流校准中的错误（DB_MC-4738）"),
    ("when compiled with newer\nC99-compliant compilers (DB_MC-5518)",
     "在使用更新的\nC99 兼容编译器编译时（DB_MC-5518）"),
    ("in foc.c to maintain\nconsistent usage of Motor Control Library functions (DB_MC-5085)",
     "以在 foc.c 中保持\n电机控制库函数的一致使用（DB_MC-5085）"),

    # ---- R9 modules (line 1065-1068) ----
    ("modules for the", "模块用于"),
    ("module for a pure C equivalent of", "模块，用于"),
    ("into separate files covering type definitions\nand core-specific differences between dsPIC33CK and dsPIC33AK (DB_MC-6093, DB_MC-5963)",
     "拆分为涵盖类型定义\n和 dsPIC33CK 与 dsPIC33AK 之间内核特定差异的独立文件（DB_MC-6093、DB_MC-5963）"),

    # ---- R9 dsPIC33AK support (line 1073) ----
    ("MCAF R9 adds support for the first dsPIC33A devices. (DB_MC-5577)",
     "MCAF R9 新增了对首批 dsPIC33A 器件的支持。（DB_MC-5577）"),

    # ---- R9 ADC calibration (line 1085-1089) ----
    ("Improved current offset calibration to allow wider maximum range in the Customize page,\nand cause a fault if outside acceptable limits\n(DB_MC-5542, DB_MC-4924, DB_MC-4180)",
     "改进了电流偏置校准以允许在 Customize 页面中更宽的最大范围，\n如果超出可接受的限制则产生故障\n（DB_MC-5542、DB_MC-4924、DB_MC-4180）"),
    ("Corrected comment in adc_compensation_types.h to describe gain values as Q14, not Q15 (DB_MC-6286)",
     "修正了 adc_compensation_types.h 中的注释，将增益值描述为 Q14 而非 Q15（DB_MC-6286）"),
    ("Implemented ADC gain compensation for dsPIC33AK devices (DB_MC-5956)",
     "实现了 dsPIC33AK 器件的 ADC 增益补偿（DB_MC-5956）"),

    # ---- R9 test harness (line 1095) ----
    ("Add option to apply intentional offset, for testing current calibration (DB_MC-6254)",
     "添加了施加有意偏移的选项，用于测试电流校准（DB_MC-6254）"),

    # ---- R9 custom board (line 1109-1112) ----
    ("Added option to remap a pin to a PCIxR PWM fault source in custom board configuration (DB_MC-6007)",
     "添加了在自定义板级配置中将引脚重新映射到 PCIxR PWM 故障源的选项（DB_MC-6007）"),
    ("Included board ID in generated hal_params.h, to add traceability and context (DB_MC-6185)",
     "在生成的 hal_params.h 中包含板级 ID，以增加可追溯性和上下文（DB_MC-6185）"),
    ("Moved potentiometer ADC signal to optional inputs; a potentiometer is no longer required (DB_MC-6225)",
     "将电位器 ADC 信号移至可选输入；不再需要电位器（DB_MC-6225）"),
    ("Added optional power-on delay (DB_MC-6252)", "添加了可选的上电延迟（DB_MC-6252）"),

    # ---- R9 HAL (line 1118-1120) ----
    ("Removed comparator DAC configuration from MCAF HAL to utilize MCC configuration instead (DB_MC-6023, DB_MC-6160)",
     "从 MCAF HAL 中移除了比较器 DAC 配置以改用 MCC 配置（DB_MC-6023、DB_MC-6160）"),
    ("which incorrectly disabled high-side output but not low-side output (DB_MC-6040)",
     "错误地禁用了高侧输出但未禁用低侧输出的问题（DB_MC-6040）"),
    ("Changed HAL UART functions to generate only if UART is available on selected board (DB_MC-5701)",
     "更改了 HAL UART 函数使其仅在所选板级上有 UART 时才生成（DB_MC-5701）"),

    # ---- R9 MISRA (line 1127-1129) ----
    ("in function parameter list for no-argument functions (DB_MC-6034)",
     "在无参数函数的函数参数列表中使用 void（DB_MC-6034）"),
    ("Rule 15.7: All if - else if constructs shall be terminated with an else statement (DB_MC-5941)",
     "规则 15.7：所有 if - else if 结构都应以 else 语句终止（DB_MC-5941）"),
    ("Rule 21.1: define and undef directives shall not be used on a reserved identifier or reserved macro name (DB_MC-5939)",
     "规则 21.1：不应在保留标识符或保留宏名称上使用 define 和 undef 指令（DB_MC-5939）"),

    # ---- R9 customize page (line 1135-1138) ----
    ("Fixed bug preventing use of optional analog inputs (DB_MC-6269)",
     "修复了阻止使用可选模拟输入的错误（DB_MC-6269）"),
    ("Provided tuning parameters for the ATPLL estimator (DB_MC-5110)",
     "提供了 ATPLL 估计器的整定参数（DB_MC-5110）"),
    ("Added options to enable/disable test harness and test profiling through Customize page (DB_MC-5874)",
     "添加了通过 Customize 页面启用/禁用测试框架和测试性能分析的选项（DB_MC-5874）"),
    ("Include yellow indicator in Customize UI to note further guidance in release notes (DB_MC-6196)",
     "在 Customize UI 中包含黄色指示器以提示发行说明中的进一步指导（DB_MC-6196）"),

    # ---- R9 startup (line 1144) ----
    ("Limited active damping current to maximum startup current (DB_MC-4559)",
     "将主动阻尼电流限制为最大启动电流（DB_MC-4559）"),

    # ---- R9 misc firmware (line 1156-1171) ----
    ("Ensured diagnostic UART TX pin sets output high at initialization (DB_MC-5652)",
     "确保诊断 UART TX 引脚在初始化时设置为输出高电平（DB_MC-5652）"),
    ("Fixed watchdog timeout when using motor phase to PWM mapping that is different from ABC ⇔ PWM123 (DB_MC-5788)",
     "修复了使用与 ABC ⇔ PWM123 不同的电机相到 PWM 映射时的看门狗超时问题（DB_MC-5788）"),
    ("Fixed code generation for outer voltage loop (DB_MC-6097)",
     "修复了外环电压环的代码生成（DB_MC-6097）"),
    ("Removed use of Q15, Q14, Q13, etc. macros (DB_MC-698) — MCAF uses a more structured mechanism at code-generation time\nin the parameters directory header files",
     "移除了 Q15、Q14、Q13 等宏的使用（DB_MC-698）——MCAF 在代码生成时\n在 parameters 目录头文件中使用更结构化的机制"),
    ("Removed remaining RTMD content from firmware package (DB_MC-5664)",
     "从固件包中移除了剩余的 RTMD 内容（DB_MC-5664）"),

    # ---- standalone "The" fragments that appear before code/link nodes ----
    # These are tricky; handle via whole_pairs below for exact matches.
]

# Whole-text-node replacements (exact match after strip)
WHOLE_PAIRS = [
    ("Motor Control Library", "电机控制库"),
    # standalone "The" before code/link nodes
    ("The", "该"),
]

def main():
    soup, path = txutil.load(REL)
    root = txutil.body(soup)
    n1 = txutil.replace_text(soup, PAIRS, root=root)
    n2 = txutil.replace_text(soup, WHOLE_PAIRS, root=root, whole=True)
    n3 = fix_remaining_english(root)
    n4 = fix_dbmc_parens(root)
    txutil.apply_punctuation(root)
    txutil.save(path, soup)
    print(f"Replaced {n1} fragment(s), {n2} whole-node(s), {n3} remaining-english, {n4} dbmc-parens. Saved to {path}")

if __name__ == "__main__":
    main()
