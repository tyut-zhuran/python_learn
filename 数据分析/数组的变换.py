# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:54:43 2017

@author: zhuran
"""

import numpy as np


'''
.reshape(shape) 不改变原数组
.reshape(shape) 改变原数组
.swapaxes(ax1,ax2) 调换两个维度
.flatten()对数组进行降维，不改变原数组
'''
a = np.ones((3,2,5),dtype = np.int32)
print(a)
print(a.reshape(5,6))
print("-----")
print(a)
print(a.resize((5,6)))#没有返回值
print(a)
print("-----")

print(a.flatten())

#数组的类型变换

b = np.ones((3,5),dtype  = np.int32)
print(b)

b = b.astype(np.float)
print(b)

print("-"*10+"数组--->列表"+"-"*10)
#数组转换成列表,仅能转换一维
#only length-1 arrays can be converted to Python scalars
c = np.full((2,3,4),3,dtype = np.int32)
print(c)
ls = c.tolist()
print(ls)
