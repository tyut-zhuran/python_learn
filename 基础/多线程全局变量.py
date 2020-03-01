import threading
import time

g_num = 100
def MyThread():
	global g_num
	g_num += 100
	print("线程一结束+%d"%g_num)

def MyThread2():
	global g_num
	print("线程2中%d"%g_num)


if __name__ == "__main__":
	t1 = threading.Thread(target = MyThread)
	t1.start()
	time.sleep(1)#保证完成对g_num的改变

	t2 = threading.Thread(target = MyThread2)
	t2.start()