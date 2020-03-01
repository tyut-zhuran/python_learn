# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:28:42 2017

@author: zhuran
"""
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
#colspan表示占的列数，rawspan表示占的行数
plt.subplot2grid((3,3),(1,0),colspan = 2)
plt.plot([1,3,5,6])
plt.subplot2grid((3,3),(0,0),colspan = 3)
plt.plot([3,4,6,7])
plt.subplot2grid((3,3),(1,2),rowspan = 2)
plt.plot([3,4,6,7])

plt.show()

#GridSpec类

gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:])
plt.plot([3,4,6,7])

ax2 = plt.subplot(gs[1,0:2])
plt.plot([5,7,8,9])

ax3 = plt.subplot(gs[1:3,2])
plt.plot([4,5,6,7])
plt.grid(True)
plt.show()




