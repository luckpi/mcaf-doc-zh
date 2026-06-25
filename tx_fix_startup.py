# -*- coding: utf-8 -*-
"""Fix startup.zh.html - the curly apostrophe caused mismatch."""
from txutil import load, save, body, replace_text, apply_punctuation

soup, path = load("algorithms/startup.zh.html")
root = body(soup)
# Use curly apostrophe (\u2019) to match the actual text
replace_text(soup, [
    ("The classic method was originally introduced in MCAF R1, and has been the only available method "
     "until MCAF R4. This method transitions by decreasing "
     "commanded current until the sensorless estimator\u2019s angle estimate approaches the forced commutation angle, or "
     "until the current has dropped below a threshold. This works by allowing the true d-axis current to decrease; "
     "as discussed further in the section on ",
     "经典方法最初在 MCAF R1 中引入，在 MCAF R4 之前一直是唯一可用的方法。"
     "该方法通过减小指令电流来进行过渡，"
     "直到无传感器估计器的角度估计接近强制换相角度，或"
     "直到电流降至某一阈值以下。其原理是允许真实的 d 轴电流减小；"
     "详见"),
    ("phasor analysis", "相量分析"),
], root=root)
apply_punctuation(root)
save(path, soup)
print("fixed: algorithms/startup.zh.html")
