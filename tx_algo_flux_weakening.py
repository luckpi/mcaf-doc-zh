# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/flux_control/flux_weakening"
title_zh = "5.5.1. \u5f31\u78c1\u63a7\u5236"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Flux control": "\u78c1\u94fe\u63a7\u5236",
    "Flux weakening": "\u5f31\u78c1\u63a7\u5236",
    "Motivation": "\u52a8\u673a",
    "Many applications require the motor to be run at a velocity greater than the rated velocity of the motor. In a":
        "\u8bb8\u591a\u5e94\u7528\u9700\u8981\u7535\u673a\u4ee5\u9ad8\u4e8e\u5176\u989d\u5b9a\u901f\u5ea6\u7684\u901f\u5ea6\u8fd0\u884c\u3002\u5728",
    ", the back emf increases in proportion to the rotor velocity. Steady-state stator voltage equations for a typical":
        "\u4e2d\uff0c\u53cd\u7535\u52a8\u52bf\u4e0e\u8f6c\u5b50\u901f\u5ea6\u6210\u6b63\u6bd4\u589e\u52a0\u3002\u5178\u578b\u7684\u7a33\u6001\u5b9a\u5b50\u7535\u538b\u65b9\u7a0b\u5982",
    "are given by": "\u6240\u793a\u3002\u8fd9\u91cc\uff0c",
    "is per-phase stator resistance,": "\u4e3a\u6bcf\u76f8\u5b9a\u5b50\u7535\u963b\uff0c",
    "and": "\u548c",
    "are motor inductance values in the d and the q axes, respectively, while":
        "\u5206\u522b\u4e3a d \u8f74\u548c q \u8f74\u7684\u7535\u673a\u7535\u611f\u503c\uff0c\u800c",
    "are stator voltage components in the d and the q axes, respectively. Back emf":
        "\u5206\u522b\u4e3a d \u8f74\u548c q \u8f74\u7684\u5b9a\u5b50\u7535\u538b\u5206\u91cf\u3002\u53cd\u7535\u52a8\u52bf",
    "lies in the q axis and is given by": "\u4f4d\u4e8e q \u8f74\uff0c\u7531",
    "is the rotor velocity in electrical rad/s and": "\u4e3a\u8f6c\u5b50\u901f\u5ea6\uff08\u5355\u4f4d\u4e3a\u7535\u6c14\u5f27\u5ea6/\u79d2\uff09\uff0c",
    "is the back emf constant in volts per electrical rad/s.":
        "\u4e3a\u53cd\u7535\u52a8\u52bf\u5e38\u6570\uff08\u5355\u4f4d\u4e3a\u4f0f\u7279/\u7535\u6c14\u5f27\u5ea6/\u79d2\uff09\u3002",
    "shows that the q-axis stator voltage will increase as the back emf increases. This is depicted in":
        "\u8868\u660e q \u8f74\u5b9a\u5b50\u7535\u538b\u5c06\u968f\u53cd\u7535\u52a8\u52bf\u7684\u589e\u52a0\u800c\u589e\u52a0\u3002\u5982",
    ". At around the rated motor velocity, the voltage reaches the motor\u2019s rated voltage value and it cannot be increased further. Often, this rated voltage also corresponds to the maximum possible voltage that can be obtained from the inverter due to DC link voltage limitations.":
        "\u6240\u793a\u3002\u5728\u63a5\u8fd1\u7535\u673a\u989d\u5b9a\u901f\u5ea6\u65f6\uff0c\u7535\u538b\u8fbe\u5230\u7535\u673a\u7684\u989d\u5b9a\u7535\u538b\u503c\uff0c\u65e0\u6cd5\u8fdb\u4e00\u6b65\u589e\u52a0\u3002\u901a\u5e38\uff0c\u7531\u4e8e\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\u7684\u9650\u5236\uff0c\u6b64\u989d\u5b9a\u7535\u538b\u4e5f\u5bf9\u5e94\u4e8e\u9006\u53d8\u5668\u80fd\u83b7\u5f97\u7684\u6700\u5927\u53ef\u80fd\u7535\u538b\u3002",
    "PMSM vector diagram:": "PMSM \u77e2\u91cf\u56fe\uff1a",
    "In order to allow a further increase in motor velocity, it is necessary to restrict the increase in":
        "\u4e3a\u4e86\u5141\u8bb8\u7535\u673a\u901f\u5ea6\u8fdb\u4e00\u6b65\u589e\u52a0\uff0c\u5fc5\u987b\u9650\u5236",
    "while allowing": "\u7684\u589e\u52a0\uff0c\u540c\u65f6\u5141\u8bb8",
    "to increase. For a positive velocity, this is achieved by making the":
        "\u589e\u52a0\u3002\u5bf9\u4e8e\u6b63\u901f\u5ea6\uff0c\u8fd9\u662f\u901a\u8fc7\u4f7f",
    "term negative, which in turn is done by making": "\u9879\u4e3a\u8d1f\u6765\u5b9e\u73b0\u7684\uff0c\u8fd9\u53c8\u662f\u901a\u8fc7\u4f7f",
    "negative.": "\u4e3a\u8d1f\u6765\u5b9e\u73b0\u7684\u3002",
    "shows the vector diagram with a negative": "\u5c55\u793a\u4e86\u6ce8\u5165\u8d1f\u7684",
    "injected in the motor. Here,": "\u540e\u7684\u77e2\u91cf\u56fe\u3002\u8fd9\u91cc\uff0c",
    "(dashed black arrow) shows the stator voltage vector with": "\uff08\u865a\u7ebf\u9ed1\u7bad\u5934\uff09\u8868\u793a\u5b9a\u5b50\u7535\u538b\u77e2\u91cf\uff0c\u5176",
    ", whereas": "\uff1b\u800c",
    "(solid black arrow) shows the stator voltage vector with": "\uff08\u5b9e\u7ebf\u9ed1\u7bad\u5934\uff09\u8868\u793a\u5b9a\u5b50\u7535\u538b\u77e2\u91cf\uff0c\u5176",
    ". Due to the opposing effect of the negative": "\u3002\u7531\u4e8e\u8d1f\u7684",
    "term, the magnitude of": "\u9879\u7684\u62b5\u6d88\u4f5c\u7528\uff0c",
    "is lower than the magnitude of": "\u7684\u5e45\u503c\u4f4e\u4e8e",
    ", for the same values of": "\u7684\u5e45\u503c\uff0c\u5728\u76f8\u540c\u7684",
    "Since injecting a negative": "\u503c\u4e0b\u3002\u7531\u4e8e\u6ce8\u5165\u8d1f\u7684",
    "in the motor effectively weakens the air-gap flux, the name flux-weakening (FW) is used. The function of the FW algorithm is the calculation of a suitable reference value for negative":
        "\u4f1a\u6709\u6548\u5730\u524a\u5f31\u6c14\u9699\u78c1\u94fe\uff0c\u56e0\u6b64\u79f0\u4e3a\u5f31\u78c1\uff08FW\uff09\u3002FW \u7b97\u6cd5\u7684\u529f\u80fd\u662f\u8ba1\u7b97\u9002\u5f53\u7684\u8d1f",
    "to operate the motor at a particular velocity and load.":
        "\u53c2\u8003\u503c\uff0c\u4ee5\u4f7f\u7535\u673a\u5728\u7279\u5b9a\u901f\u5ea6\u548c\u8d1f\u8f7d\u4e0b\u8fd0\u884c\u3002",
    "Effect on torque capability": "\u5bf9\u8f6c\u77e9\u80fd\u529b\u7684\u5f71\u54cd",
    "Electromagnetic torque produced in a": "\u5728",
    "with no saliency is given by": "\u4e2d\u4ea7\u751f\u7684\u7535\u78c1\u8f6c\u77e9\uff08\u65e0\u51f8\u6027\uff09\u7531",
    "is the number of poles in the motor. When": "\u4e3a\u7535\u673a\u7684\u6781\u5bf9\u6570\u3002\u5f53",
    "(i.e. no flux-weakening), the q-axis current": "\uff08\u5373\u65e0\u5f31\u78c1\uff09\u65f6\uff0cq \u8f74\u7535\u6d41",
    "is allowed to increase up to the total rated current of the motor. This results in the rated torque output from the motor.":
        "\u5141\u8bb8\u589e\u52a0\u5230\u7535\u673a\u7684\u603b\u989d\u5b9a\u7535\u6d41\u3002\u8fd9\u4f7f\u7535\u673a\u8f93\u51fa\u989d\u5b9a\u8f6c\u77e9\u3002",
    "However, with a negative": "\u7136\u800c\uff0c\u5f53\u5b58\u5728\u8d1f\u7684",
    ", the maximum allowed value of the q-axis current reduces to limit the total current magnitude of the motor as per":
        "\u65f6\uff0cq \u8f74\u7535\u6d41\u7684\u6700\u5927\u5141\u8bb8\u503c\u4f1a\u51cf\u5c0f\uff0c\u4ee5\u6839\u636e",
    "given below. Here,": "\u9650\u5236\u7535\u673a\u7684\u603b\u7535\u6d41\u5e45\u503c\u3002\u8fd9\u91cc\uff0c",
    "is the maximum current amplitude, which is determined by the rated current of the motor or of the drive.":
        "\u4e3a\u6700\u5927\u7535\u6d41\u5e45\u503c\uff0c\u7531\u7535\u673a\u6216\u9a71\u52a8\u5668\u7684\u989d\u5b9a\u7535\u6d41\u51b3\u5b9a\u3002",
    "With the reduction in": "\u968f\u7740",
    ", the torque capability of the motor also reduces. This reduction is more as the motor velocity increases.":
        "\u7684\u51cf\u5c0f\uff0c\u7535\u673a\u7684\u8f6c\u77e9\u80fd\u529b\u4e5f\u4f1a\u964d\u4f4e\u3002\u7535\u673a\u901f\u5ea6\u8d8a\u9ad8\uff0c\u8fd9\u79cd\u964d\u4f4e\u8d8a\u660e\u663e\u3002",
    "shows normalized plots of torque versus velocity for a non-salient motor. The per unit motor parameters are indicated at the top of the figure.":
        "\u5c55\u793a\u4e86\u975e\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9\u4e0e\u901f\u5ea6\u7684\u5f52\u4e00\u5316\u66f2\u7ebf\u3002\u6807\u4e48\u503c\u7535\u673a\u53c2\u6570\u6807\u6ce8\u5728\u56fe\u7684\u9876\u90e8\u3002",
    "is used for calculating the per unit values of motor parameters. Here,":
        "\u7528\u4e8e\u8ba1\u7b97\u7535\u673a\u53c2\u6570\u7684\u6807\u4e49\u503c\u3002\u8fd9\u91cc\uff0c",
    "is the maximum current and": "\u4e3a\u6700\u5927\u7535\u6d41\uff0c",
    "is the nominal back-emf voltage at nominal speed.":
        "\u4e3a\u989d\u5b9a\u901f\u5ea6\u4e0b\u7684\u989d\u5b9a\u53cd\u7535\u52a8\u52bf\u7535\u538b\u3002",
    "The outermost dashed red curve shows the maximum possible torque as a function of velocity. The solid red curves are constant-current plots and the solid black curves are constant-voltage plots. The region shaded light blue is without any FW, while the region shaded pink is the FW region. The dashed curve":
        "\u6700\u5916\u5c42\u7684\u865a\u7ebf\u7ea2\u66f2\u7ebf\u8868\u793a\u4f5c\u4e3a\u901f\u5ea6\u51fd\u6570\u7684\u6700\u5927\u53ef\u80fd\u8f6c\u77e9\u3002\u5b9e\u7ebf\u7ea2\u66f2\u7ebf\u4e3a\u6052\u5b9a\u7535\u6d41\u66f2\u7ebf\uff0c\u5b9e\u7ebf\u9ed1\u66f2\u7ebf\u4e3a\u6052\u5b9a\u7535\u538b\u66f2\u7ebf\u3002\u6d45\u84dd\u8272\u9634\u5f71\u533a\u57df\u4e3a\u65e0\u5f31\u78c1\u533a\u57df\uff0c\u7c89\u7ea2\u8272\u9634\u5f71\u533a\u57df\u4e3a\u5f31\u78c1\u533a\u57df\u3002\u865a\u7ebf",
    "shows the transition between FW and no-FW regions, while the dashed curve":
        "\u8868\u793a\u5f31\u78c1\u4e0e\u65e0\u5f31\u78c1\u533a\u57df\u4e4b\u95f4\u7684\u8fc7\u6e21\uff0c\u865a\u7ebf",
    "shows the limiting boundary of the FW region. It can be seen that the maximum torque value in the FW region is lower than that in the no-FW region, and it reduces as the velocity increases.":
        "\u8868\u793a\u5f31\u78c1\u533a\u57df\u7684\u6781\u9650\u8fb9\u754c\u3002\u53ef\u4ee5\u770b\u51fa\uff0c\u5f31\u78c1\u533a\u57df\u7684\u6700\u5927\u8f6c\u77e9\u503c\u4f4e\u4e8e\u65e0\u5f31\u78c1\u533a\u57df\uff0c\u5e76\u4e14\u968f\u7740\u901f\u5ea6\u7684\u589e\u52a0\u800c\u964d\u4f4e\u3002",
    "Torque-Velocity Plots: Non-salient Motor": "\u8f6c\u77e9-\u901f\u5ea6\u66f2\u7ebf\uff1a\u975e\u51f8\u6027\u7535\u673a",
    "For a salient-pole motor, the torque equation is given by":
        "\u5bf9\u4e8e\u51f8\u6027\u7535\u673a\uff0c\u8f6c\u77e9\u65b9\u7a0b\u7531",
    ". In this equation, there is an additional reluctance torque term which arises due to motor saliency.":
        "\u7ed9\u51fa\u3002\u5728\u6b64\u65b9\u7a0b\u4e2d\uff0c\u6709\u4e00\u4e2a\u7531\u7535\u673a\u51f8\u6027\u4ea7\u751f\u7684\u989d\u5916\u78c1\u963b\u8f6c\u77e9\u9879\u3002",
    "With a negative": "\u5f53\u5b58\u5728\u8d1f\u7684",
    ", even though the reluctance torque term gives a positive value, there is a reduction in the first term due to the reduction in":
        "\u65f6\uff0c\u5c3d\u7ba1\u78c1\u963b\u8f6c\u77e9\u9879\u7ed9\u51fa\u6b63\u503c\uff0c\u4f46\u7531\u4e8e",
    ". The reduction in the first term dominates over the increase in the second term, thereby reducing the overall torque capability of the motor. The torque-velocity plots for a salient-pole motor are similar to those for a non-salient motor.":
        "\u7684\u51cf\u5c0f\uff0c\u7b2c\u4e00\u9879\u4f1a\u51cf\u5c0f\u3002\u7b2c\u4e00\u9879\u7684\u51cf\u5c0f\u4e3b\u5bfc\u7b2c\u4e8c\u9879\u7684\u589e\u52a0\uff0c\u4ece\u800c\u964d\u4f4e\u4e86\u7535\u673a\u7684\u6574\u4f53\u8f6c\u77e9\u80fd\u529b\u3002\u51f8\u6027\u7535\u673a\u7684\u8f6c\u77e9-\u901f\u5ea6\u66f2\u7ebf\u4e0e\u975e\u51f8\u6027\u7535\u673a\u7c7b\u4f3c\u3002",
    "Flux-weakening algorithms": "\u5f31\u78c1\u7b97\u6cd5",
    "The flux-weakening algorithm could be implemented in different ways. Some of these methods use an open-loop approach based on motor equations. Other methods implement a closed-loop approach by adding a controller in the FW algorithm. An equation-based FW algorithm is implemented. This equation-based algorithm is an open-loop algorithm based on motor equations and does not include an additional controller. Details of this algorithm are given in the section below.":
        "\u5f31\u78c1\u7b97\u6cd5\u53ef\u4ee5\u4ee5\u4e0d\u540c\u65b9\u5f0f\u5b9e\u73b0\u3002\u5176\u4e2d\u4e00\u4e9b\u65b9\u6cd5\u4f7f\u7528\u57fa\u4e8e\u7535\u673a\u65b9\u7a0b\u7684\u5f00\u73af\u65b9\u6cd5\u3002\u5176\u4ed6\u65b9\u6cd5\u901a\u8fc7\u5728 FW \u7b97\u6cd5\u4e2d\u6dfb\u52a0\u63a7\u5236\u5668\u6765\u5b9e\u73b0\u95ed\u73af\u65b9\u6cd5\u3002\u672c\u7cfb\u7edf\u5b9e\u73b0\u4e86\u4e00\u79cd\u57fa\u4e8e\u65b9\u7a0b\u7684 FW \u7b97\u6cd5\u3002\u8be5\u57fa\u4e8e\u65b9\u7a0b\u7684\u7b97\u6cd5\u662f\u4e00\u79cd\u57fa\u4e8e\u7535\u673a\u65b9\u7a0b\u7684\u5f00\u73af\u7b97\u6cd5\uff0c\u4e0d\u5305\u542b\u989d\u5916\u7684\u63a7\u5236\u5668\u3002\u8be5\u7b97\u6cd5\u7684\u8be6\u7ec6\u4fe1\u606f\u89c1\u4e0b\u6587\u3002",
    "5.5.1. Flux weakening": "5.5.1. \u5f31\u78c1\u63a7\u5236",
    "5.5.1.1. Motivation": "5.5.1.1. \u52a8\u673a",
    "5.5.1.2. Effect on torque capability": "5.5.1.2. \u5bf9\u8f6c\u77e9\u80fd\u529b\u7684\u5f71\u54cd",
    "5.5.1.3. Flux-weakening algorithms": "5.5.1.3. \u5f31\u78c1\u7b97\u6cd5",
    "Equation based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "\u516c\u5f0f based flux-weakening": "\u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "5.5.1.3.1. Equation based flux-weakening": "5.5.1.3.1. \u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "5.5.1.3.1. \u516c\u5f0f based flux-weakening": "5.5.1.3.1. \u57fa\u4e8e\u65b9\u7a0b\u7684\u5f31\u78c1\u63a7\u5236",
    "5.5.1.3.1.1. Overview": "5.5.1.3.1.1. \u6982\u8ff0",
    "5.5.1.3.1.2. Flow chart and description": "5.5.1.3.1.2. \u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "5.5.1.3.1.3. Implementation notes": "5.5.1.3.1.3. \u5b9e\u73b0\u8bf4\u660e",
    "5.5.1.3.1.4. Factors affecting flux-weakening operation": "5.5.1.3.1.4. \u5f71\u54cd\u5f31\u78c1\u8fd0\u884c\u7684\u56e0\u7d20",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
