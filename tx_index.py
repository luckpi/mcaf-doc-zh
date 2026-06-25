# -*- coding: utf-8 -*-
"""Translate index.html (home page)."""
import txutil
from terms import CHAPTER_TITLES, UI_FRAGMENTS

rel = "index"

pairs = []
# chapter titles (appear in toctree links as "N. Title")
pairs += CHAPTER_TITLES
pairs += UI_FRAGMENTS
pairs += [
    ("Motor Control Application Framework", "电机控制应用框架"),
    ("Index", "索引"),
    (" and ", " 与 "),
]

path = txutil.translate_page(rel, "电机控制应用框架", pairs)
print("translated", path)
