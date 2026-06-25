# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/startup"
title_zh = "5.2. \u542f\u52a8"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Startup": "\u542f\u52a8",
    "Overview": "\u6982\u8ff0",
    "MCAF includes two different startup methods. Both methods are compatible with sensorless estimators that have a minimum operating speed. Each will operate in closed-loop current control with a forced commutation angle, to bring the motor from a stop to a transition speed where the motor can switch to closed-loop commutation. The only difference between the two methods is how they handle this transition.":
        "MCAF \u5305\u542b\u4e24\u79cd\u4e0d\u540c\u7684\u542f\u52a8\u65b9\u6cd5\u3002\u8fd9\u4e24\u79cd\u65b9\u6cd5\u5747\u517c\u5bb9\u5177\u6709\u6700\u4f4e\u8fd0\u884c\u901f\u5ea6\u7684\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u3002\u6bcf\u79cd\u65b9\u6cd5\u90fd\u5728\u95ed\u73af\u7535\u6d41\u63a7\u5236\u4e0b\u4ee5\u5f3a\u5236\u6362\u76f8\u89d2\u5ea6\u8fd0\u884c\uff0c\u5c06\u7535\u673a\u4ece\u505c\u6b62\u72b6\u6001\u5e26\u5230\u53ef\u5207\u6362\u81f3\u95ed\u73af\u6362\u76f8\u7684\u8fc7\u6e21\u901f\u5ea6\u3002\u4e24\u79cd\u65b9\u6cd5\u4e4b\u95f4\u7684\u552f\u4e00\u533a\u522b\u5728\u4e8e\u5b83\u4eec\u5982\u4f55\u5904\u7406\u8fd9\u4e00\u8fc7\u6e21\u3002",
    "Method 1: Classic (current decay)": "\u65b9\u6cd51\uff1a\u7ecf\u5178\u65b9\u6cd5\uff08\u7535\u6d41\u8870\u51cf\uff09",
    "The \u201cWeathervane\u201d method was introduced in MCAF R4. This method transitions by simultaneously rotating both the current vector and the reference frame angle, until the sensorless estimator\u2019s angle estimate approaches the forced commutation angle.":
        "\u201c\u98ce\u5411\u6807\u201d\u65b9\u6cd5\u5728 MCAF R4 \u4e2d\u5f15\u5165\u3002\u8be5\u65b9\u6cd5\u901a\u8fc7\u540c\u65f6\u65cb\u8f6c\u7535\u6d41\u77e2\u91cf\u548c\u53c2\u8003\u5750\u6807\u7cfb\u89d2\u5ea6\u6765\u8fdb\u884c\u8fc7\u6e21\uff0c\u76f4\u5230\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u7684\u89d2\u5ea6\u4f30\u8ba1\u63a5\u8fd1\u5f3a\u5236\u6362\u76f8\u89d2\u5ea6\u3002",
    "Method 2: Weathervane (reference frame alignment)": "\u65b9\u6cd52\uff1a\u98ce\u5411\u6807\uff08\u53c2\u8003\u5750\u6807\u7cfb\u5bf9\u9f50\uff09",
    "Method 3: ZS/MT + initial position correction": "\u65b9\u6cd53\uff1aZS/MT + \u521d\u59cb\u4f4d\u7f6e\u6821\u6b63",
    "If": "\u5982\u679c",
    "Zero-Speed / Maximum Torque (ZS/MT)": "\u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
    "is used as a primary estimator, a specialized startup algorithm is required.": "\u88ab\u7528\u4f5c\u4e3b\u4f30\u8ba1\u5668\uff0c\u5219\u9700\u8981\u4e13\u95e8\u7684\u542f\u52a8\u7b97\u6cd5\u3002",
    "Choice of startup method": "\u542f\u52a8\u65b9\u6cd5\u7684\u9009\u62e9",
    "Startup method can be chosen in the Customize page of motorBench": "\u542f\u52a8\u65b9\u6cd5\u53ef\u5728 motorBench \u7684 Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762",
    "Development Suite. Weathervane provides a faster startup, and is more robust to disturbance torques than the classic method, but it may cause larger torque transients during the transition.":
        "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\u4e2d\u9009\u62e9\u3002\u98ce\u5411\u6807\u65b9\u6cd5\u63d0\u4f9b\u66f4\u5feb\u7684\u542f\u52a8\u901f\u5ea6\uff0c\u4e14\u5bf9\u6270\u52a8\u8f6c\u77e9\u7684\u9c81\u68d2\u6027\u4f18\u4e8e\u7ecf\u5178\u65b9\u6cd5\uff0c\u4f46\u5728\u8fc7\u6e21\u671f\u95f4\u53ef\u80fd\u4ea7\u751f\u8f83\u5927\u7684\u8f6c\u77e9\u77ac\u53d8\u3002",
    "ZS/MT + IPC is required when ZS/MT is used as the primary estimator.": "\u5f53 ZS/MT \u4f5c\u4e3a\u4e3b\u4f30\u8ba1\u5668\u65f6\uff0c\u9700\u8981\u4f7f\u7528 ZS/MT + IPC\u3002",
    "Startup sequence and common elements": "\u542f\u52a8\u5e8f\u5217\u548c\u516c\u5171\u8981\u7d20",
    "Both Classic and Weathervane methods proceed through the following sequence of startup states, and require the motor to be at rest when commencing startup. For most of the startup sequence, velocity control is disabled and closed-loop current control using FOC is enabled, but with a forced commutation angle.":
        "\u7ecf\u5178\u65b9\u6cd5\u548c\u98ce\u5411\u6807\u65b9\u6cd5\u90fd\u7ecf\u8fc7\u4ee5\u4e0b\u542f\u52a8\u72b6\u6001\u5e8f\u5217\uff0c\u5e76\u8981\u6c42\u7535\u673a\u5728\u5f00\u59cb\u542f\u52a8\u65f6\u5904\u4e8e\u9759\u6b62\u72b6\u6001\u3002\u5728\u542f\u52a8\u5e8f\u5217\u7684\u5927\u90e8\u5206\u65f6\u95f4\u91cc\uff0c\u901f\u5ea6\u63a7\u5236\u88ab\u7981\u7528\uff0c\u4f7f\u7528 FOC \u7684\u95ed\u73af\u7535\u6d41\u63a7\u5236\u88ab\u542f\u7528\uff0c\u4f46\u91c7\u7528\u5f3a\u5236\u6362\u76f8\u89d2\u5ea6\u3002",
    "Startup state": "\u542f\u52a8\u72b6\u6001",
    "Current": "\u7535\u6d41",
    "Commutation": "\u6362\u76f8",
    "Notes": "\u8bf4\u660e",
    "Current rampup (": "\u7535\u6d41\u4e0a\u5347\uff08",
    "Linear increase from zero to": "\u4ece\u96f6\u7ebf\u6027\u589e\u52a0\u81f3",
    "Fixed,": "\u56fa\u5b9a\uff0c",
    "Align (": "\u5bf9\u9f50\uff08",
    "QEI back-emf synchronization": "QEI \u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "can keep startup in this state, and can modify current or commutation angle.": "\u53ef\u4f7f\u542f\u52a8\u4fdd\u6301\u5728\u6b64\u72b6\u6001\uff0c\u5e76\u53ef\u4fee\u6539\u7535\u6d41\u6216\u6362\u76f8\u89d2\u5ea6\u3002",
    "Slow acceleration (": "\u6162\u52a0\u901f\uff08",
    "Quadratic (linear velocity ramp) with constant acceleration": "\u6052\u5b9a\u52a0\u901f\u5ea6\u7684\u4e8c\u6b21\uff08\u7ebf\u6027\u901f\u5ea6\u659c\u5761\uff09",
    "Active damping allowed. Cogging torque may be the dominant mechanical load. Proceeds when": "\u5141\u8bb8\u6709\u6e90\u963b\u5c3c\u3002\u9f7f\u69fd\u8f6c\u77e9\u53ef\u80fd\u662f\u4e3b\u8981\u7684\u673a\u68b0\u8d1f\u8f7d\u3002\u5f53\u8fbe\u5230",
    "reached. (See": "\u65f6\u8fdb\u5165\u4e0b\u4e00\u72b6\u6001\u3002\uff08\u53c2\u89c1",
    ".)": "\u3002\uff09",
    "Fast acceleration (": "\u5feb\u52a0\u901f\uff08",
    "Spin (": "\u7a33\u901f\uff08",
    "Linear with constant velocity": "\u6052\u901f\u7ebf\u6027",
    "Active damping allowed. Can be held in this state for": "\u5141\u8bb8\u6709\u6e90\u963b\u5c3c\u3002\u53ef\u5728\u6b64\u72b6\u6001\u4fdd\u6301",
    "Current rampdown (": "\u7535\u6d41\u4e0b\u964d\uff08",
    ") \u2014": "\uff09\u2014",
    "classic method only": "\u4ec5\u7ecf\u5178\u65b9\u6cd5",
    "Exponential decay": "\u6307\u6570\u8870\u51cf",
    "Proceeds when angle deviation drops below a threshold, or current drops below a threshold.": "\u5f53\u89d2\u5ea6\u504f\u5dee\u964d\u81f3\u9608\u503c\u4ee5\u4e0b\u6216\u7535\u6d41\u964d\u81f3\u9608\u503c\u4ee5\u4e0b\u65f6\u8fdb\u5165\u4e0b\u4e00\u72b6\u6001\u3002",
    "Transition (": "\u8fc7\u6e21\uff08",
    "Output of velocity controller": "\u901f\u5ea6\u63a7\u5236\u5668\u8f93\u51fa",
    "Output of estimator plus small offset": "\u4f30\u8ba1\u5668\u8f93\u51fa\u52a0\u5c0f\u504f\u79fb",
    "Velocity controller enabled. Commutation angle from estimator. Offset angle chosen to create smooth transition from previous state. Startup complete when this reaches zero.":
        "\u901f\u5ea6\u63a7\u5236\u5668\u542f\u7528\u3002\u6362\u76f8\u89d2\u5ea6\u6765\u81ea\u4f30\u8ba1\u5668\u3002\u504f\u79fb\u89d2\u5ea6\u7684\u9009\u62e9\u7528\u4e8e\u5b9e\u73b0\u4ece\u524d\u4e00\u72b6\u6001\u7684\u5e73\u6ed1\u8fc7\u6e21\u3002\u5f53\u504f\u79fb\u89d2\u5ea6\u964d\u81f3\u96f6\u65f6\u542f\u52a8\u5b8c\u6210\u3002",
    "Reference frame alignment (": "\u53c2\u8003\u5750\u6807\u7cfb\u5bf9\u9f50\uff08",
    "weathervane method only": "\u4ec5\u98ce\u5411\u6807\u65b9\u6cd5",
    "Current vector rotated toward d-axis to reflect its actual value. Startup complete when angle deviation drops below a threshold.":
        "\u7535\u6d41\u77e2\u91cf\u5411 d \u8f74\u65cb\u8f6c\u4ee5\u53cd\u6620\u5176\u5b9e\u9645\u503c\u3002\u5f53\u89d2\u5ea6\u504f\u5dee\u964d\u81f3\u9608\u503c\u4ee5\u4e0b\u65f6\u542f\u52a8\u5b8c\u6210\u3002",
    "This sequence can also be seen in": "\u8be5\u5e8f\u5217\u4e5f\u53ef\u53c2\u89c1",
    "Graph of current and electrical frequency in startup sequence. (The Weathervane startup algorithm is shown.)":
        "\u542f\u52a8\u5e8f\u5217\u4e2d\u7535\u6d41\u548c\u7535\u6c14\u9891\u7387\u7684\u66f2\u7ebf\u56fe\u3002\uff08\u6240\u793a\u4e3a\u98ce\u5411\u6807\u542f\u52a8\u7b97\u6cd5\u3002\uff09",
    "MCAF R4 and R5 added the ability to adjust various startup parameters in the Customize page of motorBench":
        "MCAF R4 \u548c R5 \u589e\u52a0\u4e86\u5728 motorBench \u7684 Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762\u4e2d\u8c03\u6574\u5404\u79cd\u542f\u52a8\u53c2\u6570\u7684\u529f\u80fd",
    "Development Suite. See": "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\u3002\u53c2\u89c1",
    "Parameter customization": "\u53c2\u6570\u81ea\u5b9a\u4e49",
    "for more information.": "\u4e86\u89e3\u66f4\u591a\u4fe1\u606f\u3002",
    "Startup status codes": "\u542f\u52a8\u72b6\u6001\u7801",
    "To facilitate different startup algorithms which may not share the exact same sequence of states, a common set of status codes has been created. The status code can be read using":
        "\u4e3a\u4fbf\u4e8e\u53ef\u80fd\u4e0d\u5171\u4eab\u5b8c\u5168\u76f8\u540c\u72b6\u6001\u5e8f\u5217\u7684\u4e0d\u540c\u542f\u52a8\u7b97\u6cd5\uff0c\u5df2\u521b\u5efa\u4e86\u4e00\u7ec4\u901a\u7528\u7684\u72b6\u6001\u7801\u3002\u72b6\u6001\u7801\u53ef\u901a\u8fc7",
    "and will be one of the following:": "\u8bfb\u53d6\uff0c\u5176\u503c\u5c06\u4e3a\u4ee5\u4e0b\u4e4b\u4e00\uff1a",
    "\u2014 in an \u201calignment\u201d phase where the motor is being held at constant or slowly-changing electrical angle. The state machine can be held in this state by other algorithms, for example":
        "\u2014\u5904\u4e8e\u201c\u5bf9\u9f50\u201d\u9636\u6bb5\uff0c\u7535\u673a\u88ab\u4fdd\u6301\u5728\u6052\u5b9a\u6216\u7f13\u6162\u53d8\u5316\u7684\u7535\u6c14\u89d2\u5ea6\u3002\u72b6\u6001\u673a\u53ef\u88ab\u5176\u4ed6\u7b97\u6cd5\u4fdd\u6301\u5728\u6b64\u72b6\u6001\uff0c\u4f8b\u5982",
    "back-emf synchronization": "\u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "\u2014 in an \u201cacceleration\u201d phase where the motor is being accelerated.": "\u2014\u5904\u4e8e\u201c\u52a0\u901f\u201d\u9636\u6bb5\uff0c\u7535\u673a\u6b63\u5728\u52a0\u901f\u3002",
    "\u2014 in a \u201cspin\u201d phase where the electrical angle is being updated at constant frequency. The state machine can be held in this state by other algorithms.":
        "\u2014\u5904\u4e8e\u201c\u7a33\u901f\u201d\u9636\u6bb5\uff0c\u7535\u6c14\u89d2\u5ea6\u4ee5\u6052\u5b9a\u9891\u7387\u66f4\u65b0\u3002\u72b6\u6001\u673a\u53ef\u88ab\u5176\u4ed6\u7b97\u6cd5\u4fdd\u6301\u5728\u6b64\u72b6\u6001\u3002",
    "\u2014 startup complete.": "\u2014\u542f\u52a8\u5b8c\u6210\u3002",
    "\u2014 startup in another state besides the above.": "\u2014\u542f\u52a8\u5904\u4e8e\u4e0a\u8ff0\u4ee5\u5916\u7684\u5176\u4ed6\u72b6\u6001\u3002",
    "Phasor analysis": "\u76f8\u91cf\u5206\u6790",
    "shows a typical current vector during open-loop commutation. The magnitude of current": "\u5c55\u793a\u4e86\u5f00\u73af\u6362\u76f8\u671f\u95f4\u5178\u578b\u7684\u7535\u6d41\u77e2\u91cf\u3002\u7535\u6d41\u7684\u5e45\u503c",
    "is chosen to be significantly higher than the required torque-producing current": "\u88ab\u9009\u62e9\u4e3a\u663e\u8457\u9ad8\u4e8e\u6240\u9700\u7684\u4ea7\u751f\u8f6c\u77e9\u7684\u7535\u6d41",
    ", so that the rotor is dragged along and synchronization is maintained. (With this behavior, a PMSM behaves roughly like a stepper motor under microstepping operation.) As a result, most of the current vector is along the d-axis. In MCAF, for the majority of startup, current is applied along the q-axis of the open-loop reference frame, with no d-axis component, and therefore the open-loop reference frame\u2019s q-axis is aligned with the current vector. This means that the angle difference":
        "\uff0c\u4ee5\u4f7f\u8f6c\u5b50\u88ab\u62d6\u52a8\u5e76\u4fdd\u6301\u540c\u6b65\u3002\uff08\u5728\u6b64\u884c\u4e3a\u4e0b\uff0cPMSM \u7684\u8fd0\u884c\u5927\u81f4\u7c7b\u4f3c\u4e8e\u5fae\u6b65\u8fdb\u8fd0\u884c\u65f6\u7684\u6b65\u8fdb\u7535\u673a\u3002\uff09\u56e0\u6b64\uff0c\u5927\u90e8\u5206\u7535\u6d41\u77e2\u91cf\u6cbf d \u8f74\u65b9\u5411\u3002\u5728 MCAF \u4e2d\uff0c\u5728\u542f\u52a8\u7684\u5927\u90e8\u5206\u65f6\u95f4\u91cc\uff0c\u7535\u6d41\u6cbf\u5f00\u73af\u53c2\u8003\u5750\u6807\u7cfb\u7684 q \u8f74\u65bd\u52a0\uff0c\u6ca1\u6709 d \u8f74\u5206\u91cf\uff0c\u56e0\u6b64\u5f00\u73af\u53c2\u8003\u5750\u6807\u7cfb\u7684 q \u8f74\u4e0e\u7535\u6d41\u77e2\u91cf\u5bf9\u9f50\u3002\u8fd9\u610f\u5473\u7740",
    "between the actual q-axis and the q-axis in software, is typically in the 60 \u2013 90\u00b0 range when the mechanical torque load on the motor is relatively low.":
        "\u5b9e\u9645 q \u8f74\u4e0e\u8f6f\u4ef6\u4e2d q \u8f74\u4e4b\u95f4\u7684\u89d2\u5ea6\u5dee\uff0c\u5728\u7535\u673a\u673a\u68b0\u8f6c\u77e9\u8d1f\u8f7d\u76f8\u5bf9\u8f83\u4f4e\u65f6\u901a\u5e38\u5728 60\u201390\u00b0 \u8303\u56f4\u5185\u3002",
    "The two methods work differently to create a relatively smooth transition to closed-loop operation:":
        "\u4e24\u79cd\u65b9\u6cd5\u4ee5\u4e0d\u540c\u65b9\u5f0f\u5b9e\u73b0\u5411\u95ed\u73af\u8fd0\u884c\u7684\u76f8\u5bf9\u5e73\u6ed1\u8fc7\u6e21\uff1a",
    "in the classic method, the magnitude of current is reduced. This has the effect of reducing d-axis current while":
        "\u5728\u7ecf\u5178\u65b9\u6cd5\u4e2d\uff0c\u7535\u6d41\u5e45\u503c\u51cf\u5c0f\u3002\u8fd9\u5c06\u51cf\u5c0f d \u8f74\u7535\u6d41\uff0c\u800c",
    "will remain roughly what is needed to counteract any mechanical torque loads.": "\u5c06\u5927\u81f4\u4fdd\u6301\u4e3a\u62b5\u6d88\u4efb\u4f55\u673a\u68b0\u8f6c\u77e9\u8d1f\u8f7d\u6240\u9700\u7684\u503c\u3002",
    "in the weathervane method, the current vector is rotated so that the open-loop reference frame and actual rotor reference frames converge, with most of the applied current along the d-axis and a small portion of it along the q-axis.":
        "\u5728\u98ce\u5411\u6807\u65b9\u6cd5\u4e2d\uff0c\u7535\u6d41\u77e2\u91cf\u88ab\u65cb\u8f6c\uff0c\u4f7f\u5f00\u73af\u53c2\u8003\u5750\u6807\u7cfb\u4e0e\u5b9e\u9645\u8f6c\u5b50\u53c2\u8003\u5750\u6807\u7cfb\u6536\u655b\uff0c\u5927\u90e8\u5206\u65bd\u52a0\u7684\u7535\u6d41\u6cbf d \u8f74\u65b9\u5411\uff0c\u5c0f\u90e8\u5206\u6cbf q \u8f74\u65b9\u5411\u3002",
    "Current vector during forced commutation": "\u5f3a\u5236\u6362\u76f8\u671f\u95f4\u7684\u7535\u6d41\u77e2\u91cf",
    "\u2014 most of the current is along the d-axis.": "\u2014\u5927\u90e8\u5206\u7535\u6d41\u6cbf d \u8f74\u65b9\u5411\u3002",
    "To illustrate this more clearly, the Hurst DMB0224C10002 (": "\u4e3a\u66f4\u6e05\u695a\u5730\u8bf4\u660e\u8fd9\u4e00\u70b9\uff0c\u4f7f\u7528 Hurst DMB0224C10002\uff08",
    ") was used with an inertia load. Selected program variables were recorded during startup of both methods, with the AN1292 PLL as the estimator.":
        "\uff09\u52a0\u60ef\u6027\u8d1f\u8f7d\u8fdb\u884c\u5b9e\u9a8c\u3002\u5728\u4e24\u79cd\u65b9\u6cd5\u7684\u542f\u52a8\u8fc7\u7a0b\u4e2d\u8bb0\u5f55\u4e86\u9009\u5b9a\u7684\u7a0b\u5e8f\u53d8\u91cf\uff0c\u4ee5 AN1292 PLL \u4f5c\u4e3a\u4f30\u8ba1\u5668\u3002",
    "Classic startup (current decay)": "\u7ecf\u5178\u542f\u52a8\uff08\u7535\u6d41\u8870\u51cf\uff09",
    "In the classic method, current is decreased, as shown in": "\u5728\u7ecf\u5178\u65b9\u6cd5\u4e2d\uff0c\u7535\u6d41\u51cf\u5c0f\uff0c\u5982",
    ". This causes the forced commutation angle to converge towards the angle derived from the estimator, although sometimes this process is slow and requires a very small current.":
        "\u6240\u793a\u3002\u8fd9\u4f7f\u5f3a\u5236\u6362\u76f8\u89d2\u5ea6\u5411\u4ece\u4f30\u8ba1\u5668\u5f97\u5230\u7684\u89d2\u5ea6\u6536\u655b\uff0c\u5c3d\u7ba1\u6709\u65f6\u8be5\u8fc7\u7a0b\u8f83\u6162\u4e14\u9700\u8981\u975e\u5e38\u5c0f\u7684\u7535\u6d41\u3002",
    "Classic startup": "\u7ecf\u5178\u542f\u52a8",
    "The different startup states are highlighted:": "\u4e0d\u540c\u7684\u542f\u52a8\u72b6\u6001\u4ee5\u4e0d\u540c\u989c\u8272\u6807\u51fa\uff1a",
    "Current rampup (1): red": "\u7535\u6d41\u4e0a\u5347\uff081\uff09\uff1a\u7ea2\u8272",
    "Slow acceleration (3): yellow": "\u6162\u52a0\u901f\uff083\uff09\uff1a\u9ec4\u8272",
    "Fast acceleration (4): green": "\u5feb\u52a0\u901f\uff084\uff09\uff1a\u7eff\u8272",
    "Current rampdown (6): purple": "\u7535\u6d41\u4e0b\u964d\uff086\uff09\uff1a\u7d2b\u8272",
    "Transition (7): gray": "\u8fc7\u6e21\uff087\uff09\uff1a\u7070\u8272",
    "(Note that the align (2) and spin (5) states are skipped in this example; these states allow":
        "\uff08\u6ce8\u610f\uff0c\u5728\u6b64\u793a\u4f8b\u4e2d\u8df3\u8fc7\u4e86\u5bf9\u9f50\uff082\uff09\u548c\u7a33\u901f\uff085\uff09\u72b6\u6001\uff1b\u8fd9\u4e9b\u72b6\u6001\u5141\u8bb8",
    "to occur, but if there is no quadrature encoder or the synchronization has already occurred, then the startup sequence proceeds immediately to the next state.)":
        "\u53d1\u751f\uff0c\u4f46\u5982\u679c\u6ca1\u6709\u6b63\u4ea4\u7f16\u7801\u5668\u6216\u540c\u6b65\u5df2\u7ecf\u53d1\u751f\uff0c\u5219\u542f\u52a8\u5e8f\u5217\u7acb\u5373\u8fdb\u5165\u4e0b\u4e00\u72b6\u6001\u3002\uff09",
    "Weathervane startup": "\u98ce\u5411\u6807\u542f\u52a8",
    "In the weathervane method, the current vector is rotated, as shown in": "\u5728\u98ce\u5411\u6807\u65b9\u6cd5\u4e2d\uff0c\u7535\u6d41\u77e2\u91cf\u88ab\u65cb\u8f6c\uff0c\u5982",
    "This method has identical states as in the classic method, except that the reference frame align (state 6, highlighted purple) replaces current rampdown, and there is no transition state at the end of startup.":
        "\u8be5\u65b9\u6cd5\u7684\u72b6\u6001\u4e0e\u7ecf\u5178\u65b9\u6cd5\u76f8\u540c\uff0c\u4e0d\u540c\u4e4b\u5904\u5728\u4e8e\u53c2\u8003\u5750\u6807\u7cfb\u5bf9\u9f50\uff08\u72b6\u60016\uff0c\u4ee5\u7d2b\u8272\u6807\u51fa\uff09\u53d6\u4ee3\u4e86\u7535\u6d41\u4e0b\u964d\uff0c\u4e14\u542f\u52a8\u7ed3\u675f\u65f6\u6ca1\u6709\u8fc7\u6e21\u72b6\u6001\u3002",
    "The reference frame alignment can occur much faster than current rampdown, and does not seem to be affected by the mechanical load of the motor.":
        "\u53c2\u8003\u5750\u6807\u7cfb\u5bf9\u9f50\u53ef\u6bd4\u7535\u6d41\u4e0b\u964d\u5feb\u5f97\u591a\uff0c\u4e14\u4f3c\u4e4e\u4e0d\u53d7\u7535\u673a\u673a\u68b0\u8d1f\u8f7d\u7684\u5f71\u54cd\u3002",
    "ZS/MT + IPC startup": "ZS/MT + IPC \u542f\u52a8",
    "operation requires a different startup technique. This is described as part of": "\u8fd0\u884c\u9700\u8981\u4e0d\u540c\u7684\u542f\u52a8\u6280\u672f\u3002\u8fd9\u4f5c\u4e3a",
    "detailed information on ZS/MT": "ZS/MT \u8be6\u7ec6\u4fe1\u606f",
    "Active damping": "\u6709\u6e90\u963b\u5c3c",
    "When a PMSM is driven with constant current at a forced commutation angle at constant frequency, its dynamics are roughly a very lightly-damped second-order system. There is a virtual \u201cspring\u201d with restoring torque caused by any misalignment between the rotor magnetic field and the applied stator field. This acts with the rotor inertia to oscillate. These oscillations can grow when the motor is driven at an accelerating frequency, or if the current controller\u2019s error causes sufficient phase lag.":
        "\u5f53 PMSM \u4ee5\u6052\u5b9a\u7535\u6d41\u5728\u5f3a\u5236\u6362\u76f8\u89d2\u5ea6\u4e0b\u4ee5\u6052\u5b9a\u9891\u7387\u9a71\u52a8\u65f6\uff0c\u5176\u52a8\u6001\u7279\u6027\u5927\u81f4\u4e3a\u4e00\u4e2a\u963b\u5c3c\u975e\u5e38\u5c0f\u7684\u4e8c\u9636\u7cfb\u3002\u5b58\u5728\u4e00\u4e2a\u865a\u62df\u201c\u5f39\u7c27\u201d\uff0c\u5176\u6062\u590d\u8f6c\u77e9\u7531\u8f6c\u5b50\u78c1\u573a\u4e0e\u65bd\u52a0\u7684\u5b9a\u5b50\u78c1\u573a\u4e4b\u95f4\u7684\u4efb\u4f55\u5931\u914d\u5f15\u8d77\u3002\u8be5\u6062\u590d\u8f6c\u77e9\u4e0e\u8f6c\u5b50\u60ef\u6027\u5171\u540c\u4f5c\u7528\u4ea7\u751f\u632f\u8361\u3002\u5f53\u7535\u673a\u4ee5\u52a0\u901f\u9891\u7387\u9a71\u52a8\u65f6\uff0c\u6216\u5f53\u7535\u6d41\u63a7\u5236\u5668\u7684\u8bef\u5dee\u5bfc\u81f4\u8db3\u591f\u7684\u76f8\u4f4d\u6ede\u540e\u65f6\uff0c\u8fd9\u4e9b\u632f\u8361\u53ef\u80fd\u589e\u5927\u3002",
    "To help control this effect during forced commutation, MCAF contains an \u201cactive damping\u201d feature. This modulates the current during forced commutation, by applying a change in current that is proportional to the difference in speed between the commutation frequency and the velocity obtained by the estimator. Active damping is enabled only above a velocity threshold, since for many sensorless estimators it is not possible to obtain accurate estimates at low velocities. (The velocity threshold to enable active damping can be adjusted in the Customize page of motorBench":
        "\u4e3a\u5e2e\u52a9\u5728\u5f3a\u5236\u6362\u76f8\u671f\u95f4\u63a7\u5236\u6b64\u6548\u5e94\uff0cMCAF \u5305\u542b\u201c\u6709\u6e90\u963b\u5c3c\u201d\u529f\u80fd\u3002\u8be5\u529f\u80fd\u5728\u5f3a\u5236\u6362\u76f8\u671f\u95f4\u8c03\u5236\u7535\u6d41\uff0c\u901a\u8fc7\u65bd\u52a0\u4e0e\u6362\u76f8\u9891\u7387\u548c\u4f30\u8ba1\u5668\u5f97\u5230\u7684\u901f\u5ea6\u4e4b\u95f4\u7684\u5dee\u503c\u6210\u6b63\u6bd4\u7684\u7535\u6d41\u53d8\u5316\u6765\u5b9e\u73b0\u3002\u6709\u6e90\u963b\u5c3c\u4ec5\u5728\u901f\u5ea6\u9ad8\u4e8e\u9608\u503c\u65f6\u542f\u7528\uff0c\u56e0\u4e3a\u5bf9\u4e8e\u8bb8\u591a\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u800c\u8a00\uff0c\u5728\u4f4e\u901f\u65f6\u65e0\u6cd5\u83b7\u5f97\u51c6\u786e\u7684\u4f30\u8ba1\u503c\u3002\uff08\u542f\u7528\u6709\u6e90\u963b\u5c3c\u7684\u901f\u5ea6\u9608\u503c\u53ef\u5728 motorBench \u7684 Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762",
    "Development Suite.) This can be seen in": "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\u4e2d\u8c03\u6574\u3002\uff09\u8fd9\u53ef\u5728",
    "and": "\u548c",
    "during the fast acceleration state (highlighted green).": "\u4e2d\u7684\u5feb\u52a0\u901f\u72b6\u6001\uff08\u4ee5\u7eff\u8272\u6807\u51fa\uff09\u671f\u95f4\u770b\u5230\u3002",
    "Slow and fast acceleration": "\u6162\u52a0\u901f\u548c\u5feb\u52a0\u901f",
    "The acceleration rate during startup is increased once the velocity reaches a certain threshold. At low speeds, acceleration is lower to avoid cycle slips that can be caused by cogging torque. At higher speeds, the cogging torque occurs at a higher frequency, and this torque ripple has less of an effect on rotor dynamics, so that cycle slips are less likely to occur, and it\u2019s possible to increase velocity more quickly. (Most of cogging torque ripple is absorbed by the rotor and load inertia.)":
        "\u542f\u52a8\u671f\u95f4\u7684\u52a0\u901f\u5ea6\u5728\u901f\u5ea6\u8fbe\u5230\u4e00\u5b9a\u9608\u503c\u540e\u4f1a\u589e\u52a0\u3002\u5728\u4f4e\u901f\u65f6\uff0c\u52a0\u901f\u5ea6\u8f83\u4f4e\uff0c\u4ee5\u907f\u514d\u9f7f\u69fd\u8f6c\u77e9\u53ef\u80fd\u5bfc\u81f4\u7684\u5931\u6b65\u3002\u5728\u8f83\u9ad8\u901f\u5ea6\u65f6\uff0c\u9f7f\u69fd\u8f6c\u77e9\u4ee5\u8f83\u9ad8\u7684\u9891\u7387\u51fa\u73b0\uff0c\u8be5\u8f6c\u77e9\u7eb9\u6ce2\u5bf9\u8f6c\u5b50\u52a8\u6001\u7684\u5f71\u54cd\u8f83\u5c0f\uff0c\u56e0\u6b64\u5931\u6b65\u7684\u53ef\u80fd\u6027\u964d\u4f4e\uff0c\u53ef\u4ee5\u66f4\u5feb\u5730\u589e\u52a0\u901f\u5ea6\u3002\uff08\u5927\u90e8\u5206\u9f7f\u69fd\u8f6c\u77e9\u7eb9\u6ce2\u88ab\u8f6c\u5b50\u548c\u8d1f\u8f7d\u60ef\u6027\u5438\u6536\u3002\uff09",
    "5.2. Startup": "5.2. \u542f\u52a8",
    "5.2.1. Overview": "5.2.1. \u6982\u8ff0",
    "5.2.1.1. Method 1: Classic (current decay)": "5.2.1.1. \u65b9\u6cd51\uff1a\u7ecf\u5178\u65b9\u6cd5\uff08\u7535\u6d41\u8870\u51cf\uff09",
    "5.2.1.2. Method 2: Weathervane (reference frame alignment)": "5.2.1.2. \u65b9\u6cd52\uff1a\u98ce\u5411\u6807\uff08\u53c2\u8003\u5750\u6807\u7cfb\u5bf9\u9f50\uff09",
    "5.2.1.3. Method 3: ZS/MT + initial position correction": "5.2.1.3. \u65b9\u6cd53\uff1aZS/MT + \u521d\u59cb\u4f4d\u7f6e\u6821\u6b63",
    "5.2.1.4. Choice of startup method": "5.2.1.4. \u542f\u52a8\u65b9\u6cd5\u7684\u9009\u62e9",
    "5.2.2. Startup sequence and common elements": "5.2.2. \u542f\u52a8\u5e8f\u5217\u548c\u516c\u5171\u8981\u7d20",
    "5.2.2.1. Startup status codes": "5.2.2.1. \u542f\u52a8\u72b6\u6001\u7801",
    "5.2.2.2. Phasor analysis": "5.2.2.2. \u76f8\u91cf\u5206\u6790",
    "5.2.3. Classic startup (current decay)": "5.2.3. \u7ecf\u5178\u542f\u52a8\uff08\u7535\u6d41\u8870\u51cf\uff09",
    "5.2.4. Weathervane startup": "5.2.4. \u98ce\u5411\u6807\u542f\u52a8",
    "5.2.5. ZS/MT + IPC startup": "5.2.5. ZS/MT + IPC \u542f\u52a8",
    "5.2.6. Active damping": "5.2.6. \u6709\u6e90\u963b\u5c3c",
    "5.2.7. Slow and fast acceleration": "5.2.7. \u6162\u52a0\u901f\u548c\u5feb\u52a0\u901f",
    "Comparison between FOC and six-step control": "FOC \u4e0e\u516d\u6b65\u63a7\u5236\u7684\u6bd4\u8f83",
    "Stopping": "\u505c\u6b62",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
