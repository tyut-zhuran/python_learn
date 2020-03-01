# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:08:12 2017

@author: zhuran
"""


import numpy as np
a= np.random.rand(3,4,5)#0到1随机生成（3,4,5）的数组(标准分布)
print(a)


sn = np.random.randn(3,4,5)#（标准正态分布）
print(sn)

b = np.random.randint(100,200,(3,4))#100到200随机生成（3,4）的数组
print(b)

np.random.seed(10)#随机数种子
c = np.random.randint(100,200,(3,4))
print(c)

np.random.seed(10)#同一个随机数种子
d = np.random.randint(100,200,(3,4))
print(d)#c与d相同

     
     

'''
 np.random.shuffle(a) 根据数组a的第一轴进行随机排列，改变数组a
 
'''
a = np.arange(24).reshape((4,3,2))

print(a)
np.random.shuffle(a)
print(a)

"""
np.random.permutation(a)
不改变数组a
"""
print("*"*30)
a = np.arange(24).reshape((4,3,2))
print(np.random.permutation(a))
print("*"*30)
print(a)


"""
np.random.choice(a[,size,replace,p])

从一维数组a中以概率p抽取元素，形成size形状的数组，replace表示是否可以
重用元素，默认为False
"""
print("*"*30)
print("*"*30)
b = np.random.randint(100,200,(8,))
print(b)
print(np.random.choice(b,(3,2),replace = True))
print(np.random.choice(b,(3,2),replace = False))
print(np.random.choice(b,(3,2),replace = True,p = b/np.sum(b)))#表示元素越大，概率越大

'''
函数
np.random.uniform(low,high,size)low到high，均匀分布，形状为size
np.random.normal(loc,scale,size)正态分布，loc为均值，scale为标准差，形状为size
np.random.poisson(lam,size)lam为随机事件发生率

'''
print("*"*30)
print("*"*30)
u = np.random.uniform(5,10,(5,5))
print(u)
print("*"*30)
print("*"*30)
n = np.random.normal(10,5,(5,5)) 
print(n)