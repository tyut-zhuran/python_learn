




def decorator(func):
	print("正在装饰-----")
	def wrapped():
		print("-----wrapped1----")
		func()
		print("-----wrapped2----")
	return wrapped


@decorator
def test():
	print("-----test------")



test()



