# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:12:43 2017

@author: zhuran
"""

import numpy as np

#一维数组的索引切片
a = np.array([2,3,4,5,6])
print(a[2])
print(a[1:4:2])#在1到4之间取值，间隔为2
print("-"*30)

#多维数组的索引和切片
#切片不会改变数组的维度
b = np.arange(24).reshape((2,3,4))
print(b)
print(b[1][2][3])
print(b[-1][-2][-3])
print(b[:,:,1:2])#不关心第1,2维度第三维度取第1个元素
print(b[:,1:2,1:2])#不关心第1维度，2,3维度取第1个元素
print(b[:,1:2,0:4:2])#间隔为2