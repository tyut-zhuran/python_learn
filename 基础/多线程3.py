import threading
import time

class MyThread(threading.Thread):
	def run(self):
		for i in range(3):
			print("-----%s----%d"%(self.name,i))
			time.sleep(0.5)


if __name__ == "__main__":
	for i in range(5):
		t = MyThread()
		t.start()