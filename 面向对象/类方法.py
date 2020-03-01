







#类方法



class Test(object):
	num = 0
	def __init__(self,name):
		self.name = name
		Test.num+=1

	def __str__(self):
		return self.name

	@classmethod
	def print_num(cls):
		print("当前共有%d个实例对象！"%cls.num)


test1 = Test("zhu")
print(test1)
Test.print_num()

test2 = Test("wang")
print(test2)
Test.print_num()

test3 = Test("li")
print(test3)
Test.print_num()

test4 = Test("wu")
print(test4)
Test.print_num()
