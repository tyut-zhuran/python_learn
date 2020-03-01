# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 21:04:06 2017

@author: zhuran
"""
import numpy as np
'''
梯度即斜率
np.gradient(a)计算数组a中元素的梯度，a为多维数组时，返回每个维度的梯度
'''
a = np.random.randint(10,20,(5))
print(a)
print(np.gradient(a))
print("*"*30)
print("*"*30)

b = np.random.randint(0,50,(3,5))
print(b)
print(np.gradient(b))



