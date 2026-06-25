# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/estimators"
title_zh = "5.4. \u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "5.4.1. Firmware Interface": "5.4.1. \u56fa\u4ef6\u63a5\u53e3",
    "5.4.1.1. Overview": "5.4.1.1. \u6982\u8ff0",
    "5.4.1.2. Terminology": "5.4.1.2. \u672f\u8bed",
    "5.4.1.3. Filesystem location": "5.4.1.3. \u6587\u4ef6\u7cfb\u7edf\u4f4d\u7f6e",
    "5.4.1.4. Storage and types": "5.4.1.4. \u5b58\u50a8\u548c\u7c7b\u578b",
    "5.4.1.5. Entry points and methods": "5.4.1.5. \u5165\u53e3\u70b9\u548c\u65b9\u6cd5",
    "5.4.1.6. Method summary": "5.4.1.6. \u65b9\u6cd5\u6982\u8ff0",
    "5.4.1.7. Errata": "5.4.1.7. \u52d8\u8bef",
    "5.4.2. AN1292 Phase-locked Loop (PLL)": "5.4.2. AN1292 \u9501\u76f8\u73af\uff08PLL\uff09",
    "5.4.2.1. Overview": "5.4.2.1. \u6982\u8ff0",
    "5.4.3. Quadrature encoder support": "5.4.3. \u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "5.4.3.1. Overview": "5.4.3.1. \u6982\u8ff0",
    "5.4.3.2. Tracking loop": "5.4.3.2. \u8ddf\u8e2a\u73af",
    "5.4.3.3. Back-EMF synchronization": "5.4.3.3. \u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "5.4.4. Angle-tracking Phase-locked Loop (ATPLL)": "5.4.4. \u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09",
    "5.4.4.1. Overview": "5.4.4.1. \u6982\u8ff0",
    "5.4.4.2. Implementation Block Diagram and Description": "5.4.4.2. \u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "5.4.4.3. Application to PMSMs with Saliency": "5.4.4.3. \u5728\u5177\u6709\u51f8\u6027\u7684 PMSM \u4e2d\u7684\u5e94\u7528",
    "5.4.4.4. Sample Results": "5.4.4.4. \u793a\u4f8b\u7ed3\u679c",
    "5.4.4.5. Implementation Notes": "5.4.4.5. \u5b9e\u73b0\u8bf4\u660e",
    "5.4.5. Zero-Speed / Maximum Torque (ZS/MT)": "5.4.5. \u96f6\u901f/\u6700\u5927\u8f6c\u77e9\uff08ZS/MT\uff09",
    "5.4.5.1. Overview": "5.4.5.1. \u6982\u8ff0",
    "5.4.5.2. Further information": "5.4.5.2. \u66f4\u591a\u4fe1\u606f",
    "5.4.6. Sliding Mode Observer (SMO)": "5.4.6. \u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09",
    "5.4.6.1. Overview": "5.4.6.1. \u6982\u8ff0",
    "5.4.6.2. Implementation Block Diagram and Description": "5.4.6.2. \u5b9e\u73b0\u65b9\u6846\u56fe\u548c\u63cf\u8ff0",
    "Overview": "\u6982\u8ff0",
    "To facilitate sensorless control of a": "\u4e3a\u4e86\u652f\u6301",
    ", MCAF offers a choice between the AN1292 Phase-locked Loop (PLL), Angle-tracking Phase-locked Loop (ATPLL), and AN1078 Sliding Mode Observer (SMO) estimators. In addition to these, support is also provided for Quadrature Encoder through the dsPIC":
        "\u7684\u65e0\u4f20\u611f\u5668\u63a7\u5236\uff0cMCAF \u63d0\u4f9b\u4e86 AN1292 \u9501\u76f8\u73af\uff08PLL\uff09\u3001\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09\u548c AN1078 \u6ed1\u6a21\u89c2\u6d4b\u5668\uff08SMO\uff09\u4f30\u8ba1\u5668\u7684\u9009\u62e9\u3002\u9664\u6b64\u4e4b\u5916\uff0c\u8fd8\u901a\u8fc7 dsPIC",
    "DSC QEI (Quadrature Encoder Interface) peripheral.": "DSC \u7684 QEI\uff08\u6b63\u4ea4\u7f16\u7801\u5668\u63a5\u53e3\uff09\u5916\u8bbe\u63d0\u4f9b\u4e86\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301\u3002",
    "Comparative analysis": "\u6bd4\u8f83\u5206\u6790",
    "Summary": "\u6982\u8ff0",
    "Comparison of estimators": "\u4f30\u8ba1\u5668\u6bd4\u8f83",
    "Criteria": "\u6807\u51c6",
    "Added in MCAF version": "\u6dfb\u52a0\u7684 MCAF \u7248\u672c",
    "Sensors": "\u4f20\u611f\u5668",
    "phase currents, voltages": "\u76f8\u7535\u6d41\u3001\u7535\u538b",
    "quadrature encoder": "\u6b63\u4ea4\u7f16\u7801\u5668",
    "Intrusive?": "\u4fb5\u5165\u5f0f\uff1f",
    "no": "\u5426",
    "yes": "\u662f",
    "Usable at or near zero speed?": "\u53ef\u5728\u96f6\u901f\u6216\u63a5\u8fd1\u96f6\u901f\u65f6\u4f7f\u7528\uff1f",
    "Usable at or near full speed?": "\u53ef\u5728\u6ee1\u901f\u6216\u63a5\u8fd1\u6ee1\u901f\u65f6\u4f7f\u7528\uff1f",
    "Supports significant rotor saliency?": "\u652f\u6301\u663e\u8457\u7684\u8f6c\u5b50\u51f8\u6027\uff1f",
    "Requires significant rotor saliency?": "\u9700\u8981\u663e\u8457\u7684\u8f6c\u5b50\u51f8\u6027\uff1f",
    "Sensitivity to motor parameter inaccuracy": "\u5bf9\u7535\u673a\u53c2\u6570\u4e0d\u51c6\u786e\u7684\u654f\u611f\u6027",
    "moderate": "\u4e2d\u7b49",
    "none": "\u65e0",
    "low": "\u4f4e",
    "Notes": "\u8bf4\u660e",
    "Quadrature encoder position has been present since MCAF R1, in a limited form usable for reference comparison only, but not usable for position or velocity feedback. MCAF R4 added":
        "\u6b63\u4ea4\u7f16\u7801\u5668\u4f4d\u7f6e\u4ece MCAF R1 \u5f00\u59cb\u5b58\u5728\uff0c\u4ee5\u9650\u5b9a\u5f62\u5f0f\u4ec5\u53ef\u7528\u4e8e\u53c2\u8003\u6bd4\u8f83\uff0c\u4f46\u4e0d\u53ef\u7528\u4e8e\u4f4d\u7f6e\u6216\u901f\u5ea6\u53cd\u9988\u3002MCAF R4 \u6dfb\u52a0\u4e86",
    "commutation offset synchronization": "\u6362\u76f8\u504f\u79fb\u540c\u6b65",
    "to allow its use for commutation.": "\u4ee5\u5141\u8bb8\u5176\u7528\u4e8e\u6362\u76f8\u3002",
    "The ATPLL algorithm was added in MCAF R5, and may be undergoing some changes in future versions to improve some of its performance characteristics.":
        "ATPLL \u7b97\u6cd5\u5728 MCAF R5 \u4e2d\u6dfb\u52a0\uff0c\u53ef\u80fd\u5728\u672a\u6765\u7248\u672c\u4e2d\u8fdb\u884c\u4e00\u4e9b\u66f4\u6539\u4ee5\u6539\u5584\u5176\u6027\u80fd\u7279\u6027\u3002",
    "Since MCAF R5, phase voltages are inferred from DC link voltage and duty cycle; more accurate results can be obtained from voltage measurements but this is neither required nor supported at present.":
        "\u4ece MCAF R5 \u5f00\u59cb\uff0c\u76f8\u7535\u538b\u7531\u76f4\u6d41\u6bcd\u7ebf\u7535\u538b\u548c\u5360\u7a7a\u6bd4\u63a8\u65ad\uff1b\u901a\u8fc7\u7535\u538b\u6d4b\u91cf\u53ef\u4ee5\u83b7\u5f97\u66f4\u51c6\u786e\u7684\u7ed3\u679c\uff0c\u4f46\u76ee\u524d\u65e2\u4e0d\u9700\u8981\u4e5f\u4e0d\u652f\u6301\u3002",
    "Position control and zero-speed control are not presently supported in MCAF.":
        "MCAF \u76ee\u524d\u4e0d\u652f\u6301\u4f4d\u7f6e\u63a7\u5236\u548c\u96f6\u901f\u63a7\u5236\u3002",
    "ZS/MT by itself requires some extra voltage margin and cannot run at full speed by itself, but it can be used in a hybrid estimator to cover low- and mid-range speeds, with another estimator covering high-speed operation.":
        "ZS/MT \u672c\u8eab\u9700\u8981\u4e00\u4e9b\u989d\u5916\u7684\u7535\u538b\u4f59\u91cf\uff0c\u65e0\u6cd5\u72ec\u7acb\u5728\u6ee1\u901f\u4e0b\u8fd0\u884c\uff0c\u4f46\u5b83\u53ef\u4ee5\u5728\u6df7\u5408\u4f30\u8ba1\u5668\u4e2d\u7528\u4e8e\u8986\u76d6\u4f4e\u901f\u548c\u4e2d\u901f\u8303\u56f4\uff0c\u7531\u53e6\u4e00\u4e2a\u4f30\u8ba1\u5668\u8986\u76d6\u9ad8\u901f\u8fd0\u884c\u3002",
    "Intrusive estimators": "\u4fb5\u5165\u5f0f\u4f30\u8ba1\u5668",
    "apply a voltage or current signal to assist in position and velocity estimation.":
        "\u65bd\u52a0\u7535\u538b\u6216\u7535\u6d41\u4fe1\u53f7\u4ee5\u534f\u52a9\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u3002",
    "ZS/MT applies a voltage perturbation at high frequency to estimate rotor position.":
        "ZS/MT \u65bd\u52a0\u9ad8\u9891\u7535\u538b\u6270\u52a8\u6765\u4f30\u8ba1\u8f6c\u5b50\u4f4d\u7f6e\u3002",
    "The SMO was added in MCAF R9, and may be undergoing some changes in future versions to improve some of its performance characteristics.":
        "SMO \u5728 MCAF R9 \u4e2d\u6dfb\u52a0\uff0c\u53ef\u80fd\u5728\u672a\u6765\u7248\u672c\u4e2d\u8fdb\u884c\u4e00\u4e9b\u66f4\u6539\u4ee5\u6539\u5584\u5176\u6027\u80fd\u7279\u6027\u3002",
    "Additional details": "\u989d\u5916\u7ec6\u8282",
    "Both the AN1292 Phase-locked Loop (PLL) estimator and the Angle-tracking Phase-locked Loop (ATPLL) estimator algorithms operate on the principle that the steady-state value of the d-axis component of the back emf is equal to zero. Unlike the AN1292 PLL estimator however, the ATPLL estimator includes a PI controller module in its structure. This PI controller needs to be tuned carefully in order to operate stably and satisfactorily over the entire operating velocity range. The AN1292 PLL on the other hand does not have a PI controller and is easier to implement in practice. At the cost of the additional tuning of the PI controller, the ATPLL estimator offers the following advantages over the AN1292 PLL estimator.":
        "AN1292 \u9501\u76f8\u73af\uff08PLL\uff09\u4f30\u8ba1\u5668\u548c\u89d2\u5ea6\u8ddf\u8e2a\u9501\u76f8\u73af\uff08ATPLL\uff09\u4f30\u8ba1\u5668\u7b97\u6cd5\u90fd\u57fa\u4e8e\u53cd\u7535\u52a8\u52bf d \u8f74\u5206\u91cf\u7684\u7a33\u6001\u503c\u4e3a\u96f6\u8fd9\u4e00\u539f\u7406\u8fd0\u884c\u3002\u4e0e AN1292 PLL \u4f30\u8ba1\u5668\u4e0d\u540c\u7684\u662f\uff0cATPLL \u4f30\u8ba1\u5668\u5728\u5176\u7ed3\u6784\u4e2d\u5305\u542b\u4e00\u4e2a PI \u63a7\u5236\u5668\u6a21\u5757\u3002\u8be5 PI \u63a7\u5236\u5668\u9700\u8981\u4ed4\u7ec6\u8c03\u8282\uff0c\u4ee5\u4fbf\u5728\u6574\u4e2a\u8fd0\u884c\u901f\u5ea6\u8303\u56f4\u5185\u7a33\u5b9a\u4e14\u4ee4\u4eba\u6ee1\u610f\u5730\u8fd0\u884c\u3002\u53e6\u4e00\u65b9\u9762\uff0cAN1292 PLL \u6ca1\u6709 PI \u63a7\u5236\u5668\uff0c\u5728\u5b9e\u8df5\u4e2d\u66f4\u6613\u5b9e\u73b0\u3002\u4ee5\u989d\u5916\u8c03\u8282 PI \u63a7\u5236\u5668\u4e3a\u4ee3\u4ef7\uff0cATPLL \u4f30\u8ba1\u5668\u63d0\u4f9b\u4e86\u4ee5\u4e0b\u76f8\u5bf9\u4e8e AN1292 PLL \u4f30\u8ba1\u5668\u7684\u4f18\u52bf\u3002",
    "One of the advantages offered by the ATPLL estimator is its applicability to motors with both salient and non-salient rotors. By choosing the suitable equations for back-emf calculation for motors with salient and non-salient rotors, the rotor angle and rotor velocity can be correctly estimated by the ATPLL estimator.":
        "ATPLL \u4f30\u8ba1\u5668\u7684\u4f18\u52bf\u4e4b\u4e00\u662f\u5176\u9002\u7528\u4e8e\u5177\u6709\u51f8\u6781\u548c\u975e\u51f8\u6781\u8f6c\u5b50\u7684\u7535\u673a\u3002\u901a\u8fc7\u4e3a\u51f8\u6781\u548c\u975e\u51f8\u6781\u8f6c\u5b50\u7684\u7535\u673a\u9009\u62e9\u5408\u9002\u7684\u53cd\u7535\u52a8\u52bf\u8ba1\u7b97\u65b9\u7a0b\uff0cATPLL \u4f30\u8ba1\u5668\u53ef\u4ee5\u6b63\u786e\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\u548c\u8f6c\u5b50\u901f\u5ea6\u3002",
    "The other major advantage offered by the ATPLL estimator over the AN1292 PLL estimator is its robustness with respect to the value of the back-emf constant. For the AN1292 PLL estimator, a discrepancy between the values of the back-emf constant used by the estimator and the actual back-emf constant of the motor results in a steady-state error in the estimated rotor angle. There is no steady state error in the estimated velocity. The ATPLL estimator however is not susceptible to any discrepancy in the back-emf constant and estimates the rotor velocity and angle accurately.":
        "ATPLL \u4f30\u8ba1\u5668\u76f8\u5bf9\u4e8e AN1292 PLL \u4f30\u8ba1\u5668\u7684\u53e6\u4e00\u4e3b\u8981\u4f18\u52bf\u662f\u5176\u5bf9\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u503c\u7684\u9c81\u68d2\u6027\u3002\u5bf9\u4e8e AN1292 PLL \u4f30\u8ba1\u5668\uff0c\u4f30\u8ba1\u5668\u4f7f\u7528\u7684\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u4e0e\u7535\u673a\u5b9e\u9645\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u4e4b\u95f4\u7684\u504f\u5dee\u4f1a\u5bfc\u81f4\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\u7684\u7a33\u6001\u8bef\u5dee\u3002\u4f30\u8ba1\u901f\u5ea6\u6ca1\u6709\u7a33\u6001\u8bef\u5dee\u3002\u7136\u800c\uff0cATPLL \u4f30\u8ba1\u5668\u4e0d\u53d7\u53cd\u7535\u52a8\u52bf\u5e38\u6570\u504f\u5dee\u7684\u5f71\u54cd\uff0c\u80fd\u591f\u51c6\u786e\u4f30\u8ba1\u8f6c\u5b50\u901f\u5ea6\u548c\u89d2\u5ea6\u3002",
    "shows the actual rotor angle, the estimated angle by the ATPLL estimator and the estimated angle by AN1292 PLL estimator in steady state, when the actual back-emf constant of the motor (":
        "\u5c55\u793a\u4e86\u7a33\u6001\u4e0b\u7684\u5b9e\u9645\u8f6c\u5b50\u89d2\u5ea6\u3001ATPLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u89d2\u5ea6\u548c AN1292 PLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u89d2\u5ea6\uff0c\u5f53\u7535\u673a\u7684\u5b9e\u9645\u53cd\u7535\u52a8\u52bf\u5e38\u6570\uff08",
    ") is 20% lower than the value used by the estimator (": "\uff09\u6bd4\u4f30\u8ba1\u5668\u4f7f\u7528\u7684\u503c\uff08",
    ").": "\uff09\u4f4e 20%\u3002",
    "also shows the error in the estimated angle by the AN1292 PLL estimator and the ATPLL estimator in separate plots. It can be observed that there is a significant steady-state error in the estimated angle by the AN1292 PLL estimator, whereas there is no steady-state error in the estimated angle by the ATPLL estimator.":
        "\u8fd8\u5728\u5355\u72ec\u7684\u56fe\u4e2d\u5c55\u793a\u4e86 AN1292 PLL \u4f30\u8ba1\u5668\u548c ATPLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u89d2\u5ea6\u8bef\u5dee\u3002\u53ef\u4ee5\u89c2\u5bdf\u5230\uff0cAN1292 PLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u89d2\u5ea6\u5b58\u5728\u663e\u8457\u7684\u7a33\u6001\u8bef\u5dee\uff0c\u800c ATPLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u89d2\u5ea6\u6ca1\u6709\u7a33\u6001\u8bef\u5dee\u3002",
    "Similar plots are shown in": "\u7c7b\u4f3c\u7684\u56fe\u5c55\u793a\u5728",
    "where the actual back-emf constant of the motor (": "\u5176\u4e2d\u7535\u673a\u7684\u5b9e\u9645\u53cd\u7535\u52a8\u52bf\u5e38\u6570\uff08",
    ") is 20% higher than the value used by the estimator (": "\uff09\u6bd4\u4f30\u8ba1\u5668\u4f7f\u7528\u7684\u503c\uff08",
    "). It can be observed that there is a steady-state error in the estimated rotor angle by the AN1292 PLL estimator in this case as well, however the sign of the error is reversed. The ATPLL estimator however does not show any steady-state error in the estimated rotor angle.":
        "\uff09\u9ad8 20%\u3002\u53ef\u4ee5\u89c2\u5bdf\u5230\uff0c\u5728\u8fd9\u79cd\u60c5\u51b5\u4e0b AN1292 PLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\u4e5f\u5b58\u5728\u7a33\u6001\u8bef\u5dee\uff0c\u4f46\u8bef\u5dee\u7684\u7b26\u53f7\u76f8\u53cd\u3002\u7136\u800c\uff0cATPLL \u4f30\u8ba1\u5668\u7684\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\u4e0d\u663e\u793a\u4efb\u4f55\u7a73\u6001\u8bef\u5dee\u3002",
    "Estimated Rotor Angle by the ATPLL and AN1292 PLL for": "ATPLL \u548c AN1292 PLL \u7684\u4f30\u8ba1\u8f6c\u5b50\u89d2\u5ea6\uff08",
    "5.4. Position and Velocity Estimation": "5.4. \u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "5.4.7. Overview": "5.4.7. \u6982\u8ff0",
    "5.4.8. Comparative analysis": "5.4.8. \u6bd4\u8f83\u5206\u6790",
    "5.4.8.1. Summary": "5.4.8.1. \u6982\u8ff0",
    "5.4.8.2. Additional details": "5.4.8.2. \u989d\u5916\u7ec6\u8282",
    "Stopping": "\u505c\u6b62",
    "Firmware Interface": "\u56fa\u4ef6\u63a5\u53e3",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
