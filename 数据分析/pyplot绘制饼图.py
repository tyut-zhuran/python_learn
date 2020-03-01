

import matplotlib.pyplot as plt

labels = "name1","name2","name3","name4"
#各部分占比
sizes = [20,30,40,10]
#name2突出
explode = (0,0.1,0,0)

plt.pie(sizes,explode = explode,labels = labels,autopct = "%1.1f%%",shadow = False,startangle = 90 )
#正圆
plt.axis("equal")
plt.show()