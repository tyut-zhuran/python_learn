
#使用进程池时的通信

from multiprocessing import Manager,Pool
import time
import os
import random

def writer(q):
	print("------writer-------%d"%os.getpid())
	for i in ["zhu1","zhu2","zhu3"]:
		q.put(i)
		print("put"+i)
		time.sleep(random.random())

def reader(q):
	print("-------reader------%d"%os.getpid())
	while True:
		if not q.empty():
			print("get"+q.get())
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	print("------主进程------%d"%os.getpid())
	pool = Pool(2)#创建进程池
	q = Manager().Queue()#创建队列
	#使用阻塞模式,防止写入和读取一通乱麻
	pool.apply(writer,(q,))
	pool.apply(reader,(q,))
	pool.close()
	pool.join()
	print("--------end------")

