# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/pll"
title_zh = "5.4.2. AN1292 \u9501\u76f8\u73af\uff08PLL\uff09"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "AN1292 Phase-locked Loop (PLL)": "AN1292 \u9501\u76f8\u73af\uff08PLL\uff09",
    "Overview": "\u6982\u8ff0",
    "The sensorless estimator used to estimate position and velocity is essentially the same one described in application note":
        "\u7528\u4e8e\u4f30\u8ba1\u4f4d\u7f6e\u548c\u901f\u5ea6\u7684\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u672c\u8d28\u4e0a\u4e0e\u5e94\u7528\u7b14\u8bb0",
    "AN1292 Phase-locked loop block diagram": "AN1292 \u9501\u76f8\u73af\u65b9\u6846\u56fe",
    "Stationary-frame voltages": "\u9759\u6b62\u5750\u6807\u7cfb\u7535\u538b",
    "and currents": "\u548c\u7535\u6d41",
    "are used to estimate back-emf components": "\u7528\u4e8e\u4f30\u8ba1\u53cd\u7535\u52a8\u52bf\u5206\u91cf",
    "using a discrete-time approximation of the equation": "\u4f7f\u7528\u65b9\u7a0b\u7684\u79bb\u6563\u65f6\u95f4\u8fd1\u4f3c",
    "The feedback loop shown in": "\u53cd\u9988\u73af\u5982",
    "is then used to rotate": "\u6240\u793a\uff0c\u7528\u4e8e\u65cb\u8f6c",
    "into the synchronous (dq) frame to produce an error signal and update the electrical angle":
        "\u5230\u540c\u6b65\uff08dq\uff09\u5750\u6807\u7cfb\u4ee5\u4ea7\u751f\u8bef\u5dee\u4fe1\u53f7\u5e76\u66f4\u65b0\u7535\u6c14\u89d2\u5ea6",
    "(rather than": "\uff08\u800c\u4e0d\u662f",
    "shown in the diagram) used for rotation, where": "\u56fe\u4e2d\u6240\u793a\uff09\u7528\u4e8e\u65cb\u8f6c\uff0c\u5176\u4e2d",
    "and": "\u548c",
    "in firmware) is a parameter that defaults to zero, but can be adjusted manually with":
        "\u5728\u56fa\u4ef6\u4e2d\uff09\u662f\u4e00\u4e2a\u9ed8\u8ba4\u4e3a\u96f6\u7684\u53c2\u6570\uff0c\u4f46\u53ef\u4ee5\u901a\u8fc7",
    "real-time diagnostic tools": "\u5b9e\u65f6\u8bca\u65ad\u5de5\u5177",
    "5.4.2. AN1292 Phase-locked Loop (PLL)": "5.4.2. AN1292 \u9501\u76f8\u73af\uff08PLL\uff09",
    "5.4.2.1. Overview": "5.4.2.1. \u6982\u8ff0",
    "Firmware Interface": "\u56fa\u4ef6\u63a5\u53e3",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
