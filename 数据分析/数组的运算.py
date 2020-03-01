# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:23:02 2017

@author: zhuran
"""

import numpy as np

a = np.arange(24).reshape((2,3,4))
print(a)
print("-"*30)
print(a.mean())#计算a中元素的平均值
print("-"*30)
print(a)
print("-"*30)
print(np.square(a))#求平方
print("-"*30)
print(np.sqrt(a))#求开方
a = np.sqrt(a)
print("-"*30)
print(np.modf(a))#分离整数和小数

     
print("-"*30)
a = np.arange(24).reshape((2,3,4))
b = np.sqrt(a)
print("-"*30)
print(b)
print("-"*30)
print(a>b)
print("-"*30)
print(np.maximum(a,b))#元素级比较a与b大小
print("-"*30)
print(np.minimum(a,b))