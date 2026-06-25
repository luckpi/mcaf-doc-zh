# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/flux_control/mtpa"
title_zh = "5.5.2. \u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Flux control": "\u78c1\u94fe\u63a7\u5236",
    "Maximum Torque Per Ampere (MTPA)": "\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09",
    "Overview": "\u6982\u8ff0",
    "For a surface": "\u5bf9\u4e8e\u8868\u8d34",
    "results in Maximum Torque Per Ampere (MTPA) operation of the motor. In a":
        "\u4f1a\u4ea7\u751f\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09\u8fd0\u884c\u3002\u5728",
    "with salient pole rotor (e.g. Interior": "\u4e2d\uff0c\u51f8\u6781\u8f6c\u5b50\uff08\u4f8b\u5982\u5185\u7f6e",
    "or IPMSM), the d and q axis inductance values are different and often":
        "\u6216 IPMSM\uff09\uff0cd \u8f74\u548c q \u8f74\u7535\u611f\u503c\u4e0d\u540c\uff0c\u901a\u5e38",
    ". For a salient-pole motor, the torque equation is given by":
        "\u3002\u5bf9\u4e8e\u51f8\u6781\u7535\u673a\uff0c\u8f6c\u77e9\u65b9\u7a0b\u7531",
    ". The electromagnetic torque produced here is contributed by two terms. The first term is the permanent magnet torque and the second term is the reluctance torque. The reluctance torque is produced in the motor as a result of saliency.":
        "\u7ed9\u51fa\u3002\u6b64\u5904\u4ea7\u751f\u7684\u7535\u78c1\u8f6c\u77e9\u7531\u4e24\u4e2a\u9879\u7ec4\u6210\u3002\u7b2c\u4e00\u9879\u662f\u6c38\u78c1\u8f6c\u77e9\uff0c\u7b2c\u4e8c\u9879\u662f\u78c1\u963b\u8f6c\u77e9\u3002\u78c1\u963b\u8f6c\u77e9\u662f\u7531\u4e8e\u7535\u673a\u7684\u51f8\u6027\u800c\u4ea7\u751f\u7684\u3002",
    "Since": "\u7531\u4e8e",
    ", the reluctance torque can be made to aid the permanent magnet torque if":
        "\uff0c\u5982\u679c",
    ". With a suitable negative": "\uff0c\u53ef\u4ee5\u4f7f\u78c1\u963b\u8f6c\u77e9\u8f85\u52a9\u6c38\u78c1\u8f6c\u77e9\u3002\u901a\u8fc7\u5408\u9002\u7684\u8d1f",
    "value, the motor can be operated at the maximum efficiency yielding Maximum Torque Per Ampere (MTPA) in an IPMSM. The aim of the MTPA algorithm is to calculate such a d-axis current reference (":
        "\u503c\uff0c\u7535\u673a\u53ef\u4ee5\u5728\u6700\u9ad8\u6548\u7387\u4e0b\u8fd0\u884c\uff0c\u4ece\u800c\u5728 IPMSM \u4e2d\u5b9e\u73b0\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09\u3002MTPA \u7b97\u6cd5\u7684\u76ee\u6807\u662f\u8ba1\u7b97\u8fd9\u6837\u7684 d \u8f74\u7535\u6d41\u53c2\u8003\uff08",
    ") for a given operating point of the motor.":
        "\uff09\uff0c\u4ee5\u7528\u4e8e\u7535\u673a\u7684\u7ed9\u5b9a\u5de5\u4f5c\u70b9\u3002",
    "Flow chart and description": "\u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "The value of": "\u4f7f\u7535\u673a\u4ee5\u6700\u9ad8\u6548\u7387\u8fd0\u884c\u4ece\u800c\u5b9e\u73b0 MTPA \u7684",
    "at which the motor operates at maximum efficiency thereby yielding MTPA is derived from the torque equation, and is given by":
        "\u503c\u7531\u8f6c\u77e9\u65b9\u7a0b\u63a8\u5bfc\u51fa\uff0c\u7531",
    ". Here,": "\u7ed9\u51fa\u3002\u8fd9\u91cc\uff0c",
    "is the back emf constant in volts per electrical rad/s units and":
        "\u4e3a\u53cd\u7535\u52a8\u52bf\u5e38\u6570\uff08\u5355\u4f4d\u4e3a\u4f0f\u7279/\u7535\u6c14\u5f27\u5ea6/\u79d2\uff09\uff0c",
    "is the differential inductance given by": "\u4e3a\u5dee\u5206\u7535\u611f\uff0c\u7531",
    ". In addition to the motor parameters": "\u7ed9\u51fa\u3002\u9664\u4e86\u7535\u673a\u53c2\u6570",
    "and": "\u548c",
    ", the d-axis current needed to ensure MTPA (": "\u5916\uff0c\u786e\u4fdd MTPA \u6240\u9700\u7684 d \u8f74\u7535\u6d41\uff08",
    ") is a function of the q-axis current": "\uff09\u662f q \u8f74\u7535\u6d41",
    "shows the flow chart of the MTPA algorithm.":
        "\u7684\u51fd\u6570\u3002",
    "MTPA algorithm flow chart": "MTPA \u7b97\u6cd5\u6d41\u7a0b\u56fe",
    "value is calculated using": "\u503c\u4f7f\u7528",
    ". This calculated value further goes to": "\u8ba1\u7b97\u3002\u6b64\u8ba1\u7b97\u503c\u968f\u540e\u8fdb\u5165",
    "D-axis current reference generation": "D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
    "and is used to generate": "\u5e76\u7528\u4e8e\u751f\u6210",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "Added in R6.": "\u5728 R6 \u4e2d\u6dfb\u52a0\u3002",
    "Low-saliency optimization: In case the motor saliency is low (": "\u4f4e\u51f8\u6027\u4f18\u5316\uff1a\u5982\u679c\u7535\u673a\u51f8\u6027\u8f83\u4f4e\uff08",
    "), the MTPA calculation is skipped to reduce CPU usage, and": "\uff09\uff0c\u5219\u8df3\u8fc7 MTPA \u8ba1\u7b97\u4ee5\u51cf\u5c11 CPU \u4f7f\u7528\uff0c",
    "is set to zero. This is done if the saliency ratio": "\u88ab\u8bbe\u4e3a\u96f6\u3002\u5982\u679c\u51f8\u6027\u6bd4",
    "is less than a user-defined saliency threshold.":
        "\u5c0f\u4e8e\u7528\u6237\u5b9a\u4e49\u7684\u51f8\u6027\u9608\u503c\uff0c\u5219\u6267\u884c\u6b64\u64cd\u4f5c\u3002",
    "Square-root calculation: The present MTPA algorithm uses a full machine-precision square-root calculation. To reduce the CPU instruction cycles, the future versions of MCAF may include alternatives to this.":
        "\u5f00\u65b9\u8ba1\u7b97\uff1a\u5f53\u524d\u7684 MTPA \u7b97\u6cd5\u4f7f\u7528\u5b8c\u6574\u7684\u673a\u5668\u7cbe\u5ea6\u5f00\u65b9\u8ba1\u7b97\u3002\u4e3a\u4e86\u51cf\u5c11 CPU \u6307\u4ee4\u5468\u671f\uff0c\u672a\u6765\u7248\u672c\u7684 MCAF \u53ef\u80fd\u5305\u542b\u66ff\u4ee3\u65b9\u6848\u3002",
    "5.5.2. Maximum Torque Per Ampere (MTPA)": "5.5.2. \u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09",
    "5.5.2.1. Overview": "5.5.2.1. \u6982\u8ff0",
    "5.5.2.2. Flow chart and description": "5.5.2.2. \u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "5.5.2.3. Implementation notes": "5.5.2.3. \u5b9e\u73b0\u8bf4\u660e",
    "Equation based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "\u516c\u5f0f based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "D-axis current reference generation": "D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
