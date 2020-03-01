# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:42:55 2017

@author: zhuran
"""

import numpy as np

import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus'] = False#解决负号显示的问题
a = np.arange(0.0,5.0,0.02)

plt.xlabel(u"横轴值",fontproperties = "SimHei",fontsize = 20)
plt.ylabel(u"纵轴值",fontproperties = "SimHei",fontsize = 20)

plt.plot (a,np.cos(2*np.pi*a),"r--")
plt.axis([0,5,-2,2])
plt.savefig("test.png", format='png', dpi=100, bbox_inches='tight')#保存完整的图片
plt.show()