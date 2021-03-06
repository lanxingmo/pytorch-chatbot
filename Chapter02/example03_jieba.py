# -*- coding: utf-8 -*-
import jieba
__author__ = 'Alan Hou'

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list)) # 全模式
# Full Mode: 我/ 来到/ 北京/ 清华/ 清华大学/ 华大/ 大学

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list)) # 精确模式
# Default Mode: 我/ 来到/ 北京/ 清华大学

seg_list = jieba.cut("他来到了网易杭研大厦") # 默认为精确模式
print("，".join(seg_list))
# 他，来到，了，网易，杭研，大厦

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") # 搜索引擎模式
print("，".join(seg_list))
# 小明，硕士，毕业，于，中国，科学，学院，科学院，中国科学院，计算，计算所，，，后，在，日本，京都，大学，日本京都大学，深造