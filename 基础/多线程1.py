import threading
import time

#线程中主线程会等待其他线程结束在结束
def test():
	print("------test------")
	time.sleep(0.5)

if __name__== "__main__":
	for i in range(5):
		t = threading.Thread(target = test)
		t.start()
		print(time.ctime())