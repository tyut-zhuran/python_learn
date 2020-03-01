import threading
import time


class MyThread(threading.Thread):
	def run(self):
		for i in range(10):
			print("----%d-----"%i)
			time.sleep(0.5)


if __name__ == "__main__":
	t = MyThread()
	t.start()
