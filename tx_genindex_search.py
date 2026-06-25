# -*- coding: utf-8 -*-
"""Translate genindex and search pages."""
import txutil

# genindex page
gen_m = {
    "Index": "索引",
    "Quick search": "快速搜索",
    "Enter search terms or a module, class or function name.": "输入搜索词或模块、类、函数名。",
    "A": "A", "B": "B", "C": "C", "D": "D", "E": "E", "F": "F",
    "G": "G", "H": "H", "I": "I", "J": "J", "K": "K", "L": "L",
    "M": "M", "N": "N", "O": "O", "P": "P", "Q": "Q", "R": "R",
    "S": "S", "T": "T", "U": "U", "V": "V", "W": "W", "X": "X",
    "Y": "Y", "Z": "Z",
    "next": "下一页",
    "previous": "上一页",
}

try:
    path = txutil.translate_dict_page("genindex", "索引 — MCAF R9 RC31 文档", gen_m)
    print("translated", path)
except Exception as e:
    print("genindex skipped:", e)

# search page
search_m = {
    "Search": "搜索",
    "Quick search": "快速搜索",
    "Enter search terms or a module, class or function name.": "输入搜索词或模块、类、函数名。",
    "search": "搜索",
    "Search Results": "搜索结果",
    "Searching for": "搜索",
    "No matches found.": "未找到匹配结果。",
    "Please try again with different search terms.": "请尝试使用不同的搜索词。",
    "From here you can search these documents. Enter your search words into the text box below and click \"search\". Note: the search function will automatically search for all of the words. Pages containing fewer words won't appear in the result list.":
        "您可以在此搜索这些文档。在下方文本框中输入搜索词并点击\"搜索\"。注意：搜索功能会自动搜索所有词。包含较少词的页面不会出现在结果列表中。",
}

try:
    path = txutil.translate_dict_page("search", "搜索 — MCAF R9 RC31 文档", search_m)
    print("translated", path)
except Exception as e:
    print("search skipped:", e)
