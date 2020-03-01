from multiprocessing import Pool

import os

import time

def test(name):
	print()
	print(name)
	print("子进程：%d"%os.getpid())
	for i in range(2):
		print(i)
		time.sleep(0.5)
	print("子进程结束!")


if __name__ == "__main__":
	print("主进程：%d"%os.getpid())
	p  = Pool(3) #定义一个进程池，最大进程数为3
	for i  in range(5):
		p.apply_async(func = test,args = ("name",))#func和args,如果有参数写元组，如(name,)
	print("----start------")
	p.close()#关闭进程池，禁止再添加进程
	#不写start
	p.join()
	print("------end-------")