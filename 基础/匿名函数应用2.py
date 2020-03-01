



#匿名函数及函数做参数


def test(a,b,func):
	return func(a,b)

print(test(10,20,lambda x,y:x+y))
print(test(10,20,lambda x,y:x-y))