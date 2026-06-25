# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/atpll"
title_zh = "5.4.4. \u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Angle-tracking Phase-locked Loop (ATPLL)": "\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09",
    "Overview": "\u6982\u8ff0",
    "The Angle-tracking Phase-locked Loop (ATPLL) is a velocity and rotor angle estimation algorithm provided for sensorless closed-loop velocity control of a":
        "\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09\u662f\u4e00\u79cd\u4e3a",
    ". The algorithm has a": "\u7684\u65e0\u4f20\u611f\u5668\u95ed\u73af\u901f\u5ea6\u63a7\u5236\u63d0\u4f9b\u7684\u901f\u5ea6\u548c\u8f6c\u5b50\u89d2\u5ea6\u4f30\u8ba1\u7b97\u6cd5\u3002\u8be5\u7b97\u6cd5\u5177\u6709",
    "-like structure, and it estimates the correct rotor velocity and angle by making the d-axis component of the back emf equal to zero in steady state. The rotor velocity and angle errors are eliminated in steady state due to a PI controller module included in the structure of the ATPLL estimator. The ATPLL estimator algorithm can be used for the estimation of rotor velocity and rotor angle for PMSM motors with or without rotor saliency.":
        "\u72b6\u7ed3\u6784\uff0c\u901a\u8fc7\u5728\u7a33\u6001\u4e0b\u4f7f\u53cd\u7535\u52a8\u52bf\u7684 d \u8f74\u5206\u91cf\u4e3a\u96f6\u6765\u4f30\u8ba1\u6b63\u786e\u7684\u8f6c\u5b50\u901f\u5ea6\u548c\u89d2\u5ea6\u3002\u7531\u4e8e ATPLL \u4f30\u8ba1\u5668\u7ed3\u6784\u4e2d\u5305\u542b\u7684 PI \u63a7\u5236\u5668\u6a21\u5757\uff0c\u8f6c\u5b50\u901f\u5ea6\u548c\u89d2\u5ea6\u8bef\u5dee\u5728\u7a33\u6001\u4e0b\u88ab\u6d88\u9664\u3002ATPLL \u4f30\u8ba1\u5668\u7b97\u6cd5\u53ef\u7528\u4e8e\u5177\u6709\u6216\u4e0d\u5177\u6709\u8f6c\u5b50\u51f8\u6027\u7684 PMSM \u7535\u673a\u7684\u8f6c\u5b50\u901f\u5ea6\u548c\u8f6c\u5b50\u89d2\u5ea6\u4f30\u8ba1\u3002",
    "Implementation Block Diagram and Description": "\u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "shows the basic principle of the ATPLL estimator. Here, The outputs of the estimator are estimated rotor velocity":
        "\u5c55\u793a\u4e86 ATPLL \u4f30\u8ba1\u5668\u7684\u57fa\u672c\u539f\u7406\u3002\u8fd9\u91cc\uff0c\u4f30\u8ba1\u5668\u7684\u8f93\u51fa\u662f\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6",
    "and estimated rotor angle": "\u548c\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6",
    ". The d-axis component": "\u3002\u53cd\u7535\u52a8\u52bf\u7684 d \u8f74\u5206\u91cf",
    "of the back-emf is calculated from the motor stator voltages": "\u7531\u7535\u673a\u5b9a\u5b50\u7535\u538b",
    "and stator currents": "\u548c\u5b9a\u5b50\u7535\u6d41",
    ". The reference value of": "\u8ba1\u7b97\u5f97\u5230\u3002\u53c2\u8003\u503c",
    "is zero, therefore the error becomes equal to": "\u4e3a\u96f6\uff0c\u56e0\u6b64\u8bef\u5dee\u7b49\u4e8e",
    ". This error is fed to a PI controller. The output of the PI controller is added with a feedforward velocity term":
        "\u3002\u6b64\u8bef\u5dee\u9001\u5165 PI \u63a7\u5236\u5668\u3002PI \u63a7\u5236\u5668\u7684\u8f93\u51fa\u4e0e\u524d\u9988\u901f\u5ea6\u9879",
    ", and this addition is the estimated velocity": "\u76f8\u52a0\uff0c\u6b64\u548c\u5373\u4e3a\u4f30\u8ba1\u901f\u5ea6",
    ". The estimated velocity is integrated to obtain the estimated rotor angle": "\u3002\u4f30\u8ba1\u901f\u5ea6\u7ecf\u79ef\u5206\u5f97\u5230\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6",
    "ATPLL: Generic Block Diagram": "ATPLL\uff1a\u901a\u7528\u65b9\u6846\u56fe",
    "The MCAF implementation of the ATPLL estimator is shown in": "ATPLL \u4f30\u8ba1\u5668\u7684 MCAF \u5b9e\u73b0\u5982",
    ". A brief description of the different blocks used in the ATPLL structure is given below.":
        "\u6240\u793a\u3002\u4e0b\u9762\u7b80\u8981\u63cf\u8ff0 ATPLL \u7ed3\u6784\u4e2d\u4f7f\u7528\u7684\u4e0d\u540c\u6a21\u5757\u3002",
    "ATPLL implementation": "ATPLL \u5b9e\u73b0",
    "Inputs: The ATPLL algorithm begins by calculating the back-emf components": "\u8f93\u5165\uff1aATPLL \u7b97\u6cd5\u9996\u5148\u8ba1\u7b97\u53cd\u7535\u52a8\u52bf\u5206\u91cf",
    "from the stator voltages (": "\u7531\u5b9a\u5b50\u7535\u538b\uff08",
    ") and stator currents (": "\uff09\u548c\u5b9a\u5b50\u7535\u6d41\uff08",
    ") using the motor resistance and inductance values. These back-emf values are then used for further calculation of":
        "\uff09\u4f7f\u7528\u7535\u673a\u7535\u963b\u548c\u7535\u611f\u503c\u8ba1\u7b97\u3002\u8fd9\u4e9b\u53cd\u7535\u52a8\u52bf\u503c\u7136\u540e\u7528\u4e8e\u8fdb\u4e00\u6b65\u8ba1\u7b97",
    "as shown in": "\uff0c\u5982",
    ". For calculation of": "\u6240\u793a\u3002\u5bf9\u4e8e\u8ba1\u7b97",
    ", equation": "\uff0c\u65b9\u7a0b",
    "is used for motors without significant rotor saliency, and equation": "\u7528\u4e8e\u65e0\u663e\u8457\u8f6c\u5b50\u51f8\u6027\u7684\u7535\u673a\uff0c\u65b9\u7a0b",
    "is used for motors with rotor saliency. Motors are categorised into those with and without significant rotor saliency based on their":
        "\u7528\u4e8e\u5177\u6709\u8f6c\u5b50\u51f8\u6027\u7684\u7535\u673a\u3002\u7535\u673a\u6839\u636e\u5176",
    "Saliency Constant": "\u51f8\u6027\u5e38\u6570",
    ". In": "\u3002\u5728",
    "are per-phase stator winding resistance and inductance values respectively. In": "\u4e3a\u6bcf\u76f8\u5b9a\u5b50\u7ed5\u7ec4\u7535\u963b\u548c\u7535\u611f\u503c\u3002\u5728",
    "is the rotor angle and": "\u4e3a\u8f6c\u5b50\u89d2\u5ea6\uff0c",
    "are given by": "\u7531",
    "Two-point Averaging: As mentioned above, first": "\u4e24\u70b9\u5e73\u5747\uff1a\u5982\u4e0a\u6240\u8ff0\uff0c\u9996\u5148\u4ece",
    "is calculated from": "\u8ba1\u7b97",
    "and is fed to the Two-point Averaging block. This block helps to smooth the input to the Proportional-Integral (PI) controller (":
        "\u5f97\u5230\uff0c\u5e76\u9001\u5165\u4e24\u70b9\u5e73\u5747\u6a21\u5757\u3002\u6b64\u6a21\u5757\u6709\u52a9\u4e8e\u5e73\u6ed1\u6bd4\u4f8b-\u79ef\u5206\uff08PI\uff09\u63a7\u5236\u5668\u7684\u8f93\u5165\uff08",
    "): This block represents a PI controller which is the backbone of the ATPLL estimator. In steady state, the input to the PI controller (which is:":
        "\uff09\u3002\uff1a\u6b64\u6a21\u5757\u8868\u793a PI \u63a7\u5236\u5668\uff0c\u662f ATPLL \u4f30\u8ba1\u5668\u7684\u6838\u5fc3\u3002\u5728\u7a33\u6001\u4e0b\uff0cPI \u63a7\u5236\u5668\u7684\u8f93\u5165\uff08\u5373",
    ") is reduced to zero, thereby reducing the steady-state error in the estimated velocity and angle to zero as well. The s-domain representation of":
        "\uff09\u51cf\u5c0f\u5230\u96f6\uff0c\u4ece\u800c\u5c06\u4f30\u8ba1\u901f\u5ea6\u548c\u89d2\u5ea6\u7684\u7a33\u6001\u8bef\u5dee\u4e5f\u51cf\u5c0f\u5230\u96f6\u3002",
    "is as given below:": "\u7684 s \u57df\u8868\u793a\u5982\u4e0b\uff1a",
    ": This is a low-pass filter at the output of the PI controller. After filtering, the output is added to the reference velocity (":
        "\uff1a\u8fd9\u662f PI \u63a7\u5236\u5668\u8f93\u51fa\u7684\u4f4e\u901a\u6ee4\u6ce2\u5668\u3002\u6ee4\u6ce2\u540e\uff0c\u8f93\u51fa\u4e0e\u53c2\u8003\u901f\u5ea6\uff08",
    "). The result of this addition is the unfiltered estimated velocity and is integrated to calculate the estimated rotor angle (":
        "\uff09\u76f8\u52a0\u3002\u6b64\u52a0\u6cd5\u7684\u7ed3\u679c\u4e3a\u672a\u6ee4\u6ce2\u7684\u4f30\u8ba1\u901f\u5ea6\uff0c\u5e76\u7ecf\u79ef\u5206\u8ba1\u7b97\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\uff08",
    "). The s-domain representation of": "\uff09\u3002",
    "is as given below, where,": "\u7684 s \u57df\u8868\u793a\u5982\u4e0b\uff0c\u5176\u4e2d",
    "is the filter time constant.": "\u4e3a\u6ee4\u6ce2\u5668\u65f6\u95f4\u5e38\u6570\u3002",
    ": The result of the addition of the PI controller output and the reference velocity is further filtered using this low-pass filter. The output of this filter is the estimated rotor velocity (":
        "\uff1aPI \u63a7\u5236\u5668\u8f93\u51fa\u4e0e\u53c2\u8003\u901f\u5ea6\u7684\u52a0\u6cd5\u7ed3\u679c\u901a\u8fc7\u6b64\u4f4e\u901a\u6ee4\u6ce2\u5668\u8fdb\u4e00\u6b65\u6ee4\u6ce2\u3002\u6b64\u6ee4\u6ce2\u5668\u7684\u8f93\u51fa\u4e3a\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6\uff08",
    "Following are some important points related to the PI controller and low-pass filter blocks.":
        "\u4ee5\u4e0b\u662f\u4e0e PI \u63a7\u5236\u5668\u548c\u4f4e\u901a\u6ee4\u6ce2\u5668\u6a21\u5757\u76f8\u5173\u7684\u4e00\u4e9b\u91cd\u8981\u70b9\u3002",
    "To obtain a stable dynamic performance of the ATPLL estimator over the entire operating velocity range, the integral gain":
        "\u4e3a\u4e86\u5728\u6574\u4e2a\u8fd0\u884c\u901f\u5ea6\u8303\u56f4\u5185\u83b7\u5f97 ATPLL \u4f30\u8ba1\u5668\u7684\u7a33\u5b9a\u52a8\u6001\u6027\u80fd\uff0c\u79ef\u5206\u589e\u76ca",
    "is made dependent on the reference velocity": "\u88ab\u8bbe\u4e3a\u4f9d\u8d56\u4e8e\u53c2\u8003\u901f\u5ea6",
    ". To support motors with different parameter values, the proportional and integral gains":
        "\u3002\u4e3a\u4e86\u652f\u6301\u5177\u6709\u4e0d\u540c\u53c2\u6570\u503c\u7684\u7535\u673a\uff0c\u6bd4\u4f8b\u548c\u79ef\u5206\u589e\u76ca",
    "are made dependent on the motor\u2019s back-emf constant": "\u88ab\u8bbe\u4e3a\u4f9d\u8d56\u4e8e\u7535\u673a\u7684\u53cd\u7535\u52a8\u52bf\u5e38\u6570",
    ". Empirical tuning of the PI controller gains simplifies the design significantly. The empirical equations for":
        "\u3002PI \u63a7\u5236\u5668\u589e\u76ca\u7684\u7ecf\u9a8c\u8c03\u8282\u663e\u8457\u7b80\u5316\u4e86\u8bbe\u8ba1\u3002",
    "are given in equation": "\u7684\u7ecf\u9a8c\u65b9\u7a0b\u5728\u65b9\u7a0b",
    "Reversal of velocity is supported by the ATPLL estimator. In order to make this possible, the signs of PI controller gains are reversed based on the sign of the reference velocity.":
        "ATPLL \u4f30\u8ba1\u5668\u652f\u6301\u901f\u5ea6\u53cd\u8f6c\u3002\u4e3a\u4e86\u5b9e\u73b0\u8fd9\u4e00\u70b9\uff0cPI \u63a7\u5236\u5668\u589e\u76ca\u7684\u7b26\u53f7\u6839\u636e\u53c2\u8003\u901f\u5ea6\u7684\u7b26\u53f7\u8fdb\u884c\u53cd\u8f6c\u3002",
    "Filter constants": "\u6ee4\u6ce2\u5668\u5e38\u6570",
    "are decided based on the performance of the control algorithm for a range of motors. The filter constants may be adjusted in the":
        "\u6839\u636e\u4e00\u7cfb\u5217\u7535\u673a\u7684\u63a7\u5236\u7b97\u6cd5\u6027\u80fd\u786e\u5b9a\u3002\u6ee4\u6ce2\u5668\u5e38\u6570\u53ef\u5728",
    "Customize page": "Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762",
    "of motorBench": "\u7684 motorBench",
    "Development Suite.": "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\u4e2d\u8c03\u6574\u3002",
    "Application to PMSMs with Saliency": "\u5728\u5177\u6709\u51f8\u6027\u7684 PMSM \u4e2d\u7684\u5e94\u7528",
    "In case of interior permanent-magnet motors (IPMSMs), the": "\u5bf9\u4e8e\u5185\u7f6e\u6c38\u78c1\u7535\u673a\uff08IPMSM\uff09\uff0c",
    "- and": "\u8f74\u548c",
    "-axis inductances are not equal; typically": "\u8f74\u7535\u611f\u4e0d\u76f8\u7b49\uff1b\u901a\u5e38",
    "is larger than": "\u5927\u4e8e",
    ". In order to quantify the degree of saliency in the rotor, the following saliency constant is defined. Here,":
        "\u3002\u4e3a\u4e86\u91cf\u5316\u8f6c\u5b50\u7684\u51f8\u6027\u7a0b\u5ea6\uff0c\u5b9a\u4e49\u4e86\u4ee5\u4e0b\u51f8\u6027\u5e38\u6570\u3002\u8fd9\u91cc\uff0c",
    "is equal to": "\u7b49\u4e8e",
    "It can be noted that the saliency constant is equal to 0 for motors with no saliency and increases toward 1 as the saliency increases. For a correct rotor velocity and angle estimation, it is important that the relevant equations are used by the estimator, which are different for motors with salient and non-salient rotors. In order to differentiate the salient motors from the non-salient ones, a saliency constant threshold of 0.25 is defined. Thus, the motors satisfying the following condition are considered to be salient pole motors.":
        "\u53ef\u4ee5\u6ce8\u610f\u5230\uff0c\u5bf9\u4e8e\u65e0\u51f8\u6027\u7684\u7535\u673a\uff0c\u51f8\u6027\u5e38\u6570\u7b49\u4e8e 0\uff0c\u968f\u7740\u51f8\u6027\u589e\u52a0\u800c\u8d8b\u8fd1 1\u3002\u4e3a\u4e86\u6b63\u786e\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6\u548c\u89d2\u5ea6\uff0c\u4f30\u8ba1\u5668\u4f7f\u7528\u76f8\u5173\u65b9\u7a0b\u975e\u5e38\u91cd\u8981\uff0c\u51f8\u6781\u548c\u975e\u51f8\u6781\u8f6c\u5b50\u7535\u673a\u7684\u65b9\u7a0b\u4e0d\u540c\u3002\u4e3a\u4e86\u533a\u5206\u51f8\u6781\u7535\u673a\u548c\u975e\u51f8\u6781\u7535\u673a\uff0c\u5b9a\u4e49\u4e86 0.25 \u7684\u51f8\u6027\u5e38\u6570\u9608\u503c\u3002\u56e0\u6b64\uff0c\u6ee1\u8db3\u4ee5\u4e0b\u6761\u4ef6\u7684\u7535\u673a\u88ab\u89c6\u4e3a\u51f8\u6781\u7535\u673a\u3002",
    "This can further be simplified to": "\u8fd9\u53ef\u4ee5\u8fdb\u4e00\u6b65\u7b80\u5316\u4e3a",
    "The ATPLL estimator accommodates motors both with salient and non-salient rotors by a suitable choice of equations in its algorithm, thus preserving the accuracy of rotor velocity and angle estimation.":
        "ATPLL \u4f30\u8ba1\u5668\u901a\u8fc7\u5728\u5176\u7b97\u6cd5\u4e2d\u9009\u62e9\u5408\u9002\u7684\u65b9\u7a0b\u6765\u9002\u5e94\u51f8\u6781\u548c\u975e\u51f8\u6781\u8f6c\u5b50\u7684\u7535\u673a\uff0c\u4ece\u800c\u4fdd\u6301\u8f6c\u5b50\u901f\u5ea6\u548c\u89d2\u5ea6\u4f30\u8ba1\u7684\u51c6\u786e\u6027\u3002",
    "Sample Results": "\u793a\u4f8b\u7ed3\u679c",
    "The following results are obtained from numerical simulation for a Leadshine 400 motor. A superimposed plot of actual rotor velocity and the estimated rotor velocity by the ATPLL estimator is shown in":
        "\u4ee5\u4e0b\u7ed3\u679c\u6765\u81ea Leadshine 400 \u7535\u673a\u7684\u6570\u503c\u4eff\u771f\u3002\u5b9e\u9645\u8f6c\u5b50\u901f\u5ea6\u548c ATPLL \u4f30\u8ba1\u5668\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6\u7684\u53e0\u52a0\u56fe\u5c55\u793a\u5728",
    "along with the plot showing the error in estimated velocity. It can be observed that the steady-state velocity error is zero.":
        "\u4e2d\uff0c\u540c\u65f6\u8fd8\u5c55\u793a\u4e86\u4f30\u8ba1\u901f\u5ea6\u8bef\u5dee\u56fe\u3002\u53ef\u4ee5\u89c2\u5bdf\u5230\u7a33\u6001\u901f\u5ea6\u8bef\u5dee\u4e3a\u96f6\u3002",
    "Estimated Rotor Velocity by the ATPLL": "ATPLL \u7684\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6",
    "A superimposed plot of actual rotor angle and the estimated rotor angle by ATPLL estimator along with the error in the estimated angle is shown in":
        "\u5b9e\u9645\u8f6c\u5b50\u89d2\u5ea6\u548c ATPLL \u4f30\u8ba1\u5668\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\u7684\u53e0\u52a0\u56fe\u4ee5\u53ca\u4f30\u8ba1\u89d2\u5ea6\u8bef\u5dee\u5c55\u793a\u5728",
    ". This plot is for the same velocity transient shown in": "\u3002\u6b64\u56fe\u5bf9\u5e94\u4e8e",
    ". It can be seen that the steady-state angle error is zero.": "\u6240\u793a\u7684\u76f8\u540c\u901f\u5ea6\u77ac\u53d8\u3002\u53ef\u4ee5\u770b\u5230\u7a33\u6001\u89d2\u5ea6\u8bef\u5dee\u4e3a\u96f6\u3002",
    "Estimated Rotor Angle by the ATPLL": "ATPLL \u7684\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6",
    "Implementation Notes": "\u5b9e\u73b0\u8bf4\u660e",
    "MCAF R5 \u2013 R8": "MCAF R5 \u2013 R8",
    "The ATPLL filter constants": "ATPLL \u6ee4\u6ce2\u5668\u5e38\u6570",
    "were fixed in MCAF R5 \u2013 R8.": "\u5728 MCAF R5 \u2013 R8 \u4e2d\u662f\u56fa\u5b9a\u7684\u3002",
    "5.4.4. Angle-tracking Phase-locked Loop (ATPLL)": "5.4.4. \u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09",
    "5.4.4.1. Overview": "5.4.4.1. \u6982\u8ff0",
    "5.4.4.2. Implementation Block Diagram and Description": "5.4.4.2. \u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "5.4.4.3. Application to PMSMs with Saliency": "5.4.4.3. \u5728\u5177\u6709\u51f8\u6027\u7684 PMSM \u4e2d\u7684\u5e94\u7528",
    "5.4.4.4. Sample Results": "5.4.4.4. \u793a\u4f8b\u7ed3\u679c",
    "5.4.4.5. Implementation Notes": "5.4.4.5. \u5b9e\u73b0\u8bf4\u660e",
    "5.4.4.5.1. MCAF R5 \u2013 R8": "5.4.4.5.1. MCAF R5 \u2013 R8",
    "Pullout torque method": "\u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5",
    "Zero-Speed / Maximum Torque (ZS/MT)": "\u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
