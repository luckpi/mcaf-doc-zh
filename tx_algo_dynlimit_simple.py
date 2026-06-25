# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/dynlimit-simple"
title_zh = "5.6.5.1. \u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Current limit": "\u7535\u6d41\u9650\u5236",
    "Simple dynamic current limit": "\u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "This algorithm approximates a differential equation for a current":
        "\u6b64\u7b97\u6cd5\u8fd1\u4f3c\u4e00\u4e2a\u5173\u4e8e\u7535\u6d41",
    ", and determines the current limit": "\u7684\u5fae\u5206\u65b9\u7a0b\uff0c\u5e76\u786e\u5b9a\u7535\u6d41\u9650\u5236",
    "as the minimum of": "\u4e3a",
    "and a predetermined fixed peak current": "\u548c\u9884\u5b9a\u7684\u56fa\u5b9a\u5cf0\u503c\u7535\u6d41",
    ". This equation is given below:": "\u7684\u6700\u5c0f\u503c\u3002\u6b64\u65b9\u7a0b\u5982\u4e0b\uff1a",
    "The current relaxes asymptotically to a \u201chorizon\u201d current":
        "\u7535\u6d41\u6e10\u8fd1\u5730\u653e\u677e\u5230\u201c\u5730\u5e73\u7ebf\u201d\u7535\u6d41",
    ". An illustrated example is shown in": "\u3002\u793a\u4f8b\u5982",
    ", with": "\u6240\u793a\uff0c\u5176\u4e2d",
    "The horizon current also determines the slew rate of current as it rises from the continuous current level; specifically, if current command changes in a step from":
        "\u5730\u5e73\u7ebf\u7535\u6d41\u8fd8\u51b3\u5b9a\u4e86\u7535\u6d41\u4ece\u8fde\u7eed\u7535\u6d41\u7535\u5e73\u4e0a\u5347\u65f6\u7684\u65cb\u8f6c\u7387\uff1b\u5177\u4f53\u6765\u8bf4\uff0c\u5982\u679c\u7535\u6d41\u547d\u4ee4\u4ece",
    "to zero, the slew rate of the current limit is": "\u9636\u8dc3\u53d8\u5316\u5230\u96f6\uff0c\u7535\u6d41\u9650\u5236\u7684\u65cb\u8f6c\u7387\u4e3a",
    ". In": "\u3002\u5728",
    ", this occurs at": "\u4e2d\uff0c\u8fd9\u53d1\u751f\u5728",
    "Simulation of simple dynamic current limit. Only q-axis current":
        "\u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236\u7684\u4eff\u771f\u3002\u4ec5\u663e\u793a q \u8f74\u7535\u6d41",
    "is shown; the d-axis current": "\uff1bd \u8f74\u7535\u6d41",
    "is assumed to be regulated to zero or very near zero.":
        "\u5047\u5b9a\u88ab\u63a7\u5236\u4e3a\u96f6\u6216\u63a5\u8fd1\u96f6\u3002",
    "In this case, if the motor current has been low enough for a long enough time that the current":
        "\u5728\u6b64\u60c5\u51b5\u4e0b\uff0c\u5982\u679c\u7535\u673a\u7535\u6d41\u5728\u8db3\u591f\u957f\u7684\u65f6\u95f4\u5185\u8db3\u591f\u4f4e\uff0c\u4f7f\u7535\u6d41",
    "relaxes back nearly to the horizon current, the drive can provide 20 A current for about 1.3 seconds, decreasing to the continuous limit of 10 A after about 3 seconds. Operation at the full peak current of 30 A will use up the transient capacity more quickly, lasting for about 0.4 seconds, decreasing to the continuous limit of 10A after about 2 seconds.":
        "\u51e0\u4e4e\u653e\u677e\u56de\u5730\u5e73\u7ebf\u7535\u6d41\uff0c\u9a71\u52a8\u5668\u53ef\u4ee5\u63d0\u4f9b 20 A \u7535\u6d41\u7ea6 1.3 \u79d2\uff0c\u7ea6 3 \u79d2\u540e\u964d\u5230 10 A \u7684\u8fde\u7eed\u9650\u5236\u3002\u5728 30 A \u7684\u5b8c\u6574\u5cf0\u503c\u7535\u6d41\u4e0b\u8fd0\u884c\u4f1a\u66f4\u5feb\u7528\u5c3d\u6682\u6001\u5bb9\u91cf\uff0c\u6301\u7eed\u7ea6 0.4 \u79d2\uff0c\u7ea6 2 \u79d2\u540e\u964d\u5230 10A \u7684\u8fde\u7eed\u9650\u5236\u3002",
    "The motor torque can be fairly substantial and still allow the current limit to return to near-maximum values, because the thermally-limited components heat up proportionally to the square of the current. Even 50% of the continuous current limit causes only 25% of the temperature rise of the continuous current, which allows the motor and transistors to cool down. This is shown in":
        "\u7535\u673a\u8f6c\u77e9\u53ef\u4ee5\u76f8\u5f53\u5927\uff0c\u4ecd\u5141\u8bb8\u7535\u6d41\u9650\u5236\u56de\u5230\u63a5\u8fd1\u6700\u5927\u503c\uff0c\u56e0\u4e3a\u53d7\u70ed\u9650\u5236\u7684\u7ec4\u4ef6\u7684\u53d1\u70ed\u4e0e\u7535\u6d41\u7684\u5e73\u65b9\u6210\u6b63\u6bd4\u3002\u5373\u4f7f\u662f\u8fde\u7eed\u7535\u6d41\u9650\u5236\u7684 50%\uff0c\u4e5f\u53ea\u4ea7\u751f\u8fde\u7eed\u7535\u6d41\u6e29\u5347\u7684 25%\uff0c\u8fd9\u5141\u8bb8\u7535\u673a\u548c\u6676\u4f53\u7ba1\u51b7\u5374\u3002\u8fd9\u5982",
    "after": "\u6240\u793a\uff0c\u5728",
    "Conversely, twice the continuous current limit produces four times the power dissipation.":
        "\u4e4b\u540e\u3002\uff08\u76f8\u53cd\uff0c\u4e24\u500d\u7684\u8fde\u7eed\u7535\u6d41\u9650\u5236\u4ea7\u751f\u56db\u500d\u7684\u529f\u7387\u635f\u8017\u3002\uff09",
    "Note that since": "\u6ce8\u610f\uff0c\u7531\u4e8e",
    "accumulates to reduce the current limit, neither the direction of current nor the direction of rotation matter; positive and negative values of":
        "\u7d2f\u79ef\u4ee5\u51cf\u5c0f\u7535\u6d41\u9650\u5236\uff0c\u7535\u6d41\u65b9\u5411\u548c\u65cb\u8f6c\u65b9\u5411\u90fd\u4e0d\u91cd\u8981\uff1b",
    "affect the current limit equally.": "\u7684\u6b63\u8d1f\u503c\u5bf9\u7535\u6d41\u9650\u5236\u7684\u5f71\u54cd\u76f8\u540c\u3002",
    "Choice of parameters": "\u53c2\u6570\u9009\u62e9",
    "The choice of parameters here will be different for each board and should be validated to ensure motor and transistor are kept in their safe operating region.":
        "\u6b64\u5904\u7684\u53c2\u6570\u9009\u62e9\u5bf9\u4e8e\u6bcf\u4e2a\u677f\u4f1a\u6709\u6240\u4e0d\u540c\uff0c\u5e94\u8fdb\u884c\u9a8c\u8bc1\u4ee5\u786e\u4fdd\u7535\u673a\u548c\u6676\u4f53\u7ba1\u4fdd\u6301\u5728\u5176\u5b89\u5168\u5de5\u4f5c\u533a\u3002",
    "Aside from peak and continuous limits, which are covered in the":
        "\u9664\u4e86\u5cf0\u503c\u548c\u8fde\u7eed\u9650\u5236\uff08\u5728",
    "main section on dynamic current algorithms": "\u52a8\u6001\u7535\u6d41\u7b97\u6cd5\u4e3b\u8282",
    ", the other two parameters should be selected empirically:":
        "\u4e2d\u8bf4\u660e\uff09\u5916\uff0c\u53e6\u5916\u4e24\u4e2a\u53c2\u6570\u5e94\u6839\u636e\u7ecf\u9a8c\u9009\u62e9\uff1a",
    "time constant": "\u65f6\u95f4\u5e38\u6570",
    "should have some similarity to the thermal dynamics of the real system. Choosing too small of a value will lower the current limit prematurely, so if the motor and transistor have not heated up very much, then a larger time constant should be used. Similarly, if the motor or transistor have heated up to an unsafe level before the current limit decreases, then the time constant is probably too large.":
        "\u5e94\u4e0e\u5b9e\u9645\u7cfb\u7edf\u7684\u70ed\u52a8\u6001\u6709\u67d0\u79cd\u76f8\u4f3c\u6027\u3002\u9009\u62e9\u8fc7\u5c0f\u7684\u503c\u4f1a\u8fc7\u65e9\u964d\u4f4e\u7535\u6d41\u9650\u5236\uff0c\u56e0\u6b64\u5982\u679c\u7535\u673a\u548c\u6676\u4f53\u7ba1\u672a\u53d7\u70ed\u5f88\u591a\uff0c\u5219\u5e94\u4f7f\u7528\u66f4\u5927\u7684\u65f6\u95f4\u5e38\u6570\u3002\u540c\u6837\uff0c\u5982\u679c\u7535\u673a\u6216\u6676\u4f53\u7ba1\u5728\u7535\u6d41\u9650\u5236\u964d\u4f4e\u4e4b\u524d\u5df2\u52a0\u70ed\u5230\u4e0d\u5b89\u5168\u7684\u6c34\u5e73\uff0c\u5219\u65f6\u95f4\u5e38\u6570\u53ef\u80fd\u8fc7\u5927\u3002",
    "horizon current": "\u5730\u5e73\u7ebf\u7535\u6d41",
    "impacts how much thermal headroom is present: larger values will allow the current limit to stay higher for a longer period of time, and will allow the current limit to increase more quickly once the motor current drops back to a small value.":
        "\u5f71\u54cd\u70ed\u5bb9\u4f59\u91cf\uff1a\u66f4\u5927\u7684\u503c\u5141\u8bb8\u7535\u6d41\u9650\u5236\u5728\u66f4\u957f\u65f6\u95f4\u5185\u4fdd\u6301\u8f83\u9ad8\uff0c\u5e76\u5141\u8bb8\u7535\u6d41\u9650\u5236\u5728\u7535\u673a\u7535\u6d41\u964d\u56de\u5c0f\u503c\u540e\u66f4\u5feb\u589e\u52a0\u3002",
    "Implementation notes": "\u5b9e\u73b0\u8bf4\u660e",
    "Since the thermal dynamics are fairly slow (tenths of seconds to tens of seconds), this algorithm is partitioned, with most of this algorithm executes at a decimated rate, compared to the current control sample rate.":
        "\u7531\u4e8e\u70ed\u52a8\u6001\u76f8\u5f53\u6162\uff08\u5341\u5206\u4e4b\u4e00\u79d2\u5230\u51e0\u5341\u79d2\uff09\uff0c\u6b64\u7b97\u6cd5\u88ab\u5206\u533a\uff0c\u5176\u4e2d\u5927\u90e8\u5206\u4ee5\u76f8\u5bf9\u4e8e\u7535\u6d41\u63a7\u5236\u91c7\u6837\u7387\u62bd\u53d6\u7684\u901f\u7387\u6267\u884c\u3002",
    "At the full sample rate (sample time": "\u5728\u5b8c\u6574\u91c7\u6837\u7387\uff08\u91c7\u6837\u65f6\u95f4",
    "), the squared amplitude of current": "\uff09\u4e0b\uff0c\u7535\u6d41\u7684\u5e73\u65b9\u5e45\u503c",
    "is accumulated.": "\u88ab\u7d2f\u52a0\u3002",
    "The rest of the dynamic current limit algorithm runs at a decimated rate (period =":
        "\u52a8\u6001\u7535\u6d41\u9650\u5236\u7b97\u6cd5\u7684\u5176\u4f59\u90e8\u5206\u4ee5\u62bd\u53d6\u7387\uff08\u5468\u671f =",
    "with": "\uff0c\u5176\u4e2d",
    "by default) that updates the current": "\u4e3a\u9ed8\u8ba4\u503c\uff09\u8fd0\u884c\uff0c\u66f4\u65b0\u7535\u6d41",
    "based on the accumulated squared current.":
        "\u57fa\u4e8e\u7d2f\u52a0\u7684\u5e73\u65b9\u7535\u6d41\u3002",
    "5.6.5.1. Simple dynamic current limit": "5.6.5.1. \u7b80\u5355\u52a8\u6001\u7535\u6d41\u9650\u5236",
    "5.6.5.1.1. Choice of parameters": "5.6.5.1.1. \u53c2\u6570\u9009\u62e9",
    "5.6.5.1.2. Implementation notes": "5.6.5.1.2. \u5b9e\u73b0\u8bf4\u660e",
    "Dead-time Compensation": "\u6b7b\u533a\u8865\u507f",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
