# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/qei_sync/align-sweep"
title_zh = "5.4.3.3.3. \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "Align-and-sweep method": "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5",
    "Overview": "\u6982\u8ff0",
    "The align-and-sweep method is a slight modification to the": "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u662f\u5bf9",
    "align method": "\u5bf9\u9f50\u65b9\u6cd5",
    ". Instead of a fixed angle during the align state, the applied electrical angle is slowly rotated for one full mechanical cycle in both directions, and a commutation offset is estimated by taking an average angle difference between applied and measured angle over these two cycles. (The same calculation is used as in the align method, but a mean value over many measurements is used instead of a single measurement.) The intent is that by covering a complete mechanical rotation, angle variations due to cogging torque would be averaged out. Averaging over both positive and negative rotation cancels out most of the impact of friction torque.":
        "\u7684\u4e00\u4e2a\u5c0f\u6539\u52a8\u3002\u4e0d\u662f\u5728\u5bf9\u9f50\u72b6\u6001\u4e0b\u4f7f\u7528\u56fa\u5b9a\u89d2\u5ea6\uff0c\u800c\u662f\u5c06\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u5728\u4e24\u4e2a\u65b9\u5411\u4e0a\u7f13\u6162\u65cb\u8f6c\u4e00\u4e2a\u5b8c\u6574\u7684\u673a\u68b0\u5468\u671f\uff0c\u901a\u8fc7\u5728\u8fd9\u4e24\u4e2a\u5468\u671f\u5185\u53d6\u65bd\u52a0\u89d2\u5ea6\u4e0e\u6d4b\u91cf\u89d2\u5ea6\u4e4b\u5dee\u7684\u5e73\u5747\u503c\u6765\u4f30\u8ba1\u6362\u76f8\u504f\u79fb\u3002\uff08\u4f7f\u7528\u4e0e\u5bf9\u9f50\u65b9\u6cd5\u76f8\u540c\u7684\u8ba1\u7b97\uff0c\u4f46\u4f7f\u7528\u591a\u6b21\u6d4b\u91cf\u7684\u5e73\u5747\u503c\u4ee3\u66ff\u5355\u6b21\u6d4b\u91cf\u3002\uff09\u5176\u76ee\u7684\u662f\u901a\u8fc7\u8986\u76d6\u5b8c\u6574\u7684\u673a\u68b0\u8f6e\uff0c\u5c06\u9f7f\u69fd\u8f6c\u77e9\u5bfc\u81f4\u7684\u89d2\u5ea6\u53d8\u5316\u5e73\u5747\u6389\u3002\u5728\u6b63\u5411\u548c\u53cd\u5411\u65cb\u8f6c\u4e0a\u53d6\u5e73\u5747\u53ef\u4ee5\u6d88\u9664\u5927\u90e8\u5206\u6469\u64e6\u8f6c\u77e9\u7684\u5f71\u54cd\u3002",
    "The resulting commutation offset has extremely good": "\u5f97\u5230\u7684\u6362\u76f8\u504f\u79fb\u5177\u6709\u6781\u597d\u7684",
    "accuracy and repeatability behavior": "\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u8868\u73b0",
    ". It takes more time, however, than the simple align method, and is slightly more complex.":
        "\u3002\u7136\u800c\uff0c\u5b83\u6bd4\u7b80\u5355\u7684\u5bf9\u9f50\u65b9\u6cd5\u9700\u8981\u66f4\u591a\u65f6\u95f4\uff0c\u4e14\u7565\u5fae\u590d\u6742\u4e00\u4e9b\u3002",
    "Limitations": "\u5c40\u9650\u6027",
    "The": "\u5bf9\u9f50\u65b9\u6cd5\u7684",
    "limitations of the align method": "\u5c40\u9650\u6027",
    ", namely torque disturbances and semistable equilibrium, are less of an impact in the align-and-sweep method. Disturbance torques can still cause measurement error, however, and should be avoided.":
        "\uff0c\u5373\u8f6c\u77e9\u6270\u52a8\u548c\u534a\u7a33\u5b9a\u5e73\u8861\uff0c\u5728\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4e2d\u7684\u5f71\u54cd\u8f83\u5c0f\u3002\u7136\u800c\uff0c\u6270\u52a8\u8f6c\u77e9\u4ecd\u53ef\u80fd\u5bfc\u81f4\u6d4b\u91cf\u8bef\u5dee\uff0c\u5e94\u5c3d\u91cf\u907f\u514d\u3002",
    "Practical implementation issues": "\u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "Rampup and align angles are not particularly important to this algorithm.":
        "Rampup \u548c\u5bf9\u9f50\u89d2\u5ea6\u5bf9\u6b64\u7b97\u6cd5\u4e0d\u662f\u7279\u522b\u91cd\u8981\u3002",
    "With this method, initial alignment transients need to settle before making measurements. Alignment transients occur with any acceleration, so reversing the rotation direction causes a transient, as well as changing from no motion to the slow electrical rotation.":
        "\u5728\u6b64\u65b9\u6cd5\u4e2d\uff0c\u9700\u8981\u5728\u6d4b\u91cf\u524d\u4f7f\u521d\u59cb\u5bf9\u9f50\u77ac\u53d8\u7a33\u5b9a\u4e0b\u6765\u3002\u4efb\u4f55\u52a0\u901f\u90fd\u4f1a\u4ea7\u751f\u5bf9\u9f50\u77ac\u53d8\uff0c\u56e0\u6b64\u53cd\u8f6c\u65cb\u8f6c\u65b9\u5411\u4f1a\u4ea7\u751f\u77ac\u53d8\uff0c\u4ece\u9759\u6b62\u5230\u7f13\u6162\u7535\u6c14\u65cb\u8f6c\u7684\u53d8\u5316\u4e5f\u4f1a\u4ea7\u751f\u77ac\u53d8\u3002",
    "To manage these transients, the align-and-sweep method includes \u201csetup\u201d intervals. During the setup intervals, angular frequency is kept constant and allows alignment transients to settle, prior to the beginning of measurement intervals.":
        "\u4e3a\u4e86\u7ba1\u7406\u8fd9\u4e9b\u77ac\u53d8\uff0c\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5305\u542b\u201c\u8bbe\u7f6e\u201d\u533a\u95f4\u3002\u5728\u8bbe\u7f6e\u533a\u95f4\u5185\uff0c\u89d2\u9891\u7387\u4fdd\u6301\u6052\u5b9a\uff0c\u5141\u8bb8\u5bf9\u9f50\u77ac\u53d8\u5728\u6d4b\u91cf\u533a\u95f4\u5f00\u59cb\u524d\u7a33\u5b9a\u4e0b\u6765\u3002",
    "Selection of rotation rate": "\u65cb\u8f6c\u901f\u7387\u7684\u9009\u62e9",
    "MCAF R4 allows three choices of rotation rate during the align-and-sweep method: 1, 2, and 4 counts per control ISR, where each count is 1/65536 of an electrical cycle \u2248 0.0055\u00b0. The 4-count option is fastest, and the 1-count option is slowest.":
        "MCAF R4 \u5141\u8bb8\u5728\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u671f\u95f4\u9009\u62e9\u4e09\u79cd\u65cb\u8f6c\u901f\u7387\uff1a\u6bcf\u63a7\u5236 ISR 1\u30012 \u548c 4 \u4e2a\u8108\u51b2\uff0c\u5176\u4e2d\u6bcf\u4e2a\u8108\u51b2\u4e3a\u7535\u6c14\u5468\u671f\u7684 1/65536 \u2248 0.0055\u00b0\u30024 \u8108\u51b2\u9009\u9879\u6700\u5feb\uff0c1 \u8108\u51b2\u9009\u9879\u6700\u6162\u3002",
    "There are tradeoffs between rotation speed and accuracy. Running the align-and-sweep method at higher rotation speeds will complete the measurement more quickly, but will experience larger angle fluctuations, and the resulting angle offset may have more random errors. Slower rotation speeds will improve accuracy, but will increase the measurement time.":
        "\u65cb\u8f6c\u901f\u5ea6\u548c\u7cbe\u5ea6\u4e4b\u95f4\u5b58\u5728\u6743\u8861\u3002\u4ee5\u66f4\u9ad8\u7684\u65cb\u8f6c\u901f\u5ea6\u8fd0\u884c\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5c06\u66f4\u5feb\u5b8c\u6210\u6d4b\u91cf\uff0c\u4f46\u4f1a\u7ecf\u5386\u66f4\u5927\u7684\u89d2\u5ea6\u6ce2\u52a8\uff0c\u7ed3\u679c\u89d2\u5ea6\u504f\u79fb\u53ef\u80fd\u6709\u66f4\u591a\u7684\u968f\u673a\u8bef\u5dee\u3002\u66f4\u4f4e\u7684\u65cb\u8f6c\u901f\u5ea6\u5c06\u63d0\u9ad8\u7cbe\u5ea6\uff0c\u4f46\u4f1a\u589e\u52a0\u6d4b\u91cf\u65f6\u95f4\u3002",
    "Calculations involving angles": "\u6d89\u53ca\u89d2\u5ea6\u7684\u8ba1\u7b97",
    "Averaging measurements of angles, which involve wraparound semantics, can be tricky, since the calculations involve \u201cgood\u201d and \u201cbad\u201d overflows that must be distinguished, and avoiding overflow does not necessarily guarantee a correct result. As an example, suppose we wish to find the average value of the following sequence of angles: +176\u00b0, -170\u00b0, -174\u00b0, -167\u00b0, +177\u00b0. A simple mean value calculation will come up with -31.6\u00b0, which is not correct. There are at least two ways to handle this issue:":
        "\u5bf9\u6d89\u53ca\u56de\u7ed5\u8bed\u4e49\u7684\u89d2\u5ea6\u6d4b\u91cf\u503c\u53d6\u5e73\u5747\u53ef\u80fd\u5f88\u68d8\u624b\uff0c\u56e0\u4e3a\u8ba1\u7b97\u4e2d\u6d89\u53ca\u5fc5\u987b\u533a\u5206\u7684\u201c\u597d\u201d\u548c\u201c\u574f\u201d\u6ea2\u51fa\uff0c\u4e14\u907f\u514d\u6ea2\u51fa\u5e76\u4e0d\u4e00\u5b9a\u4fdd\u8bc1\u7ed3\u679c\u6b63\u786e\u3002\u4f5c\u4e3a\u793a\u4f8b\uff0c\u5047\u8bbe\u6211\u4eec\u5e0c\u671b\u627e\u5230\u4ee5\u4e0b\u89d2\u5ea6\u5e8f\u5217\u7684\u5e73\u5747\u503c\uff1a+176\u00b0\u3001-170\u00b0\u3001-174\u00b0\u3001-167\u00b0\u3001+177\u00b0\u3002\u7b80\u5355\u7684\u5747\u503c\u8ba1\u7b97\u5c06\u5f97\u5230 -31.6\u00b0\uff0c\u8fd9\u662f\u4e0d\u6b63\u786e\u7684\u3002\u6709\u81f3\u5c11\u4e24\u79cd\u65b9\u6cd5\u53ef\u4ee5\u5904\u7406\u6b64\u95ee\u9898\uff1a",
    "Unwrap the angles prior to averaging.": "\u5728\u53d6\u5e73\u5747\u4e4b\u524d\u5c55\u5f00\u89d2\u5ea6\u3002",
    "\u201cUnwrap\u201d here means to translate small angle changes so that the angle values remain equivalent, but are adjusted by an integer number of rotations so that there is never a jump across the branch point of \u00b1180\u00b0. In the example sequence above, unwrapping the angles would produce the sequence +176\u00b0, +190\u00b0, +186\u00b0, +193\u00b0, +177\u00b0, which yields the correct average of +184.4\u00b0 = -175.6\u00b0.":
        "\u201c\u5c55\u5f00\u201d\u5728\u8fd9\u91cc\u610f\u5473\u7740\u5c06\u5c0f\u89d2\u5ea6\u53d8\u5316\u8f6c\u6362\u4e3a\u4fdd\u6301\u89d2\u5ea6\u503c\u7b49\u4ef7\u4f46\u8c03\u6574\u6574\u6570\u8f6c\u6570\uff0c\u4ee5\u4fbf\u6c38\u8fdc\u4e0d\u4f1a\u8df3\u8fc7 \u00b1180\u00b0 \u7684\u5206\u652f\u70b9\u3002\u5728\u4e0a\u9762\u7684\u793a\u4f8b\u5e8f\u5217\u4e2d\uff0c\u5c55\u5f00\u89d2\u5ea6\u5c06\u4ea7\u751f\u5e8f\u5217 +176\u00b0\u3001+190\u00b0\u3001+186\u00b0\u3001+193\u00b0\u3001+177\u00b0\uff0c\u5f97\u5230\u6b63\u786e\u7684\u5e73\u5747\u503c +184.4\u00b0 = -175.6\u00b0\u3002",
    "Offset the angles prior to averaging.": "\u5728\u53d6\u5e73\u5747\u4e4b\u524d\u504f\u79fb\u89d2\u5ea6\u3002",
    "One simple way to avoid jumps across the branch point is to move the branch point by a fixed offset. We can use an offset that subtracts out the first measurement, and as long as the net change in angle from this first measurement stays below 180\u00b0, then it will not cross the branch point. In the example sequence above, an offset of -176\u00b0 (the negation of the first measurement) is used, and the resulting sequence becomes 0, +14\u00b0, +10\u00b0, +17\u00b0, +1\u00b0, which has an average of +8.4\u00b0; add back the first measurement of +176\u00b0 and we get +176\u00b0 + 8.4\u00b0 = -175.6\u00b0.":
        "\u907f\u514d\u8df3\u8fc7\u5206\u652f\u70b9\u7684\u4e00\u79cd\u7b80\u5355\u65b9\u6cd5\u662f\u901a\u8fc7\u56fa\u5b9a\u504f\u79fb\u79fb\u52a8\u5206\u652f\u70b9\u3002\u6211\u4eec\u53ef\u4ee5\u4f7f\u7528\u51cf\u53bb\u7b2c\u4e00\u6b21\u6d4b\u91cf\u503c\u7684\u504f\u79fb\uff0c\u53ea\u8981\u4ece\u7b2c\u4e00\u6b21\u6d4b\u91cf\u7684\u89d2\u5ea6\u51c0\u53d8\u5316\u4fdd\u6301\u5728 180\u00b0 \u4ee5\u4e0b\uff0c\u5c31\u4e0d\u4f1a\u8de8\u8fc7\u5206\u652f\u70b9\u3002\u5728\u4e0a\u9762\u7684\u793a\u4f8b\u5e8f\u5217\u4e2d\uff0c\u4f7f\u7528 -176\u00b0 \u7684\u504f\u79fb\uff08\u7b2c\u4e00\u6b21\u6d4b\u91cf\u503c\u7684\u8d1f\u503c\uff09\uff0c\u7ed3\u679c\u5e8f\u5217\u53d8\u4e3a 0\u3001+14\u00b0\u3001+10\u00b0\u3001+17\u00b0\u3001+1\u00b0\uff0c\u5e73\u5747\u503c\u4e3a +8.4\u00b0\uff1b\u52a0\u56de\u7b2c\u4e00\u6b21\u6d4b\u91cf\u503c +176\u00b0 \u5f97\u5230 +176\u00b0 + 8.4\u00b0 = -175.6\u00b0\u3002",
    "In the align-and-sweep method, the offset approach is used rather than the unwrap approach; the offset approach is less complex, and requires less memory to avoid overflow.":
        "\u5728\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4e2d\uff0c\u4f7f\u7528\u504f\u79fb\u65b9\u6cd5\u800c\u975e\u5c55\u5f00\u65b9\u6cd5\uff1b\u504f\u79fb\u65b9\u6cd5\u590d\u6742\u6027\u8f83\u4f4e\uff0c\u4e14\u9700\u8981\u66f4\u5c11\u7684\u5185\u5b58\u6765\u907f\u514d\u6ea2\u51fa\u3002",
    "State machine": "\u72b6\u6001\u673a",
    "To manage the setup and measurement intervals, the align-and-sweep method includes a simple state machine that runs through a fixed sequence:":
        "\u4e3a\u4e86\u7ba1\u7406\u8bbe\u7f6e\u548c\u6d4b\u91cf\u533a\u95f4\uff0c\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5305\u542b\u4e00\u4e2a\u7b80\u5355\u7684\u72b6\u6001\u673a\uff0c\u6309\u56fa\u5b9a\u5e8f\u5217\u8fd0\u884c\uff1a",
    "\u2014 records initial angle measurement to use as a reference point for avoiding wraparound problems.":
        "\u2014 \u8bb0\u5f55\u521d\u59cb\u89d2\u5ea6\u6d4b\u91cf\u503c\uff0c\u4f5c\u4e3a\u907f\u514d\u56de\u7ed5\u95ee\u9898\u7684\u53c2\u8003\u70b9\u3002",
    "\u2014 begins slow rotation of applied electrical angle in a positive direction, over a specified angle interval.":
        "\u2014 \u5f00\u59cb\u5728\u6b63\u65b9\u5411\u4e0a\u7f13\u6162\u65cb\u8f6c\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\uff0c\u8d8a\u8fc7\u6307\u5b9a\u7684\u89d2\u5ea6\u533a\u95f4\u3002",
    "\u2014 computes and accumulates the angle difference between the applied angle and the measured encoder angle. Continues slow positive rotation over one complete mechanical cycle.":
        "\u2014 \u8ba1\u7b97\u5e76\u7d2f\u52a0\u65bd\u52a0\u89d2\u5ea6\u4e0e\u6d4b\u91cf\u7684\u7f16\u7801\u5668\u89d2\u5ea6\u4e4b\u95f4\u7684\u89d2\u5ea6\u5dee\u3002\u7ee7\u7eed\u6b63\u65b9\u5411\u7f13\u6162\u65cb\u8f6c\u4e00\u4e2a\u5b8c\u6574\u7684\u673a\u68b0\u5468\u671f\u3002",
    "\u2014 begins slow rotation of applied electrical angle in a negative direction, over a specified angle interval.":
        "\u2014 \u5f00\u59cb\u5728\u53cd\u65b9\u5411\u4e0a\u7f13\u6162\u65cb\u8f6c\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\uff0c\u8d8a\u8fc7\u6307\u5b9a\u7684\u89d2\u5ea6\u533a\u95f4\u3002",
    "\u2014 computes and accumulates the angle difference between the applied angle and the measured encoder angle. Continues slow negative rotation over one complete mechanical cycle.":
        "\u2014 \u8ba1\u7b97\u5e76\u7d2f\u52a0\u65bd\u52a0\u89d2\u5ea6\u4e0e\u6d4b\u91cf\u7684\u7f16\u7801\u5668\u89d2\u5ea6\u4e4b\u95f4\u7684\u89d2\u5ea6\u5dee\u3002\u7ee7\u7eed\u53cd\u65b9\u5411\u7f13\u6162\u65cb\u8f6c\u4e00\u4e2a\u5b8c\u6574\u7684\u673a\u68b0\u5468\u671f\u3002",
    "\u2014 leaves electrical angle alone, allows the": "\u2014 \u4fdd\u7559\u7535\u6c14\u89d2\u5ea6\u4e0d\u53d8\uff0c\u5141\u8bb8",
    "startup sequence": "\u542f\u52a8\u5e8f\u5217",
    "to continue past the align state.": "\u7ee7\u7eed\u901a\u8fc7\u5bf9\u9f50\u72b6\u6001\u3002",
    "While in all states other than the": "\u9664\u4e86\u5728",
    "state, the": "\u72b6\u6001\u4e4b\u5916\u7684\u6240\u6709\u72b6\u6001\u4e2d\uff0c",
    "is held in the align state in order to complete the synchronization steps.":
        "\u88ab\u4fdd\u6301\u5728\u5bf9\u9f50\u72b6\u6001\u4e2d\uff0c\u4ee5\u5b8c\u6210\u540c\u6b65\u6b65\u9aa4\u3002",
    "Example data": "\u793a\u4f8b\u6570\u636e",
    "shows the use of the align-and-sweep method with the Anaheim Automation BLWS232D-24V-1350-1024SI5, which has a 1024-line encoder and fairly low cogging torque. For this motor, the align-and-sweep method works very well, with low error. The yellow highlights show the two setup states (":
        "\u5c55\u793a\u4e86\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5728 Anaheim Automation BLWS232D-24V-1350-1024SI5 \u4e0a\u7684\u4f7f\u7528\uff0c\u8be5\u7535\u673a\u5177\u6709 1024 \u7ebf\u7f16\u7801\u5668\u548c\u8f83\u4f4e\u7684\u9f7f\u69fd\u8f6c\u77e9\u3002\u5bf9\u4e8e\u6b64\u7535\u673a\uff0c\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u6548\u679c\u5f88\u597d\uff0c\u8bef\u5dee\u4f4e\u3002\u9ec4\u8272\u9ad8\u4eae\u90e8\u5206\u663e\u793a\u4e24\u4e2a\u8bbe\u7f6e\u72b6\u6001\uff08",
    "), and the green highlights show the two measurement states (": "\uff09\uff0c\u7eff\u8272\u9ad8\u4eae\u90e8\u5206\u663e\u793a\u4e24\u4e2a\u6d4b\u91cf\u72b6\u6001\uff08",
    "). The setup states allow transients to settle down sufficiently before measurement. This motor shows only around \u00b110\u00b0 of fluctuations due to cogging torque, and the fluctuations average out.":
        "\uff09\u3002\u8bbe\u7f6e\u72b6\u6001\u5141\u8bb8\u77ac\u53d8\u5728\u6d4b\u91cf\u524d\u5145\u5206\u7a33\u5b9a\u4e0b\u6765\u3002\u6b64\u7535\u673a\u7531\u4e8e\u9f7f\u69fd\u8f6c\u77e9\u4ec5\u663e\u793a\u7ea6 \u00b110\u00b0 \u7684\u6ce2\u52a8\uff0c\u6ce2\u52a8\u88ab\u5e73\u5747\u6389\u3002",
    "Align-and-sweep method with BLWS232D-24V-1350-1024SI5, sweep rate = 4 counts per control ISR":
        "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\uff08BLWS232D-24V-1350-1024SI5\uff0c\u626b\u63cf\u901f\u7387 = 4 \u8108\u51b2/\u63a7\u5236 ISR\uff09",
    "The BLY342D-24V-3000-1024SI5 has high cogging torque and presents more of a challenge for back-emf synchronization.":
        "BLY342D-24V-3000-1024SI5 \u5177\u6709\u9ad8\u9f7f\u69fd\u8f6c\u77e9\uff0c\u5bf9\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u63d0\u51fa\u4e86\u66f4\u5927\u7684\u6311\u6218\u3002",
    "show the align-and-sweep method in action with this motor; the two figures show different sweep rates. Angle fluctuations can be over 60\u00b0 peak-to-peak, and the effect of Coulomb friction is easily visible as a direction-dependent offset. The lower sweep rate helps reduce angle fluctuations, and produces a more accurate result, at the cost of the measurements taking longer.":
        "\u5c55\u793a\u4e86\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5728\u6b64\u7535\u673a\u4e0a\u7684\u5b9e\u9645\u8fd0\u884c\uff1b\u4e24\u4e2a\u56fe\u663e\u793a\u4e86\u4e0d\u540c\u7684\u626b\u63cf\u901f\u7387\u3002\u89d2\u5ea6\u6ce8\u6ce2\u53ef\u8d85\u8fc7 60\u00b0 \u5cf0\u5cf0\u503c\uff0c\u5e93\u4ed1\u6469\u64e6\u7684\u5f71\u54cd\u4f5c\u4e3a\u65b9\u5411\u76f8\u5173\u7684\u504f\u79fb\u5f88\u5bb9\u6613\u770b\u51fa\u3002\u8f83\u4f4e\u7684\u626b\u63cf\u901f\u7387\u6709\u52a9\u4e8e\u51cf\u5c0f\u89d2\u5ea6\u6ce8\u6ce2\uff0c\u5e76\u4ea7\u751f\u66f4\u51c6\u786e\u7684\u7ed3\u679c\uff0c\u4ee3\u4ef7\u662f\u6d4b\u91cf\u65f6\u95f4\u66f4\u957f\u3002",
    "Align-and-sweep method with BLY342D-24V-3000-1024SI5, sweep rate = 1 counts per control ISR":
        "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\uff08BLY342D-24V-3000-1024SI5\uff0c\u626b\u63cf\u901f\u7387 = 1 \u8108\u51b2/\u63a7\u5236 ISR\uff09",
    "Align-and-sweep method with BLY342D-24V-3000-1024SI5, sweep rate = 4 counts per control ISR":
        "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\uff08BLY342D-24V-3000-1024SI5\uff0c\u626ab\u63cf\u901f\u7387 = 4 \u8108\u51b2/\u63a7\u5236 ISR\uff09",
    "Accuracy and repeatability tests": "\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "The align-and-sweep method was tested with MCAF R4, and the resulting commutation offset from index (":
        "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5728 MCAF R4 \u4e2d\u8fdb\u884c\u4e86\u6d4b\u8bd5\uff0c\u5e76\u5c06\u4ece\u7d22\u5f15\u83b7\u5f97\u7684\u6362\u76f8\u504f\u79fb\uff08",
    ") was compared against a reference method using open-circuit voltage measurements of the motor terminals with the motor rotated mechanically at constant speed.":
        "\uff09\u4e0e\u53c2\u8003\u65b9\u6cd5\u8fdb\u884c\u4e86\u6bd4\u8f83\uff0c\u53c2\u8003\u65b9\u6cd5\u662f\u5728\u7535\u673a\u4ee5\u6052\u5b9a\u901f\u5ea6\u673a\u68b0\u8f6c\u52a8\u65f6\u6d4b\u91cf\u7535\u673a\u7aef\u5b50\u7684\u5f00\u8def\u7535\u538b\u3002",
    "describes the results. In each case, 16 iterations of the align-and-sweep method were performed. (Initial conditions were identical but do not have a significant influence over the resulting estimated offsets since the method rotates the motor over the entire mechanical rotation.) Each motor was used with a dsPICDEM":
        "\u63cf\u8ff0\u4e86\u7ed3\u679c\u3002\u5728\u6bcf\u79cd\u60c5\u51b5\u4e0b\uff0c\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u8fdb\u884c\u4e86 16 \u6b21\u8fed\u4ee3\u3002\uff08\u521d\u59cb\u6761\u4ef6\u76f8\u540c\uff0c\u4f46\u5bf9\u4f30\u8ba1\u504f\u79fb\u7684\u5f71\u54cd\u4e0d\u663e\u8457\uff0c\u56e0\u4e3a\u6b64\u65b9\u6cd5\u65cb\u8f6c\u7535\u673a\u8986\u76d6\u6574\u4e2a\u673a\u68b0\u8f6c\u52a8\u3002\uff09\u6bcf\u4e2a\u7535\u673a\u4f7f\u7528 dsPICDEM",
    "MCLV\u20112 Development Board, with default current limit of 2.29A, and default startup current at 91% of the current limit = 2.08A.":
        "MCLV-2 \u5f00\u53d1\u677f\uff0c\u9ed8\u8ba4\u7535\u6d41\u9650\u5236\u4e3a 2.29A\uff0c\u9ed8\u8ba4\u542f\u52a8\u7535\u6d41\u4e3a\u7535\u6d41\u9650\u5236\u7684 91% = 2.08A\u3002",
    "Accuracy and repeatability metrics for the align-and-sweep method.": "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u7684\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6307\u6807\u3002",
    "The value": "\u503c",
    "represents the sweep rate, in counts/ISR.": "\u8868\u793a\u626b\u63cf\u901f\u7387\uff0c\u5355\u4f4d\u4e3a\u8108\u51b2/ISR\u3002",
    "mean": "\u5747\u503c",
    "max": "\u6700\u5927\u503c",
    "stdev": "\u6807\u51c6\u5dee",
    "span": "\u6781\u5dee",
    "Test case": "\u6d4b\u8bd5\u7528\u4f8b",
    "The error metrics are as follows:": "\u8bef\u5dee\u6307\u6807\u5982\u4e0b\uff1a",
    "\u2014 mean value of the commutation offset difference between the align-and-sweep method and the reference method":
        "\u2014 \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u5747\u503c",
    "\u2014 maximum value of the commutation offset difference between the align-and-sweep method and the reference method":
        "\u2014 \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u6700\u5927\u503c",
    "\u2014 standard deviation of commutation offset estimated by the align-and-sweep method":
        "\u2014 \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6807\u51c6\u5dee",
    "\u2014 difference between minimum and maximum commutation offset estimated by the align-and-sweep method":
        "\u2014 \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6700\u5c0f\u503c\u4e0e\u6700\u5927\u503c\u4e4b\u5dee",
    "All of the motors were able to produce estimates with excellent repeatability at 4 counts/ISR sweep rate, with the exception of the BLY342D-24V-3000-1024SI5, which showed degraded accuracy at 4 counts/ISR compared to 2 counts/ISR.":
        "\u9664 BLY342D-24V-3000-1024SI5 \u5916\uff0c\u6240\u6709\u7535\u673a\u5728 4 \u8108\u51b2/ISR \u626b\u63cf\u901f\u7387\u4e0b\u90fd\u80fd\u4ea7\u751f\u5177\u6709\u4f18\u5f02\u53ef\u91cd\u590d\u6027\u7684\u4f30\u8ba1\u3002BLY342D-24V-3000-1024SI5 \u5728 4 \u8108\u51b2/ISR \u65f6\u7684\u7cbe\u5ea6\u4e0e 2 \u8108\u51b2/ISR \u76f8\u6bd4\u6709\u6240\u4e0b\u964d\u3002",
    "5.4.3.3.3. Align-and-sweep method": "5.4.3.3.3. \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5",
    "5.4.3.3.3.1. Overview": "5.4.3.3.3.1. \u6982\u8ff0",
    "5.4.3.3.3.2. Limitations": "5.4.3.3.3.2. \u5c40\u9650\u6027",
    "5.4.3.3.3.3. Practical implementation issues": "5.4.3.3.3.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.3.3.1. Selection of rotation rate": "5.4.3.3.3.3.1. \u65cb\u8f6c\u901f\u7387\u7684\u9009\u62e9",
    "5.4.3.3.3.3.2. Calculations involving angles": "5.4.3.3.3.3.2. \u6d89\u53ca\u89d2\u5ea6\u7684\u8ba1\u7b97",
    "5.4.3.3.3.3.3. State machine": "5.4.3.3.3.3.3. \u72b6\u6001\u673a",
    "5.4.3.3.3.4. Example data": "5.4.3.3.3.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.3.5. Accuracy and repeatability tests": "5.4.3.3.3.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "Align method": "\u5bf9\u9f50\u65b9\u6cd5",
    "Pullout torque method": "\u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
