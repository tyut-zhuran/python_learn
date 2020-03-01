import requests
import threading
from lxml import etree
from multiprocessing import Queue
import json

CRAWL_EXIT = False
PARSE_EXIT = False
class CrawlThread(threading.Thread):
	def __init__(self,name,page_queue,html_queue):
		threading.Thread.__init__(self)
		self.page_queue = page_queue
		self.html_queue = html_queue
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}


	def run(self):
		print("开始线程："+self.name)
		while not CRAWL_EXIT:
			try:
				#block设为false,当队列空时，抛出异常执行pass，等待主线程关闭采集线程
				print("------crawl------")
				page =self.page_queue.get(False)
				url = "http://hr.tencent.com/position.php?&start="+str(10*page)
				r = requests.get(url,headers = self.headers)
				self.html_queue.put(r.text)
			except:
				print("队列空！")
				pass

		print("线程结束！-----%s"%self.name)

class ParseThread(threading.Thread):
	def __init__(self,name,html_queue,lock):
		threading.Thread.__init__(self)
		self.name = name
		self.html_queue = html_queue
		self.lock = lock

	def run(self):
		while not PARSE_EXIT:
			try:
				print("-------parse------")
				html = self.html_queue.get()
				selector = etree.HTML(html)
				info_tag = selector.xpath('//tr[@class="even"]|//tr[@class="odd"]')
				print(len(info_tag))
				self.lock.acquire()
				with open("zhaopin.json","ab") as f:
					for info in info_tag:
						position = info.xpath('./td[1]/a/text()')[0]
						
						temp_dict = {"position":position}
						print(temp_dict)
						f.write((json.dumps(temp_dict,ensure_ascii = False)+"\n").encode())
				self.lock.release()
			except:
				pass


def main():
	html_queue = Queue()
	page_queue = Queue()
	for i in range(216):
		page_queue.put(i)
	lock = threading.Lock()
	#存放线程的名字
	crawl_name_list = ["crawl-thread-1","crawl-thread_2","ceawl-thread-3"]
	#存放线程
	crawl_thread_list = []
	for thread_name in crawl_name_list:
		t = CrawlThread(thread_name,page_queue,html_queue)
		t.start()
		crawl_thread_list.append(t)

	#存放解析线程的名字
	parse_name_list = ["paese-thread-1","parse-thread-2","parse-thread-3"]

	parse_thread_list = []
	for thread_name in parse_name_list:
		t = ParseThread(thread_name,html_queue,lock)
		t.start()
		parse_thread_list.append(t)
	#等page_queue 空，即所有的链接都被处理是再继续
	while not page_queue.empty():
		pass
	global CRAWL_EXIT
	CRAWL_EXIT = True # 全部开始处理，就不必在crawl了，用来终止各个crawl线程

	print("全部页面已经开始处理！")
	print(html_queue.qsize())
	for crawl_thread in crawl_thread_list:
		#在此处阻塞主线程，等待所有采集线程结束在继续
		crawl_thread.join()

		#主线程等待解析线程结束
	while not html_queue.empty():
		pass

	global PARSE_EXIT
	PARSE_EXIT = True
	
	for thread in parse_thread_list:
		thread.join()

	print(html_queue.qsize())


if __name__ == "__main__":
	main()









