# -*- coding: utf-8 -*-
import txutil

rel = "algorithms/qei"
title_zh = "5.4.3. \u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301"

m = {
    "Detailed Algorithm Notes": "\u8be6\u7ec6\u7b97\u6cd5\u8bf4\u660e",
    "Position and Velocity Estimation": "\u4f4d\u7f6e\u548c\u901f\u5ea6\u4f30\u8ba1",
    "Quadrature encoder support": "\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "Overview": "\u6982\u8ff0",
    "MCAF supports the use of a quadrature encoder (with or without index pulse) for closed-loop velocity operation, through the dsPIC":
        "MCAF \u652f\u6301\u901a\u8fc7 dsPIC",
    "DSC QEI (Quadrature Encoder Interface) peripheral.": "DSC \u7684 QEI\uff08\u6b63\u4ea4\u7f16\u7801\u5668\u63a5\u53e3\uff09\u5916\u8bbe\u4f7f\u7528\u6b63\u4ea4\u7f16\u7801\u5668\uff08\u5e26\u6216\u4e0d\u5e26\u7d22\u5f15\u8109\u51b2\uff09\u8fdb\u884c\u95ed\u73af\u901f\u5ea6\u8fd0\u884c\u3002",
    "Use of a quadrature encoder can be very valuable during prototyping stages, and it can be used in conjunction with a sensorless estimator to validate or troubleshoot estimator operation. MCAF allows more than one estimator to execute \u2014 at the cost of additional CPU usage \u2014 but only one estimator can be used for commutation.":
        "\u5728\u539f\u578b\u5f00\u53d1\u9636\u6bb5\uff0c\u4f7f\u7528\u6b63\u4ea4\u7f16\u7801\u5668\u975e\u5e38\u6709\u4ef7\u503c\uff0c\u5b83\u53ef\u4ee5\u4e0e\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u914d\u5408\u4f7f\u7528\uff0c\u4ee5\u9a8c\u8bc1\u6216\u6392\u67e5\u4f30\u8ba1\u5668\u7684\u8fd0\u884c\u3002MCAF \u5141\u8bb8\u591a\u4e2a\u4f30\u8ba1\u5668\u540c\u65f6\u6267\u884c \u2014 \u4ee5\u989d\u5916\u7684 CPU \u5f00\u9500\u4e3a\u4ee3\u4ef7 \u2014 \u4f46\u53ea\u80fd\u6709\u4e00\u4e2a\u4f30\u8ba1\u5668\u7528\u4e8e\u6362\u76f8\u3002",
    "A quadrature encoder can provide accurate tracking of relative position changes, as long as the encoder signals are received without significant errors. Furthermore, angle resolution is a function of the encoder; high-end encoders can provide thousands of counts per mechanical revolution. An encoder cannot, however, provide these features on its own:":
        "\u53ea\u8981\u7f16\u7801\u5668\u4fe1\u53f7\u63a5\u6536\u65e0\u663e\u8457\u8bef\u5dee\uff0c\u6b63\u4ea4\u7f16\u7801\u5668\u5c31\u80fd\u63d0\u4f9b\u76f8\u5bf9\u4f4d\u7f6e\u53d8\u5316\u7684\u51c6\u786e\u8ddf\u8e2a\u3002\u6b64\u5916\uff0c\u89d2\u5ea6\u5206\u8fa8\u7387\u662f\u7f16\u7801\u5668\u7684\u51fd\u6570\uff1b\u9ad8\u7aef\u7f16\u7801\u5668\u53ef\u4ee5\u6bcf\u673a\u68b0\u8f6c\u63d0\u4f9b\u6570\u5343\u4e2a\u8109\u51b2\u3002\u7136\u800c\uff0c\u7f16\u7801\u5668\u672c\u8eab\u65e0\u6cd5\u63d0\u4f9b\u4ee5\u4e0b\u529f\u80fd\uff1a",
    "absolute position accuracy at all times": "\u59cb\u7ec8\u4fdd\u6301\u7edd\u5bf9\u4f4d\u7f6e\u7cbe\u5ea6",
    "Encoders without index pulses can never provide absolute position accuracy": "\u65e0\u7d22\u5f15\u8109\u51b2\u7684\u7f16\u7801\u5668\u65e0\u6cd5\u63d0\u4f9b\u7edd\u5bf9\u4f4d\u7f6e\u7cbe\u5ea6",
    "Encoders with an index pulse can provide absolute accuracy once the index pulse has been detected, but prior to that, there is no way to determine absolute position from the encoder":
        "\u5e26\u7d22\u5f15\u8109\u51b2\u7684\u7f16\u7801\u5668\u5728\u68c0\u6d4b\u5230\u7d22\u5f15\u8109\u51b2\u540e\u53ef\u4ee5\u63d0\u4f9b\u7edd\u5bf9\u7cbe\u5ea6\uff0c\u4f46\u5728\u6b64\u4e4b\u524d\uff0c\u65e0\u6cd5\u4ece\u7f16\u7801\u5668\u786e\u5b9a\u7edd\u5bf9\u4f4d\u7f6e",
    "a measurement of velocity \u2014 the encoder provides quantized position; velocity must be estimated from position through a separate algorithm":
        "\u901f\u5ea6\u6d4b\u91cf \u2014 \u7f16\u7801\u5668\u63d0\u4f9b\u91cf\u5316\u4f4d\u7f6e\uff1b\u901f\u5ea6\u5fc5\u987b\u901a\u8fc7\u5355\u72ec\u7684\u7b97\u6cd5\u4ece\u4f4d\u7f6e\u4f30\u8ba1",
    "determination of the electrical commutation offset for a": "\u786e\u5b9a",
    ", to locate the motor\u2019s position of maximum rotor flux relative to encoder position": "\u7684\u7535\u6c14\u6362\u76f8\u504f\u79fb\uff0c\u4ee5\u5b9a\u4f4d\u7535\u673a\u6700\u5927\u8f6c\u5b50\u78c1\u901a\u76f8\u5bf9\u4e8e\u7f16\u7801\u5668\u4f4d\u7f6e\u7684\u4f4d\u7f6e",
    "MCAF provides these features with": "MCAF \u901a\u8fc7",
    "back-emf synchronization": "\u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "for determining commutation offset, and a": "\u6765\u786e\u5b9a\u6362\u76f8\u504f\u79fb\uff0c\u5e76\u901a\u8fc7",
    "tracking loop": "\u8ddf\u8e2a\u73af",
    "for estimating velocity from position.": "\u4ece\u4f4d\u7f6e\u4f30\u8ba1\u901f\u5ea6\u3002",
    "Usage notes": "\u4f7f\u7528\u8bf4\u660e",
    "Encoders are usually specified in \u201clines\u201d or \u201ccycles per revolution\u201d (CPR). There is a 4:1 relationship between counts per revolution and lines or CPR: for example, 256 lines = 256 CPR = 1024 counts per revolution.":
        "\u7f16\u7801\u5668\u901a\u5e38\u4ee5\u201c\u7ebf\u6570\u201d\u6216\u201c\u6bcf\u8f6c\u5468\u671f\u6570\u201d\uff08CPR\uff09\u8868\u793a\u3002\u6bcf\u8f6c\u8109\u51b2\u6570\u4e0e\u7ebf\u6570\u6216 CPR \u4e4b\u95f4\u5b58\u5728 4:1 \u7684\u5173\u7cfb\uff1a\u4f8b\u5982\uff0c256 \u7ebf = 256 CPR = 1024 \u6bcf\u8f6c\u8109\u51b2\u6570\u3002",
    "The dsPICDEM": "dsPICDEM",
    "MCLV\u20112 Development Board has 100 pF filter capacitors on its encoder/Hall inputs. These may cause problems for encoders with high count rates, in which case capacitors C49, C50, and C51 should be removed, or replaced with smaller values such as 10 pF.":
        "MCLV-2 \u5f00\u53d1\u677f\u7684\u7f16\u7801\u5668/Hall \u8f93\u5165\u4e0a\u6709 100 pF \u6ee4\u6ce2\u7535\u5bb9\u3002\u8fd9\u4e9b\u7535\u5bb9\u53ef\u80fd\u5bf9\u9ad8\u8109\u51b2\u7387\u7684\u7f16\u7801\u5668\u9020\u6210\u95ee\u9898\uff0c\u5728\u8fd9\u79cd\u60c5\u51b5\u4e0b\u5e94\u79fb\u9664\u7535\u5bb9 C49\u3001C50 \u548c C51\uff0c\u6216\u66ff\u6362\u4e3a\u66f4\u5c0f\u7684\u503c\uff0c\u5982 10 pF\u3002",
    "Limitations": "\u5c40\u9650\u6027",
    "As of MCAF R9:": "\u622a\u81f3 MCAF R9\uff1a",
    "Position control is not supported": "\u4e0d\u652f\u6301\u4f4d\u7f6e\u63a7\u5236",
    "Operation near zero speed is not supported \u2014 the QEI support is limited to use as a drop-in replacement for sensorless estimators, and startup through forced commutation is required.":
        "\u4e0d\u652f\u6301\u96f6\u901f\u9644\u8fd1\u7684\u8fd0\u884c \u2014 QEI \u652f\u6301\u4ec5\u9650\u4e8e\u4f5c\u4e3a\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u7684\u76f4\u63a5\u66ff\u4ee3\u54c1\u4f7f\u7528\uff0c\u9700\u8981\u901a\u8fc7\u5f3a\u5236\u6362\u76f8\u542f\u52a8\u3002",
    "Index pulses are supported in dsPIC": "\u7d22\u5f15\u8109\u51b2\u5728 dsPIC",
    "DSC 33F, 33E, 33C, and some 33A devices only for encoder resolutions that are a power of two. Non-power-of-two encoder counts are supported by the QEI peripheral\u2019s modulo mode; index pulses are supported by the use of the QEI peripheral\u2019s position capture feature, which cannot be used simultaneously with modulo mode in these devices.":
        "DSC 33F\u300133E\u300133C \u548c\u90e8\u5206 33A \u5668\u4ef6\u4e2d\u4ec5\u652f\u6301 2 \u7684\u5e42\u6b21\u65b9\u7f16\u7801\u5668\u5206\u8fa8\u7387\u3002\u975e 2 \u7684\u5e42\u6b21\u65b9\u7f16\u7801\u5668\u8109\u51b2\u6570\u7531 QEI \u5916\u8bbe\u7684\u53d6\u6a21\u6a21\u5f0f\u652f\u6301\uff1b\u7d22\u5f15\u8109\u51b2\u7531 QEI \u5916\u8bbe\u7684\u4f4d\u7f6e\u6355\u83b7\u529f\u80fd\u652f\u6301\uff0c\u8be5\u529f\u80fd\u5728\u8fd9\u4e9b\u5668\u4ef6\u4e2d\u4e0d\u80fd\u4e0e\u53d6\u6a21\u6a21\u5f0f\u540c\u65f6\u4f7f\u7528\u3002",
    "Tracking loop": "\u8ddf\u8e2a\u73af",
    "There are many ways to estimate velocity from encoder position. A na\u00efve implementation would attempt to differentiate the velocity signal, but because the encoder quantizes rotor position, the result at moderate speeds would be a bunch of zeros and ones. (For example, consider a 1024 count-per-revolution encoder on a motor running at 1000 RPM = 16.667 revolutions/second. This produces encoder counts at the rate of around 17067 counts/second. A control ISR running at 20 kHz would see a change of either 0 or 1 counts per ISR. At 10000 RPM the same motor/encoder pair would produce 170667 counts/second, and the control ISR would see either changes of either 8 or 9 counts per ISR. In either case, the maximum quantization error of velocity would equal 0.5 counts per ISR = 1/2048 revolution * 20 kHz = 9.77 revolutions/second = 586 RPM.)":
        "\u4ece\u7f16\u7801\u5668\u4f4d\u7f6e\u4f30\u8ba1\u901f\u5ea6\u6709\u5f88\u591a\u65b9\u6cd5\u3002\u4e00\u79cd\u7b80\u5355\u7684\u5b9e\u73b0\u4f1a\u5c1d\u8bd5\u5bf9\u901f\u5ea6\u4fe1\u53f7\u6c42\u5bfc\uff0c\u4f46\u7531\u4e8e\u7f16\u7801\u5668\u5bf9\u8f6c\u5b50\u4f4d\u7f6e\u8fdb\u884c\u91cf\u5316\uff0c\u5728\u4e2d\u7b49\u901f\u5ea6\u4e0b\u7ed3\u679c\u5c06\u662f\u4e00\u5806\u96f6\u548c\u4e00\u3002\uff08\u4f8b\u5982\uff0c\u8003\u8651\u4e00\u4e2a 1024 \u6bcf\u8f6c\u8109\u51b2\u6570\u7684\u7f16\u7801\u5668\u5728\u4ee5 1000 RPM = 16.667 \u8f6c/\u79d2\u8fd0\u884c\u7684\u7535\u673a\u4e0a\u3002\u8fd9\u4ea7\u751f\u5927\u7ea6 17067 \u8109\u51b2/\u79d2\u7684\u7f16\u7801\u5668\u8109\u51b2\u7387\u3002\u4ee5 20 kHz \u8fd0\u884c\u7684\u63a7\u5236 ISR \u6bcf\u6b21 ISR \u4f1a\u770b\u5230 0 \u6216 1 \u4e2a\u8108\u51b2\u7684\u53d8\u5316\u3002\u5728 10000 RPM \u65f6\uff0c\u540c\u4e00\u7535\u673a/\u7f16\u7801\u5668\u5c06\u4ea7\u751f 170667 \u8109\u51b2/\u79d2\uff0c\u63a7\u5236 ISR \u6bcf\u6b21\u4f1a\u770b\u5230 8 \u6216 9 \u4e2a\u8109\u51b2\u7684\u53d8\u5316\u3002\u5728\u4e24\u79cd\u60c5\u51b5\u4e0b\uff0c\u901f\u5ea6\u7684\u6700\u5927\u91cf\u5316\u8bef\u5dee\u90fd\u7b49\u4e8e 0.5 \u8109\u51b2/ISR = 1/2048 \u8f6ac * 20 kHz = 9.77 \u8f6c/\u79d2 = 586 RPM\u3002\uff09",
    "One way to estimate velocity is to compute the change in position each control cycle, and use a low-pass filter to determine velocity. MCAF uses something slightly different, known as a tracking loop.":
        "\u4f30\u8ba1\u901f\u5ea6\u7684\u4e00\u79cd\u65b9\u6cd5\u662f\u8ba1\u7b97\u6bcf\u4e2a\u63a7\u5236\u5468\u671f\u7684\u4f4d\u7f6e\u53d8\u5316\uff0c\u5e76\u4f7f\u7528\u4f4e\u901a\u6ee4\u6ce2\u5668\u786e\u5b9a\u901f\u5ea6\u3002MCAF \u4f7f\u7528\u7684\u662f\u7565\u6709\u4e0d\u540c\u7684\u65b9\u6cd5\uff0c\u79f0\u4e3a\u8ddf\u8e2a\u73af\u3002",
    "Tracking loops are essentially just a low-pass filter in state-variable form to produce useful estimates. In the tracking loop shown in":
        "\u8ddf\u8e2a\u73af\u672c\u8d28\u4e0a\u53ea\u662f\u4ee5\u72b6\u6001\u53d8\u91cf\u5f62\u5f0f\u5b9e\u73b0\u7684\u4f4e\u901a\u6ee4\u6ce2\u5668\uff0c\u4ee5\u4ea7\u751f\u6709\u7528\u7684\u4f30\u8ba1\u3002\u5728",
    ", the input angle": "\u6240\u793a\u7684\u8ddf\u8e2a\u73af\u4e2d\uff0c\u8f93\u5165\u89d2\u5ea6",
    "may be noisy, whether through analog noise or, in the case of an encoder, quantization noise. The loop itself just consists of a PI controller to estimate a velocity":
        "\u53ef\u80fd\u542b\u6709\u566a\u58f0\uff0c\u65e0\u8bba\u662f\u6a21\u62df\u566a\u58f0\u8fd8\u662f\uff08\u5bf9\u4e8e\u7f16\u7801\u5668\uff09\u91cf\u5316\u566a\u58f0\u3002\u73af\u672c\u8eab\u4ec5\u5305\u542b\u4e00\u4e2a PI \u63a7\u5236\u5668\u6765\u4f30\u8ba1\u901f\u5ea6",
    "which is then integrated to form an estimated angle": "\uff0c\u7136\u540e\u79ef\u5206\u5f62\u6210\u4f30\u8ba1\u89d2\u5ea6",
    "used to form an error term for the PI loop.": "\u7528\u4e8e\u5f62\u6210 PI \u73af\u7684\u8bef\u5dee\u9879\u3002",
    "Tracking loop for estimating velocity from position": "\u7528\u4e8e\u4ece\u4f4d\u7f6e\u4f30\u8ba1\u901f\u5ea6\u7684\u8ddf\u8e2a\u73af",
    "The outputs of a tracking loop are": "\u8ddf\u8e2a\u73af\u7684\u8f93\u51fa\u4e3a",
    "\u2014 the integrator output can be used as a moderate-bandwidth estimate of velocity.":
        "\u2014 \u79ef\u5206\u5668\u8f93\u51fa\u53ef\u7528\u4f5c\u4e2d\u7b49\u5e26\u5bbd\u7684\u901f\u5ea6\u4f30\u8ba1\u3002",
    "\u2014 the PI output contains high-frequency content needed to drive the error towards zero. It is generally not appropriate for general use, because noise from":
        "\u2014 PI \u8f93\u51fa\u5305\u542b\u5c06\u8bef\u5dee\u9a71\u52a8\u81f3\u96f6\u6240\u9700\u7684\u9ad8\u9891\u5206\u91cf\u3002\u5b83\u901a\u5e38\u4e0d\u9002\u5408\u901a\u7528\uff0c\u56e0\u4e3a\u6765\u81ea",
    "feeds directly into it from the proportional (P) term.": "\u7684\u566a\u58f0\u901a\u8fc7\u6bd4\u4f8b\uff08P\uff09\u9879\u76f4\u63a5\u9988\u5165\u3002",
    "\u2014 the estimated angle filters out high-frequency component of quantization noise, and can be used for position control applications; it can also be used for commutation applications, but the phase lag is critical and must be analyzed carefully.":
        "\u2014 \u4f30\u8ba1\u89d2\u5ea6\u6ee4\u9664\u4e86\u91cf\u5316\u566a\u58f0\u7684\u9ad8\u9891\u5206\u91cf\uff0c\u53ef\u7528\u4e8e\u4f4d\u7f6e\u63a7\u5236\u5e94\u7528\uff1b\u4e5f\u53ef\u7528\u4e8e\u6362\u76f8\u5e94\u7528\uff0c\u4f46\u76f8\u4f4d\u6ede\u540e\u81f3\u5173\u91cd\u8981\uff0c\u5fc5\u987b\u4ed4\u7ec6\u5206\u6790\u3002",
    "Note on the choice of units:": "\u5173\u4e8e\u5355\u4f4d\u9009\u62e9\u7684\u8bf4\u660e\uff1a",
    "a tracking loop can operate equally well on any sort of quantity that requires estimation of a low-frequency derivative; its input could be temperature in \u00b0C, with an output in \u00b0C/s, rather than an input of position with an output of velocity.":
        "\u8ddf\u8e2a\u73af\u53ef\u4ee5\u540c\u6837\u9002\u7528\u4e8e\u4efb\u4f55\u9700\u8981\u4f30\u8ba1\u4f4e\u9891\u5bfc\u6570\u7684\u7269\u7406\u91cf\uff1b\u5176\u8f93\u5165\u53ef\u4ee5\u662f\u4ee5 \u00b0C \u4e3a\u5355\u4f4d\u7684\u6e29\u5ea6\uff0c\u8f93\u51fa\u4e3a \u00b0C/s\uff0c\u800c\u4e0d\u662f\u4ee5\u4f4d\u7f6e\u4e3a\u8f93\u5165\u3001\u901f\u5ea6\u4e3a\u8f93\u51fa\u3002",
    "Frequency-domain equivalent": "\u9891\u57df\u7b49\u6548",
    "Transfer functions from real angle/velocity inputs (assuming additive noise) to outputs are:":
        "\u4ece\u5b9e\u9645\u89d2\u5ea6/\u901f\u5ea6\u8f93\u5165\uff08\u5047\u8bbe\u52a0\u6027\u566a\u58f0\uff09\u5230\u8f93\u51fa\u7684\u4f20\u9012\u51fd\u6570\u4e3a\uff1a",
    "A few things to note:": "\u9700\u8981\u6ce8\u610f\u4ee5\u4e0b\u51e0\u70b9\uff1a",
    "The denominator in all cases forms a 2nd-order system, and can be written in the form":
        "\u6240\u6709\u60c5\u51b5\u4e0b\u5206\u6bcd\u90fd\u6784\u6210\u4e8c\u9636\u7cfb\uff0c\u53ef\u4ee5\u5199\u6210",
    "with": "\u5176\u4e2d",
    "and": "\u548c",
    ". The quantity": "\u3002\u91cf",
    "represents damping factor and should be set conservatively, perhaps something in the 1 \u2013 1.5 range. The time constant":
        "\u8868\u793a\u963b\u5c3c\u56e0\u5b50\uff0c\u5e94\u4fdd\u5b88\u8bbe\u7f6e\uff0c\u53ef\u80fd\u5728 1\u20131.5 \u8303\u56f4\u5185\u3002\u65f6\u95f4\u5e38\u6570",
    "is inversely proportional to bandwidth.": "\u4e0e\u5e26\u5bbd\u6210\u53cd\u6bd4\u3002",
    "The velocity transfer function to": "\u5230",
    "has no zeros; the velocity transfer function to": "\u7684\u901f\u5ea6\u4f20\u9012\u51fd\u6570\u6ca1\u6709\u96f6\u70b9\uff1b\u5230",
    "has a zero at": "\u7684\u901f\u5ea6\u4f20\u9012\u51fd\u6570\u5728",
    "Implementation Notes": "\u5b9e\u73b0\u8bf4\u660e",
    "The tracking loop used in MCAF for quadrature encoder support operates on mechanical angle":
        "MCAF \u7528\u4e8e\u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301\u7684\u8ddf\u8e2a\u73af\u5bf9\u673a\u68b0\u89d2\u5ea6",
    ", with an output of estimated mechanical angular velocity": "\u8fd0\u884c\uff0c\u8f93\u51fa\u4e3a\u4f30\u8ba1\u673a\u68b0\u89d2\u901f\u5ea6",
    ". This choice preserves angular location within one complete mechanical rotation, to support future position control applications.":
        "\u3002\u6b64\u9009\u62e9\u4fdd\u7559\u4e86\u4e00\u4e2a\u5b8c\u6574\u673a\u68b0\u8f6e\u5185\u7684\u89d2\u5ea6\u4f4d\u7f6e\uff0c\u4ee5\u652f\u6301\u672a\u6765\u7684\u4f4d\u7f6e\u63a7\u5236\u5e94\u7528\u3002",
    "MCAF uses the filtered velocity,": "MCAF \u4f7f\u7528\u6ee4\u6ce2\u540e\u7684\u901f\u5ea6\uff0c",
    ", for velocity estimates.": "\u7528\u4e8e\u901f\u5ea6\u4f30\u8ba1\u3002",
    "The MCAF implementation of the tracking loop adds a limiter block, shown in":
        "MCAF \u7684\u8ddf\u8e2a\u73af\u5b9e\u73b0\u6dfb\u52a0\u4e86\u4e00\u4e2a\u9650\u5e85\u5668\u6a21\u5757\uff0c\u5982",
    ", which prevents overflow in the calculation of": "\u6240\u793a\uff0c\u9632\u6b62\u8ba1\u7b97",
    "Tracking loop implementation": "\u8ddf\u8e2a\u73af\u5b9e\u73b0",
    "Back-EMF synchronization": "\u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "The goal of back-EMF synchronization is to estimate a commutation offset such that":
        "\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u7684\u76ee\u6807\u662f\u4f30\u8ba1\u6362\u76f8\u504f\u79fb\uff0c\u4f7f\u5f97",
    "can operate with a reference frame in perfect alignment. When a rotor (": "\u80fd\u591f\u5728\u5b8c\u7f8e\u5bf9\u9f50\u7684\u53c2\u8003\u5750\u6807\u7cfb\u4e0b\u8fd0\u884c\u3002\u5f53\u8f6c\u5b50\uff08",
    ") reference frame is perfectly aligned with a": "\uff09\u53c2\u8003\u5750\u6807\u7cfb\u4e0e",
    "\u2019s rotor flux and back-EMF, it has the following properties:": "\u7684\u8f6c\u5b50\u78c1\u901a\u548c\u53cd\u7535\u52a8\u52bf\u5b8c\u7f8e\u5bf9\u9f50\u65f6\uff0c\u5177\u6709\u4ee5\u4e0b\u6027\u8d28\uff1a",
    "back-EMF": "\u53cd\u7535\u52a8\u52bf",
    "\u2014 With": "\u2014 \u5f53",
    "at nonzero speed, the terminal voltage of the motor is along the q-axis and is proportional to mechanical velocity":
        "\u4ee5\u975e\u96f6\u901f\u5ea6\u8fd0\u884c\u65f6\uff0c\u7535\u673a\u7684\u7aef\u7535\u538b\u6cbf q \u8f74\u65b9\u5411\u5e76\u4e0e\u673a\u68b0\u901f\u5ea6",
    "; the terminal voltage has no d-axis component. Changes in commutation offset would cause nonzero d-axis component.":
        "\u6210\u6b63\u6bd4\uff1b\u7aef\u7535\u538b\u6ca1\u6709 d \u8f74\u5206\u91cf\u3002\u6362\u76f8\u504f\u79fb\u7684\u53d8\u5316\u4f1a\u5bfc\u81f4\u975e\u96f6\u7684 d \u8f74\u5206\u91cf\u3002",
    "d-axis torque": "d \u8f74\u8f6c\u77e9",
    ", no torque is produced. Small changes in commutation offset would cause a net electromechanical torque that is proportional to":
        "\u65f6\uff0c\u4e0d\u4ea7\u751f\u8f6c\u77e9\u3002\u6362\u76f8\u504f\u79fb\u7684\u5c0f\u53d8\u5316\u4f1a\u5bfc\u81f4\u4e0e",
    ", the error in commutation offset:": "\uff08\u6362\u76f8\u504f\u79fb\u8bef\u5dee\uff09\u6210\u6b63\u6bd4\u7684\u51c0\u7535\u673a\u68b0\u8f6c\u77e9\uff1a",
    "q-axis torque direction": "q \u8f74\u8f6c\u77e9\u65b9\u5411",
    ", positive torque is produced. (180\u00b0 offset error produces negative torque)":
        "\u65f6\uff0c\u4ea7\u751f\u6b63\u8f6c\u77e9\u3002\uff08180\u00b0 \u504f\u79fb\u8bef\u5dee\u4ea7\u751f\u8d1f\u8f6c\u77e9\uff09",
    "\u2014 For surface permanent magnet motors (SPMSM),": "\u2014 \u5bf9\u4e8e\u8868\u8d34\u6c38\u78c1\u7535\u673a\uff08SPMSM\uff09\uff0c",
    "produces maximum torque, and any change in commutation offset reduces the generated torque. This condition is known as \u201cmaximum torque per ampere\u201d or MTPA.":
        "\u4ea7\u751f\u6700\u5927\u8f6c\u77e9\uff0c\u6362\u76f8\u504f\u79fb\u7684\u4efb\u4f55\u53d8\u5316\u90fd\u4f1a\u51cf\u5c0f\u4ea7\u751f\u7684\u8f6c\u77e9\u3002\u6b64\u6761\u4ef6\u79f0\u4e3a\u201c\u6bcf\u5b89\u57f9\u6700\u5927\u8f6c\u77e9\u201d\u6216 MTPA\u3002",
    "anisotropy due to saturation": "\u9971\u548c\u5bfc\u81f4\u7684\u5404\u5411\u5f02\u6027",
    ", iron saturation occurs at a lower current than with any change in commutation offset. Saturation results in a decreased incremental inductance":
        "\u65f6\uff0c\u94c1\u9971\u548c\u53d1\u751f\u7684\u7535\u6d41\u4f4e\u4e8e\u6362\u76f8\u504f\u79fb\u53d1\u751f\u4efb\u4f55\u53d8\u5316\u65f6\u7684\u7535\u6d41\u3002\u9971\u548c\u5bfc\u81f4\u589e\u91cf\u7535\u611f\u51cf\u5c0f",
    ". This is because the stator field adds to the magnetic field of the rotor to maximize the resulting stator field for a given stator current.":
        "\u3002\u8fd9\u662f\u56e0\u4e3a\u5b9a\u5b50\u78c1\u573a\u4e0e\u8f6c\u5b50\u78c1\u573a\u53e0\u52a0\uff0c\u4ee5\u5728\u7ed9\u5b9a\u5b9a\u5b50\u7535\u6d41\u4e0b\u6700\u5927\u5316\u5b9a\u5b50\u78c1\u573a\u3002",
    "anisotropy due to saliency": "\u51f8\u6027\u5bfc\u81f4\u7684\u5404\u5411\u5f02\u6027",
    "\u2014 For motors with rotor saliency (such as interior permanent magnet motors = IPMSM), the d- and q-axes are eigenvectors of the inductance matrix, and therefore changes in":
        "\u2014 \u5bf9\u4e8e\u5177\u6709\u8f6c\u5b50\u51f8\u6027\u7684\u7535\u673a\uff08\u5982\u5185\u7f6e\u6c38\u78c1\u7535\u673a = IPMSM\uff09\uff0cd \u8f74\u548c q \u8f74\u662f\u7535\u611f\u77e9\u9635\u7684\u7279\u5f81\u77e2\u91cf\uff0c\u56e0\u6b64",
    "produce changes in stator flux": "\u7684\u53d8\u5316\u4ea7\u751f\u5b9a\u5b50\u78c1\u901a",
    "with no change in": "\u7684\u53d8\u5316\uff0c\u800c",
    ", and similarly changes in": "\u4e0d\u53d8\uff0c\u540c\u6837",
    ". In other words, the flux equation can be written in the form shown in equation":
        "\u3002\u6362\u53e5\u8bdd\u8bf4\uff0c\u78c1\u901a\u65b9\u7a0b\u53ef\u4ee5\u5199\u6210\u65b9\u7a0b",
    ", which has no off-diagonal terms in the inductance matrix. Changes in commutation offset would cause nonzero cross-axis terms in the flux equation.":
        "\u6240\u793a\u7684\u5f62\u5f0f\uff0c\u5176\u7535\u611f\u77e9\u9635\u6ca1\u6709\u975e\u5bf9\u89d2\u9879\u3002\u6362\u76f8\u504f\u79fb\u7684\u53d8\u5316\u4f1a\u5bfc\u81f4\u78c1\u901a\u65b9\u7a0b\u4e2d\u51fa\u73b0\u975e\u96f6\u7684\u4ea4\u53c9\u8f74\u9879\u3002",
    "All sensorless estimators take advantage of at least one of these properties to discern the true rotor reference frame, with various tradeoffs in bandwidth, stability, convergence, complexity, power consumption, and accuracy.":
        "\u6240\u6709\u65e0\u4f20\u611f\u5668\u4f30\u8ba1\u5668\u90fd\u5229\u7528\u4e86\u81f3\u5c11\u4e00\u4e2a\u8fd9\u4e9b\u6027\u8d28\u6765\u8fa8\u522b\u771f\u5b9e\u7684\u8f6c\u5b50\u53c2\u8003\u5750\u6807\u7cfb\uff0c\u5728\u5e26\u5bbd\u3001\u7a33\u5b9a\u6027\u3001\u6536\u655b\u6027\u3001\u590d\u6742\u6027\u3001\u529f\u8017\u548c\u7cbe\u5ea6\u65b9\u9762\u6709\u4e0d\u540c\u7684\u6743\u8861\u3002",
    "MCAF R4 introduced back-emf synchronization in the": "MCAF R4 \u5728",
    "module. One of three methods can be selected, each of which interacts with hooks in the":
        "\u6a21\u5757\u4e2d\u5f15\u5165\u4e86\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u3002\u53ef\u4ee5\u9009\u62e9\u4e09\u79cd\u65b9\u6cd5\u4e4b\u4e00\uff0c\u6bcf\u79cd\u65b9\u6cd5\u90fd\u4e0e",
    "startup sequence": "\u542f\u52a8\u5e8f\u5217",
    "align": "align\uff08\u5bf9\u9f50\uff09",
    "\u2014 the align method applies a fixed current at a fixed angle during the align phase of startup, and expects that the rotor has a minimal mechanical load at low speeds and will rotate so that its d-axis aligns with the applied current vector. (This method relies on the d-axis torque property.) This is the default method of MCAF, is very fast, and works well for most motors, as long as cogging torque or other mechanical loads are relatively low, and the effect of any rotor saliency is fairly small at low torque loads.":
        "\u2014 \u5bf9\u9f50\u65b9\u6cd5\u5728\u542f\u52a8\u7684\u5bf9\u9f50\u9636\u6bb5\u4ee5\u56fa\u5b9a\u89d2\u5ea6\u65bd\u52a0\u56fa\u5b9a\u7535\u6d41\uff0c\u5e76\u671f\u671b\u8f6c\u5b50\u5728\u4f4e\u901f\u65f6\u5177\u6709\u6700\u5c0f\u7684\u673a\u68b0\u8d1f\u8f7d\uff0c\u4f1a\u65cb\u8f6c\u4f7f\u5176 d \u8f74\u4e0e\u65bd\u52a0\u7684\u7535\u6d41\u77e2\u91cf\u5bf9\u9f50\u3002\uff08\u6b64\u65b9\u6cd5\u4f9d\u8d56 d \u8f74\u8f6c\u77e9\u6027\u8d28\u3002\uff09\u8fd9\u662f MCAF \u7684\u9ed8\u8ba4\u65b9\u6cd5\uff0c\u901f\u5ea6\u5f88\u5feb\uff0c\u5bf9\u5927\u591a\u6570\u7535\u673a\u6548\u679c\u826f\u597d\uff0c\u53ea\u8981\u9f7f\u69fd\u8f6c\u77e9\u6216\u5176\u4ed6\u673a\u68b0\u8d1f\u8f7d\u76f8\u5bf9\u8f83\u4f4e\uff0c\u4e14\u5728\u4f4e\u8f6c\u77e9\u8d1f\u8f7d\u4e0b\u8f6c\u5b50\u51f8\u6027\u7684\u5f71\u54cd\u8f83\u5c0f\u3002",
    "pullout": "pullout\uff08\u5931\u6b65\uff09",
    "\u2014 the pullout method reduces the current used in the spin phase of startup until it observes the rotor angle start to decrease significantly from the angle of applied current. (This method relies on the MTPA property.) This method is immune from errors in cogging torque, but is sensitive to the dynamics of forced commutation.":
        "\u2014 \u5931\u6b65\u65b9\u6cd5\u51cf\u5c0f\u542f\u52a8\u7a33\u901f\u9636\u6bb5\u4f7f\u7528\u7684\u7535\u6d41\uff0c\u76f4\u5230\u89c2\u5bdf\u5230\u8f6c\u5b50\u89d2\u5ea6\u5f00\u59cb\u4ece\u65bd\u52a0\u7535\u6d41\u7684\u89d2\u5ea6\u663e\u8457\u51cf\u5c0f\u3002\uff08\u6b64\u65b9\u6cd5\u4f9d\u8d56 MTPA \u6027\u8d28\u3002\uff09\u6b64\u65b9\u6cd5\u4e0d\u53d7\u9f7f\u69fd\u8f6c\u77e9\u8bef\u5dee\u7684\u5f71\u54cd\uff0c\u4f46\u5bf9\u5f3a\u5236\u6362\u76f8\u7684\u52a8\u6001\u7279\u6027\u654f\u611f\u3002",
    "align-and-sweep": "align-and-sweep\uff08\u5bf9\u9f50\u5e76\u626b\u63cf\uff09",
    "\u2014 the align-and-sweep method applies a fixed current at a slowly changing angle during the align phase of startup. The applied electrical angle rotates through one full mechanical rotation in both forward and reverse directions, and over the two resulting intervals, averages the difference between applied electrical angle and measured encoder angle to obtain an estimate of commutation offset. This method is slow but can produce very accurate estimates of commutation offsets in most motors.":
        "\u2014 \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5\u5728\u542f\u52a8\u7684\u5bf9\u9f50\u9636\u6bb5\u4ee5\u7f13\u6162\u53d8\u5316\u7684\u89d2\u5ea6\u65bd\u52a0\u56fa\u5b9a\u7535\u6d41\u3002\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u5728\u6b63\u5411\u548c\u53cd\u5411\u65cb\u8f6c\u4e00\u4e2a\u5b8c\u6574\u7684\u673a\u68b0\u8f6e\uff0c\u5728\u4e24\u4e2a\u7ed3\u679c\u533a\u95f4\u5185\uff0c\u5bf9\u65bd\u52a0\u7684\u7535\u6c14\u89d2\u5ea6\u4e0e\u6d4b\u91cf\u7684\u7f16\u7801\u5668\u89d2\u5ea6\u4e4b\u5dee\u53d6\u5e73\u5747\uff0c\u4ee5\u83b7\u5f97\u6362\u76f8\u504f\u79fb\u7684\u4f30\u8ba1\u3002\u6b64\u65b9\u6cd5\u8f83\u6162\uff0c\u4f46\u53ef\u4ee5\u5728\u5927\u591a\u6570\u7535\u673a\u4e2d\u4ea7\u751f\u975e\u5e38\u51c6\u786e\u7684\u6362\u76f8\u504f\u79fb\u4f30\u8ba1\u3002",
    "These methods are described in more detail in the following sections.":
        "\u8fd9\u4e9b\u65b9\u6cd5\u5728\u4ee5\u4e0b\u7ae0\u8282\u4e2d\u6709\u66f4\u8be6\u7ec6\u7684\u63cf\u8ff0\u3002",
    "In all cases, commutation offset is estimated during only one startup iteration; once complete, the resulting value is reused, and subsequent startup sequences will skip back-emf synchronization.":
        "\u5728\u6240\u6709\u60c5\u51b5\u4e0b\uff0c\u6362\u76f8\u504f\u79fb\u4ec5\u5728\u4e00\u6b21\u542f\u52a8\u8fed\u4ee3\u4e2d\u4f30\u8ba1\uff1b\u4e00\u65e6\u5b8c\u6210\uff0c\u7ed3\u679c\u503c\u88ab\u91cd\u590d\u4f7f\u7528\uff0c\u540e\u7eed\u7684\u542f\u52a8\u5e8f\u5217\u5c06\u8df3\u8fc7\u53cd\u7535\u52a8\u52bf\u540c\u6b65\u3002",
    "5.4.3.3.1. Implementation issues common to all methods": "5.4.3.3.1. \u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.1.1. API of": "5.4.3.3.1.1. API",
    "5.4.3.3.1.2. Important data elements": "5.4.3.3.1.2. \u91cd\u8981\u6570\u636e\u5143\u7d20",
    "5.4.3.3.2. Align method": "5.4.3.3.2. \u5bf9\u9f50\u65b9\u6cd5",
    "5.4.3.3.2.1. Overview": "5.4.3.3.2.1. \u6982\u8ff0",
    "5.4.3.3.2.2. Limitations": "5.4.3.3.2.2. \u5c40\u9650\u6027",
    "5.4.3.3.2.3. Practical implementation issues": "5.4.3.3.2.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.2.4. Example data": "5.4.3.3.2.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.2.5. Accuracy and repeatability tests": "5.4.3.3.2.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "5.4.3.3.3. Align-and-sweep method": "5.4.3.3.3. \u5bf9\u9f50\u5e76\u626b\u63cf\u65b9\u6cd5",
    "5.4.3.3.3.1. Overview": "5.4.3.3.3.1. \u6982\u8ff0",
    "5.4.3.3.3.2. Limitations": "5.4.3.3.3.2. \u5c40\u9650\u6027",
    "5.4.3.3.3.3. Practical implementation issues": "5.4.3.3.3.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.3.4. Example data": "5.4.3.3.3.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.3.5. Accuracy and repeatability tests": "5.4.3.3.3.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "5.4.3.3.4. Pullout torque method": "5.4.3.3.4. \u5931\u6b65\u8f6c\u77e9\u65b9\u6cd5",
    "5.4.3.3.4.1. Overview": "5.4.3.3.4.1. \u6982\u8ff0",
    "5.4.3.3.4.2. Limitations": "5.4.3.3.4.2. \u5c40\u9650\u6027",
    "5.4.3.3.4.3. Practical implementation issues": "5.4.3.3.4.3. \u5b9e\u9645\u5b9e\u73b0\u95ee\u9898",
    "5.4.3.3.4.4. Example data": "5.4.3.3.4.4. \u793a\u4f8b\u6570\u636e",
    "5.4.3.3.4.5. Accuracy and repeatability tests": "5.4.3.3.4.5. \u7cbe\u5ea6\u548c\u53ef\u91cd\u590d\u6027\u6d4b\u8bd5",
    "5.4.3. Quadrature encoder support": "5.4.3. \u6b63\u4ea4\u7f16\u7801\u5668\u652f\u6301",
    "5.4.3.1. Overview": "5.4.3.1. \u6982\u8ff0",
    "5.4.3.1.1. Usage notes": "5.4.3.1.1. \u4f7f\u7528\u8bf4\u660e",
    "5.4.3.1.2. Limitations": "5.4.3.1.2. \u5c40\u9650\u6027",
    "5.4.3.2. Tracking loop": "5.4.3.2. \u8ddf\u8e2a\u73af",
    "5.4.3.2.1. Overview": "5.4.3.2.1. \u6982\u8ff0",
    "5.4.3.2.2. Frequency-domain equivalent": "5.4.3.2.2. \u9891\u57df\u7b49\u6548",
    "5.4.3.2.3. Implementation Notes": "5.4.3.2.3. \u5b9e\u73b0\u8bf4\u660e",
    "5.4.3.3. Back-EMF synchronization": "5.4.3.3. \u53cd\u7535\u52a8\u52bf\u540c\u6b65",
    "AN1292 Phase-locked Loop (PLL)": "AN1292 \u9501\u76f8\u73af\uff08PLL\uff09",
    "Implementation issues common to all methods": "\u6240\u6709\u65b9\u6cd5\u5171\u6709\u7684\u5b9e\u73b0\u95ee\u9898",
}

path = txutil.translate_dict_page(rel, title_zh, m)
print("translated", path)
