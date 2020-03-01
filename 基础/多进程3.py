from multiprocessing import Process

import os
import time


def test1():
	start_time = time.time()
	print("----test1----%d"%os.getpid())
	for i in range(3):
		time.sleep(0.5)
		print(i)
	end_time = time.time()
	print("共运行：'%.8f'"%(-start_time +end_time))


if __name__ == "__main__":
	p = Process(target = test1)
	p.start()
	p.join()
	print("----end------")

