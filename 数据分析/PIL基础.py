from PIL import Image

# 旋转图片
# im = Image.open("考拉.png").rotate(45)

im = Image.open("考拉.png")
# print(im.size)#图片尺寸
# print(im.format)#图片类型
# print(im.mode)#RGB

# im.thumbnail((100,100))#改变图片尺寸,

# im = im.resize((100,100))#改变图片尺寸
# im = im.convert("L")#换成黑白模式



#剪切，粘贴，合并
# box = (10,10,400,400) 
# region = im.crop(box)
# region.show()#剪切

# ---------定位锚-------------




# 图像增强
# im = im.point(lambda x: x*1.5)#参数为一个函数，每个像素乘以1.5

# source = im.split()
# (R,G,B) = (0,1,2)


# print(source)




im.show()
