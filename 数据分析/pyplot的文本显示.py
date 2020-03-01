# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 22:12:03 2017

@author: zhuran
"""

import matplotlib.pyplot as plt
import numpy as np
'''
plt.xlabel()
plt.ylabel()
plt.title()
plt.text()在任意位置增加文本
plt.annotate()增加带箭头的注释

'''
a=  np.arange(0,5,0.02)
plt.plot(a,np.cos(2*np.pi*a),"b--")
plt.xlabel("横轴值",fontproperties = "SimHei",fontsize = 18, color = "green")
plt.ylabel("纵轴值",fontproperties = "SimHei",fontsize = 18, color = "green")
plt.title(r"余弦波$y=2cos(2\pi x)$",fontproperties = "SimHei", fontsize = 18)#$$可以转义
plt.text(2,1,r"$\mu = 100$",fontsize = 14)
plt.annotate(r"$\mu = 100 $",xy = (4,1),xytext = (5,1.5),arrowprops = dict(facecolor = "green",shrink = 0.1, width = 3))
plt.axis([0,5,-2,2])
plt.grid(True)
plt.show()
