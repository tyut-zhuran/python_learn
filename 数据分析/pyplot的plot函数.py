# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:25:29 2017

@author: zhuran
"""

import matplotlib.pyplot as plt
import numpy as np

'''
plt.plot(x,y,format_string,**kwargs)

format_string 可以控制曲线的颜色，风格等
**kwargs 可以是更多的（x,y,format_string）
'''
a = np.arange(10)
plt.plot(a,a*1.5,"bo--",a,a*2,"r^-",a,a*3,"k*:",a,a*4,"yH-")


plt.show()
