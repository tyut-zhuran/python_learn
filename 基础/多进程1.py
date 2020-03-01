from multiprocessing import Process
import os 

def run_proc(name):
	print("子进程%d"%os.getpid())
	print("子进程参数为%s"%name)

if __name__ == "__main__":
	print("父进程%d"%os.getpid())
	p = Process(target = run_proc,args = ("test",))#参数传入为元组
	print("执行子进程")
	p.start()
	p.join()#父进程等待子进程
	print("子进程已结束")


