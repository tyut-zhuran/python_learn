#同步是指定执行的顺序


import threading
import time

def test1():
	if lock1.acquire():
		print("------test1-------")
		time.sleep(0.5)

	lock2.release()


def test2():
	if lock2.acquire():
		print("-------test2------")
		time.sleep(0.5)
	lock3.release()

def test3():
	if lock3.acquire():
		print("--------test3--------")
		time.sleep(0.5)
	lock1.release()


if __name__ == "__main__":
	lock1 = threading.Lock()
	lock2 = threading.Lock()
	lock2.acquire()
	lock3 = threading.Lock()
	lock3.acquire()
	for i in range(5):
		t1 = threading.Thread(target = test1)
		t2 = threading.Thread(target = test2)
		t3 = threading.Thread(target = test3)
		t1.start()
		t2.start()
		t3.start()















