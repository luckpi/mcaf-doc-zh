# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/temperature-measure"
title_zh = "5.9. \u6e29\u5ea6\u6d4b\u91cf"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Temperature measurement": "\u6e29\u5ea6\u6d4b\u91cf",
    "Boards with a power stage temperature sensor (\u201cbridge temperature\u201d) are supported in MCAF with basic signal conditioning. This temperature sensor should be placed on or near the power transistors of the three-phase bridge.":
        "\u5e26\u6709\u529f\u7387\u7ea7\u6e29\u5ea6\u4f20\u611f\u5668\uff08\u201c\u6865\u81c2\u6e29\u5ea6\u201d\uff09\u7684\u677f\u5728 MCAF \u4e2d\u53d7\u652f\u6301\uff0c\u5e26\u6709\u57fa\u672c\u7684\u4fe1\u53f7\u8c03\u7406\u3002\u6b64\u6e29\u5ea6\u4f20\u611f\u5668\u5e94\u653e\u7f6e\u5728\u4e09\u76f8\u6865\u7684\u529f\u7387\u6676\u4f53\u7ba1\u4e0a\u6216\u9644\u8fd1\u3002",
    "The bridge temperature signal is available for general use (for example, validation of":
        "\u6865\u81c2\u6e29\u5ea6\u4fe1\u53f7\u53ef\u4f9b\u4e00\u822c\u4f7f\u7528\uff08\u4f8b\u5982\uff0c\u9a8c\u8bc1",
    "dynamic current limit": "\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "parameters) and is also used to": "\u53c2\u6570\uff09\uff0c\u4e5f\u7528\u4e8e",
    "detect an overtemperature fault condition": "\u68c0\u6d4b\u8fc7\u6e29\u6545\u969c\u72b6\u6001",
    ", which causes the": "\uff0c\u8fd9\u4f1a\u5bfc\u81f4",
    "state machine": "\u72b6\u6001\u673a",
    "to enter the": "\u8fdb\u5165",
    "state and disable the drive.": "\u72b6\u6001\u5e76\u7981\u7528\u9a71\u52a8\u5668\u3002",
    "Filtering": "\u6ee4\u6ce2",
    "To reduce the impact of noisy measurements, a low-pass filter is used to process the raw temperature measurements":
        "\u4e3a\u4e86\u51cf\u5c11\u566a\u58f0\u6d4b\u91cf\u7684\u5f71\u54cd\uff0c\u4f7f\u7528\u4f4e\u901a\u6ee4\u6ce2\u5668\u5904\u7406\u539f\u59cb\u6e29\u5ea6\u6d4b\u91cf\u503c",
    ", as shown in": "\uff0c\u5982",
    "Figure 5.120": "\u56fe 5.120",
    ", into a temperature estimate": "\u6240\u793a\uff0c\u5f97\u5230\u6e29\u5ea6\u4f30\u8ba1\u503c",
    "Block diagram of temperature filtering": "\u6e29\u5ea6\u6ee4\u6ce2\u6846\u56fe",
    "This low-pass filter includes a slew-rate limit. As long as the output slew rate stays below a specified maximum rate of temperature change, the transfer function of the low-pass filter is":
        "\u6b64\u4f4e\u901a\u6ee4\u6ce2\u5668\u5305\u542b\u65cb\u8f6c\u7387\u9650\u5236\u3002\u53ea\u8981\u8f93\u51fa\u65cb\u8f6c\u7387\u4f4e\u4e8e\u6307\u5b9a\u7684\u6700\u5927\u6e29\u5ea6\u53d8\u5316\u7387\uff0c\u4f4e\u901a\u6ee4\u6ce2\u5668\u7684\u4f20\u9012\u51fd\u6570\u4e3a",
    ", where": "\uff0c\u5176\u4e2d",
    "is the effective time constant of the filter, determined by gain":
        "\u4e3a\u6ee4\u6ce2\u5668\u7684\u6709\u6548\u65f6\u95f4\u5e38\u6570\uff0c\u7531\u589e\u76ca",
    "The slew rate limiter is present to reduce the impact of burst noise on the temperature measurements. An example of this is shown in":
        "\u65cb\u8f6c\u7387\u9650\u5236\u5668\u7684\u5b58\u5728\u662f\u4e3a\u4e86\u51cf\u5c11\u7a81\u53d1\u566a\u58f0\u5bf9\u6e29\u5ea6\u6d4b\u91cf\u7684\u5f71\u54cd\u3002\u793a\u4f8b\u5982",
    "Figure 5.121": "\u56fe 5.121",
    "Simulation of burst noise in temperature filtering": "\u6e29\u5ea6\u6ee4\u6ce2\u4e2d\u7a81\u53d1\u566a\u58f0\u7684\u4eff\u771f",
    "While the presence of noise spikes on the raw temperature reading is a red flag that should be investigated to identify circuit design or EMI management issues, the temperature filtering in MCAF is intended to take advantage of oversampling the output of temperature sensors.":
        "\u867d\u7136\u539f\u59cb\u6e29\u5ea6\u8bfb\u6570\u4e0a\u5b58\u5728\u566a\u58f0\u5c16\u5cf0\u662f\u4e00\u4e2a\u8b66\u544a\u4fe1\u53f7\uff0c\u5e94\u8c03\u67e5\u4ee5\u786e\u5b9a\u7535\u8def\u8bbe\u8ba1\u6216 EMI \u7ba1\u7406\u95ee\u9898\uff0c\u4f46 MCAF \u4e2d\u7684\u6e29\u5ea6\u6ee4\u6ce2\u65e8\u5728\u5229\u7528\u6e29\u5ea6\u4f20\u611f\u5668\u8f93\u51fa\u7684\u8fc7\u91c7\u6837\u3002",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "Temperature sensing was added in MCAF R7.":
        "\u6e29\u5ea6\u611f\u6d4b\u5728 MCAF R7 \u4e2d\u6dfb\u52a0\u3002",
    "Implementation source code": "\u5b9e\u73b0\u6e90\u4ee3\u7801",
    "Filtering of the temperature sensors is done in":
        "\u6e29\u5ea6\u4f20\u611f\u5668\u7684\u6ee4\u6ce2\u5728",
    ", located in the": "\u4e2d\u5b8c\u6210\uff0c\u4f4d\u4e8e",
    "module.": "\u6a21\u5757\u3002",
    "Scaling": "\u7f29\u653e",
    "Temperature signals in MCAF are scaled at 0.01\u00b0C per count, for a range of \u2212327.68\u00b0C to +327.67\u00b0C.":
        "MCAF \u4e2d\u7684\u6e29\u5ea6\u4fe1\u53f7\u4ee5 0.01\u00b0C/\u8ba1\u6570 \u7f29\u653e\uff0c\u8303\u56f4\u4e3a \u2212327.68\u00b0C \u5230 +327.67\u00b0C\u3002",
    "MCAF R7 supports only linear temperature sensors at this time.":
        "MCAF R7 \u76ee\u524d\u4ec5\u652f\u6301\u7ebf\u6027\u6e29\u5ea6\u4f20\u611f\u5668\u3002",
    "Filtering parameters and state variables": "\u6ee4\u6ce2\u53c2\u6570\u548c\u72b6\u6001\u53d8\u91cf",
    "MCAF filters the temperature sense signals in each current loop sampling period":
        "MCAF \u5728\u6bcf\u4e2a\u7535\u6d41\u73af\u91c7\u6837\u5468\u671f\u5185\u6ee4\u6ce2\u6e29\u5ea6\u611f\u6d4b\u4fe1\u53f7",
    ", typically 50 \u03bcs. The state variable for the estimated temperature":
        "\uff0c\u901a\u5e38\u4e3a 50 \u03bcs\u3002\u4f30\u8ba1\u6e29\u5ea6\u7684\u72b6\u6001\u53d8\u91cf",
    "is a 32-bit integer with the high 16 bits used as its output \u2014 in other words, 0.01\u00b0C per 65536 counts for the state variable itself. This permits filter time constants as long as":
        "\u662f\u4e00\u4e2a 32 \u4f4d\u6574\u6570\uff0c\u9ad8 16 \u4f4d\u7528\u4f5c\u8f93\u51fa\u2014\u2014\u6362\u53e5\u8bdd\u8bf4\uff0c\u72b6\u6001\u53d8\u91cf\u672c\u8eab\u4e3a 0.01\u00b0C/\u6bcf 65536 \u8ba1\u6570\u3002\u8fd9\u5141\u8bb8\u6ee4\u6ce2\u65f6\u95f4\u5e38\u6570\u957f\u8fbe",
    ". (3.27 s for": "\u3002\uff083.27 s\uff0c",
    "50 \u03bcs)": "50 \u03bcs\uff09",
    "Slew rates between 1 and 32767 counts per sampling period \u2014 0.003\u00b0C/s to 100\u00b0C/s for":
        "\u6bcf\u91c7\u6837\u5468\u671f 1 \u5230 32767 \u8ba1\u6570\u4e4b\u95f4\u7684\u65cb\u8f6c\u7387\u2014\u2014\u5bf9\u4e8e",
    "50 \u03bcs \u2014 are supported.": "50 \u03bcs \u4e3a 0.003\u00b0C/s \u5230 100\u00b0C/s\u2014\u2014\u53d7\u652f\u6301\u3002",
    "Board support": "\u677f\u7ea7\u652f\u6301",
    "Both the": "\u4ee5\u4e0b\u4e24\u8005\u5747",
    "dsPIC33CK Low Voltage Motor Control (LVMC) Development Board":
        "dsPIC33CK \u4f4e\u538b\u7535\u673a\u63a7\u5236 (LVMC) \u5f00\u53d1\u677f",
    "and": "\u548c",
    "MCS MCLV\u201148V\u2011300W Development Board":
        "MCS MCLV-48V-300W \u5f00\u53d1\u677f",
    "boards include an MCP9700 temperature sensor (10mV/\u00b0C, 0.5V offset) mounted among the power transistors. The":
        "\u677f\u5747\u5305\u542b\u5b89\u88c5\u5728\u529f\u7387\u6676\u4f53\u7ba7\u4e4b\u95f4\u7684 MCP9700 \u6e29\u5ea6\u4f20\u611f\u5668\uff0810mV/\u00b0C\uff0c0.5V \u504f\u7f6e\uff09\u3002",
    "MCHV\u2011230VAC\u20111.5kW Motor Control High-Voltage Development Board":
        "MCHV-230VAC-1.5kW \u7535\u673a\u63a7\u5236\u9ad8\u538b\u5f00\u53d1\u677f",
    "power module includes a built-in NTC Thermistor for temperature monitoring, connected to an analog pin of the microcontroller.":
        "\u529f\u7387\u6a21\u5757\u5305\u542b\u5185\u7f6e NTC \u70ed\u654f\u7535\u963b\u7528\u4e8e\u6e29\u5ea6\u76d1\u63a7\uff0c\u8fde\u63a5\u5230\u5fae\u63a7\u5236\u5668\u7684\u6a21\u62df\u5f15\u811a\u3002",
    "5.9. Temperature measurement": "5.9. \u6e29\u5ea6\u6d4b\u91cf",
    "5.9.1. Filtering": "5.9.1. \u6ee4\u6ce2",
    "5.9.2. Implementation notes": "5.9.2. \u5b9e\u73b0\u8bf4\u660e",
    "5.9.2.1. Implementation source code": "5.9.2.1. \u5b9e\u73b0\u6e90\u4ee3\u7801",
    "5.9.2.2. Scaling": "5.9.2.2. \u7f29\u653e",
    "5.9.2.3. Filtering parameters and state variables": "5.9.2.3. \u6ee4\u6ce2\u53c2\u6570\u548c\u72b6\u6001\u53d8\u91cf",
    "5.9.3. Board support": "5.9.3. \u677f\u7ea7\u652f\u6301",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
