# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:36:07 2017

@author: zhuran
"""

import matplotlib.pyplot as plt
import matplotlib
#这种方法有缺陷，会改变所有的文字风格和大小
matplotlib.rcParams["font.family"] = "SimHei"
matplotlib.rcParams["font.size"] = 16
plt.plot([2,4,6,7,4])
plt.ylabel("纵轴值")
plt.xlabel("横轴值")
plt.savefig("test",dpi = 600)
plt.show()