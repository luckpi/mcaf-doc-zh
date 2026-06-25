# -*- coding: utf-8 -*-
import txutil

rel = "appendix/mclv2"
title_zh = "7.3. MCLV-2 采样电阻"

m = {
    "7.3. MCLV-2 Sense Resistors — MCAF R9 RC31 文档 (docver 9.0.1)": "7.3. MCLV-2 采样电阻 — MCAF R9 RC31 文档 (docver 9.0.1)",
    "Appendix": "附录",
    "MCLV-2 Sense Resistors": "MCLV-2 采样电阻",
    "The": "The",
    "MCLV\u20112 Development Board": "MCLV-2 开发板",
    "contains a three-phase bridge with low-side 25 m\u03a9 shunt resistors for current sense circuitry on the A and B legs of the bridge as well as in the DC current path, as shown in": "包含一个三相桥，在桥的 A 和 B 支路以及 DC 电流路径上具有低边 25 mΩ 分流电阻用于电流检测电路，如",
    ". Voltages across the sense resistors are used to sense currents": "所示。采样电阻上的电压用于检测电流",
    ", and": "和",
    "Three-phase bridge in MCLV-2, ideal circuit": "MCLV-2 中的三相桥，理想电路",
    "In a real circuit board, the current trace at node \u23cb connecting the A, B, and C legs of the bridge is not uniform in voltage, because it contains nonzero voltage drops along parasitic resistance of the trace. In the MCLV-2 board, this resistance can be modeled as three series resistors": "在实际电路板中，连接桥 A、B、C 支路的节点 \u23cb 处的电流走线电压不均匀，因为走线的寄生电阻上存在非零电压降。在 MCLV-2 板上，此电阻可建模为三个串联电阻",
    ", in": "，如",
    ". Kelvin connections are made directly from the sense resistor terminals to a differential amplifier, so that the voltage drops along these parasitic resistances do not affect the current measurements.": "。开尔文连接直接从采样电阻端子到差分放大器，使这些寄生电阻上的电压降不影响电流测量。",
    "Three-phase bridge in MCLV-2, real circuit with proper layout": "MCLV-2 中的三相桥，布局正确的实际电路",
    "Unfortunately there were some layout errors in the MCLV-2 board. Kelvin connections were used, but were shorted together in signal traces, so the voltage drops along these parasitic resistances": "遗憾的是，MCLV-2 板存在一些布局错误。虽然使用了开尔文连接，但在信号走线中被短路在一起，因此这些寄生电阻上的电压降",
    "do": "确实",
    "affect the current measurements, and can effectively be modeled as shown in": "影响电流测量，可有效建模如",
    ", where the shorted node \u2467 is used for the common terminal in all three current sensing circuits.": "所示，其中短路的节点 \u2467 用作所有三个电流检测电路的公共端。",
    "The approximate values of these trace resistances at room temperature (measured by connecting a current-limited power supply to various pairs of circuit nodes, and measuring current delivered by the power supply and voltages at various points, e.g. putting current into node \u2460 on sense resistor": "这些走线电阻在室温下的近似值（通过将限流电源连接到各对电路节点，测量电源输出的电流和各点电压来测量，例如将电流注入采样电阻",
    "and out of node \u2466 on sense resistor": "的节点 \u2460 并从采样电阻",
    ", in order to measure": "的节点 \u2466 引出，以测量",
    ") are": "）为",
    "This effectively means the voltage": "这实际上意味着节点 \u2467 处的电压",
    "at node \u2467 is a weighted average of the three voltages": "是三个电压的加权平均值：",
    "at node \u2462,": "节点 \u2462 处的",
    "at node \u2463, and": "节点 \u2463 处的，以及",
    "at node \u2465:": "节点 \u2465 处的：",
    ". Test currents were also used to measure the approximate weights": "。还使用测试电流测量了近似权重",
    "If we sample currents when all the lower switches are on, and": "如果我们在所有低侧开关导通时采样电流，且",
    "is 0, then the voltage drop across": "为 0，则",
    "is 0, and the other two voltage drops are": "上的电压降为 0，另外两个电压降为",
    ". We can analyze the circuit to determine the impact on current sensing, and if we write the sense resistors as a nominal resistance": "。我们可以分析电路以确定对电流检测的影响，如果我们将采样电阻写为标称电阻",
    "with a tolerance,": "带有容差",
    ", we can simplify the result to the following :": "，则可将结果简化为：",
    "or in matrix form:": "或以矩阵形式：",
    "with": "其中",
    "In other words, if the sense resistors had no tolerance error (": "换言之，如果采样电阻没有容差误差（",
    ") then": "），则",
    "The compensation gain would be": "补偿增益将为",
    "for the nominal values.": "（对于标称值）。",
    "This is essentially consistent with lab measurements putting in known currents into phase A and B and measuring the digitized": "这与实验室测量基本一致——向 A 相和 B 相注入已知电流并测量数字化",
    "ADC": "ADC",
    "values; one set of those measurements produced an empirical estimate of": "值；其中一组测量产生了经验估计",
    "Error code list": "错误代码列表",
    "Related Documents": "相关文档",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
