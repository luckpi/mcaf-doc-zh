# -*- coding: utf-8 -*-
"""Batch 4: fix residual English in code comments and body text for 7 pages."""
import os
import sys
from bs4 import BeautifulSoup, NavigableString
from txutil import load, save, body, replace_text, apply_punctuation

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def fix_page(rel, pairs, whole_pairs=None):
    """Load a .zh.html page, apply substring and whole-text replacements, save."""
    soup, path = load(rel + ".zh.html")
    root = soup
    n1 = replace_text(soup, pairs, root=root)
    n2 = 0
    if whole_pairs:
        n2 = replace_text(soup, whole_pairs, root=root, whole=True)
    apply_punctuation(root)
    save(path, soup)
    print(f"  {rel}.zh.html: {n1} substring + {n2} whole replacements")


# ---------------------------------------------------------------------------
# 1. algorithms/estimator-interface.zh.html
# ---------------------------------------------------------------------------
est_pairs = [
    # Body text (line 92-93)
    ("Storage for this state variable structure will be declared in",
     "此状态变量结构的存储将声明在"),
    (", which typically looks like this:", "，通常如下所示："),
    # Code comments - first code block (lines 86-117)
    ("State variable structure for use by Xyz estimator",
     "供 Xyz 估计器使用的状态变量结构"),
    ("Relative angle used for comparing estimator electrical angles",
     "用于比较估计器电气角度的相对角度"),
    ("quadrature encoder with velocity tracking loop",
     "带速度跟踪环的正交编码器"),
    ("State estimator data for position/velocity",
     "位置/速度的状态估计器数据"),
    ("XYZ estimator", "XYZ 估计器"),
    ("inputs common to most estimators",
     "大多数估计器的公共输入"),
    ("estimated rotor angle (electrical)",
     "估计的转子角度（电气）"),
    ("estimated rotor velocity (electrical)",
     "估计的转子速度（电气）"),
    # Code comments - second code block (lines 151-210) doc comments
    ("Initializes Xyz state variables on reset.",
     "在复位时初始化 Xyz 状态变量。"),
    ("Initializes Xyz state variables prior to starting motor.",
     "在启动电机前初始化 Xyz 状态变量。"),
    ("Executes one control step of the Xyz estimator.",
     "执行 Xyz 估计器的一个控制步。"),
    ("Common input signals (e.g. stationary-frame voltage and current)",
     "公共输入信号（例如静止坐标系电压和电流）"),
    ("Motor parameters (e.g. resistance, inductance, etc.)",
     "电机参数（例如电阻、电感等）"),
    ("Returns commutation angle", "返回换相角度"),
    ("Returns electrical frequency", "返回电气频率"),
    ("Determine whether startup delay is requested",
     "确定是否请求启动延迟"),
    ("whether a startup delay is requested",
     "是否请求启动延迟"),
    ("@param xyz Xyz state variable structure",
     "@param xyz Xyz 状态变量结构"),
    ("@param xyz state", "@param xyz 状态"),
    ("@param pinput", "@param pinput"),
    ("@param pmotor", "@param pmotor"),
    ("@param startupStatus startup status",
     "@param startupStatus 启动状态"),
    ("@return commutation angle", "@return 换相角度"),
    ("@return electrical frequency", "@return 电气频率"),
    ("@return whether a startup delay is requested",
     "@return 是否请求启动延迟"),
]
est_whole = [
    ("and", "和"),
]

# ---------------------------------------------------------------------------
# 2. components/foc.zh.html
# ---------------------------------------------------------------------------
foc_pairs = [
    # Order: longest first to avoid partial matches
    ("The actual minimum and maximum duty cycles created by the PWM generators",
     "PWM 生成器实际产生的最小和最大占空比"),
    ("and no significant difference in propagation delay between gate drive channels.",
     "且栅极驱动通道之间的传播延迟没有显著差异。"),
    ("from the perspective of the PWM duty cycle registers.",
     "从 PWM 占空比寄存器的角度。"),
    ("Effective limits for duty cycle as seen on the PWM outputs:",
     "PWM 输出上看到的占空比有效限制："),
    ("NOTE: this assumes identical dead time,",
     "注意：这假设死区时间相同，"),
    ("will have dead time (=0.04) added and subtracted.",
     "将加上和减去死区时间（=0.04）。"),
    ("Minimum and maximum duty cycles,",
     "最小和最大占空比，"),
    ("The minimum duty cycle of the half-bridge affects",
     "半桥的最小占空比影响"),
    ("The maximum duty cycle of the half-bridge affects",
     "半桥的最大占空比影响"),
    ("the minimum duty cycle of upper transistors",
     "上桥臂晶体管的最小占空比"),
    ("the maximum duty cycle of upper transistors",
     "上桥臂晶体管的最大占空比"),
    ("and maximum duty cycle of lower transistors.",
     "和下桥臂晶体管的最大占空比。"),
    ("and minimum duty cycle of lower transistors.",
     "和下桥臂晶体管的最小占空比。"),
    ("Minimum duty cycle register value in counts",
     "最小占空比寄存器值（计数）"),
    ("Minimum duty cycle register value, as ratio",
     "最小占空比寄存器值（比值）"),
    ("Maximum low-side duty cycle register value in counts",
     "最大低侧占空比寄存器值（计数）"),
    ("Maximum duty cycle register value in counts",
     "最大占空比寄存器值（计数）"),
    ("Maximum duty cycle register value, as ratio",
     "最大占空比寄存器值（比值）"),
    ("Minimum low-side duty cycle register value in counts",
     "最小低侧占空比寄存器值（计数）"),
    ("Minimum duty cycle on PWMxH: 0.005",
     "PWMxH 上的最小占空比：0.005"),
    ("Minimum duty cycle on PWMxL: 0.0223",
     "PWMxL 上的最小占空比：0.0223"),
    ("Maximum duty cycle on PWMxH: 0.8977",
     "PWMxH 上的最大占空比：0.8977"),
    ("Maximum duty cycle on PWMxL: 0.915",
     "PWMxL 上的最大占空比：0.915"),
]

# ---------------------------------------------------------------------------
# 3. components/mcapi.zh.html
# ---------------------------------------------------------------------------
mcapi_pairs = [
    # "or" between code tags (line 211)
    (" or ", " 或 "),
]
mcapi_whole = [
    ("Get", "获取"),
    ("The", "该"),
    ("Returns", "返回"),
]

# ---------------------------------------------------------------------------
# 4. architecture/schedopt.zh.html
# ---------------------------------------------------------------------------
sched_pairs = [
    ("// all I do is reverse args", "// 我只是反转参数"),
    ("/* function declaration only", "/* 仅函数声明"),
    ("Ha ha I don't have to tell", "哈哈，我不必告诉你"),
    ("you how it works */", "它如何工作 */"),
    ("// some other function with side effects", "// 其他有副作用的函数"),
]
sched_whole = [
    ("With", "在"),
]

# ---------------------------------------------------------------------------
# 5. architecture/statevar.zh.html
# ---------------------------------------------------------------------------
statevar_pairs = [
    # Order: longest first
    ("desired dq-frame voltage, direct output of current loop",
     "期望的 dq 坐标系电压，电流环的直接输出"),
    ("sine and cosine of electrical angle",
     "电气角度的正弦和余弦"),
    ("Calculate Sine and Cosine from pmotor->theta_e",
     "从 pmotor->theta_e 计算正弦和余弦"),
    ("Calculate vAlpha, Vbeta from Sine, Cosine, Vd and Vq",
     "从正弦、余弦、Vd 和 Vq 计算 vAlpha、Vbeta"),
    ("Angle and speed, including estimators",
     "角度和速度，包括估计器"),
    ("Current loop forward path", "电流环前向路径"),
    ("desired dq-frame voltage", "期望的 dq 坐标系电压"),
    ("desired alphabeta-frame voltage", "期望的 alphabeta 坐标系电压"),
    ("desired phase voltage", "期望的相电压"),
    ("electrical angle", "电气角度"),
    ("electrical frequency", "电气频率"),
    ("PWM count", "PWM 计数值"),
    (", and ", "，和 "),
]

# ---------------------------------------------------------------------------
# 6. architecture/config-params.zh.html
# ---------------------------------------------------------------------------
config_pairs = [
    # Order: longest first
    ("PWM loops necessary for transitioning from open loop to closed loop",
     "从开环过渡到闭环所需的 PWM 循环"),
    ("Time it takes to ramp from zero to MINSPEEDINRPM. Time represented in seconds",
     "从零斜坡到 MINSPEEDINRPM 所需的时间。时间以秒为单位"),
    ("Number of control loops that must execute before the button routine is executed.",
     "在执行按钮例程之前必须执行的控制循环数。"),
    ("PWM loops per velocity calculation",
     "每次速度计算对应的 PWM 循环数"),
    ("Instruction cycle frequency (Hz)",
     "指令周期频率（Hz）"),
    ("Instruction cycle period (sec)",
     "指令周期（秒）"),
    ("Basic loop period in units of Tcy",
     "基本循环周期（以 Tcy 为单位）"),
    ("Speed Control Period", "速度控制周期"),
    ("Dead time in dTcys", "死区时间（以 dTcy 为单位）"),
    ("PWM Period = 1.0 / PWMFREQUENCY",
     "PWM 周期 = 1.0 / PWMFREQUENCY"),
    ("Current loop gains", "电流环增益"),
    ("integral gain", "积分增益"),
    ("proportional gain", "比例增益"),
    ("--- commutation slewrate parameters ---",
     "--- 换相压摆率参数 ---"),
]

# ---------------------------------------------------------------------------
# 7. implementation/codegen.zh.html
# ---------------------------------------------------------------------------
codegen_pairs = [
    # Order: longest first
    ("Limit for output line-to-line voltage of d-axis current controller, expressed as a fraction of DC link voltage",
     "d 轴电流控制器输出线电压限值，以占 DC 母线电压的比例表示"),
    ("(c) 2018 Microchip Technology Inc. and its subsidiaries. You may use",
     "(c) 2018 Microchip Technology Inc. 及其子公司。您可以使用"),
    ("this software and any derivatives exclusively with Microchip products.",
     "此软件及其任何衍生品仅与 Microchip 产品配合使用。"),
    ("Motor Control Application Framework",
     "电机控制应用框架"),
    ("main field-oriented-control code",
     "主磁场定向控制代码"),
    ("Current loop proportional gain",
     "电流环比例增益"),
    ("Current loop integral gain",
     "电流环积分增益"),
    ("Velocity loop proportional gain",
     "速度环比例增益"),
    ("Velocity loop integral gain",
     "速度环积分增益"),
    ("PI phase at crossover = 45.000 deg",
     "交叉频率处的 PI 相位 = 45.000 度"),
    ("PI phase at crossover = 10.000 deg",
     "交叉频率处的 PI 相位 = 10.000 度"),
    ("crossover frequency = 1.531 k rad/s (243.680 Hz)",
     "交叉频率 = 1.531 k rad/s (243.680 Hz)"),
    ("crossover frequency = 93.645 rad/s (14.904 Hz)",
     "交叉频率 = 93.645 rad/s (14.904 Hz)"),
    ("phase margin = 80 deg", "相位裕度 = 80 度"),
    ("phase margin = 65 deg", "相位裕度 = 65 度"),
    ("PI Coefficients", "PI 系数"),
    ("Current loop", "电流环"),
    ("Velocity loop", "速度环"),
    ("Component: FOC", "组件：FOC"),
]

# ---------------------------------------------------------------------------
# Run all fixes
# ---------------------------------------------------------------------------
print("=== Batch 4: fixing residual English ===\n")

print("[1/7] algorithms/estimator-interface")
fix_page("algorithms/estimator-interface", est_pairs, est_whole)

print("[2/7] components/foc")
fix_page("components/foc", foc_pairs)

print("[3/7] components/mcapi")
fix_page("components/mcapi", mcapi_pairs, mcapi_whole)

print("[4/7] architecture/schedopt")
fix_page("architecture/schedopt", sched_pairs, sched_whole)

print("[5/7] architecture/statevar")
fix_page("architecture/statevar", statevar_pairs)

print("[6/7] architecture/config-params")
fix_page("architecture/config-params", config_pairs)

print("[7/7] implementation/codegen")
fix_page("implementation/codegen", codegen_pairs)

print("\n=== Done ===")
