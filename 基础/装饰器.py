


def makeBold(func):
	def wrapped():
		return "<b>"+func()+"</b>"
	return wrapped

def makeItalic(func):
	def wrapped():
		return "<i>"+func()+"</i>"
	return wrapped

@makeBold
def test():
	return "hello world!"

@makeItalic
def test2():
	return "hello world!"


#两层装饰器
@makeItalic
@makeBold
def test3():
	return "hello world!"
#装饰器相当于闭包
#test()相当于makeBold(test)
print(test())
print(test2())
print(test3())

