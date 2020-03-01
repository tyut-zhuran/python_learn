# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 20:08:40 2017

@author: zhuran
"""

import numpy as np

'''
np.sum(a,axis = None)求和，axis表示轴
np.mean(a,axis = None)求期望
np.average(a,axis = None, weights = None)求平均值，weights表示权重
np.std(a,axis = None)标准差
np.var(a,axis = None)方差
'''

a = np.arange(15).reshape((3,5))
print(np.sum(a))
print(np.sum(a,axis = 0))
print(np.sum(a,axis = 1))
print("*"*30)
print("*"*30)

print(np.mean(a))
print(np.mean(a,axis = 0))
print(np.mean(a,axis = 1))
print("*"*30)
print("*"*30)

print(np.average(a))
print(np.average(a,axis = 0))
print(np.average(a,axis = 1))
print(np.average(a,axis = 0,weights = [10,5,1]))
print("*"*30)
print("*"*30)

print(np.std(a))
print("*"*30)
print("*"*30)

print(np.var(a))




'''
np.max(a) np.min(a) 计算最大最小值
np.argmin(a) np.argmax(a) max,min的一维坐标
np.unravel_index(index, shape) 将一维坐标转换为多维坐标
np.ptp(a)  max-min
np.median(a)计算中位数
'''


print("*"*30)
print("*"*30)
b = np.arange(15,0,-1).reshape((3,5))
print(b)
print(np.max(b))
print(np.min(b))
print(np.argmax(b))
print(np.argmin(b))
print(np.unravel_index(np.argmax(b),(3,5)))
print(np.unravel_index(np.argmin(b),(3,5)))
print("*"*30)
print("*"*30)
print(np.ptp(b))
print(np.median(b))
print(np.median(b,axis = 0))