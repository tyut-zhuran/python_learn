from multiprocessing import Queue


if __name__ == "__main__":
	q = Queue(3)#创建一个队列，最多容纳3条消息
	print(q.qsize())#当前的size
	print(q.full())
	q.put("1")
	q.put("2")
	print(q.get())
	print(q.get())
	print(q.empty())
	q.put("1")
	q.put("2")
	q.put("3")
	print(q.full())
	print(q.get())
	print(q.get())
	print(q.get())
	#print(q.get_nowait()) 若队列为空，立即抛出异常，同理,q.put_nowait()
	q.put("1")
	q.put("2")
	q.put("3")
	#用这种方法得到所有消息
	if not q.empty():
		for i in range(q.qsize()):
			print(q.get())