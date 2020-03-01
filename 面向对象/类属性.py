#类属性






class Tool(object):
	num = 0#类属性
	def __init__(self,name):
		self.name = name
		Tool.num+=1#表示每次创建新的实例对象都会使数量加1



tool1 = Tool("铲子")
print("当前共有%d个工具！"%Tool.num)#获取类属性


tool2 = Tool("勺子")
print("当前共有%d个工具！"%Tool.num)

tool3 = Tool("扳手")
print("当前共有%d个工具！"%Tool.num)
