# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:19:09 2017

@author: zhuran
"""

import re
#默认为贪婪匹配。即最长
match = re.search(r'PY.*ON','PYTHONTHON')
print(match.group(0))

# 最小匹配：只要输出长度可能不同的，在操作符后面加？可以变成最小匹配

match = re.search(r'PY.*?ON',"PYTHONTHON")
print(match.group(0))