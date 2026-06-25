# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/qei_sync/align"
title_zh = "5.4.3.3.2. \u5bf9\u9f50\u65b9\u6cd5"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "Align method": "\u5bf9\u9f50\u65b9\u6cd5",
    "Overview": "\u6982\u8ff0",
    "In the absence of load torques (cogging, friction, disturbance), if a fixed \u03b1\u03b2-frame stator current vector is applied, the motor will align along the d-axis, since this reaches a point of equilibrium where the electromagnetic torque is zero.":
        "\u5728\u65e0\u8d1f\u8f7d\u8f6c\u77e9\uff08\u9f7f\u69fd\u3001\u6469\u64e6\u3001\u6270\u52a8\uff09\u7684\u60c5\u51b5\u4e0b\uff0c\u5982\u679c\u65bd\u52a0\u56fa\u5b9a\u7684 \u03b1\u03b2 \u5750\u6807\u7cfb\u5b9a\u5b50\u7535\u6d41\u77e2\u91cf\uff0c\u7535\u673a\u5c06\u6cbf d \u8f74\u5bf9\u9f50\uff0c\u56e0\u4e3a\u8fd9\u5230\u8fbe\u4e86\u7535\u78c1\u8f6c\u77e9\u4e3a\u96f6\u7684\u5e73\u8861\u70b9\u3002",
    "The align method of back-EMF synchronization uses this method for a simple and generally-reliable method of obtaining a commutation offset that is accurate within a few electrical degrees for many motors.":
        "\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u7684\u5bf9\u9f50\u65b9\u6cd5\u5229\u7528\u6b64\u539f\u7406\uff0c\u63d0\u4f9b\u4e86\u4e00\u79cd\u7b80\u5355\u4e14\u901a\u5e38\u53ef\u9760\u7684\u65b9\u6cd5\u6765\u83b7\u53d6\u6362\u76f8\u504f\u79fb\uff0c\u5bf9\u4e8e\u8bb8\u591a\u7535\u673a\u7cbe\u5ea6\u5728\u51e0\u4e2a\u7535\u89d2\u5ea6\u4ee5\u5185\u3002",
    "There are, however, subtleties with this method, especially when used with motors that have substantial cogging torque.":
        "\u7136\u800c\uff0c\u6b64\u65b9\u6cd5\u5b58\u5728\u4e00\u4e9b\u5fae\u5999\u4e4b\u5904\uff0c\u7279\u522b\u662f\u5728\u7528\u4e8e\u5177\u6709\u663e\u8457\u9f7f\u69fd\u8f6c\u77e9\u7684\u7535\u673a\u65f6\u3002",
    "If there are load torques when using the align method, the motor will reach a point of equilibrium with an electrical-angle offset":
        "\u5982\u679c\u4f7f\u7528\u5bf9\u9f50\u65b9\u6cd5\u65f6\u5b58\u5728\u8d1f\u8f7d\u8f6c\u77e9\uff0c\u7535\u673a\u5c06\u5230\u8fbe\u4e00\u4e2a\u5e26\u6709\u7535\u6c14\u89d2\u5ea6\u504f\u79fb",
    "from the d-axis such that": "\u504f\u79bb d \u8f74\u7684\u5e73\u8861\u70b9\uff0c\u4f7f\u5f97",
    ", in other words,": "\uff0c\u6362\u53e5\u8bdd\u8bf4\uff0c",
    ". Cogging/detent torque for low-cost motors may be in the range of 5% \u2013 10% of continuous rated torque plus 1% \u2013 3% for friction, so if we use a current I equal to continuous rated current we should expect on the order of":
        "\u3002\u4f4e\u6210\u672c\u7535\u673a\u7684\u9f7f\u69fd/\u51f9\u69fd\u8f6c\u77e9\u53ef\u80fd\u5728\u8fde\u7eed\u989d\u5b9a\u8f6c\u77e9\u7684 5%\u201310% \u8303\u56f4\u5185\uff0c\u52a0\u4e0a 1%\u20133% \u7684\u6469\u64e6\uff0c\u56e0\u6b64\u5982\u679c\u4f7f\u7528\u7b49\u4e8e\u8fde\u7eed\u989d\u5b9a\u7535\u6d41\u7684\u7535\u6d41 I\uff0c\u6211\u4eec\u5e94\u9884\u671f\u5927\u7ea6",
    "worst-case error. Oversized motors, where the drive cannot deliver current to achieve continuous rated torque, will have larger errors. (example: if total load torque is 13% continuous rated torque, and the drive can deliver 50% continuous rated torque, then we should expect arcsin(13/50) \u2248 15.1\u00b0 worst-case error.)":
        "\u7684\u6700\u574f\u60c5\u51b5\u8bef\u5dee\u3002\u8d85\u5927\u578b\u7535\u673a\uff0c\u5373\u9a71\u52a8\u5668\u65e0\u6cd5\u63d0\u4f9b\u8db3\u4ee5\u8fbe\u5230\u8fde\u7eed\u989d\u5b9a\u8f6c\u77e9\u7684\u7535\u6d41\u7684\u7535\u673a\uff0c\u5c06\u6709\u66f4\u5927\u7684\u8bef\u5dee\u3002\uff08\u4f8b\u5982\uff1a\u5982\u679c\u603b\u8d1f\u8f7d\u8f6c\u77e9\u4e3a 13% \u8fde\u7eed\u989d\u5b9a\u8f6c\u77e9\uff0c\u9a71\u52a8\u5668\u53ef\u4ee5\u63d0\u4f9b 50% \u8fde\u7eed\u989d\u5b9a\u8f6c\u77e9\uff0c\u5219\u9884\u671f arcsin(13/50) \u2248 15.1\u00b0 \u7684\u6700\u574f\u60c5\u51b5\u8bef\u5dee\u3002\uff09",
    "The": "\u542f\u52a8",
    "startup sequence": "\u5e8f\u5217",
    "\u2019s \u201calign\u201d state (where the current vector magnitude and angle are fixed) is utilized to allow a suitable settling time to reach mechanical equilibrium, and at the end of this time, the difference between the applied commutation angle and the encoder count is computed and used to obtain a commutation offset.":
        "\u7684\u201c\u5bf9\u9f50\u201d\u72b6\u6001\uff08\u7535\u6d41\u77e2\u91cf\u5e45\u503c\u548c\u89d2\u5ea6\u56fa\u5b9a\uff09\u88ab\u7528\u4e8e\u5141\u8bb8\u5408\u9002\u7684\u7a33\u5b9a\u65f6\u95f4\u4ee5\u8fbe\u5230\u673a\u68b0\u5e73\u8861\uff0c\u5728\u6b64\u65f6\u95f4\u7ed3\u675f\u65f6\uff0c\u8ba1\u7b97\u65bd\u52a0\u7684\u6362\u76f8\u89d2\u5ea6\u4e0e\u7f16\u7801\u5668\u8108\u51b2\u6570\u4e4b\u95f4\u7684\u5dee\u503c\uff0c\u7528\u4e8e\u83b7\u53d6\u6362\u76f8\u504f\u79fb\u3002",
    "Limitations": "\u5c40\u9650\u6027",
    "Continuous torque disturbances can prevent mechanical equilibrium": "\u8fde\u7eed\u8f6c\u77e9\u6270\u52a8\u53ef\u80fd\u963b\u6b62\u673a\u68b0\u5e73\u8861",
    "There is a semistable equilibrium point (locally stable, globally unstable) around": "\u5b58\u5728\u4e00\u4e2a\u534a\u7a33\u5b9a\u5e73\u8861\u70b9\uff08\u5c40\u90e8\u7a33\u5b9a\uff0c\u5168\u5c40\u4e0d\u7a33\u5b9a\uff09\u5728",
    "where the cogging torque pulls the rotor towards a particular detent position, and the electromagnetic torque is small enough that it cannot pull the rotor out of the detent unless a different commutation angle is applied.":
        "\u9644\u8fd1\uff0c\u9f7f\u69fd\u8f6c\u77e9\u5c06\u8f6c\u5b50\u62c9\u5411\u7279\u5b9a\u7684\u51f9\u69fd\u4f4d\u7f6e\uff0c\u7535\u78c1\u8f6c\u77e9\u8db3\u591f\u5c0f\uff0c\u9664\u975e\u65bd\u52a0\u4e0d\u540c\u7684\u6362\u76f8\u89d2\u5ea6\uff0c\u5426\u5219\u65e0\u6cd5\u5c06\u8f6c\u5b50\u4ece\u51f9\u69fd\u4e2d\u62c9\u51fa\u3002",
    "Practical implementation issues": "\u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "The angles used in the rampup and align states of startup sequence are important, particularly the angle shift: a different commutation angle can be applied during the rampup and align states, to improve the ability of the align method to overcome torque detents and keep from getting stuck at a semistable equilibrium point.":
        "\u542f\u52a8\u5e8f\u5217\u4e2d rampup \u548c align \u72b6\u6001\u4f7f\u7528\u7684\u89d2\u5ea6\u5f88\u91cd\u8981\uff0c\u7279\u522b\u662f\u89d2\u5ea6\u504f\u79fb\uff1a\u53ef\u4ee5\u5728 rampup \u548c align \u72b6\u6001\u671f\u95f4\u65bd\u52a0\u4e0d\u540c\u7684\u6362\u76f8\u89d2\u5ea6\uff0c\u4ee5\u63d0\u9ad8\u5bf9\u9f50\u65b9\u6cd5\u514b\u670d\u8f6c\u77e9\u51f5\u69fd\u7684\u80fd\u529b\uff0c\u907f\u514d\u5361\u5728\u534a\u7a33\u5b9a\u5e73\u8861\u70b9\u3002",
    "A more in-depth discussion of angle shift is shown below in the": "\u5173\u4e8e\u89d2\u5ea6\u504f\u79fb\u7684\u66f4\u6df1\u5165\u8ba8\u8bba\u89c1\u4e0b\u6587",
    "section containing example data": "\u793a\u4f8b\u6570\u636e\u90e8\u5206",
    "MCAF applies current during the align phase along the q-axis, not the d-axis, so the estimated commutation offset has a":
        "MCAF \u5728\u5bf9\u9f50\u9636\u6bb5\u6cbf q \u8f74\u800c\u975e d \u8f74\u65bd\u52a0\u7535\u6d41\uff0c\u56e0\u6b64\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u4e0e\u5bf9\u9f50\u9636\u6bb5\u7ed3\u675f\u65f6\u65bd\u52a0\u7684\u6362\u76f8\u7535\u6c14\u89d2\u5ea6\u4e0e\u6d4b\u91cf\u7684\u7f16\u7801\u5668\u7535\u6c14\u89d2\u5ea6\u4e4b\u95f4\u7684\u89d2\u5ea6\u5dee\u5b58\u5728",
    "offset from the angle difference between applied commutation electrical angle and measured encoder electrical angle at the end of the align phase. The sign of this":
        "\u504f\u79fb\u3002\u6b64",
    "offset depends on the sign of the q-axis current used. (Negative q-axis current is applied during startup when the motor is started in the reverse direction.) In other words,":
        "\u504f\u79fb\u7684\u7b26\u53f7\u53d6\u51b3\u4e8e\u4f7f\u7528\u7684 q \u8f74\u7535\u6d41\u7684\u7b26\u53f7\u3002\uff08\u5f53\u7535\u673a\u53cd\u65b9\u5411\u542f\u52a8\u65f6\uff0c\u542f\u52a8\u8fc7\u7a0b\u4e2d\u65bd\u52a0\u8d1f q \u8f74\u7535\u6d41\u3002\uff09\u6362\u53e5\u8bdd\u8bf4\uff0c",
    "where the angle subscripts": "\u5176\u4e2d\u89d2\u5ea6\u4e0b\u6807",
    "refer to commutation offset, encoder angle (in electrical terms), and forced electrical angle, respectively.":
        "\u5206\u522b\u6307\u6362\u76f8\u504f\u79fb\u3001\u7f16\u7801\u5668\u89d2\u5ea6\uff08\u7535\u6c14\u5355\u4f4d\uff09\u548c\u5f3a\u5236\u7535\u6c14\u89d2\u5ea6\u3002",
    "Example data": "\u793a\u4f8b\u6570\u636e",
    "shows the use of the align method with the Anaheim Automation BLWS232D-24V-1350-1024SI5, which has a 1024-line encoder and fairly low cogging torque. For this motor, the align method works very well, with low error. The yellow highlight shows the current rampup state (current not shown), at an applied electrical angle":
        "\u5c55\u793a\u4e86\u5bf9\u9f50\u65b9\u6cd5\u5728 Anaheim Automation BLWS232D-24V-1350-1024SI5 \u4e0a\u7684\u4f7f\u7528\uff0c\u8be5\u7535\u673a\u5177\u6709 1024 \u7ebf\u7f16\u7801\u5668\u548c\u8f83\u4f4e\u7684\u9f7f\u69fd\u8f6c\u77e9\u3002\u5bf9\u4e8e\u6b64\u7535\u673a\uff0c\u5bf9\u9f50\u65b9\u6cd5\u6548\u679c\u5f88\u597d\uff0c\u8bef\u5dee\u4f4e\u3002\u9ec4\u8272\u9ad8\u4eae\u90e8\u5206\u663e\u793a\u7535\u6d41\u4e0a\u5347\u72b6\u6001\uff08\u7535\u6d41\u672a\u663e\u793a\uff09\uff0c\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u4e3a",
    ", and the green highlight shows the align state, at an applied electrical angle": "\uff0c\u7eff\u8272\u9ad8\u4eae\u90e8\u5206\u663e\u793a\u5bf9\u9f50\u72b6\u6001\uff0c\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u4e3a",
    ". The motor takes roughly 0.15 seconds to settle to equilibrium, so the align time of 0.5s leaves plenty of time to reach an encoder angle of 120\u00b0, which is 90\u00b0 ahead of the applied electrical angle.":
        "\u3002\u7535\u673a\u5927\u7ea6\u9700\u8981 0.15 \u79d2\u8fbe\u5230\u5e73\u8861\uff0c\u56e0\u6b64 0.5 \u79d2\u7684\u5bf9\u9f50\u65f6\u95f4\u7559\u6709\u5145\u5206\u7684\u65f6\u95f4\u8fbe\u5230 120\u00b0 \u7684\u7f16\u7801\u5668\u89d2\u5ea6\uff0c\u5373\u9886\u5148\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6 90\u00b0\u3002",
    "Align method with BLWS232D-24V-1350-1024SI5,": "\u5bf9\u9f50\u65b9\u6cd5\uff08BLWS232D-24V-1350-1024SI5\uff0c",
    "The remaining graphs in this section show the use of the align method with the Anaheim Automation BLY342D-48V-3200-1024SI5. This motor has substantial cogging torque, and because of this, the success of the align method depends on initial conditions and the choice of startup angles.":
        "\u672c\u8282\u5269\u4f59\u7684\u56fe\u5c55\u793a\u4e86\u5bf9\u9f50\u65b9\u6cd5\u5728 Anaheim Automation BLY342D-48V-3200-1024SI5 \u4e0a\u7684\u4f7f\u7528\u3002\u8be5\u7535\u673a\u5177\u6709\u663e\u8457\u7684\u9f7f\u69fd\u8f6c\u77e9\uff0c\u56e0\u6b64\u5bf9\u9f50\u65b9\u6cd5\u7684\u6210\u529f\u53d6\u51b3\u4e8e\u521d\u59cb\u6761\u4ef6\u548c\u542f\u52a8\u89d2\u5ea6\u7684\u9009\u62e9\u3002",
    "shows this motor during startup, with applied electrical angles of 0\u00b0 during both rampup and align states:":
        "\u5c55\u793a\u4e86\u6b64\u7535\u673a\u542f\u52a8\u65f6\u7684\u60c5\u51b5\uff0crampup \u548c align \u72b6\u6001\u65f6\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u5747\u4e3a 0\u00b0\uff1a",
    ". In this case, the initial angle of the motor": "\u3002\u5728\u6b64\u60c5\u51b5\u4e0b\uff0c\u7535\u673a\u7684\u521d\u59cb\u89d2\u5ea6",
    "was around 65\u00b0 from equilibrium, and the transient settles down quickly.":
        "\u8ddd\u5e73\u8861\u70b9\u7ea6 65\u00b0\uff0c\u77ac\u53d8\u5f88\u5feb\u7a33\u5b9a\u4e0b\u6765\u3002",
    "Align method with BLY342D-48V-3200-1024SI5,": "\u5bf9\u9f50\u65b9\u6cd5\uff08BLY342D-48V-3200-1024SI5\uff0c",
    "When the initial position of the rotor is roughly 180\u00b0 from equilibrium, the rotor can get stuck in a detent at semistable equilibrium.":
        "\u5f53\u8f6c\u5b50\u7684\u521d\u59cb\u4f4d\u7f6e\u5927\u7ea6\u8ddd\u5e73\u8861\u70b9 180\u00b0 \u65f6\uff0c\u8f6c\u5b50\u53ef\u80fd\u4f1a\u5361\u5728\u534a\u7a33\u5b9a\u5e73\u8861\u7684\u51f5\u69fd\u4e2d\u3002",
    "shows such a case, where the rotor reaches the correct equilibrium eventually, but its transient is much longer.":
        "\u5c55\u793a\u4e86\u8fd9\u6837\u4e00\u79cd\u60c5\u51b5\uff0c\u8f6c\u5b50\u6700\u7ec8\u8fbe\u5230\u4e86\u6b63\u786e\u7684\u5e73\u8861\uff0c\u4f46\u77ac\u53d8\u8fc7\u7a0b\u957f\u5f97\u591a\u3002",
    "shows almost the same starting angle, but this time it remains stuck in a semistable equilibrium. Note that during the align phase, highlighted green, the rotor angle does not move significantly, and remains approximately 270\u00b0 ahead of the applied electrical angle, whereas in successful uses of the align method, it should reach equilibrium at 90\u00b0 ahead of the applied electrical angle. In this case, the calculated commutation offset would be off by 180\u00b0, leading to backward instead of forward rotation.":
        "\u5c55\u793a\u4e86\u51e0\u4e4e\u76f8\u540c\u7684\u8d77\u59cb\u89d2\u5ea6\uff0c\u4f46\u8fd9\u6b21\u5361\u5728\u4e86\u534a\u7a33\u5b9a\u5e73\u8861\u4e2d\u3002\u6ce8\u610f\uff0c\u5728\u4ee5\u7eff\u8272\u9ad8\u4eae\u7684\u5bf9\u9f50\u9636\u6bb5\uff0c\u8f6c\u5b50\u89d2\u5ea6\u672a\u6709\u663e\u8457\u79fb\u52a8\uff0c\u4ecd\u7ea6\u9886\u5148\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6 270\u00b0\uff0c\u800c\u5728\u6210\u529f\u7684\u5bf9\u9f50\u65b9\u6cd5\u4e2d\uff0c\u5b83\u5e94\u8fbe\u5230\u9886\u5148\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6 90\u00b0 \u7684\u5e73\u8861\u3002\u5728\u8fd9\u79cd\u60c5\u51b5\u4e0b\uff0c\u8ba1\u7b97\u7684\u6362\u76f8\u504f\u79fb\u5c06\u504f\u5dee 180\u00b0\uff0c\u5bfc\u81f4\u53cd\u65b9\u5411\u8f6c\u52a8\u800c\u975e\u6b63\u65b9\u5411\u3002",
    ", This shows the case where the rotor is stuck in semistable equilibrium near its initial conditions.":
        "\uff0c\u8fd9\u5c55\u793a\u4e86\u8f6c\u5b50\u5361\u5728\u5176\u521d\u59cb\u6761\u4ef6\u9644\u8fd1\u7684\u534a\u7a33\u5b9a\u5e73\u8861\u4e2d\u7684\u60c5\u51b5\u3002",
    "The use of an angle shift can prevent this situation.": "\u4f7f\u7528\u89d2\u5ea6\u504f\u79fb\u53ef\u4ee5\u907f\u514d\u8fd9\u79cd\u60c5\u51b5\u3002",
    "shows similar initial conditions but with the applied angle during the align phase shifted by 30\u00b0. Here the rampup phase remains stuck in semistable equilibrium, but the align phase is able to escape the detent and reach its intended position.":
        "\u5c55\u793a\u4e86\u7c7b\u4f3c\u7684\u521d\u59cb\u6761\u4ef6\uff0c\u4f46\u5bf9\u9f50\u9636\u6bb5\u65bd\u52a0\u7684\u89d2\u5ea6\u504f\u79fb\u4e86 30\u00b0\u3002\u8fd9\u91cc rampup \u9636\u6bb5\u4ecd\u5361\u5728\u534a\u7a33\u5b9a\u5e73\u8861\u4e2d\uff0c\u4f46\u5bf9\u9f50\u9636\u6bb5\u80fd\u591f\u9003\u51f5\u51f5\u69fd\u5e76\u8fbe\u5230\u9884\u5b9a\u4f4d\u7f6e\u3002",
    "shows similar initial conditions, with the applied angle during the align phase at 0\u00b0 but at 330\u00b0 during the rampup phase. In this case, the rampup phase provides enough torque to give the motor a kick and prevent it from getting stuck in equilibrium.":
        "\u5c55\u793a\u4e86\u7c7b\u4f3c\u7684\u521d\u59cb\u6761\u4ef6\uff0c\u5bf9\u9f50\u9636\u6bb5\u65bd\u52a0\u7684\u89d2\u5ea6\u4e3a 0\u00b0\uff0c\u4f46 rampup \u9636\u6bb5\u4e3a 330\u00b0\u3002\u5728\u8fd9\u79cd\u60c5\u51b5\u4e0b\uff0crampup \u9636\u6bb5\u63d0\u4f9b\u4e86\u8db3\u591f\u7684\u8f6c\u77e9\u7ed9\u7535\u673a\u4e00\u4e2a\u51b2\u51fb\uff0c\u907f\u514d\u5361\u5728\u5e73\u8861\u4e2d\u3002",
    "This technique of adding an angle shift is not foolproof, but it does seem to be reasonably robust. Tests of several motors with high cogging torque were able to align successfully with an angle shift in the 30\u00b0 \u2013 60\u00b0 range.":
        "\u8fd9\u79cd\u6dfb\u52a0\u89d2\u5ea6\u504f\u79fb\u7684\u6280\u672f\u5e76\u975e\u4e07\u65e0\u4e00\u5931\uff0c\u4f46\u4f3c\u4e4e\u76f8\u5f53\u9c81\u68d2\u3002\u5bf9\u51e0\u79cd\u9ad8\u9f7f\u69fd\u8f6c\u77e9\u7535\u673a\u7684\u6d4b\u8bd5\u8868\u660e\uff0c30\u00b0\u201360\u00b0 \u8303\u56f4\u5185\u7684\u89d2\u5ea6\u504f\u79fb\u80fd\u591f\u6210\u529f\u5bf9\u9f50\u3002",
    "Accuracy and repeatability tests": "\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "The align method was tested with MCAF R4, and the resulting commutation offset from index (":
        "\u5bf9\u9f50\u65b9\u6cd5\u5728 MCAF R4 \u4e2d\u8fdb\u884c\u4e86\u6d4b\u8bd5\uff0c\u5e76\u5c06\u4ece\u7d22\u5f15\u83b7\u5f97\u7684\u6362\u76f8\u504f\u79fb\uff08",
    ") was compared against a reference method using open-circuit voltage measurements of the motor terminals with the motor rotated mechanically at constant speed.":
        "\uff09\u4e0e\u53c2\u8003\u65b9\u6cd5\u8fdb\u884c\u4e86\u6bd4\u8f83\uff0c\u53c2\u8003\u65b9\u6cd5\u662f\u5728\u7535\u673a\u4ee5\u6052\u5b9a\u901f\u5ea6\u673a\u68b0\u8f6c\u52a8\u65f6\u6d4b\u91cf\u7535\u673a\u7aef\u5b50\u7684\u5f00\u8def\u7535\u538b\u3002",
    "describes the results. In each case, 64 iterations of the align method were performed, with initial conditions at evenly-spaced angles spanning one electrical cycle. Except where noted, the settings for the align method are the default values of":
        "\u63cf\u8ff0\u4e86\u7ed3\u679c\u3002\u5728\u6bcf\u79cd\u60c5\u51b5\u4e0b\uff0c\u5bf9\u9f50\u65b9\u6cd5\u8fdb\u884c\u4e86 64 \u6b21\u8fed\u4ee3\uff0c\u521d\u59cb\u6761\u4ef6\u4e3a\u8de8\u8d8a\u4e00\u4e2a\u7535\u6c14\u5468\u671f\u7684\u5747\u5300\u95f4\u8ddd\u89d2\u5ea6\u3002\u9664\u53e6\u6709\u8bf4\u660e\u5916\uff0c\u5bf9\u9f50\u65b9\u6cd5\u7684\u8bbe\u7f6e\u4e3a\u9ed8\u8ba4\u503c",
    "during the rampup state and": "\uff08rampup \u72b6\u6001\uff09\u548c",
    "during the align state (angle shift of 30\u00b0). Each motor was used with a dsPICDEM": "\uff08align \u72b6\u6001\uff0c\u89d2\u5ea6\u504f\u79fb 30\u00b0\uff09\u3002\u6bcf\u4e2a\u7535\u673a\u4f7f\u7528 dsPICDEM",
    "MCLV\u20112 Development Board, with default current limit of 2.29A, and default startup current at 91% of the current limit = 2.08A.":
        "MCLV-2 \u5f00\u53d1\u677f\uff0c\u9ed8\u8ba4\u7535\u6d41\u9650\u5236\u4e3a 2.29A\uff0c\u9ed8\u8ba4\u542f\u52a8\u7535\u6d41\u4e3a\u7535\u6d41\u9650\u5236\u7684 91% = 2.08A\u3002",
    "Accuracy and repeatability metrics for the align method": "\u5bf9\u9f50\u65b9\u6cd5\u7684\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6307\u6807",
    "mean": "\u5747\u503c",
    "max": "\u6700\u5927\u503c",
    "stdev": "\u6807\u51c6\u5dee",
    "span": "\u6781\u5dee",
    "Test case": "\u6d4b\u8bd5\u7528\u4f8b",
    "The error metrics are as follows:": "\u8bef\u5dee\u6307\u6807\u5982\u4e0b\uff1a",
    "\u2014 mean value of the commutation offset difference between the align method and the reference method":
        "\u2014 \u5bf9\u9f50\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u5747\u503c",
    "\u2014 maximum value of the commutation offset difference between the align method and the reference method":
        "\u2014 \u5bf9\u9f50\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u6700\u5927\u503c",
    "\u2014 standard deviation of commutation offset estimated by the align method":
        "\u2014 \u5bf9\u9f50\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6807\u51c6\u5dee",
    "\u2014 difference between minimum and maximum commutation offset estimated by the align method":
        "\u2014 \u5bf9\u9f50\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6700\u5c0f\u503c\u4e0e\u6700\u5927\u503c\u4e4b\u5dee",
    "The BLY342D-24V-3000-1024SI5 required a larger angle shift (60\u00b0) to work reliably. With the default value of 30\u00b0, initial conditions near 180\u00b0 from equilibrium cause the motor to get stuck in semistable equilibrium. This is more severe with the BLY342D-24V-3000 than the BLY342D-48V-3200; both motors use the same lamination stack and rotor but are wound differently, with the BLY342D-24V-3000 having higher rated current and a lower value of":
        "BLY342D-24V-3000-1024SI5 \u9700\u8981\u66f4\u5927\u7684\u89d2\u5ea6\u504f\u79fb\uff0860\u00b0\uff09\u624d\u80fd\u53ef\u9760\u5de5\u4f5c\u3002\u4f7f\u7528\u9ed8\u8ba4\u503c 30\u00b0 \u65f6\uff0c\u63a5\u8fd1 180\u00b0 \u5e73\u8861\u70b9\u7684\u521d\u59cb\u6761\u4ef6\u4f1a\u5bfc\u81f4\u7535\u673a\u5361\u5728\u534a\u7a33\u5b9a\u5e73\u8861\u4e2d\u3002\u8fd9\u5728 BLY342D-24V-3000 \u4e0a\u6bd4 BLY342D-48V-3200 \u66f4\u4e3a\u4e25\u91cd\uff1b\u4e24\u4e2a\u7535\u673a\u4f7f\u7528\u76f8\u540c\u7684\u53e0\u7247\u548c\u8f6c\u5b50\uff0c\u4f46\u7ed5\u7ec4\u65b9\u5f0f\u4e0d\u540c\uff0cBLY342D-24V-3000 \u5177\u6709\u66f4\u9ad8\u7684\u989d\u5b9a\u7535\u6d41\u548c\u66f4\u4f4e\u7684",
    ", so that the 2.08A is not able to exert as much torque during the align phase.":
        "\u503c\uff0c\u56e0\u6b64 2.08A \u5728\u5bf9\u9f50\u9636\u6bb5\u65e0\u6cd5\u4ea7\u751f\u540c\u6837\u5927\u7684\u8f6c\u77e9\u3002",
    "5.4.3.3.2. Align method": "5.4.3.3.2. \u5bf9\u9f50\u65b9\u6cd5",
    "5.4.3.3.2.1. Overview": "5.4.3.3.2.1. \u6982\u8ff0",
    "5.4.3.3.2.2. Limitations": "5.4.3.3.2.2. \u5c40\u9650\u6027",
    "5.4.3.3.2.3. Practical implementation issues": "5.4.3.3.2.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.2.4. Example data": "5.4.3.3.2.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.2.5. Accuracy and repeatability tests": "5.4.3.3.2.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "Implementation issues common to all methods": "\u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898",
    "Align-and-sweep method": "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
