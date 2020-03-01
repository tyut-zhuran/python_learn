# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:14:13 2017

@author: zhuran
"""
import matplotlib.pyplot as plt

'''
plt.subplot(nrows, ncols, plot_number)
nrow 表示将区域分为几行，ncol表示列
plot_number表示当前绘图区域
'''

plt.subplot(3,2,1)
plt.plot([2,3,4,5])
plt.subplot(3,2,2)
plt.plot([3,5,6,8])

plt.subplot(3,2,5)
plt.plot([5,6,8,7])

plt.subplot(3,2,4)
plt.plot([4,6,8,9])

plt.subplot(3,2,6)
plt.plot([1,2,3,4])
plt.show()