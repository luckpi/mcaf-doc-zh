# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/qei_sync/common"
title_zh = "5.4.3.3.1. \u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "Implementation issues common to all methods": "\u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898",
    "API of": "API",
    "Each of the back-emf synchronization methods has been designed to meet the following":
        "\u6bcf\u79cd\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u65b9\u6cd5\u90fd\u88ab\u8bbe\u8ba1\u4e3a\u6ee1\u8db3\u4ee5\u4e0b",
    "API": "API",
    "for all methods:": "\uff08\u9002\u7528\u4e8e\u6240\u6709\u65b9\u6cd5\uff09\uff1a",
    "The generated code is located in the": "\u751f\u6210\u7684\u4ee3\u7801\u4f4d\u4e8e",
    "module": "\u6a21\u5757",
    "Dependencies of the": "\u4f9d\u8d56\u5173\u7cfb\uff1a",
    "It may depend on the": "\u5b83\u53ef\u80fd\u4f9d\u8d56\u4e8e",
    "startup": "startup",
    "and": "\u548c",
    "qei": "qei",
    "modules": "\u6a21\u5757",
    "There are no dependencies on the": "\u4e0d\u4f9d\u8d56\u4e8e",
    "system_state": "system_state",
    "or": "\u6216",
    "commutation": "commutation",
    "It does not access any HAL functions directly": "\u5b83\u4e0d\u76f4\u63a5\u8bbf\u95ee\u4efb\u4f55 HAL \u51fd\u6570",
    "State data of the": "\u72b6\u6001\u6570\u636e\u4f4d\u4e8e",
    "is located in": "\u4e2d",
    "is a flag that denotes whether back-emf synchronization is complete. To re-run the synchronization, set this flag to":
        "\u662f\u4e00\u4e2a\u6807\u5fd7\uff0c\u8868\u793a\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u662f\u5426\u5b8c\u6210\u3002\u8981\u91cd\u65b0\u8fd0\u884c\u540c\u6b65\uff0c\u5c06\u6b64\u6807\u5fd7\u8bbe\u7f6e\u4e3a",
    "using the real-time diagnostic software.": "\uff08\u4f7f\u7528\u5b9e\u65f6\u8bca\u65ad\u8f6f\u4ef6\uff09\u3002",
    "Methods": "\u65b9\u6cd5",
    "\u2014 initialization function, runs once": "\u2014 \u521d\u59cb\u5316\u51fd\u6570\uff0c\u8fd0\u884c\u4e00\u6b21",
    "\u2014 update function, runs in control ISR, returns action flags to influence startup behavior in certain states. These action flags are only valid in":
        "\u2014 \u66f4\u65b0\u51fd\u6570\uff0c\u5728\u63a7\u5236 ISR \u4e2d\u8fd0\u884c\uff0c\u8fd4\u56de\u52a8\u4f5c\u6807\u5fd7\u4ee5\u5728\u67d0\u4e9b\u72b6\u6001\u4e2d\u5f71\u54cd\u542f\u52a8\u884c\u4e3a\u3002\u8fd9\u4e9b\u52a8\u4f5c\u6807\u5fd7\u4ec5\u5728",
    "startup states with a status code": "\u542f\u52a8\u72b6\u6001\u4e2d\u4e14\u72b6\u6001\u7801\u4e3a",
    "of": "\u65f6\u6709\u6548",
    ". The return value can contain any of the following bit flags:":
        "\u3002\u8fd4\u56de\u503c\u53ef\u4ee5\u5305\u542b\u4ee5\u4e0b\u4efb\u4f55\u4f4d\u6807\u5fd7\uff1a",
    "\u2014 startup state machine will be delayed, and remain in its current state":
        "\u2014 \u542f\u52a8\u72b6\u6001\u673a\u5c06\u88ab\u5ef6\u8fdf\uff0c\u5e76\u4fdd\u6301\u5728\u5f53\u524d\u72b6\u6001",
    "will be called": "\u5c06\u88ab\u8c03\u7528",
    "\u2014 returns whether synchronization is complete": "\u2014 \u8fd4\u56de\u540c\u6b65\u662f\u5426\u5b8c\u6210",
    "\u2014 returns commutation offset computed by the": "\u2014 \u8fd4\u56de\u7531",
    "module. This result is only required to be valid if synchronization is complete (otherwise this function\u2019s return value should be considered invalid)":
        "\u6a21\u5757\u8ba1\u7b97\u7684\u6362\u76f8\u504f\u79fb\u3002\u6b64\u7ed3\u679c\u4ec5\u5728\u540c\u6b65\u5b8c\u6210\u65f6\u9700\u8981\u6709\u6548\uff08\u5426\u5219\u6b64\u51fd\u6570\u7684\u8fd4\u56de\u503c\u5e94\u88ab\u89c6\u4e3a\u65e0\u6548\uff09",
    "Override handlers": "\u8986\u5199\u5904\u7406\u51fd\u6570",
    "The handler functions listed below are special methods that get called during appropriate stages of the":
        "\u4e0b\u9762\u5217\u51fa\u7684\u5904\u7406\u51fd\u6570\u662f\u5728",
    "startup sequence": "\u542f\u52a8\u5e8f\u5217",
    ". A pointer to specific data is provided by the caller. This facilitates modularity by eliminating coupling between the":
        "\u7684\u9002\u5f53\u9636\u6bb5\u88ab\u8c03\u7528\u7684\u7279\u6b8a\u65b9\u6cd5\u3002\u8c03\u7528\u8005\u63d0\u4f9b\u6307\u5411\u7279\u5b9a\u6570\u636e\u7684\u6307\u9488\u3002\u8fd9\u901a\u8fc7\u6d88\u9664",
    "modules; intercommunication is performed in the": "\u6a21\u5757\u4e4b\u95f4\u7684\u8026\u5408\u6765\u4fc3\u8fdb\u6a21\u5757\u5316\uff1b\u6a21\u5757\u95f4\u901a\u4fe1\u5728",
    "module.": "\u6a21\u5757\u4e2d\u8fdb\u884c\u3002",
    "Each handler has the option to change data or not, and is generally declared":
        "\u6bcf\u4e2a\u5904\u7406\u51fd\u6570\u53ef\u4ee5\u9009\u62e9\u662f\u5426\u66f4\u6539\u6570\u636e\uff0c\u901a\u5e38\u58f0\u660e\u4e3a",
    "so that an empty handler function would be optimized out.": "\u4ee5\u4fbf\u7a7a\u7684\u5904\u7406\u51fd\u6570\u4f1a\u88ab\u4f18\u5316\u6389\u3002",
    "Method": "\u65b9\u6cd5",
    "Applicable state": "\u9002\u7528\u72b6\u6001",
    "Behavior": "\u884c\u4e3a",
    "Can set current": "\u53ef\u8bbe\u7f6e\u7535\u6d41",
    "Can set the applied electrical angle": "\u53ef\u8bbe\u7f6e\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6",
    "Can set the applied electrical frequency": "\u53ef\u8bbe\u7f6e\u65bd\u52a0\u7684\u7535\u6c14\u9891\u7387",
    "Important data elements": "\u91cd\u8981\u6570\u636e\u5143\u7d20",
    "The following data members are available, regardless of which": "\u65e0\u8bba\u4f7f\u7528\u54ea\u79cd",
    "method is used:": "\u65b9\u6cd5\uff0c\u4ee5\u4e0b\u6570\u636e\u6210\u5458\u5747\u53ef\u7528\uff1a",
    "\u2014 controls commutation offset, which is the angle added to the raw electrical angle from the encoder before it is used for commutation. This can be modified using a real-time diagnostic tool to adjust the commutation offset while the motor is running. Any such changes should be slow: maximum recommended step size is 11 electrical degrees (2000 counts). Step changes larger than this may cause the control loops in FOC to lose synchronism.":
        "\u2014 \u63a7\u5236\u6362\u76f8\u504f\u79fb\uff0c\u5373\u5728\u7f16\u7801\u5668\u7684\u539f\u59cb\u7535\u6c14\u89d2\u5ea6\u7528\u4e8e\u6362\u76f8\u4e4b\u524d\u52a0\u4e0a\u7684\u89d2\u5ea6\u3002\u53ef\u4ee5\u4f7f\u7528\u5b9e\u65f6\u8bca\u65ad\u5de5\u5177\u5728\u7535\u673a\u8fd0\u884c\u65f6\u4fee\u6539\u6362\u76f8\u504f\u79fb\u3002\u4efb\u4f55\u6b64\u7c7b\u66f4\u6539\u5e94\u7f13\u6162\u8fdb\u884c\uff1a\u5efa\u8bae\u7684\u6700\u5927\u6b65\u8fdb\u4e3a 11 \u7535\u89d2\u5ea6\uff082000 \u8108\u51b2\uff09\u3002\u5927\u4e8e\u6b64\u7684\u6b65\u8fdb\u53d8\u5316\u53ef\u80fd\u5bfc\u81f4 FOC \u4e2d\u7684\u63a7\u5236\u73af\u5931\u53bb\u540c\u6b65\u3002",
    "\u2014 this is a convenience calculation provided at the end of back-emf synchronization, and it measures the commutation offset relative to the index position within one electrical cycle. When using a motor with an encoder that has an index pulse, the values of":
        "\u2014 \u8fd9\u662f\u5728\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u7ed3\u675f\u65f6\u63d0\u4f9b\u7684\u4e00\u4e2a\u4fbf\u6377\u8ba1\u7b97\uff0c\u5b83\u6d4b\u91cf\u5728\u4e00\u4e2a\u7535\u6c14\u5468\u671f\u5185\u76f8\u5bf9\u4e8e\u7d22\u5f15\u4f4d\u7f6e\u7684\u6362\u76f8\u504f\u79fb\u3002\u5f53\u4f7f\u7528\u5e26\u6709\u7d22\u5f15\u8109\u51b2\u7f16\u7801\u5668\u7684\u7535\u673a\u65f6\uff0c",
    "will be fairly consistent, independent of the starting position of the motor when the":
        "\u7684\u503c\u5c06\u76f8\u5f53\u4e00\u81f4\uff0c\u4e0e",
    "peripheral is enabled.": "\u5916\u8bbe\u542f\u7528\u65f6\u7535\u673a\u7684\u8d77\u59cb\u4f4d\u7f6e\u65e0\u5173\u3002",
    "5.4.3.3.1. Implementation issues common to all methods": "5.4.3.3.1. \u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.1.1. API of": "5.4.3.3.1.1. API",
    "5.4.3.3.1.2. Important data elements": "5.4.3.3.1.2. \u91cd\u8981\u6570\u636e\u5143\u7d20",
    "Back-EMF synchronization": "\u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "Align method": "\u5bf9\u9f50\u65b9\u6cd5",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
