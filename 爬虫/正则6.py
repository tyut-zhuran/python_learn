# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:14:02 2017

@author: zhuran
"""
import re

m = re.search(r'[1-9]\d{5}',"ZHU 100086 RAN 100056")

print(m.re)
print(m.string)
print(m.pos)
print(m.endpos)
print(m.group(0))
print(m.start())
print(m.end())
print(m.span())