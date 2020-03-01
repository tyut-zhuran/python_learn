from multiprocessing import Process
import os
import time


def run_proc():
	print("--------")
	for i in range(10):
		time.sleep(0.5)
		print(str(i)+"、"+str(os.getpid()))


if __name__ == "__main__":
	p = Process(target = run_proc)
	print("父进程%d"%os.getpid())
	p.start()
	time.sleep(3)
	p.terminate()#强制退出子进程
	p.join()
	print("子进程结束!")



