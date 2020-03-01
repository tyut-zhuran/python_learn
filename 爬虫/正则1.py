# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:47:52 2017

@author: zhuran
"""

import re

match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))