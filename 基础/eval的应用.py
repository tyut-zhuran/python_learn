#eval相当于去掉字符串的 ""
#使他变为可使用的表达式





def test(a,b,func):
	return func(a,b)



func = input("输入函数")
func = eval(func)

print(test(10,20,func))
