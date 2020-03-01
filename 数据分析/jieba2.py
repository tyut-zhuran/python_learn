import jieba.analyse
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt 
from wordcloud import ImageColorGenerator,WordCloud 

image = Image.open("考拉.png")
graph = np.array(image)
wc = WordCloud(font_path = "./fonts/simhei.ttf",background_color= "white", max_words = 50,mask = graph)

f = open ("歌词.txt","r")
lyric = f.read()
keywords = {}
result = jieba.analyse.textrank(lyric,topK = 50,withWeight = True)
for it in result:
	keywords[it[0]] = it[1]

wc.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)
plt.figure(figsize = (10,10))
plt.imshow(wc)

#让颜色对应
# plt.imshow(wc.recolor(color_func = image_color))
plt.axis("off")
plt.savefig("考拉词云.png",dpi = 800)
plt.show()