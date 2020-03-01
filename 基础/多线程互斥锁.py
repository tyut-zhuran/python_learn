'''
mutex = threading.Lock()
mutex.acquire([blocking])参数为TRUE时堵塞
mutex.release()
'''


import threading
import time
g_num = 0

def test():
	global g_num
	if mutex.acquire():
		for i in range(1000000):
			g_num += 1
		mutex.release()

def test2():
	global g_num
	if mutex.acquire():
		for i in range(1000000):
			g_num += 1
		mutex.release()
if __name__ == "__main__":
	mutex = threading.Lock()
	t1 = threading.Thread(target = test)
	t2 = threading.Thread(target = test2)
	t1.start()
	t2.start()
	time.sleep(2)
	print(g_num)

