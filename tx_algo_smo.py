# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/smo"
title_zh = "5.4.6. \u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Sliding Mode Observer (SMO)": "\u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09",
    "Overview": "\u6982\u8ff0",
    "The Sliding Mode Observer (SMO) is used here for the velocity and rotor angle estimation of a":
        "\u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09\u5728\u6b64\u7528\u4e8e",
    "to achieve sensorless control. The algorithm uses the PMSM current dynamics and forces the estimated current to match the measured current using a sliding mode gain. The estimated back-emf is used to calculate the position and velocity as shown in the implementation block diagram. The implementation is based on":
        "\u7684\u901f\u5ea6\u548c\u8f6c\u5b50\u89d2\u5ea6\u4f30\u8ba1\uff0c\u4ee5\u5b9e\u73b0\u65e0\u4f20\u611f\u5668\u63a7\u5236\u3002\u8be5\u7b97\u6cd5\u4f7f\u7528 PMSM \u7535\u6d41\u52a8\u6001\u5b66\uff0c\u5e76\u901a\u8fc7\u6ed1\u6a21\u589e\u76ca\u5f3a\u5236\u4f30\u8ba1\u7535\u6d41\u5339\u914d\u6d4b\u91cf\u7535\u6d41\u3002\u4f30\u8ba1\u7684\u53cd\u7535\u52a8\u52bf\u7528\u4e8e\u8ba1\u7b97\u4f4d\u7f6e\u548c\u901f\u5ea6\uff0c\u5982\u5b9e\u73b0\u65b9\u6846\u56fe\u6240\u793a\u3002\u5b9e\u73b0\u57fa\u4e8e",
    ", with some improvements in parameter calculations.": "\uff0c\u5728\u53c2\u6570\u8ba1\u7b97\u65b9\u9762\u6709\u4e00\u4e9b\u6539\u8fdb\u3002",
    "Implementation Block Diagram and Description": "\u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "SMO: High-level Block Diagram": "SMO\uff1a\u9ad8\u5c42\u65b9\u6846\u56fe",
    "The observer model uses current dynamics (": "\u89c2\u6d4b\u5668\u6a21\u578b\u4f7f\u7528\u7535\u6d41\u52a8\u6001\u5b66\uff08",
    ") in the stationary frame (": "\uff09\u5728\u9759\u6b62\u5750\u6807\u7cfb\uff08",
    "-domain).": "\u57df\uff09\u4e2d\u3002",
    "SMO": "SMO",
    "Calculation": "\u8ba1\u7b97",
    "To prevent possible chattering, a smoothly-saturating function has been used instead of a signum function. The sliding gains (":
        "\u4e3a\u4e86\u9632\u6b62\u53ef\u80fd\u7684\u6296\u632f\uff0c\u4f7f\u7528\u4e86\u5e73\u6ed1\u9971\u548c\u51fd\u6570\u4ee3\u66ff\u7b26\u53f7\u51fd\u6570\u3002\u6ed1\u6a21\u589e\u76ca\uff08",
    ") and the boundary layer width (": "\uff09\u548c\u8fb9\u754c\u5c42\u5bbd\u5ea6\uff08",
    ") have been calculated using Lyapunov and describing function methods. The low-pass filters (LPFs) used for the back-emf filtering are adaptive filters, such that the cut-off frequency is always equal to the reference speed. These filters introduce a delay which needs to be compensated (":
        "\uff09\u4f7f\u7528 Lyapunov \u548c\u63cf\u8ff0\u51fd\u6570\u65b9\u6cd5\u8ba1\u7b97\u3002\u7528\u4e8e\u53cd\u7535\u52a8\u52bf\u6ee4\u6ce2\u7684\u4f4e\u901a\u6ee4\u6ce2\u5668\uff08LPF\uff09\u662f\u81ea\u9002\u5e94\u6ee4\u6ce2\u5668\uff0c\u5176\u622a\u6b62\u9891\u7387\u59cb\u7ec8\u7b49\u4e8e\u53c2\u8003\u901f\u5ea6\u3002\u8fd9\u4e9b\u6ee4\u6ce2\u5668\u5f15\u5165\u4e86\u9700\u8981\u8865\u507f\u7684\u5ef6\u8fdf\uff08",
    "). The estimated position from the back-emf is differentiated with respect to time to estimate the speed. This estimated speed is further filtered using another adaptive LPF to get the final speed.":
        "\uff09\u3002\u4ece\u53cd\u7535\u52a8\u52bf\u4f30\u8ba1\u7684\u4f4d\u7f6e\u5bf9\u65f6\u95f4\u6c42\u5bfc\u4ee5\u4f30\u8ba1\u901f\u5ea6\u3002\u6b64\u4f30\u8ba1\u901f\u5ea6\u518d\u901a\u8fc7\u53e6\u4e00\u4e2a\u81ea\u9002\u5e94 LPF \u6ee4\u6ce2\u4ee5\u83b7\u5f97\u6700\u7ec8\u901f\u5ea6\u3002",
    "5.4.6. Sliding Mode Observer (SMO)": "5.4.6. \u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09",
    "5.4.6.1. Overview": "5.4.6.1. \u6982\u8ff0",
    "5.4.6.2. Implementation Block Diagram and Description": "5.4.6.2. \u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "Zero-Speed / Maximum Torque (ZS/MT)": "\u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
    "Flux control": "\u78c1\u901a\u63a7\u5236",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
