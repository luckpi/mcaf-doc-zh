# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/qei_sync/pullout"
title_zh = "5.4.3.3.4. \u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "Pullout torque method": "\u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5",
    "Note": "\u6ce8\u610f",
    "This is a deprecated feature that may be removed in an upcoming release of MCAF.":
        "\u8fd9\u662f\u4e00\u4e2a\u5df2\u5f03\u7528\u7684\u529f\u80fd\uff0c\u53ef\u80fd\u5728\u5373\u5c06\u53d1\u5e03\u7684 MCAF \u7248\u672c\u4e2d\u88ab\u79fb\u9664\u3002",
    "Overview": "\u6982\u8ff0",
    "At startup, when the motor is spinning in open loop, the rotor lags the voltage vector at an unknown angle. This is because there is more than required current to meet the load torque. In other words there is a non-zero component of the":
        "\u542f\u52a8\u65f6\uff0c\u5f53\u7535\u673a\u4ee5\u5f00\u73af\u65b9\u5f0f\u65cb\u8f6c\u65f6\uff0c\u8f6c\u5b50\u4ee5\u672a\u77e5\u89d2\u5ea6\u6ede\u540e\u4e8e\u7535\u538b\u77e2\u91cf\u3002\u8fd9\u662f\u56e0\u4e3a\u7535\u6d41\u5927\u4e8e\u6ee1\u8db3\u8d1f\u8f7d\u8f6c\u77e9\u6240\u9700\u7684\u7535\u6d41\u3002\u6362\u53e5\u8bdd\u8bf4\uff0c",
    "current. When the current magnitude is reduced gradually the value of": "\u7535\u6d41\u5b58\u5728\u975e\u96f6\u5206\u91cf\u3002\u5f53\u7535\u6d41\u5e45\u503c\u9010\u6e10\u51cf\u5c0f\u65f6\uff0c",
    "automatically goes towards zero with": "\u7684\u503c\u81ea\u52a8\u8d8b\u5411\u96f6\uff0c\u800c",
    "remaining the same until the pullout torque angle is reached. The raw reading from the QEI position counter at the instance of pullout corresponds to":
        "\u4fdd\u6301\u4e0d\u53d8\uff0c\u76f4\u5230\u8fbe\u5230\u5931\u6b65\u8f6c\u77e9\u89d2\u5ea6\u3002\u5931\u6b65\u77ac\u95f4 QEI \u4f4d\u7f6e\u8ba1\u6570\u5668\u7684\u539f\u59cb\u8bfb\u6570\u5bf9\u5e94\u4e8e",
    "plus a small load angle behind the voltage vector depending on the the direction of rotation. This reading is called \u2018pullout position\u2019 in equation":
        "\u52a0\u4e0a\u53d6\u51b3\u4e8e\u65cb\u8f6c\u65b9\u5411\u7684\u6ede\u540e\u4e8e\u7535\u538b\u77e2\u91cf\u7684\u5c0f\u8d1f\u8f7d\u89d2\u3002\u6b64\u8bfb\u6570\u5728\u65b9\u7a0b",
    ". The rotor offset is calculated as": "\u4e2d\u79f0\u4e3a\u201c\u5931\u6b65\u4f4d\u7f6e\u201d\u3002\u8f6c\u5b50\u504f\u79fb\u8ba1\u7b97\u4e3a",
    "The load angle is insignificant owing to very small currents (": "\u8d1f\u8f7d\u89d2\u53ef\u5ffd\u7565\uff0c\u56e0\u4e3a\u5728\u65e0\u8d1f\u8f7d\u548c\u4f4e\u901f\u65f6\u7535\u6d41\u975e\u5e38\u5c0f\uff08",
    "at pullout) during no load and lower speeds.": "\u5931\u6b65\u65f6\uff09\u3002",
    "The critical factor therefore with this approach is that the": "\u56e0\u6b64\u6b64\u65b9\u6cd5\u7684\u5173\u952e\u56e0\u7d20\u662f",
    "value of the mechanical parameters must be high enough to bring the motor to standstill unassisted in a few seconds approximately. If it takes several seconds other methods should be explored.":
        "\u673a\u68b0\u53c2\u6570\u7684\u503c\u5fc5\u987b\u8db3\u591f\u9ad8\uff0c\u4ee5\u4f7f\u7535\u673a\u5728\u5927\u7ea6\u51e0\u79d2\u5185\u65e0\u5916\u529b\u534f\u52a9\u4e0b\u8fbe\u5230\u9759\u6b62\u3002\u5982\u679c\u9700\u8981\u591a\u79d2\uff0c\u5e94\u63a2\u7d22\u5176\u4ed6\u65b9\u6cd5\u3002",
    "The": "\u542f\u52a8",
    "startup": "\u5e8f\u5217",
    "sequence\u2019s \u201cSPIN\u201d state (where the rotor has been accelerated to the open loop max. speed) is utilized to allow a suitable settling time to reach mechanical equilibrium, and at the end of this time, the current":
        "\u7684\u201cSPIN\u201d\u72b6\u6001\uff08\u8f6c\u5b50\u5df2\u52a0\u901f\u5230\u5f00\u73af\u6700\u5927\u901f\u5ea6\uff09\u88ab\u7528\u4e8e\u5141\u8bb8\u5408\u9002\u7684\u7a33\u5b9a\u65f6\u95f4\u4ee5\u8fbe\u5230\u673a\u68b0\u5e73\u8861\uff0c\u5728\u6b64\u65f6\u95f4\u7ed3\u675f\u65f6\uff0c\u7535\u6d41",
    "is reduced to the point of pullout when the pullout position which is the difference between the applied commutation angle (":
        "\u88ab\u51cf\u5c0f\u5230\u5931\u6b65\u70b9\uff0c\u6b64\u65f6\u8ba1\u7b97\u5931\u6b65\u4f4d\u7f6e\uff0c\u5373\u65bd\u52a0\u7684\u6362\u76f8\u89d2\u5ea6\uff08",
    ") and the raw encoder count is computed. Once the rotor offset is computed actual rotor position is computed while running as":
        "\uff09\u4e0e\u539f\u59cb\u7f16\u7801\u5668\u8108\u51b2\u6570\u4e4b\u5dee\u3002\u4e00\u65e6\u8f6c\u5b50\u504f\u79fb\u88ab\u8ba1\u7b97\u51fa\uff0c\u8fd0\u884c\u65f6\u7684\u5b9e\u9645\u8f6c\u5b50\u4f4d\u7f6e\u8ba1\u7b97\u4e3a",
    "Limitations": "\u5c40\u9650\u6027",
    "When the rotor is approaching the pullout offset relative to commutation angle, the electromagnetic torque is just enough to balance the load torque. Any minor disturbance or cogging effects could stall the motor beyond recovery. This requires the rotor not be subjected to any torque disturbances during measurement. This method is robust to steady frictional or viscous torques, however.":
        "\u5f53\u8f6c\u5b50\u63a5\u8fd1\u76f8\u5bf9\u4e8e\u6362\u76f8\u89d2\u5ea6\u7684\u5931\u6b65\u504f\u79fb\u65f6\uff0c\u7535\u78c1\u8f6c\u77e9\u4ec5\u591f\u5e73\u8861\u8d1f\u8f7d\u8f6c\u77e9\u3002\u4efb\u4f55\u8f7b\u5fae\u6270\u52a8\u6216\u9f7f\u69fd\u6548\u5e94\u90fd\u53ef\u80fd\u5bfc\u81f4\u7535\u673a\u505c\u8f6c\u4e14\u65e0\u6cd5\u6062\u590d\u3002\u8fd9\u8981\u6c42\u5728\u6d4b\u91cf\u671f\u95f4\u8f6c\u5b50\u4e0d\u53d7\u4efb\u4f55\u8f6c\u77e9\u6270\u52a8\u3002\u7136\u800c\uff0c\u6b64\u65b9\u6cd5\u5bf9\u7a33\u5b9a\u7684\u6469\u64e6\u6216\u9ecf\u6027\u8f6c\u77e9\u5177\u6709\u9c81\u68d2\u6027\u3002",
    "This method of offset measurement has certain drawbacks. High inertia motors will not show rapid changes in speed when":
        "\u6b64\u504f\u79fb\u6d4b\u91cf\u65b9\u6cd5\u5b58\u5728\u4e00\u4e9b\u7f3a\u70b9\u3002\u9ad8\u60ef\u6027\u7535\u673a\u5728",
    "approaches zero. Since the firmware looks for an abnormal rate of increase in this relative angular position there will be larger errors for motors with high inertia. The method relies on gradual current reduction and multiple retries for accurate pullout detection which consumes a lot of time. The pullout method typically takes 30 \u2013 45 seconds to complete.":
        "\u8d8b\u8fd1\u96f6\u65f6\u4e0d\u4f1a\u663e\u793a\u901f\u5ea6\u7684\u5feb\u901f\u53d8\u5316\u3002\u7531\u4e8e\u56fa\u4ef6\u5bfb\u627e\u6b64\u76f8\u5bf9\u89d2\u4f4d\u7684\u5f02\u5e38\u589e\u957f\u7387\uff0c\u9ad8\u60ef\u6027\u7535\u673a\u4f1a\u6709\u66f4\u5927\u7684\u8bef\u5dee\u3002\u6b64\u65b9\u6cd5\u4f9d\u8d56\u9010\u6e10\u51cf\u5c0f\u7535\u6d41\u548c\u591a\u6b21\u91cd\u8bd5\u4ee5\u51c6\u786e\u68c0\u6d4b\u5931\u6b65\uff0c\u6d88\u8017\u5927\u91cf\u65f6\u95f4\u3002\u5931\u6b65\u65b9\u6cd5\u901a\u5e38\u9700\u8981 30\u201345 \u79d2\u5b8c\u6210\u3002",
    "Cogging torque effects, limited resolution of sensors, and slower rotational speeds can all cause the relative angle between the voltage vector and QEI position counter to abruptly change which poses challenges to the filtering software.":
        "\u9f7f\u69fd\u8f6c\u77e9\u6548\u5e94\u3001\u4f20\u611f\u5668\u6709\u9650\u5206\u8fa8\u7387\u548c\u8f83\u4f4e\u7684\u65cb\u8f6c\u901f\u5ea6\u90fd\u53ef\u80fd\u5bfc\u81f4\u7535\u538b\u77e2\u91cf\u4e0e QEI \u4f4d\u7f6e\u8ba1\u6570\u5668\u4e4b\u95f4\u7684\u76f8\u5bf9\u89d2\u5ea6\u7a81\u53d8\uff0c\u8fd9\u7ed9\u6ee4\u6ce2\u8f6f\u4ef6\u5e26\u6765\u6311\u6218\u3002",
    "Practical implementation issues": "\u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "The pullout slip threshold was chosen to keep the absolute error for a wide range of motors within limits. With motors having low inertia the error will be on the positive side and for ones with high inertia the error is on the negative. A future implementation could configure the velocity threshold used to detect pullout to the motor, which will further reduce the absolute error in most cases.":
        "\u5931\u6b65\u6ed1\u5dee\u9608\u503c\u7684\u9009\u62e9\u662f\u4e3a\u4e86\u5c06\u5e7f\u8303\u56f4\u7535\u673a\u7684\u7edd\u5bf9\u8bef\u5dee\u4fdd\u6301\u5728\u9650\u5236\u5185\u3002\u5bf9\u4e8e\u4f4e\u60ef\u6027\u7535\u673a\uff0c\u8bef\u5dee\u504f\u6b63\uff1b\u5bf9\u4e8e\u9ad8\u60ef\u6027\u7535\u673a\uff0c\u8bef\u5dee\u504f\u8d1f\u3002\u672a\u6765\u7684\u5b9e\u73b0\u53ef\u4ee5\u5c06\u7528\u4e8e\u68c0\u6d4b\u5931\u6b65\u7684\u901f\u5ea6\u9608\u503c\u914d\u7f6e\u4e3a\u4e0e\u7535\u673a\u76f8\u5339\u914d\uff0c\u8fd9\u5c06\u5728\u5927\u591a\u6570\u60c5\u51b5\u4e0b\u8fdb\u4e00\u6b65\u51cf\u5c0f\u7edd\u5bf9\u8bef\u5dee\u3002",
    "The time it takes to complete the measurement is based on 4 trials which makes the measurement duration high. With lower resolution encoders a larger number of trials are needed for the same accuracy. For example, with a 250 line encoder 8 re-tries had better results.":
        "\u5b8c\u6210\u6d4b\u91cf\u6240\u9700\u7684\u65f6\u95f4\u57fa\u4e8e 4 \u6b21\u8bd5\u9a8c\uff0c\u8fd9\u4f7f\u6d4b\u91cf\u65f6\u95f4\u8f83\u957f\u3002\u5bf9\u4e8e\u4f4e\u5206\u8fa8\u7387\u7f16\u7801\u5668\uff0c\u9700\u8981\u66f4\u591a\u6b21\u8bd5\u9a8c\u624d\u80fd\u8fbe\u5230\u76f8\u540c\u7cbe\u5ea6\u3002\u4f8b\u5982\uff0c\u5bf9\u4e8e 250 \u7ebf\u7f16\u7801\u5668\uff0c8 \u6b21\u91cd\u8bd5\u7684\u7ed3\u679c\u66f4\u597d\u3002",
    "Since a retry has to be started before the motor actually stalls, the exact point of pullout is only approached and never attained which makes this method always have some small non-zero error.":
        "\u7531\u4e8e\u91cd\u8bd5\u5fc5\u987b\u5728\u7535\u673a\u5b9e\u9645\u505c\u8f6c\u4e4b\u524d\u5f00\u59cb\uff0c\u5931\u6b65\u70b9\u53ea\u662f\u88ab\u903c\u8fd1\u800c\u4ece\u672a\u771f\u6b63\u8fbe\u5230\uff0c\u8fd9\u4f7f\u5f97\u6b64\u65b9\u6cd5\u59cb\u7ec8\u5b58\u5728\u4e00\u4e9b\u5c0f\u7684\u975e\u96f6\u8bef\u5dee\u3002",
    "Example data": "\u793a\u4f8b\u6570\u636e",
    "The tests are done on 4 different motors equipped with an encoder and Index. The index is only used to compute the difference between measured and precomputed offsets for the motor. This value is used only for test purposes.":
        "\u6d4b\u8bd5\u5728 4 \u4e2a\u4e0d\u540c\u7684\u914d\u6709\u7f16\u7801\u5668\u548c\u7d22\u5f15\u7684\u7535\u673a\u4e0a\u8fdb\u884c\u3002\u7d22\u5f15\u4ec5\u7528\u4e8e\u8ba1\u7b97\u6d4b\u91cf\u504f\u79fb\u4e0e\u9884\u8ba1\u7b97\u504f\u79fb\u4e4b\u95f4\u7684\u5dee\u503c\u3002\u6b64\u503c\u4ec5\u7528\u4e8e\u6d4b\u8bd5\u76ee\u7684\u3002",
    "shows the use of the pullout method with the Anaheim Automation BLWS232D-24V-1350-1024SI5, which has a 1024-line encoder and fairly low cogging torque. For this motor, the pullout method works very well with low error. The yellow highlight shows the speed ramp up states (speed not shown), once speed has stabilized in the \u201cSPIN\u201d state,":
        "\u5c55\u793a\u4e86\u5931\u6b65\u65b9\u6cd5\u5728 Anaheim Automation BLWS232D-24V-1350-1024SI5 \u4e0a\u7684\u4f7f\u7528\uff0c\u8be5\u7535\u673a\u5177\u6709 1024 \u7ebf\u7f16\u7801\u5668\u548c\u8f83\u4f4e\u7684\u9f7f\u69fd\u8f6c\u77e9\u3002\u5bf9\u4e8e\u6b64\u7535\u673a\uff0c\u5931\u6b65\u65b9\u6cd5\u6548\u679c\u5f88\u597d\uff0c\u8bef\u5dee\u4f4e\u3002\u9ec4\u8272\u9ad8\u4eae\u90e8\u5206\u663e\u793a\u901f\u5ea6\u4e0a\u5347\u72b6\u6001\uff08\u901f\u5ea6\u672a\u663e\u793a\uff09\uff0c\u4e00\u65e6\u901f\u5ea6\u5728\u201cSPIN\u201d\u72b6\u6001\u4e2d\u7a33\u5b9a\uff0c",
    "current is reduced until it reaches the maximum value of pullout torque angle. During the first iteration the current reduction happens at a higher rate and is primarily to arrive in the proximity of the pullout. The subsequent iterations will then repeat the same procedure at a much reduced rate for better accuracy. The plot shows 4 more re-tries, the results of which are averaged to obtain the commutation offset. Note":
        "\u7535\u6d41\u88ab\u51cf\u5c0f\u76f4\u5230\u8fbe\u5230\u5931\u6b65\u8f6c\u77e9\u89d2\u5ea6\u7684\u6700\u5927\u503c\u3002\u5728\u7b2c\u4e00\u6b21\u8fed\u4ee3\u4e2d\uff0c\u7535\u6d41\u51cf\u5c0f\u901f\u7387\u8f83\u9ad8\uff0c\u4e3b\u8981\u662f\u4e3a\u4e86\u8fbe\u5230\u5931\u6b65\u70b9\u9644\u8fd1\u3002\u540e\u7eed\u8fed\u4ee3\u5c06\u4ee5\u5927\u5927\u964d\u4f4e\u7684\u901f\u7387\u91cd\u590d\u76f8\u540c\u7684\u8fc7\u7a0b\u4ee5\u83b7\u5f97\u66f4\u597d\u7684\u7cbe\u5ea6\u3002\u56fe\u4e2d\u663e\u793a\u4e86 4 \u6b21\u989d\u5916\u7684\u91cd\u8bd5\uff0c\u5176\u7ed3\u679c\u53d6\u5e73\u5747\u4ee5\u83b7\u5f97\u6362\u76f8\u504f\u79fb\u3002\u6ce8\u610f",
    "goes close to 0 after the retry stage in each of the plots when the \u201cSPIN\u201d state is completed.":
        "\u5728\u6bcf\u4e2a\u56fe\u4e2d\u7684\u91cd\u8bd5\u9636\u6bb5\u540e\u201cSPIN\u201d\u72b6\u6001\u5b8c\u6210\u65f6\u63a5\u8fd1 0\u3002",
    "Pullout method with BLWS232D-24V-1350-1024SI5": "\u5931\u6b65\u65b9\u6cd5\uff08BLWS232D-24V-1350-1024SI5\uff09",
    "shows the use of the pullout method with the Anaheim Automation BLY342D-24V-3200-1024SI5, which has a 1024-line encoder and substantial cogging torque.":
        "\u5c55\u793a\u4e86\u5931\u6b65\u65b9\u6cd5\u5728 Anaheim Automation BLY342D-24V-3200-1024SI5 \u4e0a\u7684\u4f7f\u7528\uff0c\u8be5\u7535\u673a\u5177\u6709 1024 \u7ebf\u7f16\u7801\u5668\u548c\u663e\u8457\u7684\u9f7f\u69fd\u8f6c\u77e9\u3002",
    "pullout method with BLY342D-24V-3000-1024SI5": "\u5931\u6b65\u65b9\u6cd5\uff08BLY342D-24V-3000-1024SI5\uff09",
    "shows the use of the pullout method with the Anaheim Automation BLY171D-24V-4000, which has a 4096-line encoder and almost no cogging torque.":
        "\u5c55\u793a\u4e86\u5931\u6b65\u65b9\u6cd5\u5728 Anaheim Automation BLY171D-24V-4000 \u4e0a\u7684\u4f7f\u7528\uff0c\u8be5\u7535\u673a\u5177\u6709 4096 \u7ebf\u7f16\u7801\u5668\u548c\u51e0\u4e4e\u6ca1\u6709\u9f7f\u69fd\u8f6c\u77e9\u3002",
    "Pullout method with BLY171D-24V-4000": "\u5931\u6b65\u65b9\u6cd5\uff08BLY171D-24V-4000\uff09",
    "In this case due to lesser inertia the default slip threshold results in detecting pullout late or past the actual pullout point. This results in the errors having an opposite sign ( see":
        "\u5728\u6b64\u60c5\u51b5\u4e0b\uff0c\u7531\u4e8e\u60ef\u6027\u8f83\u5c0f\uff0c\u9ed8\u8ba4\u7684\u6ed1\u5dee\u9608\u503c\u5bfc\u81f4\u5931\u6b65\u68c0\u6d4b\u6ed1\u6216\u8d85\u8fc7\u5b9e\u9645\u5931\u6b65\u70b9\u3002\u8fd9\u5bfc\u81f4\u8bef\u5dee\u5177\u6709\u76f8\u53cd\u7684\u7b26\u53f7\uff08\u53c2\u89c1",
    ") compared to the other motors for which the slip threshold is optimal. This motor is an example for a larger value of the slip threshold.":
        "\uff09\uff0c\u4e0e\u6ed1\u5dee\u9608\u503c\u6700\u4f73\u7684\u5176\u4ed6\u7535\u673a\u76f8\u6bd4\u3002\u6b64\u7535\u673a\u662f\u9700\u8981\u66f4\u5927\u6ed1\u5dee\u9608\u503c\u7684\u793a\u4f8b\u3002",
    "Accuracy and repeatability tests": "\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "The pullout method was tested with MCAF R4, and the resulting commutation offset from index (":
        "\u5931\u6b65\u65b9\u6cd5\u5728 MCAF R4 \u4e2d\u8fdb\u884c\u4e86\u6d4b\u8bd5\uff0c\u5e76\u5c06\u4ece\u7d22\u5f15\u83b7\u5f97\u7684\u6362\u76f8\u504f\u79fb\uff08",
    ") was compared against a reference method using open-circuit voltage measurements of the motor terminals with the motor rotated mechanically at constant speed.":
        "\uff09\u4e0e\u53c2\u8003\u65b9\u6cd5\u8fdb\u884c\u4e86\u6bd4\u8f83\uff0c\u53c2\u8003\u65b9\u6cd5\u662f\u5728\u7535\u673a\u4ee5\u6052\u5b9a\u901f\u5ea6\u673a\u68b0\u8f6c\u52a8\u65f6\u6d4b\u91cf\u7535\u673a\u7aef\u5b50\u7684\u5f00\u8def\u7535\u538b\u3002",
    "describes the results. In each case, 8 iterations of the pullout method were performed. Each motor was tested in both directions which are indicated by CW and CCW suffixes. All motors were tested with the default slip threshold value.":
        "\u63cf\u8ff0\u4e86\u7ed3\u679c\u3002\u5728\u6bcf\u79cd\u60c5\u51b5\u4e0b\uff0c\u5931\u6b65\u65b9\u6cd5\u8fdb\u884c\u4e86 8 \u6b21\u8fed\u4ee3\u3002\u6bcf\u4e2a\u7535\u673a\u5728\u4e24\u4e2a\u65b9\u5411\u4e0a\u8fdb\u884c\u4e86\u6d4b\u8bd5\uff0c\u4ee5 CW \u548c CCW \u540e\u7f00\u8868\u793a\u3002\u6240\u6709\u7535\u673a\u5747\u4f7f\u7528\u9ed8\u8ba4\u7684\u6ed1\u5dee\u9608\u503c\u8fdb\u884c\u6d4b\u8bd5\u3002",
    "Accuracy and repeatability metrics for the pullout method": "\u5931\u6b65\u65b9\u6cd5\u7684\u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6307\u6807",
    "mean": "\u5747\u503c",
    "max": "\u6700\u5927\u503c",
    "stdev": "\u6807\u51c6\u5dee",
    "span": "\u6781\u5dee",
    "Test case": "\u6d4b\u8bd5\u7528\u4f8b",
    "The error metrics are as follows:": "\u8bef\u5dee\u6307\u6807\u5982\u4e0b\uff1a",
    "\u2014 mean value of the commutation offset difference between the pullout method and the reference method":
        "\u2014 \u5931\u6b65\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u5747\u503c",
    "\u2014 maximum value of the commutation offset difference between the pullout method and the reference method":
        "\u2014 \u5931\u6b65\u65b9\u6cd5\u4e0e\u53c2\u8003\u65b9\u6cd5\u4e4b\u95f4\u6362\u76f8\u504f\u79fb\u5dee\u503c\u7684\u6700\u5927\u503c",
    "\u2014 standard deviation of commutation offset estimated by the pullout method":
        "\u2014 \u5931\u6b65\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6807\u51c6\u5dee",
    "\u2014 difference between minimum and maximum commutation offset estimated by the pullout method":
        "\u2014 \u5931\u6b65\u65b9\u6cd5\u4f30\u8ba1\u7684\u6362\u76f8\u504f\u79fb\u7684\u6700\u5c0f\u503c\u4e0e\u6700\u5927\u503c\u4e4b\u5dee",
    "Motors with low inertia, such as the BLY171D-24V-4000, could benefit from a higher value of slip threshold for better accuracy. Please refer to the parameter customization notes on":
        "\u4f4e\u60ef\u6027\u7535\u673a\uff0c\u5982 BLY171D-24V-4000\uff0c\u53ef\u4ee5\u4ece\u66f4\u9ad8\u7684\u6ed1\u5dee\u9608\u503c\u4e2d\u53d7\u76ca\u4ee5\u83b7\u5f97\u66f4\u597d\u7684\u7cbe\u5ea6\u3002\u8bf7\u53c2\u9605\u5173\u4e8e",
    "pullout slip threshold": "\u5931\u6b65\u6ed1\u5dee\u9608\u503c",
    "for more information.": "\u7684\u53c2\u6570\u81ea\u5b9a\u4e49\u8bf4\u660e\u4e86\u89e3\u66f4\u591a\u4fe1\u606f\u3002",
    "5.4.3.3.4. Pullout torque method": "5.4.3.3.4. \u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5",
    "5.4.3.3.4.1. Overview": "5.4.3.3.4.1. \u6982\u8ff0",
    "5.4.3.3.4.2. Limitations": "5.4.3.3.4.2. \u5c40\u9650\u6027",
    "5.4.3.3.4.3. Practical implementation issues": "5.4.3.3.4.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.4.4. Example data": "5.4.3.3.4.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.4.5. Accuracy and repeatability tests": "5.4.3.3.4.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "Align-and-sweep method": "\u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5",
    "Angle-tracking Phase-locked Loop (ATPLL)": "\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
