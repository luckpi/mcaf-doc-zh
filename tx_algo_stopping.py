# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/stopping"
title_zh = "5.3. \u505c\u6b62"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Stopping": "\u505c\u6b62",
    "Overview": "\u6982\u8ff0",
    "\u201cStopping\u201d is the process of bringing the motor to a complete stop, after normal operation, with the intent of leaving the motor unpowered and at rest in the":
        "\u201c\u505c\u6b62\u201d\u662f\u5728\u6b63\u5e38\u8fd0\u884c\u4e4b\u540e\u4f7f\u7535\u673a\u5b8c\u5168\u505c\u6b62\u7684\u8fc7\u7a0b\uff0c\u76ee\u7684\u662f\u4f7f\u7535\u673a\u65ad\u7535\u5e76\u9759\u6b62\u4e8e",
    "STOPPED state": "STOPPED \u72b6\u6001",
    "MCAF includes": "MCAF \u5305\u542b",
    "several different options for stopping": "\u51e0\u79cd\u4e0d\u540c\u7684\u505c\u6b62\u9009\u9879",
    "which can be selected in the Customize page of motorBench": "\u53ef\u5728 motorBench \u7684 Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762\u4e2d\u9009\u62e9",
    "Development Suite:": "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\uff1a",
    "Minimal-impact PWM (\u201copen-loop\u201d stopping or \u201ccoastdown\u201d)": "\u6700\u5c0f\u5f71\u54cd PWM\uff08\u201c\u5f00\u73af\u201d\u505c\u6b62\u6216\u201c\u81ea\u7531\u505c\u8f6c\u201d\uff09",
    "Closed-loop current": "\u95ed\u73af\u7535\u6d41",
    "Closed-loop velocity": "\u95ed\u73af\u901f\u5ea6",
    "In each of these, operation in the": "\u5728\u6bcf\u79cd\u65b9\u6cd5\u4e2d\uff0c\u5728",
    "STOPPING state": "STOPPING \u72b6\u6001",
    "continues until one of the following conditions is true:": "\u4e2d\u7684\u8fd0\u884c\u6301\u7eed\u76f4\u5230\u4ee5\u4e0b\u6761\u4ef6\u4e4b\u4e00\u6210\u7acb\uff1a",
    "something causes the motor to exit normal operation (example: a fault occurs, or an operator enters a test mode using real-time diagnostic tools)":
        "\u67d0\u4e9b\u539f\u56e0\u5bfc\u81f4\u7535\u673a\u9000\u51fa\u6b63\u5e38\u8fd0\u884c\uff08\u4f8b\u5982\uff1a\u53d1\u751f\u6545\u969c\uff0c\u6216\u64cd\u4f5c\u5458\u4f7f\u7528\u5b9e\u65f6\u8bca\u65ad\u5de5\u5177\u8fdb\u5165\u6d4b\u8bd5\u6a21\u5f0f\uff09",
    "the motor is requested to run again": "\u7535\u673a\u88ab\u8981\u6c42\u518d\u6b21\u8fd0\u884c",
    "a stop completion flag is set \u2014 this condition is determined differently for each of the different stopping methods.":
        "\u505c\u6b62\u5b8c\u6210\u6807\u5fd7\u88ab\u8bbe\u7f6e \u2014 \u6b64\u6761\u4ef6\u5bf9\u4e8e\u4e0d\u540c\u7684\u505c\u6b62\u65b9\u6cd5\u6709\u4e0d\u540c\u7684\u5224\u5b9a\u65b9\u5f0f\u3002",
    "Minimal-impact PWM": "\u6700\u5c0f\u5f71\u54cd PWM",
    "With minimal-impact PWM \u2014 also known as \u201copen-loop\u201d stopping or \u201ccoastdown\u201d \u2014 the PWM outputs are changed to":
        "\u5728\u6700\u5c0f\u5f71\u54cd PWM \u2014 \u4e5f\u79f0\u201c\u5f00\u73af\u201d\u505c\u6b62\u6216\u201c\u81ea\u7531\u505c\u8f6c\u201d \u2014 \u4e2d\uff0cPWM \u8f93\u51fa\u88ab\u6539\u53d8\u4e3a",
    "the minimal-impact state": "\u6700\u5c0f\u5f71\u54cd\u72b6\u6001",
    ". This is essentially an open-circuit condition on the three-phase bridge; for bootstrap gate drives, the lower transistors are maintained at a low duty cycle to maintain charge in the bootstrap capacitors.":
        "\u3002\u8fd9\u672c\u8d28\u4e0a\u662f\u4e09\u76f8\u6865\u7684\u5f00\u8def\u72b6\u6001\uff1b\u5bf9\u4e8e\u81ea\u4e3e\u6805\u9a71\u52a8\uff0c\u4e0b\u6865\u81f4\u5f00\u5173\u7ba1\u4ee5\u4f4e\u5360\u7a7a\u6bd4\u7ef4\u6301\uff0c\u4ee5\u4fdd\u6301\u81ea\u4e3e\u7535\u5bb9\u5668\u7684\u7535\u8377\u3002",
    "Current measurements may be lost, and sensorless estimators may not be able to provide valid estimates of commutation angle and motor velocity.":
        "\u7535\u6d41\u6d4b\u91cf\u53ef\u80fd\u4e22\u5931\uff0c\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u53ef\u80fd\u65e0\u6cd5\u63d0\u4f9b\u6709\u6548\u7684\u6362\u76f8\u89d2\u5ea6\u548c\u7535\u673a\u901f\u5ea6\u4f30\u8ba1\u3002",
    "Stop completion:": "\u505c\u6b62\u5b8c\u6210\uff1a",
    "Because a velocity estimate may not be available, open-loop stopping waits for a fixed coastdown time interval":
        "\u7531\u4e8e\u901f\u5ea6\u4f30\u8ba1\u53ef\u80fd\u4e0d\u53ef\u7528\uff0c\u5f00\u73af\u505c\u6b62\u7b49\u5f85\u56fa\u5b9a\u7684\u81ea\u7531\u505c\u8f6c\u65f6\u95f4\u95f4\u9694",
    ", assuming that the initial velocity is the worst-case maximum (in case the angle estimator is wrong, or the system comes out of reset). At the end of the coastdown interval, the stop completion flag is set, when it is likely that motor velocity is below":
        "\uff0c\u5047\u8bbe\u521d\u59cb\u901f\u5ea6\u4e3a\u6700\u574f\u60c5\u51b5\u4e0b\u7684\u6700\u5927\u503c\uff08\u4ee5\u9632\u89d2\u5ea6\u4f30\u8ba1\u5668\u9519\u8bef\u6216\u7cfb\u7edf\u4ece\u590d\u4f4d\u4e2d\u6062\u590d\uff09\u3002\u5728\u81ea\u7531\u505c\u8f6c\u95f4\u9694\u7ed3\u675f\u65f6\uff0c\u505c\u6b62\u5b8c\u6210\u6807\u5fd7\u88ab\u8bbe\u7f6e\uff0c\u6b64\u65f6\u7535\u673a\u901f\u5ea6\u5f88\u53ef\u80fd\u4f4e\u4e8e",
    "the coastdown speed threshold": "\u81ea\u7531\u505c\u8f6c\u901f\u5ea6\u9608\u503c",
    "Under these conditions, the only torque acting on the motor is assumed to be from viscous damping":
        "\u5728\u8fd9\u4e9b\u6761\u4ef6\u4e0b\uff0c\u4f5c\u7528\u4e8e\u7535\u673a\u7684\u552f\u4e00\u8f6c\u77e9\u5047\u5b9a\u6765\u81ea\u9ecf\u6027\u963b\u5c3c",
    "and friction": "\u548c\u6469\u64e6",
    "acting on the rotor inertia": "\u4f5c\u7528\u4e8e\u8f6c\u5b50\u60ef\u6027",
    "so that the motor coasts down towards rest, as shown in": "\uff0c\u4f7f\u7535\u673a\u81ea\u7531\u505c\u8f6c\u81f3\u9759\u6b62\uff0c\u5982",
    "and described in \u516c\u5f0f": "\u6240\u793a\uff0c\u5e76\u5728\u516c\u5f0f",
    "Coastdown curve showing the time from initial velocity": "\u81ea\u7531\u505c\u8f6c\u66f2\u7ebf\uff0c\u5c55\u793a\u4ece\u521d\u59cb\u901f\u5ea6",
    "to reach a threshold velocity": "\u5230\u8fbe\u5230\u9608\u503c\u901f\u5ea6\u7684\u65f6\u95f4",
    "This can be solved analytically for the mechanical velocity:": "\u53ef\u4ee5\u5206\u6790\u6c42\u89e3\u673a\u68b0\u901f\u5ea6\uff1a",
    "where": "\u5176\u4e2d",
    "is the initial velocity,": "\u4e3a\u521d\u59cb\u901f\u5ea6\uff0c",
    ", and time constant": "\uff0c\u4ee5\u53ca\u65f6\u95f4\u5e38\u6570",
    "The coastdown time": "\u81ea\u7531\u505c\u8f6c\u65f6\u95f4",
    "is estimated from \u516c\u5f0f": "\u7531\u516c\u5f0f",
    "to determine the time at which motor velocity": "\u4f30\u8ba1\uff0c\u4ee5\u786e\u5b9a\u7535\u673a\u901f\u5ea6",
    "is below the coastdown speed threshold": "\u4f4e\u4e8e\u81ea\u7531\u505c\u8f6c\u901f\u5ea6\u9608\u503c\u7684\u65f6\u95f4",
    "NOTE": "\u6ce8\u610f",
    ": Minimal-impact PWM should": "\uff1a\u6700\u5c0f\u5f71\u54cd PWM \u4e0d\u5e94",
    "not": "\u4e0d\u5e94",
    "be relied on under any the following conditions:": "\u5728\u4ee5\u4e0b\u4efb\u4f55\u6761\u4ef6\u4e0b\u4f7f\u7528\uff1a",
    "the motor has high inertia (can coast down for at least several seconds) and the motor parameters are uncertain":
        "\u7535\u673a\u5177\u6709\u9ad8\u60ef\u6027\uff08\u81f3\u5c11\u9700\u8981\u51e0\u79d2\u949f\u624d\u80fd\u81ea\u7531\u505c\u8f6c\uff09\u4e14\u7535\u673a\u53c2\u6570\u4e0d\u786e\u5b9a",
    "the motor is subject to regenerative torque from its environment that can maintain motor velocity (example: e-bikes, generators, fans subject to windmilling, etc.)":
        "\u7535\u673a\u53d7\u5230\u6765\u81ea\u73af\u5883\u7684\u518d\u751f\u8f6c\u77e9\u4f5c\u7528\uff0c\u53ef\u7ef4\u6301\u7535\u673a\u901f\u5ea6\uff08\u4f8b\u5982\uff1a\u7535\u52a8\u81ea\u884c\u8f66\u3001\u53d1\u7535\u673a\u3001\u53d7\u98ce\u8f66\u5f71\u54cd\u7684\u98ce\u6247\u7b49\uff09",
    "Closed-loop methods": "\u95ed\u73af\u65b9\u6cd5",
    "Under closed-loop stopping, field-oriented current control is maintained, with PWM outputs continuing normal switch-mode operation. This allows sensorless estimators to continue operating, so that a velocity estimate is still available.":
        "\u5728\u95ed\u73af\u505c\u6b62\u4e0b\uff0c\u78c1\u573a\u5b9a\u5411\u7535\u6d41\u63a7\u5236\u5f97\u4ee5\u7ef4\u6301\uff0cPWM \u8f93\u51fa\u7ee7\u7eed\u6b63\u5e38\u7684\u5f00\u5173\u6a21\u5f0f\u8fd0\u884c\u3002\u8fd9\u4f7f\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u80fd\u7ee7\u7eed\u8fd0\u884c\uff0c\u4ece\u800c\u901f\u5ea6\u4f30\u8ba1\u4ecd\u7136\u53ef\u7528\u3002",
    "The stop completion flag is set when the motor velocity has remained below a speed threshold for a minimum time interval.":
        "\u5f53\u7535\u673a\u901f\u5ea6\u5728\u6700\u5c0f\u65f6\u95f4\u95f4\u9694\u5185\u6301\u7eed\u4f4e\u4e8e\u901f\u5ea6\u9608\u503c\u65f6\uff0c\u505c\u6b62\u5b8c\u6210\u6807\u5fd7\u88ab\u8bbe\u7f6e\u3002",
    ": Closed-loop stopping methods should only be used with estimators that are able to maintain velocity estimates below the stopping threshold. (ZS/MT and QEI are good examples. The AN1292 PLL may be able to maintain a velocity estimate, but use of closed-loop stopping should be checked carefully. The ATPLL is known to have stability issues operating at very low speeds.)":
        "\uff1a\u95ed\u73af\u505c\u6b62\u65b9\u6cd5\u4ec5\u5e94\u4e0e\u80fd\u591f\u5728\u505c\u6b62\u9608\u503c\u4ee5\u4e0b\u7ef4\u6301\u901f\u5ea6\u4f30\u8ba1\u7684\u4f30\u8ba1\u5668\u4e00\u8d77\u4f7f\u7528\u3002\uff08ZS/MT \u548c QEI \u662f\u5408\u9002\u7684\u4f8b\u5b50\u3002AN1292 PLL \u53ef\u80fd\u80fd\u591f\u7ef4\u6301\u901f\u5ea6\u4f30\u8ba1\uff0c\u4f46\u5e94\u4ed4\u7ec6\u68c0\u67e5\u95ed\u73af\u505c\u6b62\u7684\u4f7f\u7528\u3002\u5df2\u77e5 ATPLL \u5728\u6781\u4f4e\u901f\u8fd0\u884c\u65f6\u5b58\u5728\u7a33\u5b9a\u6027\u95ee\u9898\u3002\uff09",
    "Under closed-loop current stopping, the motor current is commanded to zero. This allows the motor to coast down towards rest with similar dynamics as in the minimal-impact PWM case.":
        "\u5728\u95ed\u73af\u7535\u6d41\u505c\u6b62\u4e0b\uff0c\u7535\u673a\u7535\u6d41\u88ab\u6307\u4ee4\u4e3a\u96f6\u3002\u8fd9\u5141\u8bb8\u7535\u673a\u4ee5\u4e0e\u6700\u5c0f\u5f71\u54cd PWM \u60c5\u51b5\u7c7b\u4f3c\u7684\u52a8\u6001\u81ea\u7531\u505c\u8f6c\u81f3\u9759\u6b62\u3002",
    "Under closed-loop velocity stopping, the outer loop is commanded to zero velocity. This will bring the motor to rest very quickly, but also regenerates energy back onto the DC link.":
        "\u5728\u95ed\u73af\u901f\u5ea6\u505c\u6b62\u4e0b\uff0c\u5916\u73af\u88ab\u6307\u4ee4\u4e3a\u96f6\u901f\u5ea6\u3002\u8fd9\u5c06\u4f7f\u7535\u673a\u975e\u5e38\u5feb\u5730\u505c\u6b62\uff0c\u4f46\u4e5f\u4f1a\u5c06\u80fd\u91cf\u518d\u751f\u56de\u5230\u76f4\u6d41\u6bcd\u7ebf\u4e0a\u3002",
    ": Closed-loop velocity control should only be when there is a reliable path for the regenerated energy to flow \u2014 for example, a shunt voltage regulator or a battery connected to the DC link.":
        "\uff1a\u95ed\u73af\u901f\u5ea6\u63a7\u5236\u4ec5\u5728\u6709\u53ef\u9760\u7684\u518d\u751f\u80fd\u91cf\u6d41\u52a8\u8def\u5f84\u65f6\u624d\u5e94\u4f7f\u7528 \u2014 \u4f8b\u5982\uff0c\u7535\u963b\u7535\u538b\u8c03\u8282\u5668\u6216\u8fde\u63a5\u5230\u76f4\u6d41\u6bcd\u7ebf\u7684\u7535\u6c60\u3002",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "Support for closed-loop methods was added in MCAF R7.": "\u95ed\u73af\u65b9\u6cd5\u7684\u652f\u6301\u5728 MCAF R7 \u4e2d\u6dfb\u52a0\u3002",
    "5.3. Stopping": "5.3. \u505c\u6b62",
    "5.3.1. Overview": "5.3.1. \u6982\u8ff0",
    "5.3.2. Minimal-impact PWM": "5.3.2. \u6700\u5c0f\u5f71\u54cd PWM",
    "5.3.3. Closed-loop methods": "5.3.3. \u95ed\u73af\u65b9\u6cd5",
    "5.3.3.1. Closed-loop current": "5.3.3.1. \u95ed\u73af\u7535\u6d41",
    "5.3.3.2. Closed-loop velocity": "5.3.3.2. \u95ed\u73af\u901f\u5ea6",
    "5.3.4. Implementation notes": "5.3.4. \u5b9e\u73b0\u8bf4\u660e",
    "Startup": "\u542f\u52a8",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
