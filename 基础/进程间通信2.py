from multiprocessing import Process,Queue
import time
import random

class myProcess(Process):
	def __init__(self,q):
		Process.__init__(self)
		self.q = q

	def run(self):
		for i in ["消息1","消息2","消息3"]:
			self.q.put(i)
			print("put"+i)
			time.sleep(random.random())

		print("写进程结束！")


class myProcess2(Process):
	def __init__(self,q):
		Process.__init__(self)
		self.q = q

	def run(self):
		while True:
			if not self.q.empty():
				value = self.q.get()
				print("get"+value)
			else:
				break

if __name__ == "__main__":
	q = Queue(3)
	print("------------")
	p1 = myProcess(q)
	p2 = myProcess2(q)
	p1.start()
	p1.join()



	p2.start()
	p2.join()
	print("------end-------")