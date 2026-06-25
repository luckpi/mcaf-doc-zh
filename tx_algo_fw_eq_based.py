# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/flux_control/fw_types/fw_eq_based"
title_zh = "5.5.1.3.1. \u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Flux control": "\u78c1\u94fe\u63a7\u5236",
    "Flux weakening": "\u5f31\u78c1\u63a7\u5236",
    "Equation based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "\u516c\u5f0f based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "Overview": "\u6982\u8ff0",
    "The flux-weakening (FW) module is required to calculate a suitable d-axis current reference":
        "\u5f31\u78c1\uff08FW\uff09\u6a21\u5757\u9700\u8981\u8ba1\u7b97\u9002\u5f53\u7684 d \u8f74\u7535\u6d41\u53c2\u8003",
    "so as to operate the motor at a velocity higher than the rated velocity without increasing the motor voltage. An equation-based algorithm is implemented for flux-weakening. This algorithm is based on an open-loop approach of calculating the current reference for FW operation (":
        "\uff0c\u4ee5\u4f7f\u7535\u673a\u5728\u4e0d\u589e\u52a0\u7535\u673a\u7535\u538b\u7684\u60c5\u51b5\u4e0b\u4ee5\u9ad8\u4e8e\u989d\u5b9a\u901f\u5ea6\u7684\u901f\u5ea6\u8fd0\u884c\u3002\u5b9e\u73b0\u4e86\u4e00\u79cd\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u7b97\u6cd5\u3002\u8be5\u7b97\u6cd5\u57fa\u4e8e\u5f00\u73af\u65b9\u6cd5\u8ba1\u7b97 FW \u8fd0\u884c\u7684\u7535\u6d41\u53c2\u8003\uff08",
    ") using the motor voltage equations. Depending on the application requirements, the user can enable or disable flux-weakening.":
        "\uff09\uff0c\u4f7f\u7528\u7535\u673a\u7535\u538b\u65b9\u7a0b\u3002\u6839\u636e\u5e94\u7528\u9700\u6c42\uff0c\u7528\u6237\u53ef\u4ee5\u542f\u7528\u6216\u7981\u7528\u5f31\u78c1\u3002",
    "Flow chart and description": "\u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "shows the flow chart of the flux-weakening algorithm.":
        "\u5c55\u793a\u4e86\u5f31\u78c1\u7b97\u6cd5\u7684\u6d41\u7a0b\u56fe\u3002",
    "Flux-weakening algorithm flow chart": "\u5f31\u78c1\u7b97\u6cd5\u6d41\u7a0b\u56fe",
    "The equation-based FW algorithm performs two important tasks. First, it checks if there is a need for injecting a negative":
        "\u57fa\u4e8e\u65b9\u7a0b\u7684 FW \u7b97\u6cd5\u6267\u884c\u4e24\u4e2a\u91cd\u8981\u4efb\u52a1\u3002\u9996\u5148\uff0c\u5b83\u68c0\u67e5\u662f\u5426\u9700\u8981\u6ce8\u5165\u8d1f\u7684",
    "in the motor. This is done by considering the q-axis voltage equation of the motor in the steady state given by":
        "\u3002\u8fd9\u662f\u901a\u8fc7\u8003\u8651\u7535\u673a\u5728\u7a33\u6001\u4e0b\u7684 q \u8f74\u7535\u538b\u65b9\u7a0b\uff08\u7531",
    ". If the available q-axis voltage (": "\u7ed9\u51fa\uff09\u6765\u5b8c\u6210\u7684\u3002\u5982\u679c\u53ef\u7528\u7684 q \u8f74\u7535\u538b\uff08",
    ") is enough to overcome the addition of": "\uff09\u8db3\u4ee5\u514b\u670d",
    ", there is no need for FW and": "\u7684\u52a0\u548c\uff0c\u5219\u4e0d\u9700\u8981\u5f31\u78c1\uff0c",
    "is made equal to zero. Here,": "\u88ab\u8bbe\u4e3a\u96f6\u3002\u8fd9\u91cc\uff0c",
    "is the back emf magnitude.": "\u4e3a\u53cd\u7535\u52a8\u52bf\u5e45\u503c\u3002",
    "The available q-axis voltage (": "\u53ef\u7528\u7684 q \u8f74\u7535\u538b\uff08",
    ") is calculated by taking the d-axis stator voltage (": "\uff09\u662f\u901a\u8fc7\u53d6 d \u8f74\u5b9a\u5b50\u7535\u538b\uff08",
    ") as an input and performing the following calculation. Here,": "\uff09\u4f5c\u4e3a\u8f93\u5165\u5e76\u6267\u884c\u4ee5\u4e0b\u8ba1\u7b97\u5f97\u51fa\u7684\u3002\u8fd9\u91cc\uff0c",
    "is the maximum possible voltage that can be safely applied to the motor. This is calculated based on the value of DC link voltage":
        "\u662f\u53ef\u4ee5\u5b89\u5168\u65bd\u52a0\u5230\u7535\u673a\u7684\u6700\u5927\u53ef\u80fd\u7535\u538b\u3002\u8fd9\u662f\u57fa\u4e8e\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b",
    "and a voltage limit multiplier": "\u548c\u7535\u538b\u9650\u5236\u4e58\u6570",
    "as mentioned in": "\u7684\u503c\u8ba1\u7b97\u7684\uff0c\u5982",
    "Parameter Customization": "\u53c2\u6570\u81ea\u5b9a\u4e49",
    "The terms on the right hand side of": "\u53f3\u4fa7\u7684\u9879",
    "are calculated by adding": "\u662f\u901a\u8fc7\u5c06",
    "to": "\u52a0\u5230",
    ". The difference between": "\u6765\u8ba1\u7b97\u7684\u3002\u7136\u540e\u8ba1\u7b97",
    "and (": "\u4e0e\uff08",
    ") is then calculated. If this difference is positive, it means that there is sufficient q-axis voltage available to operate at that velocity and load. In this case,":
        "\uff09\u4e4b\u95f4\u7684\u5dee\u3002\u5982\u679c\u8be5\u5dee\u4e3a\u6b63\uff0c\u8868\u793a\u6709\u8db3\u591f\u7684 q \u8f74\u7535\u538b\u53ef\u7528\u4e8e\u5728\u8be5\u901f\u5ea6\u548c\u8d1f\u8f7d\u4e0b\u8fd0\u884c\u3002\u5728\u6b64\u60c5\u51b5\u4e0b\uff0c",
    "is made equal to zero.": "\u88ab\u8bbe\u4e3a\u96f6\u3002",
    "If this difference comes out to be negative, there is a need for flux-weakening and the algorithm then proceeds to calculate the reference current":
        "\u5982\u679c\u8be5\u5dee\u4e3a\u8d1f\uff0c\u5219\u9700\u8981\u5f31\u78c1\uff0c\u7b97\u6cd5\u968f\u540e\u8ba1\u7b97\u53c2\u8003\u7535\u6d41",
    ". As seen from": "\u3002\u5982",
    ", the calculated difference should match the term": "\u6240\u793a\uff0c\u8ba1\u7b97\u5f97\u5230\u7684\u5dee\u5e94\u5339\u914d\u9879",
    "so as to satisfy this equation. This difference term is divided by":
        "\u4ee5\u6ee1\u8db3\u6b64\u65b9\u7a0b\u3002\u6b64\u5dee\u503c\u9879\u9664\u4ee5",
    "to find": "\u4ee5\u6c42\u5f97",
    ". After calculation,": "\u3002\u8ba1\u7b97\u540e\uff0c",
    "is an input to the": "\u4f5c\u4e3a",
    "D-axis current reference generation": "D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
    "module, where it is used for": "\u6a21\u5757\u7684\u8f93\u5165\uff0c\u7528\u4e8e",
    "generation.": "\u751f\u6210\u3002",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "Added in R6.": "\u5728 R6 \u4e2d\u6dfb\u52a0\u3002",
    "Following are some important points related to equation-based FW implementation.":
        "\u4ee5\u4e0b\u662f\u4e0e\u57fa\u4e8e\u65b9\u7a0b\u7684 FW \u5b9e\u73b0\u76f8\u5173\u7684\u4e00\u4e9b\u91cd\u8981\u70b9\u3002",
    "Filter on": "\u6ee4\u6ce2",
    ": After calculation, the back emf magnitude": "\uff1a\u8ba1\u7b97\u540e\uff0c\u53cd\u7535\u52a8\u52bf\u5e45\u503c",
    "is passed through a low-pass filter to smooth it out. This filtered value is then used for the calculation of":
        "\u901a\u8fc7\u4f4e\u901a\u6ee4\u6ce2\u5668\u4ee5\u5e73\u6ed1\u3002\u6b64\u6ee4\u6ce2\u540e\u7684\u503c\u968f\u540e\u7528\u4e8e\u8ba1\u7b97",
    "Voltage limit: The maximum voltage magnitude (": "\u7535\u538b\u9650\u5236\uff1a\u6700\u5927\u7535\u538b\u5e45\u503c\uff08",
    ") is the limit on the magnitude of voltage. This is also equal to the voltage that is applied to the motor in the flux-weakening region of operation. It is calculated from the DC link voltage magnitude and the voltage limit parameter (":
        "\uff09\u662f\u7535\u538b\u5e45\u503c\u7684\u9650\u5236\u3002\u8fd9\u4e5f\u7b49\u4e8e\u5728\u5f31\u78c1\u8fd0\u884c\u533a\u57df\u65bd\u52a0\u5230\u7535\u673a\u7684\u7535\u538b\u3002\u5b83\u7531\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\u5e45\u503c\u548c\u7535\u538b\u9650\u5236\u53c2\u6570\uff08",
    "). The calculation is based on the following equation. The": "\uff09\u8ba1\u7b97\u5f97\u51fa\u3002\u8ba1\u7b97\u57fa\u4e8e\u4ee5\u4e0b\u65b9\u7a0b\u3002\u5206\u6bcd\u4e2d\u7684",
    "in the denominator appears due to the conversion from the line-line voltage to the line-neutral voltage.":
        "\u662f\u7531\u4e8e\u4ece\u7ebf\u7535\u538b\u5230\u76f8\u7535\u538b\u7684\u8f6c\u6362\u3002",
    "Factors affecting flux-weakening operation": "\u5f71\u54cd\u5f31\u78c1\u8fd0\u884c\u7684\u56e0\u7d20",
    "Effect of": "\u7684\u5f71\u54cd",
    ": The value of": "\uff1a",
    "plays an essential role in the FW operation. It affects the calculated value of the available q-axis voltage (":
        "\u7684\u503c\u5728 FW \u8fd0\u884c\u4e2d\u8d77\u7740\u5173\u952e\u4f5c\u7528\u3002\u5b83\u5f71\u54cd\u53ef\u7528 q \u8f74\u7535\u538b\uff08",
    "), which in turn affects the velocity at which the motor makes a transition to the FW region of operation. It should be noted that this value is calculated based on the DC link voltage (":
        "\uff09\u7684\u8ba1\u7b97\u503c\uff0c\u8fdb\u800c\u5f71\u54cd\u7535\u673a\u8fc7\u6e21\u5230 FW \u8fd0\u884c\u533a\u57df\u7684\u901f\u5ea6\u3002\u5e94\u6ce8\u610f\u6b64\u503c\u662f\u57fa\u4e8e\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\uff08",
    ") and voltage limit parameter (": "\uff09\u548c\u7535\u538b\u9650\u5236\u53c2\u6570\uff08",
    "). The maximum value of": "\uff09\u8ba1\u7b97\u7684\u3002",
    "is 1.": "\u7684\u6700\u5927\u503c\u4e3a 1\u3002",
    "A simplified set of equations is given below to understand the relation between the value of":
        "\u4e0b\u9762\u7ed9\u51fa\u4e86\u4e00\u7ec4\u7b80\u5316\u65b9\u7a0b\uff0c\u4ee5\u7406\u89e3",
    "and the velocity at which a transition is made to the FW region.":
        "\u7684\u503c\u4e0e\u8fc7\u6e21\u5230 FW \u533a\u57df\u7684\u901f\u5ea6\u4e4b\u95f4\u7684\u5173\u7cfb\u3002",
    "gives steady-state motor voltage equations along with the calculation of the available q-axis voltage (":
        "\u7ed9\u51fa\u4e86\u7a33\u6001\u7535\u673a\u7535\u538b\u65b9\u7a0b\u4ee5\u53ca\u53ef\u7528 q \u8f74\u7535\u538b\uff08",
    ").": "\uff09\u7684\u8ba1\u7b97\u3002",
    "As the motor velocity (considered to be positive here) increases, magnitude of":
        "\u968f\u7740\u7535\u673a\u901f\u5ea6\uff08\u6b64\u5904\u5047\u8bbe\u4e3a\u6b63\uff09\u7684\u589e\u52a0\uff0c",
    "increases and as a result, the magnitude of": "\u7684\u5e45\u503c\u589e\u52a0\uff0c\u56e0\u6b64",
    "reduces. Due to this, the initially positive term": "\u7684\u5e45\u503c\u51cf\u5c0f\u3002\u7531\u6b64\uff0c\u521d\u59cb\u4e3a\u6b63\u7684\u9879",
    "as calculated from": "\uff08\u7531",
    "equation reduces in magnitude. At the boundary of transition to the FW region, this term becomes zero. If the stator resistance term (":
        "\u65b9\u7a0b\u8ba1\u7b97\uff09\u7684\u5e45\u503c\u51cf\u5c0f\u3002\u5728\u8fc7\u6e21\u5230 FW \u533a\u57df\u7684\u8fb9\u754c\u5904\uff0c\u6b64\u9879\u53d8\u4e3a\u96f6\u3002\u5982\u679c\u5b9a\u5b50\u7535\u963b\u9879\uff08",
    ") is neglected for simplification, the velocity at which the transition happens to the FW region (":
        "\uff09\u4e3a\u7b80\u5316\u800c\u5ffd\u7565\uff0c\u5219\u8fc7\u6e21\u5230 FW \u533a\u57df\u7684\u901f\u5ea6\uff08",
    ") can be given by": "\uff09\u53ef\u7531",
    ". Thus, as": "\u7ed9\u51fa\u3002\u56e0\u6b64\uff0c\u968f\u7740",
    "increases,": "\u7684\u589e\u52a0\uff0c",
    "increases.": "\u4e5f\u589e\u52a0\u3002",
    "For a given": "\u5bf9\u4e8e\u7ed9\u5b9a\u7684",
    ", if the DC link voltage is higher,": "\uff0c\u5982\u679c\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\u66f4\u9ad8\uff0c",
    "will also increase in proportion (": "\u4e5f\u5c06\u6309\u6bd4\u4f8b\u589e\u52a0\uff08",
    "). This will result in the motor making a transition to the FW region at a higher velocity. Likewise, reduction in the value of DC link voltage or the value of":
        "\uff09\u3002\u8fd9\u5c06\u5bfc\u81f4\u7535\u673a\u5728\u66f4\u9ad8\u7684\u901f\u5ea6\u4e0b\u8fc7\u6e21\u5230 FW \u533a\u57df\u3002\u540c\u6837\uff0c\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\u6216",
    "will cause the transition to the FW region to happen at a lower velocity.":
        "\u7684\u503c\u7684\u51cf\u5c0f\u5c06\u5bfc\u81f4\u8fc7\u6e21\u5230 FW \u533a\u57df\u53d1\u751f\u5728\u66f4\u4f4e\u7684\u901f\u5ea6\u3002",
    "Velocity extension in FW region: The limit on velocity extension in the FW region depends on factors such as motor\u2019s rated current, inductance and back emf constant.":
        "FW \u533a\u57df\u7684\u901f\u5ea6\u6269\u5c55\uff1aFW \u533a\u57df\u4e2d\u901f\u5ea6\u6269\u5c55\u7684\u9650\u5236\u53d6\u51b3\u4e8e\u7535\u673a\u7684\u989d\u5b9a\u7535\u6d41\u3001\u7535\u611f\u548c\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u7b49\u56e0\u7d20\u3002",
    "shows the relation between the approximate gain in velocity as a function of motor maximum current":
        "\u5c55\u793a\u4e86\u901f\u5ea6\u7684\u8fd1\u4f3c\u589e\u76ca\u4f5c\u4e3a\u7535\u673a\u6700\u5927\u7535\u6d41",
    "and": "\u548c",
    ". For motors with larger inductance and larger rated current, the velocity extension in FW region is more, while for motors with lower back emf constant, the extension in the FW region is found to be more.":
        "\u7684\u51fd\u6570\u7684\u5173\u7cfb\u3002\u5bf9\u4e8e\u7535\u611f\u66f4\u5927\u548c\u989d\u5b9a\u7535\u6d41\u66f4\u5927\u7684\u7535\u673a\uff0cFW \u533a\u57df\u7684\u901f\u5ea6\u6269\u5c55\u66f4\u5927\uff1b\u800c\u5bf9\u4e8e\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u66f4\u4f4e\u7684\u7535\u673a\uff0cFW \u533a\u57df\u7684\u6269\u5c55\u4e5f\u66f4\u5927\u3002",
    "shows the torque-velocity capability curves for a non-salient motor. The per unit motor parameters are indicated at the top of the figure. The outermost dashed red curve shows the maximum possible torque as a function of velocity. The solid red curves are constant-current plots and the solid black plots are constant-voltage plots. The region shaded light blue is without any FW, while the region shaded pink is the FW region. The shaded curve":
        "\u5c55\u793a\u4e86\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\u3002\u6807\u4e49\u503c\u7535\u673a\u53c2\u6570\u6807\u6ce8\u5728\u56fe\u7684\u9876\u90e8\u3002\u6700\u5916\u5c42\u7684\u865a\u7ebf\u7ea2\u66f2\u7ebf\u8868\u793a\u4f5c\u4e3a\u901f\u5ea6\u51fd\u6570\u7684\u6700\u5927\u53ef\u80fd\u8f6c\u77e9\u3002\u5b9e\u7ebf\u7ea2\u66f2\u7ebf\u4e3a\u6052\u5b9a\u7535\u6d41\u66f2\u7ebf\uff0c\u5b9e\u7ebf\u9ed1\u66f2\u7ebf\u4e3a\u6052\u5b9a\u7535\u538b\u66f2\u7ebf\u3002\u6d45\u84dd\u8272\u9634\u5f71\u533a\u57df\u4e3a\u65e0\u5f31\u78c1\u533a\u57df\uff0c\u7c89\u7ea2\u8272\u9633\u5f71\u533a\u57df\u4e3a\u5f31\u78c1\u533a\u57df\u3002\u9634\u5f71\u66f2\u7ebf",
    "shows the boundary between FW and no-FW regions, while the shaded curve":
        "\u8868\u793a\u5f31\u78c1\u4e0e\u65e0\u5f31\u78c1\u533a\u57df\u4e4b\u95f4\u7684\u8fb9\u754c\uff0c\u9633\u5f71\u66f2\u7ebf",
    "shows the limiting boundary of the FW region. Point B and point C show the velocity at no-load condition in the FW motoring and FW generating regions, respectively. These values are the theoretical maximum achievable velocity values in absence of Coulomb friction and viscous drag. In":
        "\u8868\u793a\u5f31\u78c1\u533a\u57df\u7684\u6781\u9650\u8fb9\u754c\u3002\u70b9 B \u548c\u70b9 C \u5206\u522b\u8868\u793a\u65e0\u8d1f\u8f7d\u6761\u4ef6\u4e0b FW \u7535\u52a8\u548c FW \u53d1\u7535\u533a\u57df\u7684\u901f\u5ea6\u3002\u8fd9\u4e9b\u503c\u662f\u5728\u65e0\u5e93\u4ed1\u6469\u64e6\u548c\u9ecf\u6027\u963b\u529b\u60c5\u51b5\u4e0b\u7684\u7406\u8bba\u6700\u5927\u53ef\u8fbe\u901f\u5ea6\u503c\u3002\u5728",
    ", the maximum velocity in motoring region is around 1.28 per unit.":
        "\u4e2d\uff0c\u7535\u52a8\u533a\u57df\u7684\u6700\u5927\u901f\u5ea6\u7ea6\u4e3a 1.28 \u6807\u4e49\u503c\u3002",
    "shows the torque-velocity capability curves for the same motor, however with a 50% increase in motor inductance values. It can be seen that the velocity limit in the FW motoring region is increased and is around 1.5 per unit.":
        "\u5c55\u793a\u4e86\u540c\u4e00\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff0c\u4f46\u7535\u673a\u7535\u611f\u503c\u589e\u52a0\u4e86 50%\u3002\u53ef\u4ee5\u770b\u51fa\uff0cFW \u7535\u52a8\u533a\u57df\u7684\u901f\u5ea6\u9650\u5236\u589e\u52a0\u4e86\uff0c\u7ea6\u4e3a 1.5 \u6807\u4e49\u503c\u3002",
    "shows the torque-velocity capability curves for the same motor with original inductance values, however with a 50% increase in motor current rating. The velocity limit in the FW motoring region is around 1.48 per unit and is larger as compared to the value of 1.28 per unit in":
        "\u5c55\u793a\u4e86\u540c\u4e00\u7535\u673a\u5728\u539f\u59cb\u7535\u611f\u503c\u4e0b\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff0c\u4f46\u7535\u673a\u7535\u6d41\u989d\u5b9a\u589e\u52a0\u4e86 50%\u3002FW \u7535\u52a8\u533a\u57df\u7684\u901f\u5ea6\u9650\u5236\u7ea6\u4e3a 1.48 \u6807\u4e49\u503c\uff0c\u5927\u4e8e",
    "shows the torque-velocity capability curves for the same motor with original inductance values and motor current rating, however with a back emf constant reduced to 75% of its original value. The velocity limit in the FW motoring region is around 1.4 per unit and is larger as compared to the value of 1.28 per unit in":
        "\u5c55\u793a\u4e86\u540c\u4e00\u7535\u673a\u5728\u539f\u59cb\u7535\u611f\u503c\u548c\u7535\u673a\u7535\u6d41\u989d\u5b9a\u4e0b\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff0c\u4f46\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u51cf\u5c0f\u5230\u539f\u59cb\u503c\u7684 75%\u3002FW \u7535\u52a8\u533a\u57df\u7684\u901f\u5ea6\u9650\u5236\u7ea6\u4e3a 1.4 \u6807\u4e49\u503c\uff0c\u5927\u4e8e",
    "Torque-velocity capability curves for a non-salient motor": "\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf",
    "Torque-velocity capability curves for a non-salient motor, with higher inductance":
        "\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff08\u66f4\u9ad8\u7535\u611f\uff09",
    "Torque-velocity capability curves for a non-salient motor, with higher current rating":
        "\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff08\u66f4\u9ad8\u7535\u6d41\u989d\u5b9a\uff09",
    "Torque-velocity capability curves for a non-salient motor, with lower back emf constant":
        "\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u80fd\u529b\u66f2\u7ebf\uff08\u66f4\u4f4e\u53cd\u7535\u52a8\u52bf\u5e38\u6570\uff09",
    "5.5.1.3.1. Equation based flux-weakening": "5.5.1.3.1. \u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "5.5.1.3.1. \u516c\u5f0f based flux-weakening": "5.5.1.3.1. \u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "5.5.1.3.1.1. Overview": "5.5.1.3.1.1. \u6982\u8ff0",
    "5.5.1.3.1.2. Flow chart and description": "5.5.1.3.1.2. \u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "5.5.1.3.1.3. Implementation notes": "5.5.1.3.1.3. \u5b9e\u73b0\u8bf4\u660e",
    "5.5.1.3.1.4. Factors affecting flux-weakening operation": "5.5.1.3.1.4. \u5f71\u54cd\u5f31\u78c1\u8fd0\u884c\u7684\u56e0\u7d20",
    "Flux weakening": "\u5f31\u78c1\u63a7\u5236",
    "Maximum Torque Per Ampere (MTPA)": "\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
