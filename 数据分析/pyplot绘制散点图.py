import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

ax.plot(10*np.random.randn(100), 10*np.random.randn(100),"o")
ax.axis([-30,30,-30,30])
ax.set_title("scatter")
#ax.set_title ("zhuran")
plt.show()



