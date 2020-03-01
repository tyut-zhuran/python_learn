# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:57:33 2017

@author: zhuran
"""

import re

text = "zhuranshigerenzidonghua1504"
it = re.findall(r"[a-z]*",text)
print(it)