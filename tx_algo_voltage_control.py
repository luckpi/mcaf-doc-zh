# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/voltage-control"
title_zh = "5.8. \u7535\u538b\u63a7\u5236"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Voltage Control": "\u7535\u538b\u63a7\u5236",
    "Overview": "\u6982\u8ff0",
    "Voltage control is an alternative to velocity control. This feature provides the use of q-axis voltage":
        "\u7535\u538b\u63a7\u5236\u662f\u901f\u5ea6\u63a7\u5236\u7684\u66ff\u4ee3\u65b9\u6848\u3002\u6b64\u529f\u80fd\u63d0\u4f9b\u4e86\u4f7f\u7528 q \u8f74\u7535\u538b",
    "rather than velocity as an outer control loop. Voltage control acts upon back-emf as a proxy for velocity control, with some compliance (velocity is allowed to decrease with an increased torque load). The velocity command":
        "\u800c\u975e\u901f\u5ea6\u4f5c\u4e3a\u5916\u73af\u63a7\u5236\u56de\u8def\u3002\u7535\u538b\u63a7\u5236\u4f5c\u7528\u4e8e\u53cd\u7535\u52a8\u52bf\u4f5c\u4e3a\u901f\u5ea6\u63a7\u5236\u7684\u4ee3\u7406\uff0c\u5e26\u6709\u4e00\u5b9a\u7684\u67d4\u6027\uff08\u5141\u8bb8\u901f\u5ea6\u968f\u8f6c\u77e9\u8d1f\u8f7d\u589e\u52a0\u800c\u964d\u4f4e\uff09\u3002\u901f\u5ea6\u547d\u4ee4",
    "is transformed to a equivalent voltage": "\u88ab\u8f6c\u6362\u4e3a\u7b49\u6548\u7535\u538b",
    "using the back-emf constant of the motor. The modified FOC block diagram describing voltage control is shown in":
        "\uff0c\u4f7f\u7528\u7535\u673a\u7684\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u3002\u63cf\u8ff0\u7535\u538b\u63a7\u5236\u7684\u4fee\u6539\u540e FOC \u6846\u56fe\u5982",
    "Figure 5.119": "\u56fe 5.119",
    ". This feature repurposes the velocity controller as a voltage controller with different control parameters.":
        "\u6240\u793a\u3002\u6b64\u529f\u80fd\u5c06\u901f\u5ea6\u63a7\u5236\u5668\u91cd\u65b0\u7528\u4f5c\u5177\u6709\u4e0d\u540c\u63a7\u5236\u53c2\u6570\u7684\u7535\u538b\u63a7\u5236\u5668\u3002",
    "Block diagram of MCAF Field Oriented Control using q-axis voltage as the outer control loop.":
        "\u4ee5 q \u8f74\u7535\u538b\u4f5c\u4e3a\u5916\u73af\u63a7\u5236\u56de\u8def\u7684 MCAF \u77e2\u91cf\u63a7\u5236\u6846\u56fe\u3002",
    "Voltage control can provide a high-bandwidth alternative to velocity control. In some motor control systems, a traditional velocity loop may be constrained in bandwidth, because of the error or the control delay (phase lag) does not allow a stable, high bandwidth voltage control loop. In such systems, a voltage controller can respond faster, limited only by the bandwidth of the current loop.":
        "\u7535\u538b\u63a7\u5236\u53ef\u4ee5\u63d0\u4f9b\u9ad8\u5e26\u5bbd\u7684\u901f\u5ea6\u63a7\u5236\u66ff\u4ee3\u65b9\u6848\u3002\u5728\u67d0\u4e9b\u7535\u673a\u63a7\u5236\u7cfb\u7edf\u4e2d\uff0c\u4f20\u7edf\u7684\u901f\u5ea6\u73af\u53ef\u80fd\u53d7\u5e26\u5bbd\u9650\u5236\uff0c\u56e0\u4e3a\u8bef\u5dee\u6216\u63a7\u5236\u5ef6\u8fdf\uff08\u76f8\u4f4d\u6ede\u540e\uff09\u4e0d\u5141\u8bb8\u7a33\u5b9a\u7684\u9ad8\u5e26\u5bbd\u7535\u538b\u63a7\u5236\u73af\u3002\u5728\u8fd9\u7c7b\u7cfb\u7edf\u4e2d\uff0c\u7535\u538b\u63a7\u5236\u5668\u53ef\u4ee5\u66f4\u5feb\u54cd\u5e94\uff0c\u4ec5\u53d7\u7535\u6d41\u73af\u5e26\u5bbd\u9650\u5236\u3002",
    "Systems which need high bandwidth and cannot tolerate the phase lag of the velocity estimator may be able to use voltage control instead. This feeds back the q-axis voltage from the current controller, filtered, as a feedback term to use in the velocity controller, reappropriated as a voltage controller. The voltage controller will reach equilibrium when":
        "\u9700\u8981\u9ad8\u5e26\u5bbd\u4e14\u65e0\u6cd5\u5bb9\u5fcd\u901f\u5ea6\u4f30\u8ba1\u5668\u76f8\u4f4d\u6ede\u540e\u7684\u7cfb\u7edf\u53ef\u4ee5\u6539\u7528\u7535\u538b\u63a7\u5236\u3002\u8fd9\u5c06\u7535\u6d41\u63a7\u5236\u5668\u7684 q \u8f74\u7535\u538b\u7ecf\u6ee4\u6ce2\u540e\u53cd\u9988\u4f5c\u4e3a\u901f\u5ea6\u63a7\u5236\u5668\uff08\u91cd\u65b0\u7528\u4f5c\u7535\u538b\u63a7\u5236\u5668\uff09\u7684\u53cd\u9988\u9879\u3002\u7535\u538b\u63a7\u5236\u5668\u5728",
    "With": "\u5f53",
    "(no flux weakening), this effectively is a velocity controller with a compliance or \u201cdroop\u201d due to the IR drop across the stator. The phase lag caused by the voltage controller can be less than the position and velocity estimator, and in some applications the droop behavior may be advantageous.":
        "\uff08\u65e0\u5f31\u78c1\uff09\u65f6\u8fbe\u5230\u5e73\u8861\u3002\u8fd9\u5b9e\u9645\u4e0a\u662f\u4e00\u4e2a\u5e26\u6709\u7531\u5b9a\u5b50 IR \u538b\u964d\u5f15\u8d77\u7684\u67d4\u6027\u6216\u201c\u4e0b\u5782\u201d\u7684\u901f\u5ea6\u63a7\u5236\u5668\u3002\u7535\u538b\u63a7\u5236\u5668\u4ea7\u751f\u7684\u76f8\u4f4d\u6ede\u540e\u53ef\u4ee5\u5c0f\u4e8e\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668\uff0c\u5728\u67d0\u4e9b\u5e94\u7528\u4e2d\u4e0b\u5782\u884c\u4e3a\u53ef\u80fd\u662f\u6709\u5229\u7684\u3002",
    "Note:": "\u6ce8\u610f\uff1a",
    "This feature has not been tested extensively. The guidance in this section is preliminary and is based on limited testing so far. Future work may help improve this guidance.":
        "\u6b64\u529f\u80fd\u5c1a\u672a\u7ecf\u8fc7\u5e7f\u6cdb\u6d4b\u8bd5\u3002\u672c\u8282\u4e2d\u7684\u6307\u5357\u662f\u521d\u6b65\u7684\uff0c\u57fa\u4e8e\u76ee\u524d\u6709\u9650\u7684\u6d4b\u8bd5\u3002\u672a\u6765\u7684\u5de5\u4f5c\u53ef\u80fd\u6709\u52a9\u4e8e\u6539\u5584\u6b64\u6307\u5357\u3002",
    "Effects of motor parameters on mechanical compliance": "\u7535\u673a\u53c2\u6570\u5bf9\u673a\u68b0\u67d4\u6027\u7684\u5f71\u54cd",
    "The torque compliance of voltage control can be stated analytically as follows:":
        "\u7535\u538b\u63a7\u5236\u7684\u8f6c\u77e9\u67d4\u6027\u53ef\u4ee5\u89e3\u6790\u5730\u8868\u8ff0\u5982\u4e0b\uff1a",
    "where": "\u5176\u4e2d",
    "captures the effect of flux weakening due to nonzero d-axis current, and":
        "\u6355\u6349\u4e86\u7531\u4e8e\u975e\u96f6 d \u8f74\u7535\u6d41\u5f15\u8d77\u7684\u5f31\u78c1\u6548\u5e94\uff0c",
    "captures the mechanical compliance with load torque.":
        "\u6355\u6349\u4e86\u5bf9\u8d1f\u8f7d\u8f6c\u77e9\u7684\u673a\u68b0\u67d4\u6027\u3002",
    "Equation": "\u65b9\u7a0b",
    "can be derived from the PMSM voltage equations \u2014 Equation": "\u53ef\u4ee5\u4ece PMSM \u7535\u538b\u65b9\u7a0b\u2014\u2014\u65b9\u7a0b",
    "\u2014 in three steps:": "\u2014\u2014\u4e2d\u63a8\u5bfc\uff0c\u5206\u4e3a\u4e09\u6b65\uff1a",
    "setting derivative": "\u5c06\u5bfc\u6570",
    "to zero, yielding": "\u8bbe\u4e3a\u96f6\uff0c\u5f97\u5230",
    "substituting the equation for electromechanical torque:":
        "\u4ee3\u5165\u7535\u673a\u68b0\u8f6c\u77e9\u65b9\u7a0b\uff1a",
    "substituting the voltage control command:": "\u4ee3\u5165\u7535\u538b\u63a7\u5236\u547d\u4ee4\uff1a",
    "and rewriting to relate velocity command, velocity, and torque when current is in steady state.":
        "\u5e76\u91cd\u5199\u4ee5\u5173\u8054\u901f\u5ea6\u547d\u4ee4\u3001\u901f\u5ea6\u548c\u8f6c\u77e9\uff08\u5f53\u7535\u6d41\u5904\u4e8e\u7a33\u6001\u65f6\uff09\u3002",
    "(no flux weakening), the mechanical compliance increases with greater back-emf and decreases with larger stator resistance.":
        "\uff08\u65e0\u5f31\u78c1\uff09\u65f6\uff0c\u673a\u68b0\u67d4\u6027\u968f\u53cd\u7535\u52a8\u52bf\u589e\u5927\u800c\u589e\u5927\uff0c\u968f\u5b9a\u5b50\u7535\u963b\u589e\u5927\u800c\u51cf\u5c0f\u3002",
    "Choosing algorithm parameters": "\u9009\u62e9\u7b97\u6cd5\u53c2\u6570",
    "The voltage controller is not autotuned; control parameters must be tuned manually. At this time, tuning guidance for the voltage loop is limited. Empirical tuning of the voltage loop is acceptable. One approach is to start with the default gains (":
        "\u7535\u538b\u63a7\u5236\u5668\u4e0d\u662f\u81ea\u52a8\u8c03\u53c2\u7684\uff1b\u63a7\u5236\u53c2\u6570\u5fc5\u987b\u624b\u52a8\u8c03\u6574\u3002\u76ee\u524d\uff0c\u7535\u538b\u73af\u7684\u8c03\u53c2\u6307\u5357\u6709\u9650\u3002\u7535\u538b\u73af\u7684\u7ecf\u9a8c\u8c03\u53c2\u662f\u53ef\u63a5\u53d7\u7684\u3002\u4e00\u79cd\u65b9\u6cd5\u662f\u4ece\u9ed8\u8ba4\u589e\u76ca\uff08",
    "), increasing": "\uff09\u5f00\u59cb\uff0c\u9010\u6e10\u589e\u52a0",
    "gradually until there are hints of instability (increased noise in the current loop) and then increasing":
        "\u76f4\u5230\u51fa\u73b0\u4e0d\u7a33\u5b9a\u7684\u8ff9\u8c61\uff08\u7535\u6d41\u73af\u4e2d\u566a\u58f0\u589e\u52a0\uff09\uff0c\u7136\u540e\u589e\u52a0",
    "until there are hints of further instability. (Firmware implementation uses":
        "\u76f4\u5230\u51fa\u73b0\u8fdb\u4e00\u6b65\u4e0d\u7a33\u5b9a\u7684\u8ff9\u8c61\u3002\uff08\u56fa\u4ef6\u5b9e\u73b0\u4f7f\u7528",
    ", so runtime adjustment of": "\uff0c\u56e0\u6b64\u8fd0\u884c\u65f6\u8c03\u6574",
    "is not directly possible; instead, adjust voltage loop": "\u4e0d\u76f4\u63a5\u53ef\u884c\uff1b\u800c\u662f\u8c03\u6574\u7535\u538b\u73af",
    "5.8. Voltage Control": "5.8. \u7535\u538b\u63a7\u5236",
    "5.8.1. Overview": "5.8.1. \u6982\u8ff0",
    "5.8.2. Effects of motor parameters on mechanical compliance": "5.8.2. \u7535\u673a\u53c2\u6570\u5bf9\u673a\u68b0\u67d4\u6027\u7684\u5f71\u54cd",
    "5.8.3. Choosing algorithm parameters": "5.8.3. \u9009\u62e9\u7b97\u6cd5\u53c2\u6570",
    "Temperature Measurement": "\u6e29\u5ea6\u6d4b\u91cf",
    "and": "\u548c",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
