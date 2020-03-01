# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:39:12 2017

@author: zhuran
"""

import numpy as np
'''
csv文件只能存储一维和二维数组
    
'''
'''
np.savetxt(frame,array,fmt = "%.18e",delimiter = None)
fmt 为保存的数据类型默认为科学计数法，常用%d,%.1f......
delimiter为分隔符
'''
a = np.arange(100).reshape(5,20)
np.savetxt("a.csv", a, fmt = "%d", delimiter = ",")

'''
np.loadtxt(frame,dtype = np.float, delimiter = None, unpack = False)
frame:文件可以是.csv,.gz,.bz2
unpack:如果是True，读入属性将分别写入不同的变量
'''

b = np.loadtxt("a.csv",dtype = np.int32, delimiter = ",")
print(b)


'''
多维数组用.tofile 和 .fromfile
'''

'''
a.tofile(frame,sep = '', format = "%s")
frame :文件
sep:数据分割字符串，如果为空，写入文件为二进制
formt:写入数据的格式
'''

a2 = np.arange(100).reshape((5,10,2))
a2.tofile("a2.dat",sep = ",", format = "%d")



'''
np.fromfile(frame, dtype = float, count = -1, sep= '')
count:表示读入元素的个数，-1表示全部读入

读出为一维数组，需要用reshape转换
'''

b2 = np.fromfile("a2.dat",sep = ",", count = -1, dtype = np.int32).reshape((5,10,2))
print(b2)