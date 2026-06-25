# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/foc/overview"
title_zh = "5.1.1. 磁场定向控制（FOC）：概述"

m = {
    "Detailed Algorithm Notes": "详细算法说明",
    "Field-oriented Current Control": "磁场定向电流控制",
    "Field-oriented control (FOC): an overview": "磁场定向控制（FOC）：概述",
    "Fundamentals of FOC": "FOC 基础",
    "Field-oriented control (FOC), also known as vector control, is a technique of controlling the stator magnetic field of a motor relative to a rotating reference frame of electrical excitation. It can achieve smooth torque, high torque capability, high efficiency, and high bandwidth.":
        "磁场定向控制（FOC），又称矢量控制，是一种相对于电励磁的旋转参考坐标系来控制电机定子磁场的技术。它能够实现平滑转矩、高转矩能力、高效率和高带宽。",
    "FOC can be used by several types of motors: permanent-magnet synchronous motors, synchronous reluctance motors, and induction motors. The reference frame is chosen to decouple the components of the stator field into a flux-producing component and a torque-producing component, which can be managed separately. In permanent-magnet synchronous motors and synchronous reluctance motors, a reference frame is used that rotates synchronously with the rotor, aligned along the axis of rotor magnetic flux. In induction motors, the reference frame rotates at the required synchronous speed needed to achieve a desired slip.":
        "FOC 可用于多种类型的电机：永磁同步电机、同步磁阻电机和感应电机。通过选择适当的参考坐标系，可将定子磁场的分量解耦为产生磁通的分量和产生转矩的分量，从而分别加以控制。在永磁同步电机和同步磁阻电机中，所采用的参考坐标系与转子同步旋转，并沿转子磁通轴线对齐。在感应电机中，参考坐标系以实现所需转差率所要求的同步转速旋转。",
    "FOC does have more stringent signal sensing and conditioning requirements than six-step control, requiring the following:":
        "与六步控制相比，FOC 对信号检测与调理的要求更为严格，需要以下条件：",
    "phase current measurements, to estimate the stator field vector":
        "相电流测量，用于估计定子磁场矢量",
    "an estimate of rotor angle, usually within 5 – 10 electrical degrees (higher pole count motors require better mechanical accuracy)":
        "转子角度估计，通常精度需在 5–10 电角度以内（极对数越多的电机要求更高的机械精度）",
    "Computational requirements of FOC vary, but are generally higher than six-step. Currents and voltages are translated between reference frames by matrix multiplications, effectively a few calculations of the form":
        "FOC 的计算量因实现而异，但通常高于六步控制。电流和电压通过矩阵乘法在不同参考坐标系之间转换，实际上就是若干形如",
    "or": "或",
    ". If the rotor angle is not sensed directly — with resolver or quadrature encoder — it can be estimated from a sensorless estimator through calculations based on current and voltage measurements.":
        "的计算。如果转子角度未直接检测（例如使用旋变或正交编码器），则可基于电流和电压测量，通过无传感器估计器计算得到。",
    "The benefits of high-performance torque control are often worth the costs, even in applications with relatively slow dynamics, such as pumps and fans.":
        "高性能转矩控制所带来的收益通常值得其代价，即使在动态响应相对较慢的应用（如水泵和风机）中也是如此。",
    "© Copyright 2017-2026, Microchip Technology, Inc..": "© 版权所有 2017-2026，Microchip Technology, Inc..",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
