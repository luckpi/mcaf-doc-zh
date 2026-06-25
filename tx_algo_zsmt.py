# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/zsmt"
title_zh = "5.4.5. \u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Zero-Speed / Maximum Torque (ZS/MT)": "\u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
    "Overview": "\u6982\u8ff0",
    "Zero-Speed / Maximum Torque (ZS/MT) provides high torque capability at standstill and at moderate speeds for some permanent-magnet synchronous motors with":
        "\u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09\u4e3a\u67d0\u4e9b\u5177\u6709",
    "rotor saliency": "\u8f6c\u5b50\u51f8\u6027",
    ", such as interior permanent-magnet synchronous motors (": "\u7684\u6c38\u78c1\u540c\u6b65\u7535\u673a\uff0c\u5982\u5185\u7f6e\u6c38\u78c1\u540c\u6b65\u7535\u673a\uff08",
    ").": "\uff09\uff0c\u5728\u9759\u6b62\u548c\u4e2d\u7b49\u901f\u5ea6\u4e0b\u63d0\u4f9b\u9ad8\u8f6c\u77e9\u80fd\u529b\u3002",
    "ZS/MT applies a high-frequency excitation signal to estimate position from the motor\u2019s inductance characteristics. (This makes it an":
        "ZS/MT \u65bd\u52a0\u9ad8\u9891\u6fc0\u52b1\u4fe1\u53f7\uff0c\u901a\u8fc7\u7535\u673a\u7684\u7535\u611f\u7279\u6027\u6765\u4f30\u8ba1\u4f4d\u7f6e\u3002\uff08\u8fd9\u4f7f\u5b83\u6210\u4e3a\u4e00\u4e2a",
    "intrusive": "\u4fb5\u5165\u5f0f",
    "estimator.)": "\u4f30\u8ba1\u5668\u3002\uff09",
    "shows a high-level block diagram containing the excitation, phase detection, and phase-locked loop blocks of ZS/MT.":
        "\u5c55\u793a\u4e86 ZS/MT \u7684\u9ad8\u5c42\u65b9\u6846\u56fe\uff0c\u5305\u542b\u6fc0\u52b1\u3001\u76f8\u4f4d\u68c0\u6d4b\u548c\u9501\u76f8\u73af\u6a21\u5757\u3002",
    "ZS/MT block diagram": "ZS/MT \u65b9\u6846\u56fe",
    "Further information": "\u66f4\u591a\u4fe1\u606f",
    "This feature is freely available as of MCAF R7, but documentation is provided only by request. For more information, please":
        "\u6b64\u529f\u80fd\u4ece MCAF R7 \u5f00\u59cb\u514d\u8d39\u63d0\u4f9b\uff0c\u4f46\u6587\u6863\u4ec5\u5e94\u8bf7\u63d0\u4f9b\u3002\u5982\u9700\u66f4\u591a\u4fe1\u606f\uff0c\u8bf7",
    "contact Microchip": "\u8054\u7cfb Microchip",
    "5.4.5. Zero-Speed / Maximum Torque (ZS/MT)": "5.4.5. \u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
    "5.4.5.1. Overview": "5.4.5.1. \u6982\u8ff0",
    "5.4.5.2. Further information": "5.4.5.2. \u66f4\u591a\u4fe1\u606f",
    "Angle-tracking Phase-locked Loop (ATPLL)": "\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09",
    "Sliding Mode Observer (SMO)": "\u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
