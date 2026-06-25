# -*- coding: utf-8 -*-
"""Batch fix residual English text in 23 zh.html pages (batch 2)."""
import os
from bs4 import BeautifulSoup
from txutil import load, save, body, replace_text, apply_punctuation, set_title

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

def fix_page(rel, pairs=None, whole_pairs=None, use_body=True, title_zh=None):
    """Load a .zh.html page, apply fragment pairs and whole pairs, save."""
    soup, path = load(rel + ".zh.html")
    if title_zh:
        set_title(soup, title_zh)
    root = body(soup) if use_body else soup
    if root is not None:
        if pairs:
            replace_text(soup, pairs, root=root)
        if whole_pairs:
            replace_text(soup, whole_pairs, root=root, whole=True)
        apply_punctuation(root)
    save(path, soup)
    print(f"  fixed: {rel}.zh.html")
    return path


print("=== Batch 2: fixing 23 pages ===\n")

# 1. algorithms/foc/fundamentals.zh.html (12 fragments - references)
fix_page("algorithms/foc/fundamentals", pairs=[
    # "shown in 公式" -> "如公式" (fix stray paren too)
    ("), shown in 公式", "），如公式"),
    ("），它允许", "所示，它允许"),
    # author "and" -> "和"
    ("Schulz and E. Clarke", "Schulz 和 E. Clarke"),
    ("Overlin and J. L. Kirtley", "Overlin 和 J. L. Kirtley"),
    ("Schlegel and G. Skibinski", "Schlegel 和 G. Skibinski"),
    ("Jouanne and Haoran Zhang", "Jouanne 和 Haoran Zhang"),
    # "Also available via" -> "也可通过"
    ("Also available via", "也可通过"),
    # copper temperature coefficient paragraph (3 text nodes)
    ("For copper temperature coefficient, see the two sources below. "
     "The figure 0.00393/°C is bandied about quite a lot, but "
     "this was decided by convention in 1913, based on data available at the time. "
     "(See ",
     "关于铜的温度系数，请参见以下两个来源。"
     "0.00393/°C 这一数值被广泛引用，但"
     "这是 1913 年根据当时可用的数据通过约定确定的。"
     "（参见 "),
    (", page 4.)  The 1979 article by Matula",
     "，第 4 页。）Matula 在 1979 年的文章"),
    (" identifies and re-publishes numerous datasets for "
     "copper resistivity measurements and proposes "
     "an interpolated table of Recommended Values for the Electrical Resistivity of Copper "
     "(see table 2) vs. temperature.",
     " 中识别并重新发布了大量铜电阻率测量数据集，"
     "并提出了一份铜电阻率推荐值的插值表"
     "（见表 2）与温度的关系。"),
])

# 2. algorithms/foc/overmodulation.zh.html (3 fragments - references)
fix_page("algorithms/foc/overmodulation", pairs=[
    ("Vrancic and R. Hanus", "Vrancic 和 R. Hanus"),
    ("Degner and R. D. Lorenz", "Degner 和 R. D. Lorenz"),
])

# 3. algorithms/foc/comparison-6step.zh.html (2 fragments)
fix_page("algorithms/foc/comparison-6step", whole_pairs=[
    (", and", "，以及"),
])

# 4. algorithms/flux_control/flux_weakening.zh.html (3 fragments - Figure refs)
fix_page("algorithms/flux_control/flux_weakening", pairs=[
    ("Figure 5.79", "图 5.79"),
    ("Figure 5.80", "图 5.80"),
    ("Figure 5.81", "图 5.81"),
])

# 5. algorithms/dynlimit-simple.zh.html (1 fragment)
fix_page("algorithms/dynlimit-simple", pairs=[
    ("8 seconds. "
     "(Conversely, twice the continuous current limit "
     "produces four times the power dissipation.)",
     "8 秒。"
     "（反之，两倍的连续电流限制"
     "会产生四倍的功率损耗。）"),
])

# 6. algorithms/qei.zh.html (1 fragment - method name "align-and-sweep", leave as is)
# "align-and-sweep" is a method name, "and" is part of the name - no change needed
print("  skip: algorithms/qei.zh.html (method name align-and-sweep, no change)")

# 7. algorithms/qei_sync/align.zh.html (2 fragments)
fix_page("algorithms/qei_sync/align", pairs=[
    ("with 4096-line encoder", "配 4096 线编码器"),
], whole_pairs=[
    (", and", " 和"),
])

# 8. algorithms/qei_sync/common.zh.html (1 fragment)
fix_page("algorithms/qei_sync/common", pairs=[
    ("has type", "类型为"),
])

# 9. algorithms/qei_sync/pullout.zh.html (2 fragments)
fix_page("algorithms/qei_sync/pullout", pairs=[
    ("with 4096-line encoder", "配 4096 线编码器"),
])

# 10. algorithms/startup.zh.html (1 fragment - full paragraph)
fix_page("algorithms/startup", pairs=[
    ("The classic method was originally introduced in MCAF R1, and has been the only available method "
     "until MCAF R4. This method transitions by decreasing "
     "commanded current until the sensorless estimator's angle estimate approaches the forced commutation angle, or "
     "until the current has dropped below a threshold. This works by allowing the true d-axis current to decrease; "
     "as discussed further in the section on ",
     "经典方法最初在 MCAF R1 中引入，在 MCAF R4 之前一直是唯一可用的方法。"
     "该方法通过减小指令电流来进行过渡，"
     "直到无传感器估计器的角度估计接近强制换相角度，或"
     "直到电流降至某一阈值以下。其原理是允许真实的 d 轴电流减小；"
     "详见"),
    ("phasor analysis", "相量分析"),
])

# 11. algorithms/voltage-control.zh.html (2 fragments)
fix_page("algorithms/voltage-control", pairs=[
    (". With", "时达到平衡。当"),
    ("（无弱磁）时达到平衡。", "（无弱磁）时，"),
    ("can be derived from the PMSM voltage equations — 公式",
     "可以从 PMSM 电压方程——公式"),
])

# 12. appendix/glossary.zh.html (3 fragments)
fix_page("appendix/glossary", pairs=[
    ("The section of the", "指"),
])

# 13. architecture/codegen.zh.html (2 fragments - code block content, leave as is)
# "Where am I?" and "<some Java object...>" are YAML values inside <pre> code blocks
print("  skip: architecture/codegen.zh.html (code block content, no change)")

# 14. architecture/naming.zh.html (2 fragments)
fix_page("architecture/naming", pairs=[
    ("use of implementation-dependent types", "使用依赖于实现的类型"),
], whole_pairs=[
    (", and", "，以及"),
])

# 15. components/diagnostics.zh.html (1 fragment)
fix_page("components/diagnostics", pairs=[
    ("X2Cscope is configured to sample data at the control",
     "X2Cscope 被配置为在控制"),
])

# 16. components/supervisory.zh.html (4 fragments - "The")
fix_page("components/supervisory", whole_pairs=[
    ("The", "该"),
])

# 17. genindex.zh.html (1 fragment)
fix_page("genindex", pairs=[
    ("see also", "另见"),
])

# 18. implementation/custom-board-support/configuration.zh.html (4 fragments)
# Only "Specify the pin mapping for" is translatable; the 3 <em> placeholders
# are inside <pre> code blocks and should not be translated.
fix_page("implementation/custom-board-support/configuration", pairs=[
    ("Specify the pin mapping for", "在"),
])

# 19. implementation/custom-board-support/custom_board_definitions.zh.html (4 fragments)
fix_page("implementation/custom-board-support/custom_board_definitions", pairs=[
    ("This is a comment", "这是一个注释"),
], whole_pairs=[
    (", and", "，以及"),
])

# 20. implementation/custom-board-support/verification.zh.html (2 fragments)
fix_page("implementation/custom-board-support/verification", whole_pairs=[
    ("The", "该"),
    ("Note", "注意"),
])

# 21. implementation/resource-usage.zh.html (4 fragments)
fix_page("implementation/resource-usage", pairs=[
    ("(approximate number of cycles, "
     "and percentage at 200 MIPS, 20 kHz ISR)",
     "（近似周期数，"
     "及 200 MIPS、20 kHz ISR 下的百分比）"),
], whole_pairs=[
    ("Note", "注意"),
])

# 22. implementation/ui-customization.zh.html (1 fragment)
fix_page("implementation/ui-customization", whole_pairs=[
    ("The", "该"),
])

# 23. search.zh.html (2 fragments) - no div.body, use whole soup
fix_page("search", use_body=False, pairs=[
    ("Please activate JavaScript to enable the search functionality.",
     "请启用 JavaScript 以使用搜索功能。"),
    ("Searching for multiple words only shows matches that contain all words.",
     "搜索多个词时只显示包含所有词的匹配结果。"),
])

print("\n=== Done! ===")
