from PIL import Image
import matplotlib.pyplot as plt  
import numpy as np
def process_img(img):
	scale = 50#确定图片的大小
	width,height = img.size
	if width>height:
		max = width
	else:
		max = height
	#伸缩倍数
	delta = max/scale
	width,height = int(width/delta),int(height/delta)
	#width,height = (50,int((height/width)*25))#另一种方法
	img = img.resize((width,height))
	return img
def gray_to_char(gray):
	string = "abcdefghijklmnopqrstuvwxyz "
	max_index = len(string)
	grad = 256/max_index
	return string[int(gray/grad)]
def img_to_chars(array):
	text = ''
	for i in range(array.shape[0]):
		line = ''
		for j in range(array.shape[1]):
			line = line + gray_to_char(array[i][j])
		line = line+"\n"
		text = text + line
	print(len(text))
	with open("考拉字符.txt","w") as f:
		f.write(text)

img = Image.open("考拉.png").convert("L")
img = process_img(img)
array = np.array(img)
print(img_to_chars(array))




