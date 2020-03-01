# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:20:51 2017

@author: zhuran
"""

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


a = np.arange(0,5,0.02)
plt.subplot(211)
plt.plot(a,f(a))

plt.subplot(212)
plt.plot(a,np.cos(2*np.pi*a),"r--")

plt.show()