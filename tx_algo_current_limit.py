# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/current-limit"
title_zh = "5.6. \u7535\u6d41\u9650\u5236"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Current limit": "\u7535\u6d41\u9650\u5236",
    "Overview": "\u6982\u8ff0",
    "The outer loop controller (": "\u5916\u73af\u63a7\u5236\u5668\uff08",
    "velocity control": "\u901f\u5ea6\u63a7\u5236",
    ", for example) commands q-axis current which saturates at well-defined limits. These limits are configurable, and may have a fixed or dynamic behavior. Dynamic current limits are appropriate when short peak transient currents are desired.":
        "\uff0c\u4f8b\u5982\uff09\u547d\u4ee4 q \u8f74\u7535\u6d41\uff0c\u8be5\u7535\u6d41\u5728\u660e\u786e\u5b9a\u4e49\u7684\u9650\u5236\u5904\u9971\u548c\u3002\u8fd9\u4e9b\u9650\u5236\u53ef\u914d\u7f6e\uff0c\u53ef\u4ee5\u662f\u56fa\u5b9a\u7684\u6216\u52a8\u6001\u7684\u3002\u5f53\u9700\u8981\u77ed\u6682\u5cf0\u503c\u6682\u6001\u7535\u6d41\u65f6\uff0c\u52a8\u6001\u7535\u6d41\u9650\u5236\u662f\u5408\u9002\u7684\u3002",
    "Implications of operating at the current limit": "\u5728\u7535\u6d41\u9650\u5236\u4e0b\u8fd0\u884c\u7684\u5f15\u7533",
    "When the outer loop controller saturates at the current limit, it can no longer achieve its control goal, and will instead come as close to that goal as it can without exceeding the current limit.":
        "\u5f53\u5916\u73af\u63a7\u5236\u5668\u5728\u7535\u6d41\u9650\u5236\u5904\u9971\u548c\u65f6\uff0c\u5b83\u65e0\u6cd5\u518d\u5b9e\u73b0\u5176\u63a7\u5236\u76ee\u6807\uff0c\u800c\u662f\u5728\u4e0d\u8d85\u8fc7\u7535\u6d41\u9650\u5236\u7684\u524d\u63d0\u4e0b\u5c3d\u53ef\u80fd\u63a5\u8fd1\u8be5\u76ee\u6807\u3002",
    "The MCAF velocity controller, for example, will no longer regulate velocity if the current limit is reached, and will instead command the current limit while in control saturation. If the velocity command is 3000 RPM, but at a 10 A current limit the motor can only reach 2400 RPM instead, then the velocity controller will maintain 10 A at 2400 RPM.":
        "\u4f8b\u5982\uff0cMCAF \u901f\u5ea6\u63a7\u5236\u5668\u5728\u8fbe\u5230\u7535\u6d41\u9650\u5236\u65f6\u5c06\u4e0d\u518d\u8c03\u8282\u901f\u5ea6\uff0c\u800c\u662f\u5728\u63a7\u5236\u9971\u548c\u65f6\u547d\u4ee4\u7535\u6d41\u9650\u5236\u3002\u5982\u679c\u901f\u5ea6\u547d\u4ee4\u4e3a 3000 RPM\uff0c\u4f46\u5728 10 A \u7535\u6d41\u9650\u5236\u4e0b\u7535\u673a\u53ea\u80fd\u8fbe\u5230 2400 RPM\uff0c\u5219\u901f\u5ea6\u63a7\u5236\u5668\u5c06\u5728 2400 RPM \u65f6\u7ef4\u6301 10 A\u3002",
    "In field-oriented control, constant q-axis current results in nearly constant torque over a wide range \u2014 so, in practice, the motor speed will be determined by the balance between motor torque and load torque. Speed can change fairly quickly if load torque changes and exceeds the current limit.":
        "\u5728\u77e2\u91cf\u63a7\u5236\u4e2d\uff0c\u6052\u5b9a\u7684 q \u8f74\u7535\u6d41\u5728\u5bbd\u8303\u56f4\u5185\u4ea7\u751f\u8fd1\u4e4e\u6052\u5b9a\u7684\u8f6c\u77e9\u2014\u56e0\u6b64\uff0c\u5728\u5b9e\u9645\u5e94\u7528\u4e2d\uff0c\u7535\u673a\u901f\u5ea6\u5c06\u7531\u7535\u673a\u8f6c\u77e9\u4e0e\u8d1f\u8f7d\u8f6c\u77e9\u4e4b\u95f4\u7684\u5e73\u8861\u51b3\u5b9a\u3002\u5982\u679c\u8d1f\u8f7d\u8f6c\u77e9\u53d8\u5316\u5e76\u8d85\u8fc7\u7535\u6d41\u9650\u5236\uff0c\u901f\u5ea6\u53ef\u4ee5\u76f8\u5f53\u5feb\u5730\u53d8\u5316\u3002",
    "In motoring operation, speed will reach stable equilibrium when motor and load torque balance. Increases in load torque will slow the motor down, and decreases load torque allow the motor to speed up until the outer loop comes out of saturation.":
        "\u5728\u7535\u52a8\u8fd0\u884c\u4e2d\uff0c\u5f53\u7535\u673a\u8f6c\u77e9\u4e0e\u8d1f\u8f7d\u8f6c\u77e9\u5e73\u8861\u65f6\uff0c\u901f\u5ea6\u5c06\u8fbe\u5230\u7a33\u5b9a\u5e73\u8861\u3002\u8d1f\u8f7d\u8f6c\u77e9\u589e\u52a0\u4f1a\u4f7f\u7535\u673a\u51cf\u901f\uff0c\u8d1f\u8f7d\u8f6c\u77e9\u51cf\u5c0f\u5219\u5141\u8bb8\u7535\u673a\u52a0\u901f\uff0c\u76f4\u5230\u5916\u73af\u9000\u51fa\u9971\u548c\u3002",
    "In regenerating operation, the equilibrium is unstable: if the current limit is reached, and there is still an external mechanical torque driving the motor shaft, then the motor will speed up until the external mechanical torque decreases. For near-constant-torque loads (for example, a load of ore attached to a conveyor belt or winch that is being lowered in a controlled fashion), reaching the torque limit can cause a runaway condition where the speed increases rapidly until something breaks.":
        "\u5728\u518d\u751f\u8fd0\u884c\u4e2d\uff0c\u5e73\u8861\u662f\u4e0d\u7a33\u5b9a\u7684\uff1a\u5982\u679c\u8fbe\u5230\u7535\u6d41\u9650\u5236\uff0c\u4e14\u4ecd\u6709\u5916\u90e8\u673a\u68b0\u8f6c\u77e9\u9a71\u52a8\u7535\u673a\u8f74\uff0c\u5219\u7535\u673a\u5c06\u52a0\u901f\u76f4\u5230\u5916\u90e8\u673a\u68b0\u8f6c\u77e9\u51cf\u5c0f\u3002\u5bf9\u4e8e\u8fd1\u4e4e\u6052\u5b9a\u8f6c\u77e9\u7684\u8d1f\u8f7d\uff08\u4f8b\u5982\uff0c\u9644\u7740\u5728\u4f20\u9001\u5e26\u6216\u7ede\u8f66\u4e0a\u4ee5\u53d7\u63a7\u65b9\u5f0f\u4e0b\u653e\u7684\u77ff\u77f3\u8d1f\u8f7d\uff09\uff0c\u8fbe\u5230\u8f6c\u77e9\u9650\u5236\u53ef\u80fd\u5bfc\u81f4\u5931\u63a7\u72b6\u51b5\uff0c\u901f\u5ea6\u5feb\u901f\u589e\u52a0\u76f4\u5230\u53d1\u751f\u673a\u68b0\u7834\u574f\u3002",
    "For this reason, it is important to consider the entire system and understand the desired behavior of motor and load, in order to select a current limit.":
        "\u56e0\u6b64\uff0c\u91cd\u8981\u7684\u662f\u8003\u8651\u6574\u4e2a\u7cfb\u7edf\u5e76\u7406\u89e3\u7535\u673a\u548c\u8d1f\u8f7d\u7684\u9884\u671f\u884c\u4e3a\uff0c\u4ee5\u9009\u62e9\u5408\u9002\u7684\u7535\u6d41\u9650\u5236\u3002",
    "Dynamic current limit": "\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "Continuous current limits in both the motor and power electronics are determined by thermal constraints: specifically, the rated temperatures of the motor windings and transistor junctions. At the continuous current limit, motor and transistors can operate indefinitely. But the thermal time constants of motors and transistors are usually longer than transient torque requirements: this means that both motor and transistors have the capability of carrying currents above the continuous limit for a short time.":
        "\u7535\u673a\u548c\u529f\u7387\u7535\u5b50\u5668\u4ef6\u4e2d\u7684\u8fde\u7eed\u7535\u6d41\u9650\u5236\u7531\u70ed\u7ea6\u675f\u51b3\u5b9a\uff1a\u5177\u4f53\u800c\u8a00\uff0c\u662f\u7535\u673a\u7ed5\u7ec4\u548c\u6676\u4f53\u7ba1\u7ed3\u70b9\u7684\u989d\u5b9a\u6e29\u5ea6\u3002\u5728\u8fde\u7eed\u7535\u6d41\u9650\u5236\u4e0b\uff0c\u7535\u673a\u548c\u6676\u4f53\u7ba1\u53ef\u4ee5\u65e0\u9650\u671f\u8fd0\u884c\u3002\u4f46\u7535\u673a\u548c\u6676\u4f53\u7ba1\u7684\u70ed\u65f6\u95f4\u5e38\u6570\u901a\u5e38\u5927\u4e8e\u6682\u6001\u8f6c\u77e9\u9700\u6c42\uff1a\u8fd9\u610f\u5473\u7740\u7535\u673a\u548c\u6676\u4f53\u7ba1\u90fd\u6709\u80fd\u529b\u5728\u77ed\u65f6\u95f4\u5185\u627f\u53d7\u8d85\u8fc7\u8fde\u7eed\u9650\u5236\u7684\u7535\u6d41\u3002",
    "A useful dynamic current limit algorithm meets several requirements:":
        "\u4e00\u4e2a\u6709\u7528\u7684\u52a8\u6001\u7535\u6d41\u9650\u5236\u7b97\u6cd5\u9700\u6ee1\u8db3\u4ee5\u4e0b\u51e0\u4e2a\u8981\u6c42\uff1a",
    "At any given time, the current limit": "\u5728\u4efb\u4f55\u7ed9\u5b9a\u65f6\u95f4\uff0c\u7535\u6d41\u9650\u5236",
    "varies between continuous and peak limits:":
        "\u5728\u8fde\u7eed\u9650\u5236\u548c\u5cf0\u503c\u9650\u5236\u4e4b\u95f4\u53d8\u5316\uff1a",
    "The magnitude of the commanded motor current vector":
        "\u547d\u4ee4\u7684\u7535\u673a\u7535\u6d41\u77e2\u91cf\u7684\u5e45\u503c",
    "should always be kept below the current limit; in other words,":
        "\u5e94\u59cb\u7ec8\u4fdd\u6301\u5728\u7535\u6d41\u9650\u5236\u4ee5\u4e0b\uff1b\u6362\u53e5\u8bdd\u8bf4\uff0c",
    "The dynamics of the current limit should be controlled so that motor and transistors are kept within their safe operating temperature.":
        "\u7535\u6d41\u9650\u5236\u7684\u52a8\u6001\u5e94\u53d7\u63a7\uff0c\u4ee5\u4f7f\u7535\u673a\u548c\u6676\u4f53\u7ba1\u4fdd\u6301\u5728\u5176\u5b89\u5168\u5de5\u4f5c\u6e29\u5ea6\u8303\u56f4\u5185\u3002",
    "MCAF R7 provides such a current limit algorithm.":
        "MCAF R7 \u63d0\u4f9b\u4e86\u8fd9\u6837\u7684\u7535\u6d41\u9650\u5236\u7b97\u6cd5\u3002",
    "Thermal modeling background": "\u70ed\u6a21\u578b\u80cc\u666f",
    "A detailed description of thermal modeling and the selection of current limit parameters is beyond the scope of this documentation at present, but there are a few key principles to note.":
        "\u70ed\u6a21\u578b\u548c\u7535\u6d41\u9650\u5236\u53c2\u6570\u9009\u62e9\u7684\u8be6\u7ec6\u63cf\u8ff0\u8d85\u51fa\u4e86\u672c\u6587\u6863\u7684\u8303\u56f4\uff0c\u4f46\u6709\u51e0\u4e2a\u5173\u952e\u539f\u5219\u9700\u8981\u6ce8\u610f\u3002",
    "For stator windings, the thermal time constant is often tens of seconds or even minutes, and transient currents of 3-5\u00d7 larger than the continuous limit are common in some applications.":
        "\u5bf9\u4e8e\u5b9a\u5b50\u7ed5\u7ec4\uff0c\u70ed\u65f6\u95f4\u5e38\u6570\u901a\u5e38\u4e3a\u51e0\u5341\u79d2\u751a\u81f3\u51e0\u5206\u949f\uff0c\u5728\u67d0\u4e9b\u5e94\u7528\u4e2d\uff0c\u6682\u6001\u7535\u6d41\u8d85\u8fc7\u8fde\u7eed\u9650\u5236 3-5 \u500d\u662f\u5e38\u89c1\u7684\u3002",
    "In transistors, there are three relevant materials: the transistor junction, the transistor case, and the heat sink.":
        "\u5728\u6676\u4f53\u7ba1\u4e2d\uff0c\u6709\u4e09\u79cd\u76f8\u5173\u6750\u6599\uff1a\u6676\u4f53\u7ba1\u7ed3\u70b9\u3001\u6676\u4f53\u7ba1\u5916\u58f3\u548c\u6563\u70ed\u5668\u3002",
    "The junction is small and thin, and heats up quickly (typically on the order of milliseconds or tens of milliseconds), but the thermal resistance between junction and case is typically small; in many cases, the junction may be only a few degrees hotter than the case.":
        "\u7ed3\u70b9\u5c0f\u800c\u8584\uff0c\u5347\u6e29\u5f88\u5feb\uff08\u901a\u5e38\u5728\u6beb\u79d2\u6216\u51e0\u5341\u6beb\u79d2\u7684\u6570\u91cf\u7ea7\uff09\uff0c\u4f46\u7ed3\u70b9\u4e0e\u5916\u58f3\u4e4b\u95f4\u7684\u70ed\u963b\u901a\u5e38\u5f88\u5c0f\uff1b\u5728\u8bb8\u591a\u60c5\u51b5\u4e0b\uff0c\u7ed3\u70b9\u53ef\u80fd\u53ea\u6bd4\u5916\u58f3\u70ed\u51e0\u5ea6\u3002",
    "The transistor case, especially in larger packages such as TO-252 (DPAK), TO-263 (D\u00b2PAK), TO-220, and TO-247, contains a metal tab with enough thermal capacity to act as a short temporary heat sink.":
        "\u6676\u4f53\u7ba1\u5916\u58f3\uff0c\u5c24\u5176\u662f\u5728\u8f83\u5927\u7684\u5c01\u88c5\u4e2d\uff0c\u5982 TO-252 (DPAK)\u3001TO-263 (D\u00b2PAK)\u3001TO-220 \u548c TO-247\uff0c\u5305\u542b\u4e00\u4e2a\u91d1\u5c5e\u6807\u7b7e\uff0c\u5176\u70ed\u5bb9\u8db3\u4ee5\u4f5c\u4e3a\u77ed\u6682\u7684\u4e34\u65f6\u6563\u70ed\u5668\u3002",
    "External heat sink \u2014 if present, this provides additional thermal capacity and a path for heat to flow to ambient. (Note: on a printed circuit board, copper pours with thermal vias are an effective method of providing at least some additional thermal capacity and conductivity from the PCB itself. See":
        "\u5916\u90e8\u6563\u70ed\u5668\u2014\u2014\u5982\u679c\u5b58\u5728\uff0c\u5b83\u63d0\u4f9b\u989d\u5916\u7684\u70ed\u5bb9\u548c\u70ed\u91cf\u6d41\u5411\u73af\u5883\u7684\u8def\u5f84\u3002\uff08\u6ce8\u610f\uff1a\u5728\u5370\u5236\u7535\u8def\u677f\u4e0a\uff0c\u5e26\u6709\u70ed\u901a\u5b54\u7684\u94dc\u7ba1\u662f\u4ece PCB \u672c\u8eab\u63d0\u4f9b\u81f3\u5c11\u4e00\u4e9b\u989d\u5916\u70ed\u5bb9\u548c\u5bfc\u70ed\u6027\u7684\u6709\u6548\u65b9\u6cd5\u3002\u53c2\u89c1",
    "AN8826 PCB Mounting Guidelines for Surface Mount Packages":
        "AN8826 \u8868\u9762\u8d34\u88c5\u5c01\u88c5 PCB \u5b89\u88c5\u6307\u5357",
    "for more information.)": "\u4e86\u89e3\u66f4\u591a\u4fe1\u606f\u3002\uff09",
    "shows a thermal simulation of a MOSFET dissipating constant power loss after time":
        "\u5c55\u793a\u4e86 MOSFET \u5728\u65f6\u95f4",
    ". The junction-to-case temperature rises to its final value very quickly. Transistor case and heatsink heat up more slowly. The thermal capacity of transistor case and heatsink allow peak transient currents above the continuous current capacity.":
        "\u540e\u4ee5\u6052\u5b9a\u529f\u7387\u635f\u8017\u6563\u70ed\u7684\u70ed\u4eff\u771f\u3002\u7ed3\u70b9\u5230\u5916\u58f3\u7684\u6e29\u5ea6\u5347\u9ad8\u5230\u6700\u7ec8\u503c\u7684\u901f\u5ea6\u975e\u5e38\u5feb\u3002\u6676\u4f53\u7ba1\u5916\u58f3\u548c\u6563\u70ed\u5668\u5347\u6e29\u8f83\u6162\u3002\u6676\u4f53\u7ba1\u5916\u58f3\u548c\u6563\u70ed\u5668\u7684\u70ed\u5bb9\u5141\u8bb8\u6682\u6001\u7535\u6d41\u8d85\u8fc7\u8fde\u7eed\u7535\u6d41\u5bb9\u91cf\u3002",
    "Thermal simulation of a MOSFET dissipating 10W, R": "MOSFET \u4ee5 10W \u529f\u7387\u6563\u70ed\u7684\u70ed\u4eff\u771f\uff0cR",
    "= 0.4 K/W.": "= 0.4 K/W\u3002",
    "Available current limit algorithms in MCAF": "MCAF \u4e2d\u53ef\u7528\u7684\u7535\u6d41\u9650\u5236\u7b97\u6cd5",
    "The following are available current limit algorithms in MCAF:":
        "\u4ee5\u4e0b\u662f MCAF \u4e2d\u53ef\u7528\u7684\u7535\u6d41\u9650\u5236\u7b97\u6cd5\uff1a",
    "Static current limit": "\u9759\u6001\u7535\u6d41\u9650\u5236",
    "(No dynamic current limit) \u2014 maintains a constant continuous current limit, taking the lower value of the board continuous current limit and the motor continuous current limit":
        "\uff08\u65e0\u52a8\u6001\u7535\u6d41\u9650\u5236\uff09\u2014\u2014\u7ef4\u6301\u6052\u5b9a\u7684\u8fde\u7eed\u7535\u6d41\u9650\u5236\uff0c\u53d6\u677f\u7ea7\u8fde\u7eed\u7535\u6d41\u9650\u5236\u548c\u7535\u673a\u8fde\u7eed\u7535\u6d41\u9650\u5236\u4e2d\u7684\u8f83\u5c0f\u503c",
    "Simple current limit": "\u7b80\u5355\u7535\u6d41\u9650\u5236",
    "(\u201cdyn1\u201d) \u2014 uses a first-order model dependent on motor current.":
        "\uff08\u201cdyn1\u201d\uff09\u2014\u2014\u4f7f\u7528\u4f9d\u8d56\u7535\u673a\u7535\u6d41\u7684\u4e00\u9636\u6a21\u578b\u3002",
    "Peak and continuous limits": "\u5cf0\u503c\u548c\u8fde\u7eed\u9650\u5236",
    "Continuous and peak current limits are independent of the algorithm used.":
        "\u8fde\u7eed\u548c\u5cf0\u503c\u7535\u6d41\u9650\u5236\u4e0e\u6240\u4f7f\u7528\u7684\u7b97\u6cd5\u65e0\u5173\u3002",
    "The continuous current should be chosen based on a system-level requirement, for example, continuous operation for 15 minutes with motor and drive in free air of up to 50\u00b0C ambient. (In some cases, \u201ccontinuous\u201d really is an indefinitely long period of time, and in others the time is limited.)":
        "\u8fde\u7eed\u7535\u6d41\u5e94\u6839\u636e\u7cfb\u7edf\u7ea7\u9700\u6c42\u9009\u62e9\uff0c\u4f8b\u5982\uff0c\u5728\u6700\u9ad8 50\u00b0C \u73af\u5883\u6e29\u5ea6\u7684\u81ea\u7136\u51b7\u5374\u4e0b\u7535\u673a\u548c\u9a71\u52a8\u5668\u8fde\u7eed\u8fd0\u884c 15 \u5206\u949f\u3002\uff08\u5728\u67d0\u4e9b\u60c5\u51b5\u4e0b\uff0c\u201c\u8fde\u7eed\u201d\u786e\u5b9e\u662f\u65e0\u9650\u957f\u7684\u65f6\u95f4\u6bb5\uff0c\u800c\u5728\u5176\u4ed6\u60c5\u51b5\u4e0b\u65f6\u95f4\u662f\u6709\u9650\u7684\u3002\uff09",
    "Peak current should be chosen as the minimum of all short-time constraints, typically including the following:":
        "\u5cf0\u503c\u7535\u6d41\u5e94\u9009\u62e9\u4e3a\u6240\u6709\u77ed\u65f6\u7ea6\u675f\u7684\u6700\u5c0f\u503c\uff0c\u901a\u5e38\u5305\u62ec\u4ee5\u4e0b\u5185\u5bb9\uff1a",
    "motor: demagnetization current \u2014 above some point, stator magnetic field can cause irreversible demagnetization of rotor magnets.":
        "\u7535\u673a\uff1a\u53bb\u78c1\u7535\u6d41\u2014\u2014\u8d85\u8fc7\u67d0\u4e00\u70b9\u540e\uff0c\u5b9a\u5b50\u78c1\u573a\u53ef\u80fd\u5bfc\u81f4\u8f6c\u5b50\u78c1\u94c1\u7684\u4e0d\u53ef\u9006\u53bb\u78c1\u3002",
    "motor: iron saturation \u2014 above some point, torque degrades and inductance decreases, causing an increase in ripple current. Iron saturation usually occurs at a lower current than the demagnetization current.":
        "\u7535\u673a\uff1a\u94c1\u82af\u9971\u548c\u2014\u2014\u8d85\u8fc7\u67d0\u4e00\u70b9\u540e\uff0c\u8f6c\u77e9\u964d\u4f4e\u4e14\u7535\u611f\u51cf\u5c0f\uff0c\u5bfc\u81f4\u7eb9\u6ce2\u7535\u6d41\u589e\u52a0\u3002\u94c1\u82af\u9971\u548c\u901a\u5e38\u53d1\u751f\u5728\u4f4e\u4e8e\u53bb\u78c1\u7535\u6d41\u7684\u7535\u6d41\u4e0b\u3002",
    "drive: ADC input current saturation \u2014 can\u2019t control what you aren\u2019t able to measure":
        "\u9a71\u52a8\u5668\uff1aADC \u8f93\u5165\u7535\u6d41\u9971\u548c\u2014\u2014\u65e0\u6cd5\u63a7\u5236\u65e0\u6cd5\u6d4b\u91cf\u7684\u4fe1\u53f7",
    "drive: hardware current limit \u2014 this should be reserved for detecting catastrophic failures, for example a short-circuit within one of the transistors, or an external short-circuit of one of the motor phases to either the positive or negative DC link":
        "\u9a71\u52a8\u5668\uff1a\u786c\u4ef6\u7535\u6d41\u9650\u5236\u2014\u2014\u8fd9\u5e94\u4fdd\u7559\u7528\u4e8e\u68c0\u6d4b\u707e\u96be\u6027\u6545\u969c\uff0c\u4f8b\u5982\u6676\u4f53\u7ba1\u5185\u90e8\u77ed\u8def\u6216\u7535\u673a\u67d0\u4e00\u76f8\u5bf9\u76f4\u6d41\u6bcd\u7ebf\u6b63\u6781\u6216\u8d1f\u6781\u7684\u5916\u90e8\u77ed\u8def",
    "drive: gate drive \u2014 above a certain current, the gate drive may not work reliably. Put another way: the gate drive should be designed and tested to handle some peak current that should never be exceeded.":
        "\u9a71\u52a8\u5668\uff1a\u6805\u9a71\u52a8\u2014\u2014\u8d85\u8fc7\u67d0\u4e00\u7535\u6d41\u540e\uff0c\u6805\u9a71\u52a8\u53ef\u80fd\u65e0\u6cd5\u53ef\u9760\u5de5\u4f5c\u3002\u6362\u53e5\u8bdd\u8bf4\uff0c\u6805\u9a71\u52a8\u5e94\u8bbe\u8ba1\u548c\u6d4b\u8bd5\u4e3a\u80fd\u627f\u53d7\u4e00\u4e9b\u4e0d\u5e94\u8d85\u8fc7\u7684\u5cf0\u503c\u7535\u6d41\u3002",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "So far, all versions of MCAF (R1 \u2013 R7) support only symmetric current limits: the same current level is applied to both positive and negative currents, whether the motor is rotating forward or backward, and whether the motor is in motoring or regenerative operation.":
        "\u76ee\u524d\u4e3a\u6b62\uff0c\u6240\u6709\u7248\u672c\u7684 MCAF\uff08R1\u2013R7\uff09\u4ec5\u652f\u6301\u5bf9\u79f0\u7535\u6d41\u9650\u5236\uff1a\u65e0\u8bba\u7535\u673a\u6b63\u8f6c\u8fd8\u662f\u53cd\u8f6c\uff0c\u65e0\u8bba\u7535\u673a\u5904\u4e8e\u7535\u52a8\u8fd8\u662f\u518d\u751f\u8fd0\u884c\uff0c\u6b63\u8d1f\u7535\u6d41\u5747\u65bd\u52a0\u76f8\u540c\u7684\u7535\u6d41\u7535\u5e73\u3002",
    "The": "",
    "simple dynamic current limit": "\u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "has been added in MCAF R7.":
        "\u5728 MCAF R7 \u4e2d\u6dfb\u52a0\u3002",
    "For other implementation notes, see the detailed information in each current limit option.":
        "\u5176\u4ed6\u5b9e\u73b0\u8bf4\u660e\uff0c\u8bf7\u53c2\u9605\u6bcf\u4e2a\u7535\u6d41\u9650\u5236\u9009\u9879\u4e2d\u7684\u8be6\u7ec6\u4fe1\u606f\u3002",
    "5.6. Current limit": "5.6. \u7535\u6d41\u9650\u5236",
    "5.6.1. Overview": "5.6.1. \u6982\u8ff0",
    "5.6.2. Implications of operating at the current limit": "5.6.2. \u5728\u7535\u6d41\u9650\u5236\u4e0b\u8fd0\u884c\u7684\u5f15\u7533",
    "5.6.3. Dynamic current limit": "5.6.3. \u52a8\u6001\u7535\u6d41\u9650\u5236",
    "5.6.4. Thermal modeling background": "5.6.4. \u70ed\u6a21\u578b\u80cc\u666f",
    "5.6.5. Available current limit algorithms in MCAF": "5.6.5. MCAF \u4e2d\u53ef\u7528\u7684\u7535\u6d41\u9650\u5236\u7b97\u6cd5",
    "5.6.6. Peak and continuous limits": "5.6.6. \u5cf0\u503c\u548c\u8fde\u7eed\u9650\u5236",
    "5.6.7. Implementation notes": "5.6.7. \u5b9e\u73b0\u8bf4\u660e",
    "D-axis current reference generation": "D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
    "Simple dynamic current limit": "\u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
