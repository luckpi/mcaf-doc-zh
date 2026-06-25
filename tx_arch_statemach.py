# -*- coding: utf-8 -*-
import txutil

rel = "architecture/statemach"
title_zh = "3.7. 状态机"

m = {
    # breadcrumb / sidebar / headings
    "Architecture": "架构",
    "State Machine": "状态机",
    "States": "状态",
    "Scheduling and Optimization": "调度与优化",
    "Treatment of Numerical Algorithms": "数值算法处理",
    # TOC entries
    "3.7. State Machine": "3.7. 状态机",
    "3.7.1. States": "3.7.1. 状态",
    # body
    "The motor control state machine can be described as a hierarchical state machine, shown below in":
        "电机控制状态机可以描述为分层状态机，如下",
    ". The states are shown in blue; the names (":
        "所示。状态以蓝色显示；名称（",
    ") are the ones used in the application framework code. Transition conditions are shown as labeled arrows.":
        "）是应用框架代码中使用的名称。转换条件以带标签的箭头表示。",
    "This state machine is intended to treat the motor controller at a very high level: rather than concern itself with detailed information about the motor (is a stall occurring? is there an overvoltage?), the state machine is designed around general events like whether a fault has been detected, or whether a start or stop sequence is complete.":
        "此状态机旨在从非常高的层面处理电机控制器：它不关注电机的详细信息（是否发生堵转？是否过压？），而是围绕一般事件设计，例如是否检测到故障，或者启动或停止序列是否完成。",
    "Motor controller state diagram": "电机控制器状态图",
    "These states are divided into subgroups:":
        "这些状态分为以下子组：",
    "Primary states: all the states except for those used in test operation.":
        "主要状态：除测试操作中使用的状态外的所有状态。",
    "Normal states: states where a fault is not occurring.":
        "正常状态：未发生故障的状态。",
    ": a fault has occurred.": "：已发生故障。",
    "Secondary states: all the states used in test operation. These states cause the normal state machine to be ignored, along with some of the fault detection algorithms that may produce false positives when in test modes.":
        "次要状态：测试操作中使用的所有状态。这些状态会使正常状态机被忽略，同时也会忽略一些在测试模式下可能产生误报的故障检测算法。",
    "The grouping here forms a hierarchical state machine. For example: any of the normal states will transition to":
        "此处的分组构成了分层状态机。例如：任何正常状态在检测到故障时都会转换到",
    "if a fault has been detected. (Traditional state machines would require transitions to":
        "。（传统状态机需要显示从",
    "to be shown from": "到",
    ", and": "、",
    ".)": "。）",
    "Further detail is given in the": "更多细节见",
    "section.": "部分。",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
