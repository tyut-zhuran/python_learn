# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:38:40 2017

@author: zhuran
"""

import numpy as np
# a = np.array(list/tuple, dtype = "")
a = np.array([1,2,3,4])#用列表创建
b = np.array((1,2,3,4))#用元组创建

c = np.array([[1,3,4],[2,3,4],(4,5,6)])#同时用列表和元组
d = np.arange(10)
e = np.ones((2,4))

f = np.zeros((2,3),dtype = np.int32)
g = np.eye(5)#生成单位矩阵
h = np.ones_like(c)#根据c的形状生成全是1的ndarray

i = np.zeros_like(c)
j = np.full_like(c,3)#根据c的形状生成全是3的ndarray  ===np.full((3,3),3)
k = np.linspace(1,10,4,endpoint = False)

l = np.linspace(1,10,4,endpoint = True)#1到10等间距的生成元素
m = np.concatenate((k,l))#合并两数组                   
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

