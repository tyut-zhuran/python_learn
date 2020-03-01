# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:09:15 2017

@author: zhuran
"""

import re

ls = re.finditer(r'[1-9]\d{5}',"ZHU 100086 RAN 100056")
print(ls)
if ls:
    for match in ls:
        print(match.group(0))

print(re.sub(r'[1-9]\d{5}',"******","ZHU 100086 RAN 100056"))