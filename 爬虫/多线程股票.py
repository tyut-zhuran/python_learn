#https://gupiao.baidu.com/stock/

#http://quote.eastmoney.com/stocklist.html

#shanghai 
#shenzhen 


import urllib.request
import urllib.parse
from lxml import etree
from multiprocessing import Queue,Lock
import threading
import json
import os
import time


SH_CRAWL_EXIT = False
SZ_CRAWL_EXIT = False
SH_PARSE_EXIT = False
SZ_PARSE_EXIT = False

def get_html_text(url):
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
	request = urllib.request.Request(url,headers = headers)
	response = urllib.request.urlopen(request)
	html = response.read()
	return html
def get_all_link(url,sh_href_queue,sz_href_queue):
	html = get_html_text(url)
	selector = etree.HTML(html)
	sh_list = selector.xpath("//*[@id='quotesearch']/ul[1]/li")
	sz_list = selector.xpath("//*[@id='quotesearch']/ul[2]/li")
	for sh in sh_list:
		href = sh.xpath("./a/@href")[0]

		#上海链接放入队列
		sh_href_queue.put(href)
	for sz in sz_list:
		href = sz.xpath("./a/@href")[0]

		#深圳链接放入队列
		sz_href_queue.put(href)

	print(sh_href_queue.qsize())
	print(sz_href_queue.qsize())

class ShCrawlThread(threading.Thread):
	def __init__(self,name,sh_href_queue,sh_html_queue):
		threading.Thread.__init__(self)
		self.name = name
		self.sh_href_queue = sh_href_queue
		self.sh_html_queue = sh_html_queue
	def run(self):
		while not SH_CRAWL_EXIT:
			try:
				#设为false，队列空时抛出异常
				code = self.sh_href_queue.get(False)[-13:]
				if int(code[2:8])%10 == 0:
					print("sh")
				url = "https://gupiao.baidu.com/stock/"+code
				html = get_html_text(url)
				self.sh_html_queue.put(html)
				
			except:
				print("sh_href_queue队列已空！")
		print("线程结束！"+"----->"+self.name)
class SzCrawlThread(threading.Thread):
	def __init__(self,name,sz_href_queue,sz_html_queue):
		threading.Thread.__init__(self)
		self.name = name
		self.sz_href_queue = sz_href_queue
		self.sz_html_queue = sz_html_queue
	def run(self):
		while not SZ_CRAWL_EXIT:
			try:
				#设为false，队列空时抛出异常
				code = self.sz_href_queue.get(False)[-13:]
				if int(code[2:8])%10 == 0:
					print("sz")
				url = "https://gupiao.baidu.com/stock/"+code
				html = get_html_text(url)
				self.sz_html_queue.put(html)
				
				
			except:
				print("sz_href_queue队列已空！")
		print("线程结束！"+"----->"+self.name)

class ShParseThread(threading.Thread):
	def __init__(self,name,sh_html_queue,sh_lock):
		threading.Thread.__init__(self)
		self.name = name
		self.sh_html_queue = sh_html_queue
		self.sh_lock = sh_lock
	def run(self):
		while not SH_PARSE_EXIT:
			try:
				html = self.sh_html_queue.get(False)
				selector = etree.HTML(html)
				info_dict = {}
				info_dict["type"] = "sh"
				try:
					info_dict["name"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/h1/a/text()[1]")[0].strip()+"sh"+selector.xpath("//*[@id='app-wrap']/div[2]/div/h1/a/span/text()")[0]+")"
				except:
					info_dict["name"] = "null"
				try:
					info_dict["今开"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[1]/dd/text()")[0]
				except:
					info_dict["今开"] = "null"
				try:
					info_dict["昨收"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[1]/dd/text()")[0]
				except:
					info_dict["昨收"] = "null"
				
				self.sh_lock.acquire()
				with open("shanhai1.json","ab") as f:
					f.write((json.dumps(info_dict,ensure_ascii = False)+"\n").encode("utf-8"))
				self.sh_lock.release()

			except:
				time.sleep(0.5)
				print("...")
				pass
				#print("sh_html_queue已空！")
		print("解析线程结束！"+"-------->"+self.name)
class SzParseThread(threading.Thread):
	def __init__(self,name,sz_html_queue,sz_lock):
		threading.Thread.__init__(self)
		self.name = name
		self.sz_html_queue = sz_html_queue
		self.sz_lock = sz_lock
	def run(self):
		while not SZ_PARSE_EXIT:
			try:
				html = self.sz_html_queue.get(False)
				selector = etree.HTML(html)
				info_dict = {}
				info_dict["type"] = "sz"
				try:
					info_dict["name"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/h1/a/text()[1]")[0].strip()+"sz"+selector.xpath("//*[@id='app-wrap']/div[2]/div/h1/a/span/text()")[0]+")"
				except:
					info_dict["name"] = "null"
				try:
					info_dict["今开"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[1]/dl[1]/dd/text()")[0]
				except:
					info_dict["今开"] = "null"
				try:
					info_dict["昨收"] = selector.xpath("//*[@id='app-wrap']/div[2]/div/div[2]/div[2]/dl[1]/dd/text()")[0]
				except:
					info_dict["昨收"] = "null"
				
				self.sz_lock.acquire()
				with open("shenzhen1.json","ab") as f:
					f.write((json.dumps(info_dict,ensure_ascii = False)+"\n").encode("utf-8"))
				self.sz_lock.release()

			except:
				time.sleep(0.5)
				print("...")
				pass
				#print("sz_html_queue已空！")
		print("解析线程结束！"+"-------->"+self.name)


def main():
	sh_lock = Lock()
	sz_lock  = Lock()
	sh_href_queue = Queue()
	sz_href_queue = Queue()
	sh_html_queue = Queue()
	sz_html_queue = Queue()
	url = "http://quote.eastmoney.com/stocklist.html"
	get_all_link(url,sh_href_queue,sz_href_queue)
	sh_crawl_thread_list = []
	sz_crawl_thread_list = []
	sh_parse_thread_list = []
	sz_parse_thread_list = []
	sh_crawl_thread_name_list = ["上海crawl1","上海crawl2","上海crawl3","上海crawl4","上海crawl5","上海crawl6","上海crawl7","上海crawl8"]
	sz_crawl_thread_name_list = ["深圳crawl1","深圳crawl2","深圳crawl3","深圳crawl4","深圳crawl5","深圳crawl6","深圳crawl7","深圳crawl8"]
	sh_parse_thread_name_list = ["上海parse1","上海parse2","上海parse3","上海parse4","上海parse5","上海parse6","上海parse7","上海parse8"]
	sz_parse_thread_name_list = ["深圳parse1","深圳parse2","深圳parse3","深圳parse4","深圳parse5","深圳parse6","深圳parse7","深圳parse8"]
	#创建上海线程
	for name in sh_crawl_thread_name_list:
		t = ShCrawlThread(name,sh_href_queue,sh_html_queue)
		t.start()
		sz_crawl_thread_list.append(t)
	#创建深圳线程
	for name in sz_crawl_thread_name_list:
		t = SzCrawlThread(name,sz_href_queue,sz_html_queue)
		t.start()
		sz_crawl_thread_list.append(t)
		
	for name in sh_parse_thread_name_list:
		t = ShParseThread(name,sh_html_queue,sh_lock)
		t.start()
		sh_parse_thread_list.append(t)
	for name in sz_parse_thread_name_list:
		t = SzParseThread(name,sz_html_queue,sz_lock)
		t.start()
		sz_parse_thread_list.append(t)

	global SH_CRAWL_EXIT
	global SZ_CRAWL_EXIT
	global SH_PARSE_EXIT
	global SZ_PARSE_EXIT
	#暂停主线程
	while not sh_href_queue.empty():
		time.sleep(1)
		pass
	SH_CRAWL_EXIT = True
	print("true")
	for t in sh_crawl_thread_list:
		t.join()
		print("shjoin")
	print("3333")
	while not sz_href_queue.empty():
		time.sleep(1)
		pass
	SZ_CRAWL_EXIT = True
	for t in sz_crawl_thread_list:
		t.join()
		print("---")

	
	while not sh_html_queue.empty():
		time.sleep(1)
		pass
	SH_PARSE_EXIT  = True
	for t in sh_parse_thread_list:
		t.join()

	while not SZ_PARSE_EXIT:
		time.sleep(1)
		pass
	SZ_PARSE_EXIT = True
	for t in sz_parse_thread_list:
		t.join()


if __name__ == "__main__":
	main()
