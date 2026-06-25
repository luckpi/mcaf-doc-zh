# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/estimator-interface"
title_zh = "5.4.1. \u56fa\u4ef6\u63a5\u53e3"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Firmware Interface": "\u56fa\u4ef6\u63a5\u53e3",
    "Overview": "\u6982\u8ff0",
    "Position and velocity estimators in MCAF have several common characteristics. This section describes their methods, types, and semantics. A fictional estimator called":
        "MCAF \u4e2d\u7684\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668\u5177\u6709\u51e0\u4e2a\u5171\u540c\u7279\u6027\u3002\u672c\u8282\u63cf\u8ff0\u5b83\u4eec\u7684\u65b9\u6cd5\u3001\u7c7b\u578b\u548c\u8bed\u4e49\u3002\u4e00\u4e2a\u540d\u4e3a",
    "will be used for example purposes.": "\u7684\u865a\u6784\u4f30\u8ba1\u5668\u5c06\u7528\u4e8e\u793a\u4f8b\u76ee\u7684\u3002",
    "Terminology": "\u672f\u8bed",
    "The following terms are used in MCAF to describe estimators:": "MCAF \u4e2d\u4f7f\u7528\u4ee5\u4e0b\u672f\u8bed\u6765\u63cf\u8ff0\u4f30\u8ba1\u5668\uff1a",
    "Term": "\u672f\u8bed",
    "Description": "\u63cf\u8ff0",
    "active": "\u6d3b\u8dc3",
    "An active estimator is in operation and determining an angle and velocity. (All estimators that are selected in the Customize page of motorBench":
        "\u6d3b\u8dc3\u4f30\u8ba1\u5668\u6b63\u5728\u8fd0\u884c\u5e76\u786e\u5b9a\u89d2\u5ea6\u548c\u901f\u5ea6\u3002\uff08\u5728 motorBench \u7684 Customize\uff08\u81ea\u5b9a\u4e49\uff09\u9875\u9762\u4e2d\u9009\u62e9",
    "Development Suite are active by default.)": "Development Suite\uff08\u5f00\u53d1\u5957\u4ef6\uff09\u4e2d\u7684\u6240\u6709\u4f30\u8ba1\u5668\u9ed8\u8ba4\u4e3a\u6d3b\u8dc3\u72b6\u6001\u3002\uff09",
    "primary": "\u4e3b",
    "The primary estimator determines the angle and velocity used for commutation and feedback. Several estimators can be active simultaneously, but only one can be the primary estimator at any given instant.":
        "\u4e3b\u4f30\u8ba1\u5668\u786e\u5b9a\u7528\u4e8e\u6362\u76f8\u548c\u53cd\u9988\u7684\u89d2\u5ea6\u548c\u901f\u5ea6\u3002\u591a\u4e2a\u4f30\u8ba1\u5668\u53ef\u4ee5\u540c\u65f6\u6d3b\u8dc3\uff0c\u4f46\u5728\u4efb\u4f55\u7ed9\u5b9a\u65f6\u523b\u53ea\u80fd\u6709\u4e00\u4e2a\u4e3b\u4f30\u8ba1\u5668\u3002",
    "intrusive": "\u4fb5\u5165\u5f0f",
    "An intrusive estimator is one that perturbs controller outputs with some sort of excitation waveform, which may have a minor impact on the motor currents and voltages. A non-intrusive estimator determines an angle and velocity through existing measurements of current, voltage, or other sensors, and does not affect operation except through its use as a primary estimator. Most estimators are non-intrusive.":
        "\u4fb5\u5165\u5f0f\u4f30\u8ba1\u5668\u662f\u7528\u67d0\u79cd\u6fc0\u52b1\u6ce2\u5f62\u6270\u52a8\u63a7\u5236\u5668\u8f93\u51fa\u7684\u4f30\u8ba1\u5668\uff0c\u53ef\u80fd\u5bf9\u7535\u673a\u7535\u6d41\u548c\u7535\u538b\u6709\u8f7b\u5fae\u5f71\u54cd\u3002\u975e\u4fb5\u5165\u5f0f\u4f30\u8ba1\u5668\u901a\u8fc7\u73b0\u6709\u7684\u7535\u6d41\u3001\u7535\u538b\u6216\u5176\u4ed6\u4f20\u611f\u5668\u6d4b\u91cf\u6765\u786e\u5b9a\u89d2\u5ea6\u548c\u901f\u5ea6\uff0c\u9664\u4e86\u4f5c\u4e3a\u4e3b\u4f30\u8ba1\u5668\u4f7f\u7528\u5916\u4e0d\u5f71\u54cd\u8fd0\u884c\u3002\u5927\u591a\u6570\u4f30\u8ba1\u5668\u662f\u975e\u4fb5\u5165\u5f0f\u7684\u3002",
    "Filesystem location": "\u6587\u4ef6\u7cfb\u7edf\u4f4d\u7f6e",
    "Call sites utilizing the estimators can be found in": "\u4f7f\u7528\u4f30\u8ba1\u5668\u7684\u8c03\u7528\u70b9\u53ef\u5728",
    "; storage is declared in": "\u4e2d\u627e\u5230\uff1b\u5b58\u50a8\u58f0\u660e\u5728",
    "Implementation of individual estimator modules are found in the": "\u5404\u4e2a\u4f30\u8ba1\u5668\u6a21\u5757\u7684\u5b9e\u73b0\u4f4d\u4e8e",
    "directory. They will typically consist of at least one .h file and one .c file, for example": "\u76ee\u5f55\u4e2d\u3002\u5b83\u4eec\u901a\u5e38\u81f3\u5c11\u5305\u542b\u4e00\u4e2a .h \u6587\u4ef6\u548c\u4e00\u4e2a .c \u6587\u4ef6\uff0c\u4f8b\u5982",
    ". Some estimator modules set apart type definitions in a types.h file, for example": "\u3002\u4e00\u4e9b\u4f30\u8ba1\u5668\u6a21\u5757\u5c06\u7c7b\u578b\u5b9a\u4e49\u5355\u72ec\u653e\u5728 types.h \u6587\u4ef6\u4e2d\uff0c\u4f8b\u5982",
    ". The estimator\u2019s state variable structure is defined in the types.h file, if it is present, along with inline static getter methods; otherwise they are defined in the main .h file. Function prototypes are declared in the main .h file.":
        "\u3002\u4f30\u8ba1\u5668\u7684\u72b6\u6001\u53d8\u91cf\u7ed3\u6784\u5b9a\u4e49\u5728 types.h \u6587\u4ef6\u4e2d\uff08\u5982\u679c\u5b58\u5728\uff09\uff0c\u8fde\u540c\u5185\u8054\u9759\u6001\u83b7\u53d6\u65b9\u6cd5\uff1b\u5426\u5219\u5b9a\u4e49\u5728\u4e3b .h \u6587\u4ef6\u4e2d\u3002\u51fd\u6570\u539f\u578b\u58f0\u660e\u5728\u4e3b .h \u6587\u4ef6\u4e2d\u3002",
    "Estimator-specific parameters, such as delays, limits, and tuning gains, are generated in": "\u4f30\u8ba1\u5668\u7279\u5b9a\u53c2\u6570\uff08\u5982\u5ef6\u8fdf\u3001\u9650\u5236\u548c\u8c03\u8282\u589e\u76ca\uff09\u751f\u6210\u5728",
    "Storage and types": "\u5b58\u50a8\u548c\u7c7b\u578b",
    "Each estimator will have a state variable structure defined in": "\u6bcf\u4e2a\u4f30\u8ba1\u5668\u90fd\u6709\u4e00\u4e2a\u72b6\u6001\u53d8\u91cf\u7ed3\u6784\u5b9a\u4e49\u5728",
    "or": "\u6216",
    ", for example:": "\uff0c\u4f8b\u5982\uff1a",
    "where": "\u5176\u4e2d",
    "is referenced in": "\u5728",
    "as part of the main motor data structure, so that the Xyz estimator state variable is located in": "\u4e2d\u5f15\u7528\uff0c\u4f5c\u4e3a\u4e3b\u7535\u673a\u6570\u636e\u7ed3\u6784\u7684\u4e00\u90e8\u5206\uff0c\u56e0\u6b64 Xyz \u4f30\u8ba1\u5668\u72b6\u6001\u53d8\u91cf\u4f4d\u4e8e",
    "More than one estimator may be actively operating in code generated from MCAF, but exactly one estimator is the primary estimator used for commutation feedback.":
        "\u5728 MCAF \u751f\u6210\u7684\u4ee3\u7801\u4e2d\uff0c\u53ef\u80fd\u6709\u591a\u4e2a\u4f30\u8ba1\u5668\u540c\u65f6\u8fd0\u884c\uff0c\u4f46\u6070\u597d\u53ea\u6709\u4e00\u4e2a\u4f30\u8ba1\u5668\u662f\u7528\u4e8e\u6362\u76f8\u53cd\u9988\u7684\u4e3b\u4f30\u8ba1\u5668\u3002",
    "The values in": "\u4e2d\u7684\u503c",
    "are the commutation angle of estimators, relative to the primary estimator. These values may be used for debugging or performance analysis, and include all estimators that are selected as":
        "\u662f\u4f30\u8ba1\u5668\u7684\u6362\u76f8\u89d2\u5ea6\uff0c\u76f8\u5bf9\u4e8e\u4e3b\u4f30\u8ba1\u5668\u3002\u8fd9\u4e9b\u503c\u53ef\u7528\u4e8e\u8c03\u8bd5\u6216\u6027\u80fd\u5206\u6790\uff0c\u5e76\u5305\u62ec\u6240\u6709\u88ab\u9009\u4e3a",
    "reference estimators": "\u53c2\u8003\u4f30\u8ba1\u5668",
    "The": "\u8be5",
    "function is a constant value that returns true or false for each estimator to indicate if it is the primary estimator.":
        "\u51fd\u6570\u662f\u4e00\u4e2a\u5e38\u503c\uff0c\u4e3a\u6bcf\u4e2a\u4f30\u8ba1\u5668\u8fd4\u56de true \u6216 false\uff0c\u4ee5\u6307\u793a\u5b83\u662f\u5426\u4e3a\u4e3b\u4f30\u8ba1\u5668\u3002",
    "Note:": "\u6ce8\u610f\uff1a",
    "The use of \u201cactive\u201d in the estimator firmware interface is incorrect at present. See the":
        "\u4f30\u8ba1\u5668\u56fa\u4ef6\u63a5\u53e3\u4e2d\u4f7f\u7528\u201c\u6d3b\u8dc3\u201d\u4e00\u8bcd\u76ee\u524d\u662f\u4e0d\u6b63\u786e\u7684\u3002\u53c2\u89c1",
    "Errata": "\u52d8\u8bef",
    "for more information.": "\u4e86\u89e3\u66f4\u591a\u4fe1\u606f\u3002",
    "Entry points and methods": "\u5165\u53e3\u70b9\u548c\u65b9\u6cd5",
    "There are several entry points and methods associated with position and velocity estimators.":
        "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1\u5668\u6709\u51e0\u4e2a\u5165\u53e3\u70b9\u548c\u65b9\u6cd5\u3002",
    "The entry points are as follows:": "\u5165\u53e3\u70b9\u5982\u4e0b\uff1a",
    "Initialization": "\u521d\u59cb\u5316",
    "is called during overall initialization. This happens once, shortly after power-on reset, and gives the estimator a chance to initialize its own state variables. Some estimators may depend on others, in which case the function":
        "\u5728\u6574\u4f53\u521d\u59cb\u5316\u671f\u95f4\u88ab\u8c03\u7528\u3002\u8fd9\u53d1\u751f\u5728\u4e0a\u7535\u590d\u4f4d\u540e\u4e0d\u4e45\uff0c\u53ea\u6267\u884c\u4e00\u6b21\uff0c\u7ed9\u4f30\u8ba1\u5668\u673a\u4f1a\u521d\u59cb\u5316\u81ea\u5df1\u7684\u72b6\u6001\u53d8\u91cf\u3002\u67d0\u4e9b\u4f30\u8ba1\u5668\u53ef\u80fd\u4f9d\u8d56\u5176\u4ed6\u4f30\u8ba1\u5668\uff0c\u5728\u8fd9\u79cd\u60c5\u51b5\u4e0b\u8fd8\u4f1a\u8c03\u7528\u51fd\u6570",
    "is also called, to provide access from other estimator outputs.": "\uff0c\u4ee5\u63d0\u4f9b\u5bf9\u5176\u4ed6\u4f30\u8ba1\u5668\u8f93\u51fa\u7684\u8bbf\u95ee\u3002",
    "Reinitialization at motor start": "\u7535\u673a\u542f\u52a8\u65f6\u7684\u91cd\u65b0\u521d\u59cb\u5316",
    "is called whenever the": "\u5728",
    "main motor state machine": "\u4e3b\u7535\u673a\u72b6\u6001\u673a",
    "transitions into the": "\u8f6c\u5165",
    "state. This gives the estimator a chance to reinitialize its state variables at the beginning of motor startup.":
        "\u72b6\u6001\u65f6\u88ab\u8c03\u7528\u3002\u8fd9\u7ed9\u4f30\u8ba1\u5668\u673a\u4f1a\u5728\u7535\u673a\u542f\u52a8\u5f00\u59cb\u65f6\u91cd\u65b0\u521d\u59cb\u5316\u5176\u72b6\u6001\u53d8\u91cf\u3002",
    "Step function": "\u6b65\u51fd\u6570",
    "is called at the main control rate, from": "\u5728\u4e3b\u63a7\u5236\u901f\u7387\u4e0b\u88ab\u8c03\u7528\uff0c\u7531",
    "in commutation.c.": "\u5728 commutation.c \u4e2d\u3002",
    "Some estimators may also have other entry points, called at the same rate as the step function:":
        "\u67d0\u4e9b\u4f30\u8ba1\u5668\u8fd8\u53ef\u80fd\u6709\u5176\u4ed6\u5165\u53e3\u70b9\uff0c\u4ee5\u4e0e\u6b65\u51fd\u6570\u76f8\u540c\u7684\u901f\u7387\u8c03\u7528\uff1a",
    "\u2014 this contains any actions that are tightly coupled with other MCAF modules, and has access to the full":
        "\u2014 \u5305\u542b\u4e0e\u5176\u4ed6 MCAF \u6a21\u5757\u7d27\u5bc6\u8026\u5408\u7684\u4efb\u4f55\u64cd\u4f5c\uff0c\u5e76\u53ef\u8bbf\u95ee\u5b8c\u6574\u7684",
    "data structure. (This is discouraged because it violates modularity, but is unavoidable in certain cases.)":
        "\u6570\u636e\u7ed3\u6784\u3002\uff08\u4e0d\u9f13\u52b1\u8fd9\u6837\u505a\uff0c\u56e0\u4e3a\u5b83\u8fdd\u53cd\u4e86\u6a21\u5757\u5316\uff0c\u4f46\u5728\u67d0\u4e9b\u60c5\u51b5\u4e0b\u4e0d\u53ef\u907f\u514d\u3002\uff09",
    "\u2014 this is a getter function that allows estimators to delay startup progress at certain points, so that the estimator can complete tasks of its own.":
        "\u2014 \u8fd9\u662f\u4e00\u4e2a\u83b7\u53d6\u51fd\u6570\uff0c\u5141\u8bb8\u4f30\u8ba1\u5668\u5728\u67d0\u4e9b\u70b9\u5ef6\u8fdf\u542f\u52a8\u8fdb\u5ea6\uff0c\u4ee5\u4fbf\u4f30\u8ba1\u5668\u5b8c\u6210\u81ea\u5df1\u7684\u4efb\u52a1\u3002",
    "Selection of active commutation angle and velocity": "\u6d3b\u8dc3\u6362\u76f8\u89d2\u5ea6\u548c\u901f\u5ea6\u7684\u9009\u62e9",
    ": In commutation.c,": "\uff1a\u5728 commutation.c \u4e2d\uff0c",
    "determines the angle and velocity from among the available estimators, typically via the following construct:":
        "\u4ece\u53ef\u7528\u7684\u4f30\u8ba1\u5668\u4e2d\u786e\u5b9a\u89d2\u5ea6\u548c\u901f\u5ea6\uff0c\u901a\u5e38\u901a\u8fc7\u4ee5\u4e0b\u7ed3\u6784\uff1a",
    "The compiler will optimize out blocks of this sort for inactive estimators, where": "\u7f16\u8bd1\u5668\u4f1a\u4f18\u5316\u6389\u975e\u6d3b\u8dc3\u4f30\u8ba1\u5668\u7684\u6b64\u7c7b\u4ee3\u7801\u5757\uff0c\u5176\u4e2d",
    "is known at compile time to be": "\u5728\u7f16\u8bd1\u65f6\u5df2\u77e5\u4e3a",
    "The following are methods associated with each estimator.": "\u4ee5\u4e0b\u662f\u4e0e\u6bcf\u4e2a\u4f30\u8ba1\u5668\u76f8\u5173\u7684\u65b9\u6cd5\u3002",
    "Method summary": "\u65b9\u6cd5\u6982\u8ff0",
    "These methods are summarized in the following table. (To save space, the prefix":
        "\u8fd9\u4e9b\u65b9\u6cd5\u5728\u4e0b\u8868\u4e2d\u6982\u8ff0\u3002\uff08\u4e3a\u8282\u7701\u7a7a\u95f4\uff0c\u524d\u7f00",
    "is elided, so for example": "\u88ab\u7701\u7565\uff0c\u56e0\u6b64\u4f8b\u5982",
    "refers to": "\u6307\u7684\u662f",
    "Method": "\u65b9\u6cd5",
    "Summary": "\u6982\u8ff0",
    "Call site": "\u8c03\u7528\u70b9",
    "Applicability": "\u9002\u7528\u6027",
    "One-time initialization": "\u4e00\u6b21\u6027\u521d\u59cb\u5316",
    "all": "\u5168\u90e8",
    "One-time initialization for output dependencies": "\u8f93\u51fa\u4f9d\u8d56\u7684\u4e00\u6b21\u6027\u521d\u59cb\u5316",
    "Hybrid estimators": "\u6df7\u5408\u4f30\u8ba1\u5668",
    "Reinitialization at each startup": "\u6bcf\u6b21\u542f\u52a8\u65f6\u7684\u91cd\u65b0\u521d\u59cb\u5316",
    "Step update function": "\u6b65\u66f4\u65b0\u51fd\u6570",
    "Secondary update function; needed only when tightly coupled to other modules":
        "\u6b21\u7ea7\u66f4\u65b0\u51fd\u6570\uff1b\u4ec5\u5728\u4e0e\u5176\u4ed6\u6a21\u5757\u7d27\u5bc6\u8026\u5408\u65f6\u9700\u8981",
    "as needed": "\u6309\u9700",
    "Getter, returns commutation angle": "\u83b7\u53d6\u51fd\u6570\uff0c\u8fd4\u56de\u6362\u76f8\u89d2\u5ea6",
    "Getter, returns electrical frequency": "\u83b7\u53d6\u51fd\u6570\uff0c\u8fd4\u56de\u7535\u6c14\u9891\u7387",
    "Getter, returns whether a delay is requested.": "\u83b7\u53d6\u51fd\u6570\uff0c\u8fd4\u56de\u662f\u5426\u8bf7\u6c42\u5ef6\u8fdf\u3002",
    "Estimator may delay startup progress at certain points, by returning": "\u4f30\u8ba1\u5668\u53ef\u5728\u67d0\u4e9b\u70b9\u5ef6\u8fdf\u542f\u52a8\u8fdb\u5ea6\uff0c\u901a\u8fc7\u8fd4\u56de",
    "Getter, returns true if estimator angle is the primary estimator selected for commutation":
        "\u83b7\u53d6\u51fd\u6570\uff0c\u5982\u679c\u4f30\u8ba1\u5668\u89d2\u5ea6\u662f\u9009\u5b9a\u7528\u4e8e\u6362\u76f8\u7684\u4e3b\u4f30\u8ba1\u5668\u5219\u8fd4\u56de true",
    "Use of \u201cactive\u201d instead of \u201cprimary\u201d (DB_MC-4325; Applicability: MCAF R4, R5, R6, R7) \u2014 the word \u201cactive\u201d is used incorrectly in commutation.c and commutation_types.h and this will be fixed to \u201cprimary\u201d in a future release, including changing":
        "\u4f7f\u7528\u201c\u6d3b\u8dc3\u201d\u800c\u975e\u201c\u4e3b\u201d\uff08DB_MC-4325\uff1b\u9002\u7528\u6027\uff1aMCAF R4\u3001R5\u3001R6\u3001R7\uff09\u2014 \u201c\u6d3b\u8dc3\u201d\u4e00\u8bcd\u5728 commutation.c \u548c commutation_types.h \u4e2d\u4f7f\u7528\u4e0d\u6b63\u786e\uff0c\u5c06\u5728\u672a\u6765\u7248\u672c\u4e2d\u4fee\u590d\u4e3a\u201c\u4e3b\u201d\uff0c\u5305\u62ec\u5c06",
    "to": "\u6539\u4e3a",
    "5.4.1. Firmware Interface": "5.4.1. \u56fa\u4ef6\u63a5\u53e3",
    "5.4.1.1. Overview": "5.4.1.1. \u6982\u8ff0",
    "5.4.1.2. Terminology": "5.4.1.2. \u672f\u8bed",
    "5.4.1.3. Filesystem location": "5.4.1.3. \u6587\u4ef6\u7cfb\u7edf\u4f4d\u7f6e",
    "5.4.1.4. Storage and types": "5.4.1.4. \u5b58\u50a8\u548c\u7c7b\u578b",
    "5.4.1.5. Entry points and methods": "5.4.1.5. \u5165\u53e3\u70b9\u548c\u65b9\u6cd5",
    "5.4.1.6. Method summary": "5.4.1.6. \u65b9\u6cd5\u6982\u8ff0",
    "5.4.1.7. Errata": "5.4.1.7. \u52d8\u8bef",
    "AN1292 Phase-locked Loop (PLL)": "AN1292 \u9501\u76f8\u73af\uff08PLL\uff09",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
