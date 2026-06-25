# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/flux_control/flux_weakening_mtpa_integration"
title_zh = "5.5.3. D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Flux control": "\u78c1\u94fe\u63a7\u5236",
    "D-axis current reference generation": "D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
    "Overview": "\u6982\u8ff0",
    "The flux-weakening module calculates the d-axis current reference": "\u5f31\u78c1\u6a21\u5757\u8ba1\u7b97 d \u8f74\u7535\u6d41\u53c2\u8003",
    ", whereas the MTPA module calculates the d-axis current reference": "\uff0c\u800c MTPA \u6a21\u5757\u8ba1\u7b97 d \u8f74\u7535\u6d41\u53c2\u8003",
    ". The": "\u3002",
    "generation module chooses the appropriate value between": "\u751f\u6210\u6a21\u5757\u5728",
    "and": "\u548c",
    "and generates the d-axis current reference": "\u4e4b\u95f4\u9009\u62e9\u9002\u5f53\u7684\u503c\uff0c\u5e76\u751f\u6210 d \u8f74\u7535\u6d41\u53c2\u8003",
    "to be given as an input to the current controller.":
        "\u4f5c\u4e3a\u7535\u6d41\u63a7\u5236\u5668\u7684\u8f93\u5165\u3002",
    "The q-axis current limit is computed from the value of":
        "q \u8f74\u7535\u6d41\u9650\u5236\u7531",
    ", to keep the overall motor current within acceptable bounds.":
        "\u7684\u503c\u8ba1\u7b97\u5f97\u51fa\uff0c\u4ee5\u4fdd\u6301\u7535\u673a\u603b\u7535\u6d41\u5728\u53ef\u63a5\u53d7\u7684\u8303\u56f4\u5185\u3002",
    "Flow chart and description": "\u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "shows a flow chart of the": "\u5c55\u793a\u4e86",
    "module. This module takes": "\u6a21\u5757\u7684\u6d41\u7a0b\u56fe\u3002\u6b64\u6a21\u5757\u63a5\u6536",
    "from the MTPA and FW modules, respectively.":
        "\uff0c\u5206\u522b\u6765\u81ea MTPA \u548c FW \u6a21\u5757\u3002",
    "generation flow chart": "\u751f\u6210\u6d41\u7a0b\u56fe",
    "Possible user inputs for enabling/disabling MTPA and FW are listed in the table below. It is observed that the correct choice for":
        "\u542f\u7528/\u7981\u7528 MTPA \u548c FW \u7684\u53ef\u80fd\u7528\u6237\u8f93\u5165\u5217\u5728\u4e0b\u8868\u4e2d\u3002\u53ef\u4ee5\u89c2\u5bdf\u5230\uff0c",
    "is the minimum of": "\u7684\u6b63\u786e\u9009\u62e9\u662f",
    "in all cases. Based on this, after calculation of": "\u7684\u6700\u5c0f\u503c\u3002\u57fa\u4e8e\u6b64\uff0c\u5728\u8ba1\u7b97",
    ", the algorithm calculates the minimum of the two (": "\u540e\uff0c\u7b97\u6cd5\u8ba1\u7b97\u4e24\u8005\u7684\u6700\u5c0f\u503c\uff08",
    ").": "\uff09\u3002",
    "User Selection": "\u7528\u6237\u9009\u62e9",
    "No-FW Region": "\u975e\u5f31\u78c1\u533a\u57df",
    "FW Region": "\u5f31\u78c1\u533a\u57df",
    "MTPA Disabled,": "MTPA \u7981\u7528\uff0c",
    "FW Disabled": "FW \u7981\u7528",
    "Does not enter": "\u4e0d\u8fdb\u5165",
    "FW Enabled": "FW \u542f\u7528",
    "MTPA Enabled,": "MTPA \u542f\u7528\uff0c",
    "The calculated": "\u8ba1\u7b97\u5f97\u5230\u7684",
    "is checked against a user-defined minimum value (": "\u4e0e\u7528\u6237\u5b9a\u4e49\u7684\u6700\u5c0f\u503c\uff08",
    "), and if found lower than": "\uff09\u8fdb\u884c\u68c0\u67e5\uff0c\u5982\u679c\u4f4e\u4e8e",
    ", it is limited to": "\uff0c\u5219\u9650\u5236\u4e3a",
    "The value thus obtained (": "\u5982\u6b64\u83b7\u5f97\u7684\u503c\uff08",
    ") is passed through a first-order low pass filter, and the output":
        "\uff09\u901a\u8fc7\u4e00\u9636\u4f4e\u901a\u6ee4\u6ce2\u5668\uff0c\u8f93\u51fa",
    "gives the d-axis reference as an input to the current controller.":
        "\u4f5c\u4e3a d \u8f74\u53c2\u8003\u8f93\u5165\u7535\u6d41\u63a7\u5236\u5668\u3002",
    "Calculation of q-axis current limit": "Q \u8f74\u7535\u6d41\u9650\u5236\u7684\u8ba1\u7b97",
    "Similar to the limit on the d-axis current, a limit is also imposed on the q-axis current in the motor. Two different methods of limiting the motor current are implemented viz. rectangular limits and quadratic limits. This choice can be made in":
        "\u4e0e d \u8f74\u7535\u6d41\u9650\u5236\u7c7b\u4f3c\uff0c\u7535\u673a\u7684 q \u8f74\u7535\u6d41\u4e5f\u65bd\u52a0\u4e86\u9650\u5236\u3002\u5b9e\u73b0\u4e86\u4e24\u79cd\u4e0d\u540c\u7684\u7535\u6d41\u9650\u5236\u65b9\u6cd5\uff0c\u5373\u77e9\u5f62\u9650\u5236\u548c\u4e8c\u6b21\u9650\u5236\u3002\u6b64\u9009\u62e9\u53ef\u4ee5\u5728",
    "Parameter Customization": "\u53c2\u6570\u81ea\u5b9a\u4e49",
    "Rectangular current limits: In this method, the limits on the d-axis and q-axis currents are defined independently. The limits are specified in":
        "\u77e9\u5f62\u7535\u6d41\u9650\u5236\uff1a\u5728\u6b64\u65b9\u6cd5\u4e2d\uff0cd \u8f74\u548c q \u8f74\u7535\u6d41\u7684\u9650\u5236\u72ec\u7acb\u5b9a\u4e49\u3002\u9650\u5236\u5728",
    "Quadratic current limits: In this method, after generation of the d-axis current reference (": "\u4e8c\u6b21\u7535\u6d41\u9650\u5236\uff1a\u5728\u6b64\u65b9\u6cd5\u4e2d\uff0c\u751f\u6210 d \u8f74\u7535\u6d41\u53c2\u8003\uff08",
    "), the q-axis current limit is calculated with the help of a quadratic approximation of a circular function as given below.":
        "\uff09\u540e\uff0cq \u8f74\u7535\u6d41\u9650\u5236\u901a\u8fc7\u4e0b\u9762\u7ed9\u51fa\u7684\u5706\u51fd\u6570\u7684\u4e8c\u6b21\u8fd1\u4f3c\u6765\u8ba1\u7b97\u3002",
    "The calculated q-axis current limit is used by the velocity controller in the FOC path to limit the q-axis current reference.":
        "\u8ba1\u7b97\u5f97\u5230\u7684 q \u8f74\u7535\u6d41\u9650\u5236\u88ab FOC \u8def\u5f84\u4e2d\u7684\u901f\u5ea6\u63a7\u5236\u5668\u7528\u4e8e\u9650\u5236 q \u8f74\u7535\u6d41\u53c2\u8003\u3002",
    "An illustration of these two methods is shown in":
        "\u8fd9\u4e24\u79cd\u65b9\u6cd5\u7684\u793a\u610f\u56fe\u5982",
    "calculation as a function of": "\u4f5c\u4e3a",
    "The striped curve represents a maximum amplitude of 1.0 normalized to":
        "\u7684\u51fd\u6570\u6240\u793a\u3002\u6761\u7eb9\u66f2\u7ebf\u8868\u793a\u5f52\u4e00\u5316\u5230",
    ", with thinner circular contours shown in steps of 0.01 amplitude above and below it. A rectangular limit is shown in orange, and a quadratic limit is shown in blue. Limits should be chosen to minimize the excursions above 1.0 amplitude. With the limits shown, a rectangular limit keeps the maximum amplitude below about 1.05 for":
        "\u7684\u6700\u5927\u5e45\u503c 1.0\uff0c\u4e0a\u4e0b\u4ee5 0.01 \u5e45\u503c\u4e3a\u6b65\u957f\u663e\u793a\u66f4\u7ec6\u7684\u5706\u5f62\u8f6e\u5ed3\u7ebf\u3002\u6a59\u8272\u8868\u793a\u77e9\u5f62\u9650\u5236\uff0c\u84dd\u8272\u8868\u793a\u4e8c\u6b21\u9650\u5236\u3002\u5e94\u9009\u62e9\u9650\u5236\u4ee5\u6700\u5c0f\u5316\u8d85\u8fc7 1.0 \u5e45\u503c\u7684\u504f\u79bb\u3002\u5728\u6240\u793a\u7684\u9650\u5236\u4e0b\uff0c\u77e9\u5f62\u9650\u5236\u4f7f",
    "; a quadratic limit keeps the maximum amplitude below about 1.03 for":
        "\u7684\u6700\u5927\u5e45\u503c\u4fdd\u6301\u5728\u7ea6 1.05 \u4ee5\u4e0b\uff1b\u4e8c\u6b21\u9650\u5236\u4f7f",
    "5.5.3. D-axis current reference generation": "5.5.3. D \u8f74\u7535\u6d41\u53c2\u8003\u751f\u6210",
    "5.5.3.1. Overview": "5.5.3.1. \u6982\u8ff0",
    "5.5.3.2. Flow chart and description": "5.5.3.2. \u6d41\u7a0b\u56fe\u548c\u8bf4\u660e",
    "5.5.3.3. Calculation of q-axis current limit": "5.5.3.3. Q \u8f74\u7535\u6d41\u9650\u5236\u7684\u8ba1\u7b97",
    "Maximum Torque Per Ampere (MTPA)": "\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\uff08MTPA\uff09",
    "Current limit": "\u7535\u6d41\u9650\u5236",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
