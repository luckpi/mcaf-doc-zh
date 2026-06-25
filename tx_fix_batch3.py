# -*- coding: utf-8 -*-
"""Batch fix residual English text in 6 zh.html pages."""
import txutil

def fix_page(rel, pairs, whole_pairs=None):
    soup, path = txutil.load(rel + ".zh.html")
    root = txutil.body(soup)
    if root is not None:
        txutil.replace_text(soup, pairs, root=root)
        if whole_pairs:
            txutil.replace_text(soup, whole_pairs, root=root, whole=True)
        txutil.apply_punctuation(root)
    txutil.save(path, soup)
    print("Fixed: " + rel)

# ============================================================
# 1. atpll.zh.html (10 fragments)
# ============================================================
atpll_pairs = [
    # The full untranslated paragraph fragment
    ("This block represents a PI controller which is the backbone of the ATPLL estimator. In steady state, the\ninput to the PI controller (which is:",
     "该模块表示一个 PI 控制器，它是 ATPLL 估计器的核心。在稳态下，PI 控制器的输入（即："),
]
atpll_whole = [
    ("and", "和"),
]
fix_page("algorithms/atpll", atpll_pairs, atpll_whole)

# ============================================================
# 2. foc/current_measure.zh.html (9 fragments)
# ============================================================
cm_pairs = [
    ("measures current", "测量电流"),
    (", which equals", "，等于"),
    ("as long as\nthe lower transistor Q", "只要下桥臂晶体管 Q"),
    ("has been turned on.", "已导通。"),
    ("This has several minor disadvantages:", "这有几个次要缺点："),
    ("The low-side transistors must be turned on long enough for any transients to settle,\nso that the ADC can obtain a good sample of currents. (This usually isn\u2019t a big deal,\nespecially if bootstrap gate drives are used, where the low-side transistors need\nto be turned on enough to recharge bootstrap capacitors.)",
     "低侧晶体管必须导通足够长时间以使任何瞬变稳定下来，以便 ADC 能够获得良好的电流采样。（这通常不是大问题，特别是如果使用自举栅极驱动，其中低侧晶体管需要导通足够长时间以给自举电容充电。）"),
    ("Required signal bandwidth of signal conditioning is much greater than the bandwidth\nof interest of the phase currents; usually at least 500 kHz so the settling time is small\nand the low-side transistor on-time can be short. The op-amps used for signal\nconditioning must have an appropriate gain-bandwidth product (GBWP) to support this,\nfor example 10 MHz GBWP for a gain of 20, in order to reach a signal bandwidth of 500 kHz.",
     "信号调理所需的信号带宽远大于相电流的有用带宽；通常至少 500 kHz，以使建立时间短且低侧晶体管导通时间可以较短。用于信号调理的运算放大器必须具有适当的增益带宽积（GBWP）来支持这一点，例如增益为 20 时需要 10 MHz GBWP，以达到 500 kHz 的信号带宽。"),
    ("Gate charge current conducts through the shunt resistors, so during turn-on and turn-off,\nthe voltages across the current sensor experience additional spikes",
     "栅极充电电流流经分流电阻，因此在导通和关断期间，电流传感器上的电压会经历额外的尖峰"),
    ("The required voltage across the shunt resistors takes away some of the available voltage\nneeded to turn on the low-side transistors. Make sure there is sufficient gate voltage\nremaining to guarantee the low-side transistors are fully on when the drive is\noperating at its highest rated output currents \u2014 which is also when full transistor turn-on\nis needed the most.",
     "分流电阻上所需的电压占用了部分可用于导通低侧晶体管的电压。确保剩余的栅极电压足够，以保证在驱动器以其最高额定输出电流运行时低侧晶体管完全导通——这也是最需要晶体管完全导通的时候。"),
]
fix_page("algorithms/foc/current_measure", cm_pairs)

# ============================================================
# 3. foc/tuning.zh.html (9 fragments)
# ============================================================
tuning_pairs = [
    (", but for ", "，但对于"),
    (", and ", "，和"),
    (" 12168\xa0V/As) at 0 RPM. Velocity tuning has ", " 12168\xa0V/As）在 0 RPM。速度整定具有 "),
    (" 12168\xa0V/As) at 1200 RPM. Velocity tuning has ", " 12168\xa0V/As）在 1200 RPM。速度整定具有 "),
    (" 12168\xa0V/As) at 2400 RPM. Velocity tuning has ", " 12168\xa0V/As）在 2400 RPM。速度整定具有 "),
    ("M. W. Degner and R. D. Lorenz,", "M. W. Degner 和 R. D. Lorenz,"),
]
fix_page("algorithms/foc/tuning", tuning_pairs)

# ============================================================
# 4. appendix/mclv2.zh.html (8 fragments)
# ============================================================
mclv2_pairs = [
    ("In a real circuit board, the current trace at node \u24c1 connecting the A, B, and C\nlegs of the bridge is not uniform in voltage, because it contains nonzero voltage drops along parasitic\nresistance of the trace. In the MCLV-2 board, this resistance can be modeled as three series resistors",
     "在实际电路板中，连接桥的 A、B 和 C 支路的节点 \u24c1 处的电流走线电压不均匀，因为它包含沿走线寄生电阻的非零电压降。在 MCLV-2 板中，该电阻可建模为三个串联电阻"),
    (", where the shorted node \u2466 is used for the common terminal in all three current sensing circuits.",
     "，其中短路的节点 \u2466 用作所有三个电流检测电路的公共端。"),
    (" and out of node \u2465 on sense resistor ", " 并从采样电阻 "),
    (" at node \u2466 is a weighted average of the three voltages", " 在节点 \u2466 处是三个电压的加权平均值"),
    (" at node \u2462, and ", " 在节点 \u2462 处，和"),
    (" at node \u2461, ", " 在节点 \u2461 处，"),
    (" at node \u2464: ", " 在节点 \u2464 处："),
]
mclv2_whole = [
    ("The", ""),
    ("and", "和"),
]
fix_page("appendix/mclv2", mclv2_pairs, mclv2_whole)

# ============================================================
# 5. components/testharness.zh.html (23 fragments)
# ============================================================
th_pairs = [
    ("The type of ", ""),
    ("// repeat the following block for each motor", "// 对每个电机重复以下代码块"),
    ("/* update test perturbation waveform */", "/* 更新测试扰动波形 */"),
    ("/* Ensure square wave value maintains sign and is +/- 1 */", "/* 确保方波值保持符号且为 +/- 1 */"),
    ("        * Reverse sign after N cycles (N = sqwave.halfperiod)",
     "        * N 个周期后反转符号（N = sqwave.halfperiod）"),
    (", set ", "，设置"),
    ("Profiling with", "使用"),
]
th_whole = [
    ("The", ""),
    ("the", ""),
    ("is", "的类型为"),
    ("and", "和"),
]
fix_page("components/testharness", th_pairs, th_whole)

# ============================================================
# 6. qei_sync/align-sweep.zh.html (5 fragments)
# ============================================================
as_pairs = [
    ("BLY171D-24V-4000 with 4096-line encoder", "BLY171D-24V-4000 带 4096 线编码器"),
    ("Figures 5.65", "图 5.65"),
]
as_whole = [
    ("and", "和"),
]
fix_page("algorithms/qei_sync/align-sweep", as_pairs, as_whole)

print("\nAll 6 pages fixed.")
