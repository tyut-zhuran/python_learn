def outer_decorator(a):
	def decorator(func):
		print("------装饰-------")
		def wrapped(*args, **kwargs):
			print("------记录-----%s"%a)
			return func(*args, **kwargs)
		return wrapped
	return decorator

@outer_decorator("zhu")
def test(a,b):
	return "a = %d, b = %d"%(a,b)

@outer_decorator("wang")
def test2(a,b,c):
	return "a = %d, b = %d, c = %d"%(a,b,c)

print(test(1,2))
print(test2(1,2,3))