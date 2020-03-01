# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:59:11 2017

@author: zhuran
"""

import re

ls = re.findall(r'[1-9]\d{5}','BIT 100081 100056')
if ls:
    print(ls)