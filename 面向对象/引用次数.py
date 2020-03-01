#引用次数

import sys

class Test(object):
	def __init__(self,name):
		self.name = name

	def __del__(self):#对象占用的内存被释放时调用  或   对象的引用次数为0时被调用
		print("%s的内存被释放！"%self.name)


test1 = Test("zhu")
test2 = test1
#得到对象的引用次数
#print(sys.getrefcount(test1))
#del test1
#程序结束也会自动调用

