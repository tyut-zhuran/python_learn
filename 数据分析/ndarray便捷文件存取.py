# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:59:15 2017

@author: zhuran
"""

import numpy as np

'''
np.save(fname,array)或np.savez(fname,array)
fname:文件名.npy,压缩扩展名为.npz
array:
    
    
np.load(fname)

'''
a3 = np.arange(100).reshape((5,10,2))
np.save("a3.npy",a3)
b = np.load("a3.npy")
print(b)