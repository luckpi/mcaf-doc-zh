# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/dead-time-comp"
title_zh = "5.7. \u6b7b\u533a\u8865\u507f"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Dead-time Compensation": "\u6b7b\u533a\u8865\u507f",
    "Overview": "\u6982\u8ff0",
    "position and velocity estimators": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668",
    "flux control algorithms": "\u78c1\u94fe\u63a7\u5236\u7b97\u6cd5",
    "Definition and origin of dead time": "\u6b7b\u533a\u7684\u5b9a\u4e49\u548c\u6765\u6e90",
    "Dead-time distortion": "\u6b7b\u533a\u7578\u53d8",
    "Output voltage during dead time": "\u6b7b\u533a\u671f\u95f4\u7684\u8f93\u51fa\u7535\u538b",
    "Analysis of error bounds": "\u8bef\u5dee\u8fb9\u754c\u5206\u6790",
    "Behavior during discontinuous conduction": "\u65ad\u7eed\u5bfc\u901a\u671f\u95f4\u7684\u884c\u4e3a",
    "Dead-time distortion voltage in field-oriented current control": "\u77e2\u91cf\u7535\u6d41\u63a7\u5236\u4e2d\u7684\u6b7b\u533a\u7578\u53d8\u7535\u538b",
    "Practical effects of dead-time distortion": "\u6b7b\u533a\u7578\u53d8\u7684\u5b9e\u9645\u6548\u5e94",
    "effect on current control": "\u5bf9\u7535\u6d41\u63a7\u5236\u7684\u5f71\u54cd",
    "effect on position and velocity estimators": "\u5bf9\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668\u7684\u5f71\u54cd",
    "Dead-time distortion and field-oriented current control": "\u6b7b\u533a\u7578\u53d8\u4e0e\u77e2\u91cf\u7535\u6d41\u63a7\u5236",
    "Dead-time distortion with low-bandwidth current controllers": "\u4f4e\u5e26\u5bbd\u7535\u6d41\u63a7\u5236\u5668\u4e0b\u7684\u6b7b\u533a\u7578\u53d8",
    "Dead-time distortion and sensorless estimation": "\u6b7b\u533a\u7578\u53d8\u4e0e\u65e0\u4f20\u611f\u5668\u4f30\u8ba1",
    "Dead-time compensation": "\u6b7b\u533a\u8865\u507f",
    "MCAF per-phase dead-time compensation algorithm": "MCAF \u9010\u76f8\u6b7b\u533a\u8865\u507f\u7b97\u6cd5",
    "Behavior when disabled": "\u7981\u7528\u65f6\u7684\u884c\u4e3a",
    "Choice of parameters": "\u53c2\u6570\u9009\u62e9",
    "Experimental results": "\u5b9e\u9a8c\u7ed3\u679c",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "References": "\u53c2\u8003\u6587\u732e",
    # TOC
    "5.7. Dead-time Compensation": "5.7. \u6b7b\u533a\u8865\u507f",
    "5.7.1. Overview": "5.7.1. \u6982\u8ff0",
    "5.7.2. Definition and origin of dead time": "5.7.2. \u6b7b\u533a\u7684\u5b9a\u4e49\u548c\u6765\u6e90",
    "5.7.3. Dead-time distortion": "5.7.3. \u6b7b\u533a\u7578\u53d8",
    "5.7.3.1. Output voltage during dead time": "5.7.3.1. \u6b7b\u533a\u671f\u95f4\u7684\u8f93\u51fa\u7535\u538b",
    "5.7.3.2. Analysis of error bounds": "5.7.3.2. \u8bef\u5dee\u8fb9\u754c\u5206\u6790",
    "5.7.3.3. Behavior during discontinuous conduction": "5.7.3.3. \u65ad\u7eed\u5bfc\u901a\u671f\u95f4\u7684\u884c\u4e3a",
    "5.7.3.4. Dead-time distortion voltage in field-oriented current control": "5.7.3.4. \u77e2\u91cf\u7535\u6d41\u63a7\u5236\u4e2d\u7684\u6b7b\u533a\u7578\u53d8\u7535\u538b",
    "5.7.4. Practical effects of dead-time distortion": "5.7.4. \u6b7b\u533a\u7578\u53d8\u7684\u5b9e\u9645\u6548\u5e94",
    "5.7.4.1. Dead-time distortion and field-oriented current control": "5.7.4.1. \u6b7b\u533a\u7578\u53d8\u4e0e\u77e2\u91cf\u7535\u6d41\u63a7\u5236",
    "5.7.4.1.1. Dead-time distortion with low-bandwidth current controllers": "5.7.4.1.1. \u4f4e\u5e26\u5bbd\u7535\u6d41\u63a7\u5236\u5668\u4e0b\u7684\u6b7b\u533a\u7578\u53d8",
    "5.7.4.2. Dead-time distortion and sensorless estimation": "5.7.4.2. \u6b7b\u533a\u7578\u53d8\u4e0e\u65e0\u4f20\u611f\u5668\u4f30\u8ba1",
    "5.7.5. Dead-time compensation": "5.7.5. \u6b7b\u533a\u8865\u507f",
    "5.7.5.1. MCAF per-phase dead-time compensation algorithm": "5.7.5.1. MCAF \u9010\u76f8\u6b7b\u533a\u8865\u507f\u7b97\u6cd5",
    "5.7.5.2. Behavior when disabled": "5.7.5.2. \u7981\u7528\u65f6\u7684\u884c\u4e3a",
    "5.7.5.3. Choice of parameters": "5.7.5.3. \u53c2\u6570\u9009\u62e9",
    "5.7.5.3.1. Current linearity range": "5.7.5.3.1. \u7535\u6d41\u7ebf\u6027\u8303\u56f4",
    "5.7.5.3.2. Forward-path gain": "5.7.5.3.2. \u524d\u5411\u901a\u9053\u589e\u76ca",
    "5.7.5.3.3. Feedback-path gain": "5.7.5.3.3. \u53cd\u9988\u901a\u9053\u589e\u76ca",
    "5.7.5.4. Experimental results": "5.7.5.4. \u5b9e\u9a8c\u7ed3\u679c",
    "5.7.5.5. Implementation notes": "5.7.5.5. \u5b9e\u73b0\u8bf4\u660e",
    "5.7.6. References": "5.7.6. \u53c2\u8003\u6587\u732e",
    "Simple dynamic current limit": "\u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "Voltage Control": "\u7535\u538b\u63a7\u5236",
    # Key prose
    "Dead time is the delay during a": "\u6b7b\u533a\u662f\u5728",
    "cycle in which gate drive signals for both high-side and low-side transistors are inactive. This presents itself as a voltage distortion of roughly fixed amplitude and depends on the direction of phase current. In field-oriented control, this voltage distortion repeats six times per electrical cycle, with short transients near each zero-crossing of phase current.":
        "\u5468\u671f\u4e2d\u9ad8\u4fa7\u548c\u4f4e\u4fa7\u6676\u4f53\u7ba1\u7684\u6805\u9a71\u52a8\u4fe1\u53f7\u5747\u4e0d\u6d3b\u52a8\u7684\u5ef6\u8fdf\u3002\u8fd9\u8868\u73b0\u4e3a\u5e45\u503c\u5927\u81f4\u56fa\u5b9a\u7684\u7535\u538b\u7578\u53d8\uff0c\u5e76\u53d6\u51b3\u4e8e\u76f8\u7535\u6d41\u65b9\u5411\u3002\u5728\u77e2\u91cf\u63a7\u5236\u4e2d\uff0c\u6b64\u7535\u538b\u7578\u53d8\u5728\u6bcf\u4e2a\u7535\u6c14\u5468\u671f\u5185\u91cd\u590d\u516d\u6b21\uff0c\u5728\u76f8\u7535\u6d41\u6bcf\u6b21\u8fc7\u96f6\u9644\u8fd1\u6709\u77ed\u6682\u6682\u6001\u3002",
    "Dead-time compensation in MCAF can be used to counteract some of the dead-time distortion, both in the current control loop itself, and in the feedback signals used in":
        "MCAF \u4e2d\u7684\u6b7b\u533a\u8865\u507f\u53ef\u7528\u4e8e\u62b5\u6d88\u90e8\u5206\u6b7b\u533a\u7578\u53d8\uff0c\u65e2\u4f5c\u7528\u4e8e\u7535\u6d41\u63a7\u5236\u73af\u672c\u8eab\uff0c\u4e5f\u4f5c\u7528\u4e8e",
    "Three-phase bridge, consisting of three half-bridges driving motor terminals A, B, and C. Each half-bridge has a high-side and low-side transistor that can connect the corresponding motor terminal to either the positive or negative end of the DC link.":
        "\u4e09\u76f8\u6865\uff0c\u7531\u9a71\u52a8\u7535\u673a\u7aef\u5b50 A\u3001B \u548c C \u7684\u4e09\u4e2a\u534a\u6865\u7ec4\u6210\u3002\u6bcf\u4e2a\u534a\u6865\u6709\u4e00\u4e2a\u9ad8\u4fa7\u548c\u4f4e\u4fa7\u6676\u4f53\u7ba1\uff0c\u53ef\u4ee5\u5c06\u76f8\u5e94\u7684\u7535\u673a\u7aef\u5b50\u8fde\u63a5\u5230\u76f4\u6d41\u6bcd\u7ebf\u7684\u6b63\u6781\u6216\u8d1f\u6781\u3002",
    "An example of gate drive signals for one of the motor\u2019s half bridges":
        "\u7535\u673a\u67d0\u4e00\u534a\u6865\u7684\u6805\u9a71\u52a8\u4fe1\u53f7\u793a\u4f8b",
    "Effective duty cycle over an entire PWM period": "\u6574\u4e2a PWM \u5468\u671f\u5185\u7684\u6709\u6548\u5360\u7a7a\u6bd4",
    "Examples of nonlinear functions": "\u975e\u7ebf\u6027\u51fd\u6570\u793a\u4f8b",
    "Unit voltage disturbances from dead-time distortion. Per-phase components":
        "\u6b7b\u533a\u7578\u53d8\u4ea7\u751f\u7684\u5355\u4f4d\u7535\u538b\u6270\u52a8\u3002\u6bcf\u76f8\u5206\u91cf",
    "Characteristic": "\u7279\u6027",
    "Value": "\u503c",
    "D-axis peak disturbance": "D \u8f74\u5cf0\u503c\u6270\u52a8",
    "D-axis RMS disturbance": "D \u8f74\u6709\u6548\u503c\u6270\u52a8",
    "Q-axis peak disturbance": "Q \u8f74\u5cf0\u503c\u6270\u52a8",
    "Q-axis mean disturbance": "Q \u8f74\u5e73\u5747\u6270\u52a8",
    "Q-axis RMS disturbance": "Q \u8f74\u6709\u6548\u503c\u6270\u52a8",
    "Thermal simulation of a MOSFET dissipating 10W, R": "MOSFET \u4ee5 10W \u529f\u7387\u6563\u70ed\u7684\u70ed\u4eff\u771f\uff0cR",
    "= 0.4 K/W.": "= 0.4 K/W\u3002",
    "where": "\u5176\u4e2d",
    "and": "\u548c",
    "is the effective duty cycle,": "\u4e3a\u6709\u6548\u5360\u7a7a\u6bd4\uff0c",
    "is the desired duty cycle, and": "\u4e3a\u671f\u671b\u5360\u7a7a\u6bd4\uff0c",
    "is the effective duty cycle error. This error is caused by the dead time, and it is known as dead-time distortion.":
        "\u4e3a\u6709\u6548\u5360\u7a7a\u6bd4\u8bef\u5dee\u3002\u6b64\u8bef\u5dee\u7531\u6b7b\u533a\u5f15\u8d77\uff0c\u79f0\u4e3a\u6b7b\u533a\u7578\u53d8\u3002",
    "are shown, along with unit voltage disturbances": "\u5df2\u663e\u793a\uff0c\u8fd8\u6709\u9759\u6b62\u53c2\u8003\u5750\u6807\u7cfb\u4e2d\u7684\u5355\u4f4d\u7535\u538b\u6270\u52a8",
    "in the stationary reference frame, and": "\u548c\u540c\u6b65\u53c2\u8003\u5750\u6807\u7cfb\u4e2d\u7684",
    "in the synchronous frame": "\u5728\u540c\u6b65\u5750\u6807\u7cfb\u4e2d",
    "with amplitude": "\uff0c\u5e45\u503c\u4e3a",
    "with two degrees of freedom,": "\u7684\u7d2f\u79ef\u5206\u5e03\u51fd\u6570\uff08CDF\uff09\uff0c\u81ea\u7531\u5ea6\u4e3a 2\u3002",
    "chi-squared distribution": "\u5361\u65b9\u5206\u5e03",
    "There are three main methods for mitigating dead-time distortion, roughly in order of priority:":
        "\u6709\u4e09\u79cd\u4e3b\u8981\u65b9\u6cd5\u53ef\u4ee5\u51cf\u8f7b\u6b7b\u533a\u7578\u53d8\uff0c\u5927\u81f4\u6309\u4f18\u5148\u7ea7\u6392\u5e8f\uff1a",
    "Reduce the dead time.": "\u51cf\u5c0f\u6b7b\u533a\u3002",
    "This may be possible with careful gate drive design and testing.":
        "\u8fd9\u53ef\u80fd\u901a\u8fc7\u7cbe\u5fc3\u7684\u6805\u9a71\u52a8\u8bbe\u8ba1\u548c\u6d4b\u8bd5\u6765\u5b9e\u73b0\u3002",
    "Note:": "\u6ce8\u610f\uff1a",
    "Increase the current loop bandwidth.": "\u63d0\u9ad8\u7535\u6d41\u73af\u5e26\u5bbd\u3002",
    "Add voltage compensation.": "\u6dfb\u52a0\u7535\u538b\u8865\u507f\u3002",
    "Added in R6.": "\u5728 R6 \u4e2d\u6dfb\u52a0\u3002",
    "Output voltage of a half-bridge with inductive load during dead time. Delay times":
        "\u6b7b\u533a\u671f\u95f4\u611f\u6027\u8d1f\u8f7d\u4e0b\u534a\u6865\u7684\u8f93\u51fa\u7535\u538b\u3002\u5ef6\u8fdf\u65f6\u95f4",
    "represent the propagation delay between the edge of the gate drive signal, and the moment the transistor voltage starts to change.":
        "\u8868\u793a\u6805\u9a71\u52a8\u4fe1\u53f7\u8fb9\u6cbf\u4e0e\u6676\u4f53\u7ba1\u7535\u538b\u5f00\u59cb\u53d8\u5316\u65f6\u523b\u4e4b\u95f4\u7684\u4f20\u64ad\u5ef6\u8fdf\u3002",
    "Output voltage behavior during dead time, falling transition on phase voltage output. Faint purple indicates persistence over many captured traces.":
        "\u6b7b\u533a\u671f\u95f4\u7684\u8f93\u51fa\u7535\u538b\u884c\u4e3a\uff0c\u76f8\u7535\u538b\u8f93\u51fa\u4e0b\u964d\u6cbf\u3002\u6de1\u7d2b\u8272\u8868\u793a\u591a\u6b21\u6355\u83b7\u8f68\u8ff9\u7684\u4f59\u8f89\u3002",
    "Output voltage behavior during dead time, rising transition on phase voltage output. Faint purple indicates persistence over many captured traces.":
        "\u6b7b\u533a\u671f\u95f4\u7684\u8f93\u51fa\u7535\u538b\u884c\u4e3a\uff0c\u76f8\u7535\u538b\u8f93\u51fa\u4e0a\u5347\u6cbf\u3002\u6de1\u7d2b\u8272\u8868\u793a\u591a\u6b21\u6355\u83b7\u8f68\u8ff9\u7684\u4f59\u8f89\u3002",
    "Output voltage behavior during dead time, falling transition on phase voltage output for current near zero.":
        "\u6b7b\u533a\u671f\u95f4\u7684\u8f93\u51fa\u7535\u538b\u884c\u4e3a\uff0c\u7535\u6d41\u8fd1\u96f6\u65f6\u76f8\u7535\u538b\u8f93\u51fa\u4e0b\u964d\u6cbf\u3002",
    "Voltage plots in stationary and synchronous frames for various dead times.":
        "\u4e0d\u540c\u6b7b\u533a\u4e0b\u9759\u6b62\u548c\u540c\u6b65\u5750\u6807\u7cfb\u4e2d\u7684\u7535\u538b\u56fe\u3002",
    "Current plots in the stationary (\u03b1\u03b2) and synchronous (dq) frames for various dead times. The black circle (in the \u03b1\u03b2 frame) and dot (in the dq frame) represent average q-axis reference current; these are shown directly on top of the gray circle (\u03b1\u03b2 frame) and bar (dq) that represent the measured q-axis reference current, which fluctuates slightly with velocity and load changes.":
        "\u4e0d\u540c\u6b7b\u533a\u4e0b\u9759\u6b62\uff08\u03b1\u03b2\uff09\u548c\u540c\u6b65\uff08dq\uff09\u5750\u6807\u7cfb\u4e2d\u7684\u7535\u6d41\u56fe\u3002\u9ed1\u8272\u5706\uff08\u03b1\u03b2 \u5750\u6807\u7cfb\uff09\u548c\u70b9\uff08dq \u5750\u6807\u7cfb\uff09\u8868\u793a\u5e73\u5747 q \u8f74\u53c2\u8003\u7535\u6d41\uff1b\u8fd9\u4e9b\u76f4\u63a5\u663e\u793a\u5728\u4ee3\u8868\u6d4b\u91cf q \u8f74\u53c2\u8003\u7535\u6d41\u7684\u7070\u8272\u5706\uff08\u03b1\u03b2 \u5750\u6807\u7cfb\uff09\u548c\u6761\uff08dq\uff09\u4e0a\u65b9\uff0c\u540e\u8005\u968f\u901f\u5ea6\u548c\u8d1f\u8f7d\u53d8\u5316\u7565\u5fae\u6ce2\u52a8\u3002",
    "Current plots in the stationary and synchronous frames for various dead times. (See":
        "\u4e0d\u540c\u6b7b\u533a\u4e0b\u9759\u6b62\u548c\u540c\u6b65\u5750\u6807\u7cfb\u4e2d\u7684\u7535\u6d41\u56fe\u3002\uff08\u53c2\u89c1",
    "for more information about this type of graph.)": "\u4e86\u89e3\u6b64\u7c7b\u56fe\u7684\u66f4\u591a\u4fe1\u606f\u3002\uff09",
    "Voltage disturbances from dead-time distortion in stationary (\u03b1\u03b2) frame (left) and synchronous (dq) frame (right). This case represents large phase currents (so that discontinuous conduction can be neglected) with a desired voltage of some amplitude":
        "\u9759\u6b62\uff08\u03b1\u03b2\uff09\u5750\u6807\u7cfb\uff08\u5de6\uff09\u548c\u540c\u6b65\uff08dq\uff09\u5750\u6807\u7cfb\uff08\u53f3\uff09\u4e2d\u6b7b\u533a\u7578\u53d8\u7684\u7535\u538b\u6270\u52a8\u3002\u6b64\u60c5\u51b5\u8868\u793a\u5927\u76f8\u7535\u6d41\uff08\u53ef\u5ffd\u7565\u65ad\u7eed\u5bfc\u901a\uff09\uff0c\u671f\u671b\u7535\u538b\u5e45\u503c\u4e3a",
    "Dead-time compensation in MCAF, in context of the main FOC block diagram.":
        "MCAF \u4e2d\u7684\u6b7b\u533a\u8865\u507f\uff0c\u5728\u4e3b FOC \u6846\u56fe\u7684\u4e0a\u4e0b\u6587\u4e2d\u3002",
    "Per-phase dead-time compensation in MCAF.": "MCAF \u4e2d\u7684\u9010\u76f8\u6b7b\u533a\u8865\u507f\u3002",
    "A block diagram of the dead-time compensation module": "\u6b7b\u533a\u8865\u507f\u6a21\u5757",
    "Characteristics of the unit dead-time distortion voltage": "\u5355\u4f4d\u6b7b\u533a\u7578\u53d8\u7535\u538b\u7684\u7279\u6027",
    "From top to bottom:": "\u4ece\u4e0a\u5230\u4e0b\uff1a",
    "There are two main areas in which dead-time distortion is detrimental to motor control:":
        "\u6b7b\u533a\u7578\u53d8\u5728\u4e24\u4e2a\u4e3b\u8981\u65b9\u9762\u5bf9\u7535\u673a\u63a7\u5236\u6709\u5bb3\uff1a",
    "The effects of dead-time distortion change as velocity increases.":
        "\u6b7b\u533a\u7578\u53d8\u7684\u6548\u5e94\u968f\u901f\u5ea6\u589e\u52a0\u800c\u53d8\u5316\u3002",
    "The total resulting voltage shifts are consistent with the figures.":
        "\u603b\u7535\u538b\u504f\u79fb\u4e0e\u56fe\u4e2d\u7684\u503c\u4e00\u81f4\u3002",
    "We can take similar measurements for a low-bandwidth current controller.":
        "\u6211\u4eec\u53ef\u4ee5\u5bf9\u4f4e\u5e26\u5bbd\u7535\u6d41\u63a7\u5236\u5668\u8fdb\u884c\u7c7b\u4f3c\u7684\u6d4b\u91cf\u3002",
    "sigmoid function": "S \u578b\u51fd\u6570",
    "AN1292 PLL": "AN1292 PLL",
    "Position and velocity estimators": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668",
    "forward path": "\u524d\u5411\u901a\u9053",
    "Computation of estimated unit disturbance signals": "\u8ba1\u7b97\u4f30\u8ba1\u5355\u4f4d\u6270\u52a8\u4fe1\u53f7",
    "Computation of feedback-path dead-time compensation vector": "\u8ba1\u7b97\u53cd\u9988\u901a\u9053\u6b7b\u533a\u8865\u507f\u77e2\u91cf",
    "Computation of forward-path dead-time compensation vector": "\u8ba1\u7b97\u524d\u5411\u901a\u9053\u6b7b\u533a\u8865\u507f\u77e2\u91cf",
    "as a per-phase set.": "\u4f5c\u4e3a\u9010\u76f8\u96c6\u3002",
    "from estimated unit disturbance signals": "\u4ece\u4f30\u8ba1\u5355\u4f4d\u6270\u52a8\u4fe1\u53f7",
    "in the stationary frame": "\u5728\u9759\u6b62\u5750\u6807\u7cfb\u4e2d",
    "calculating estimator feedback voltages": "\u8ba1\u7b97\u4f30\u8ba1\u5668\u53cd\u9988\u7535\u538b",
    "still executes, but compensation values": "\u4ecd\u7136\u6267\u884c\uff0c\u4f46\u8865\u507f\u503c",
    "are set to zero.": "\u88ab\u8bbe\u4e3a\u96f6\u3002",
    "Current linearity range": "\u7535\u6d41\u7ebf\u6027\u8303\u56f4",
    "as a fraction of fullscale current": "\u4f5c\u4e3a\u6ee1\u91cf\u7a0b\u7535\u6d41\u7684\u6bd4\u4f8b",
    "Forward-path gain": "\u524d\u5411\u901a\u9053\u589e\u76ca",
    "Feedback-path gain": "\u53cd\u9988\u901a\u9053\u589e\u76ca",
    "The forward and feedback gains are selected as a proportion of the expected dead time.":
        "\u524d\u5411\u548c\u53cd\u9988\u589e\u76ca\u4f5c\u4e3a\u9884\u671f\u6b7b\u533a\u7684\u6bd4\u4f8b\u6765\u9009\u62e9\u3002",
    "The guidance in this section is preliminary and is based on available testing so far. Future work may help improve this guidance.":
        "\u672c\u8282\u4e2d\u7684\u6307\u5357\u662f\u521d\u6b65\u7684\uff0c\u57fa\u4e8e\u76ee\u524d\u53ef\u7528\u7684\u6d4b\u8bd5\u3002\u672a\u6765\u7684\u5de5\u4f5c\u53ef\u80fd\u6709\u52a9\u4e8e\u6539\u5584\u6b64\u6307\u5357\u3002",
    "Some experimental data showing the improvement from feedback-path dead-time compensation is shown below in":
        "\u4e00\u4e9b\u663e\u793a\u53cd\u9988\u901a\u9053\u6b7b\u533a\u8865\u507f\u6539\u5584\u6548\u679c\u7684\u5b9e\u9a8c\u6570\u636e\u5982\u4e0b",
    "Fixed gain scaling factor": "\u56fa\u5b9a\u589e\u76ca\u7f29\u653e\u56e0\u5b50",
    "The preceding sections have applied to a single half-bridge with inductive load. In field-oriented current control of a three-phase motor, the transformation of the dead-time voltage distortion into the synchronous (dq) frame is of interest, since this is the disturbance \u201cseen\u201d by the motor.":
        "\u524d\u9762\u7684\u5404\u8282\u9002\u7528\u4e8e\u5355\u4e2a\u534a\u6865\u5e26\u611f\u6027\u8d1f\u8f7d\u7684\u60c5\u51b5\u3002\u5728\u4e09\u76f8\u7535\u673a\u7684\u77e2\u91cf\u7535\u6d41\u63a7\u5236\u4e2d\uff0c\u6b7b\u533a\u7535\u538b\u7578\u53d8\u8f6c\u6362\u5230\u540c\u6b65\uff08dq\uff09\u5750\u6807\u7cfb\u662f\u6709\u610f\u4e49\u7684\uff0c\u56e0\u4e3a\u8fd9\u662f\u7535\u673a\u201c\u770b\u5230\u201d\u7684\u6270\u52a8\u3002",
    "In FOC, the current controllers operate in the synchronous (dq) reference frame. Dead-time distortion causes a voltage disturbance to the current controllers at":
        "\u5728 FOC \u4e2d\uff0c\u7535\u6d41\u63a7\u5236\u5668\u5728\u540c\u6b65\uff08dq\uff09\u53c2\u8003\u5750\u6807\u7cfb\u4e2d\u8fd0\u884c\u3002\u6b7b\u533a\u7578\u53d8\u5728",
    "(six times the electrical frequency) that occurs around each zero-crossing of phase current.":
        "\uff08\u516d\u500d\u7535\u6c14\u9891\u7387\uff09\u5904\u5bf9\u7535\u6d41\u63a7\u5236\u5668\u4ea7\u751f\u7535\u538b\u6270\u52a8\uff0c\u51fa\u73b0\u5728\u76f8\u7535\u6d41\u6bcf\u6b21\u8fc7\u96f6\u9644\u8fd1\u3002",
    "At low velocity, the current controllers will eventually regain zero steady-state error after each transient. The disturbance shown on the right of":
        "\u5728\u4f4e\u901f\u65f6\uff0c\u7535\u6d41\u63a7\u5236\u5668\u6700\u7ec8\u4f1a\u5728\u6bcf\u6b21\u6682\u6682\u540e\u6062\u590d\u96f6\u7a33\u6001\u8bef\u5dee\u3002",
    "must be counteracted by an increase in voltage of opposite sign:":
        "\u53f3\u4fa7\u6240\u793a\u7684\u6270\u52a8\u5fc5\u987b\u901a\u8fc7\u589e\u52a0\u76f8\u53cd\u7b26\u53f7\u7684\u7535\u538b\u6765\u62b5\u6d88\uff1a",
    "The average reduction in q-axis voltage at the motor must be canceled by the q-axis current controller increasing its voltage by the same amount":
        "\u7535\u673a\u5904 q \u8f74\u7535\u538b\u7684\u5e73\u5747\u964d\u4f4e\u5fc5\u987b\u7531 q \u8f74\u7535\u6d41\u63a7\u5236\u5668\u589e\u52a0\u76f8\u540c\u6570\u91cf\u7684\u7535\u538b\u6765\u62b5\u6d88",
    "The d-axis disturbance, roughly a linear ramp, must be canceled by the d-axis current controller with a change in controller output in the opposite direction.":
        "d \u8f74\u6270\u52a8\u7ea6\u4e3a\u7ebf\u6027\u659c\u5761\uff0c\u5fc5\u987b\u7531 d \u8f74\u7535\u6d41\u63a7\u5236\u5668\u4ee5\u76f8\u53cd\u65b9\u5411\u7684\u63a7\u5236\u5668\u8f93\u51fa\u53d8\u5316\u6765\u62b5\u6d88\u3002",
    "At high velocity, the changes in output voltage required to counteract the dead-time voltage distortion occur fast enough and often enough that the current controllers are unable to cancel the distortion completely.":
        "\u5728\u9ad8\u901f\u65f6\uff0c\u62b5\u6d88\u6b7b\u533a\u7535\u538b\u7578\u53d8\u6240\u9700\u7684\u8f93\u51fa\u7535\u538b\u53d8\u5316\u53d1\u751f\u5f97\u8db3\u591f\u5feb\u4e14\u8db3\u591f\u9891\u7e41\uff0c\u4ee5\u81f4\u4e8e\u7535\u6d41\u63a7\u5236\u5668\u65e0\u6cd5\u5b8c\u5168\u62b5\u6d88\u7578\u53d8\u3002",
    "Most sensorless estimators are less sensitive to q-axis voltage errors, which affect only the amplitude of the estimated back-emf vector once the estimator has locked onto it), and more sensitive to d-axis voltage errors, which perturb the angle of the estimated back-emf vector.":
        "\u5927\u591a\u6570\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u5bf9 q \u8f74\u7535\u538b\u8bef\u5dee\u8f83\u4e0d\u654f\u611f\uff08\u4e00\u65e6\u4f30\u8ba1\u5668\u9501\u5b9a\uff0c\u5b83\u4eec\u53ea\u5f71\u54cd\u4f30\u8ba1\u53cd\u7535\u52a8\u52bf\u77e2\u91cf\u7684\u5e45\u503c\uff09\uff0c\u800c\u5bf9 d \u8f74\u7535\u538b\u8bef\u5dee\u66f4\u654f\u611f\uff08\u5b83\u4eec\u6270\u52a8\u4f30\u8ba1\u53cd\u7535\u52a8\u52bf\u77e2\u91cf\u7684\u89d2\u5ea6\uff09\u3002",
    "Dead-time compensation can improve the performance of sensorless estimators at low velocities, by correcting the estimated back-emf for the effects of dead-time distortion.":
        "\u6b7b\u533a\u8865\u507f\u53ef\u4ee5\u901a\u8fc7\u4fee\u6b63\u6b7b\u533a\u7578\u53d8\u5bf9\u4f30\u8ba1\u53cd\u7535\u52a8\u52bf\u7684\u5f71\u54cd\uff0c\u6539\u5584\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u5728\u4f4e\u901f\u4e0b\u7684\u6027\u80fd\u3002",
    "do not assume that dead time is adequate based only on testing one sample of a motor drive board at room temperature! Attempts to minimize the dead time, while still protecting against shoot-through, require a detailed understanding of the switching transient\u2019s sensitivity to temperature, duty cycle, current, and part-to-part variation of the transistors and the gate drive circuitry.":
        "\u4e0d\u8981\u4ec5\u57fa\u4e8e\u5728\u5ba4\u6e29\u4e0b\u6d4b\u8bd5\u4e00\u4e2a\u7535\u673a\u9a71\u52a8\u677f\u6837\u54c1\u5c31\u5047\u5b9a\u6b7b\u533a\u8db3\u591f\uff01\u5c1d\u8bd5\u6700\u5c0f\u5316\u6b7b\u533a\u540c\u65f6\u4ecd\u4fdd\u62a4\u514d\u76f4\u901a\uff0c\u9700\u8981\u5bf9\u5f00\u5173\u6682\u6682\u5bf9\u6e29\u5ea6\u3001\u5360\u7a7a\u6bd4\u3001\u7535\u6d41\u4ee5\u53ca\u6676\u4f53\u7ba1\u548c\u6805\u9a71\u52a8\u7535\u8def\u7684\u5668\u4ef6\u95f4\u5dee\u5f02\u7684\u654f\u611f\u6027\u6709\u8be6\u7ec6\u4e86\u89e3\u3002",
    "This inherently compensates for dead-time distortion, at least at electrical frequencies below the current loop bandwidth. As discussed above,":
        "\u8fd9\u672c\u8d28\u4e0a\u8865\u507f\u4e86\u6b7b\u533a\u7578\u53d8\uff0c\u81f3\u5c11\u5bf9\u4e8e\u4f4e\u4e8e\u7535\u6d41\u73af\u5e26\u5bbd\u7684\u7535\u6c14\u9891\u7387\u5982\u6b64\u3002\u5982\u4e0a\u6240\u8ff0\uff0c",
    "low-bandwidth current control loops are unable to counteract the effects of dead-time distortion.":
        "\u4f4e\u5e26\u5bbd\u7535\u6d41\u63a7\u5236\u73af\u65e0\u6cd5\u62b5\u6d88\u6b7b\u533a\u7578\u53d8\u7684\u6548\u5e94\u3002",
    "Although this is the least desirable of the three methods, it can potentially reduce the effects of dead-time distortion.":
        "\u5c3d\u7ba1\u8fd9\u662f\u4e09\u79cd\u65b9\u6cd5\u4e2d\u6700\u4e0d\u7406\u60f3\u7684\uff0c\u4f46\u5b83\u53ef\u4ee5\u6f5c\u5728\u5730\u51cf\u8f7b\u6b7b\u533a\u7578\u53d8\u7684\u6548\u5e94\u3002",
    "The voltage compensation method available in MCAF is based on per-phase estimates of the dead-time distortion voltage, added to the":
        "MCAF \u4e2d\u53ef\u7528\u7684\u7535\u538b\u8865\u507f\u65b9\u6cd5\u57fa\u4e8e\u6b7b\u533a\u7578\u53d8\u7535\u538b\u7684\u9010\u76f8\u4f30\u8ba1\uff0c\u6dfb\u52a0\u5230",
    "of the current control loop, and the feedback path of the position and velocity estimator. This is known as the \u201cper-phase\u201d method and can be selected in the Customize page of motorBench":
        "\u7535\u6d41\u63a7\u5236\u73af\u7684\u524d\u5411\u901a\u9053\uff0c\u4ee5\u53ca\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668\u7684\u53cd\u9988\u901a\u9053\u3002\u8fd9\u88ab\u79f0\u4e3a\u201c\u9010\u76f8\u201d\u65b9\u6cd5\uff0c\u53ef\u4ee5\u5728 motorBench",
    "Development Suite.": "Development Suite \u7684\u81ea\u5b9a\u4e49\u9875\u9762\u4e2d\u9009\u62e9\u3002",
    "If the \u201cNone\u201d variant of dead-time compensation is chosen in the Customize page of motorBench":
        "\u5982\u679c\u5728 motorBench",
    "Each of the three parameters may be adjusted:":
        "\u4e09\u4e2a\u53c2\u6570\u5747\u53ef\u8c03\u6574\uff1a",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
