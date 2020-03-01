from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
im = Image.open("考拉.png").convert("L")
im2 = Image.open("星空.png").convert("L")

kaola =np.array(im)
xingkong = np.array(im2)[150:476,250:575]
print(kaola.shape)
print(xingkong.shape)
plt.imshow(Image.fromarray(kaola+xingkong))
plt.show()
print(im)