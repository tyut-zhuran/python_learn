from multiprocessing import Process

import os

import time


class myProcess(Process):#继承自Process类
	def __init__(self,interval):
		Process.__init__(self)
		self.interval = interval

	def run(self):
		print("子进程：%d"%os.getpid())
		for i in range(10):
			print(i)
			time.sleep(self.interval)


if __name__ == "__main__":
	print("主进程：%d"%os.getpid())
	p = myProcess(0.5)
	p.start()
	p.join()
	print("---------")
