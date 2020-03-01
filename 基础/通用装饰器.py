
def decorator(func):
	print("-----装饰------")
	def warpped(*args, **kwargs):
		return func(*args, **kwargs)
	return warpped

@decorator
def test(a,b):
	print("a = %d , b = %d"%(a,b))

@decorator
def test2(a,b):
	return "a = %d, b= %d"%(a,b)

@decorator
def test3(a,b,c):
	return "a = %d, b = %d, c = %d"%(a,b,c)

@decorator
def test4():
	print("----test4----")

test(1,2)
print(test2(1,2))
print(test3(1,2,3))
test4()






