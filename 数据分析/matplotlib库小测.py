# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:09:00 2017

@author: zhuran
"""

import matplotlib.pyplot as plt
plt.figure(num = 1)
plt.plot([2,4,7,1,3])
plt.plot([3,4,5,6,7],[2,4,7,1,3])
plt.ylabel("Grade")#y轴文字
plt.axis([-1,8,0,8])#指定坐标轴显示的范围
plt.grid(True)#画出方格
plt.savefig("test",dpi = 600)
plt.show()