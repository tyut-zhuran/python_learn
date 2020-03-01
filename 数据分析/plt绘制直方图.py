import numpy as np 
import matplotlib.pyplot as plt 

np.random.seed(0)


mu,sigma = 100,20#设置标准差和均值

a = np.random.normal(mu,sigma, size = 100)

plt.hist(a,20,normed  =1, histtype = "stepfilled", facecolor = "#505050",alpha = 0.75)

plt.title("直方图",fontproperties = "SimHei",fontsize = 18)

plt.show()