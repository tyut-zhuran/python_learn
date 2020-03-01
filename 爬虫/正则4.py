# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:06:15 2017

@author: zhuran
"""

import re 

print(re.split(r'[1-9]\d{5}',"BIT 100086 ZHU 100056"))
print(re.split(r'[1-9]\d{5}',"BIT 100086 ZHU 100056",maxsplit = 1))