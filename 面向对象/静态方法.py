#静态方法


class Test(object):
	def __init__(self,name):
		self.name = name


	@staticmethod
	def print_info():#不需要传self或cls
		print("test----------")


Test.print_info()