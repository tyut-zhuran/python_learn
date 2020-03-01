# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:51:54 2017

@author: zhuran
"""

import re
# re.match 从开头匹配
match = re.match(r'[1-9]\d{5}','100081 BIT') 
if match:
    print(match.group(0))