# -*- coding: utf-8 -*-
import txutil

rel = "appendix/error_codes"
title_zh = "7.2. 错误代码列表"

m = {
    "7.2. Error code list — MCAF R9 RC31 文档 (docver 9.0.1)": "7.2. 错误代码列表 — MCAF R9 RC31 文档 (docver 9.0.1)",
    "Appendix": "附录",
    "Error code list": "错误代码列表",
    "Blink Pattern": "闪烁模式",
    "ID": "ID",
    "Description": "描述",
    "Comments": "备注",
    "Traps": "陷阱",
    "oscillator failure": "振荡器故障",
    "address error (e.g. alignment)": "地址错误（如对齐）",
    "hard trap": "硬陷阱",
    "stack pointer error": "堆栈指针错误",
    "arithmetic error": "算术错误",
    "DMA bus error for 33A; reserved trap 5 for 33CK": "33A 的 DMA 总线错误；33CK 的保留陷阱 5",
    "soft trap": "软陷阱",
    "illegal opcode error for 33A; reserved trap 7 for 33CK and 33EP": "33A 的非法操作码错误；33CK 和 33EP 的保留陷阱 7",
    "unexpected trap from MCC trap handler": "来自 MCC 陷阱处理程序的意外陷阱",
    "Application errors": "应用错误",
    "number of stall retries exceeded": "堵转重试次数超限",
    "invalid startup FSM state": "无效的启动 FSM 状态",
    "hardware overcurrent": "硬件过流",
    "DC link overvoltage": "DC 母线过压",
    "DC link undervoltage": "DC 母线欠压",
    "Overtemperature": "过温",
    "Commutation failure, detected within estimator": "换相失败，在估计器内检测到",
    "Commutation failure, detected within application": "换相失败，在应用内检测到",
    "Current offset calibration out of range": "电流偏置校准超出范围",
    "ADC gain compensation out of range": "ADC 增益补偿超出范围",
    "trap conflict": "陷阱冲突",
    "IOPUWR illegal opcode / uninitialized W": "IOPUWR 非法操作码/未初始化 W",
    "configuration mismatch": "配置不匹配",
    "watchdog timeout, ISR": "看门狗超时，ISR",
    "watchdog timeout, main loop": "看门狗超时，主循环",
    "board configuration failed": "板级配置失败",
    "board fault detected": "检测到板级故障",
    "Unexpected interrupt errors": "意外中断错误",
    "This covers a range of codes; if you encounter blink patterns in a similar range, please": "这涵盖了一系列代码；如果您遇到类似范围的闪烁模式，请",
    "contact Microchip": "联系 Microchip",
    ", as this indicates an unexpected error that may be caused by a software bug.": "，因为这表示可能由软件错误引起的意外错误。",
    "Glossary": "术语表",
    "MCLV-2 Sense Resistors": "MCLV-2 采样电阻",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
