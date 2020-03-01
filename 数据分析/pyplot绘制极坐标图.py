import numpy as np 

import matplotlib.pyplot as plt 

#理解为条形转化为极坐标
N = 20

theta = np.linspace(0,2*np.pi, N, endpoint = False)

#半径
radii = 10*np.random.rand(N)

#弧形部分的弧度值
width = np.pi/8 * np.random.rand(N)

ax = plt.subplot(111,projection = "polar")
bars = ax.bar(theta, radii, width = width)

#设置颜色
for r,bar in zip(radii, bars):
	bar.set_facecolor(plt.cm.viridis(r/10))
	#设置透明度
	bar.set_alpha(0.5)
plt.show()