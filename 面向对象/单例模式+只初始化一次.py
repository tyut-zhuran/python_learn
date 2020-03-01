class Test(object):

	__instance = None#未创建任何对象时取None
	__init_flag = False
	def __new__(cls,name):
		if cls.__instance == None :
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else :
			return cls.__instance

	def __init__(self,name):
		if Test.__init_flag == False:
			Test.__init_flag = True
			self.name = name

test1 = Test("zhu")
test2 = Test("ran")
print(test1.name,test2.name)