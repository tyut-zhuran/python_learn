import urllib.request
import re

class NeihanSpider():
	def __init__(self):
		self.file = "内涵段子.txt"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
		self.page = 1
		self.url = "http://www.neihan8.com/article/"
		self.content_num = 0


	def start_work(self):
		'''
		开始工作
		'''
		fullurl = self.url
		self.load_page(fullurl)
		

	def load_page(self,fullurl):
		'''
        
		下载页面，得到html
		'''
		command = "y"
		while(command != "n" and command != "N"):
			request = urllib.request.Request(fullurl,headers = self.headers)
			print("开始下载第" + str(self.page) +"页！")
			response = urllib.request.urlopen(request)
			print(response.getcode())
			html = (response.read().decode("utf-8"))
			self.parse_page(html)
			command = input("是否继续?(停止输入n/N):")
			self.page = self.page + 1
			fullurl = self.url+"index_"+str(self.page)+".html"

	def parse_page(self,html):
		'''
		解析页面，找出页面中的段子
		'''
		pattern = re.compile('<div class="desc">(.*)</div>')
		content_list = pattern.findall(html)
		for content in content_list:
			self.write_to_file(content)
	def write_to_file(self,content):
		'''
		解析出的内容写入文件
		'''
		with open(self.file,"a") as f:
			self.content_num = self.content_num+1
			f.write(str(self.content_num)+"、"+content.strip().replace("&amp;hellip;","")+"\n")
		print(str(self.content_num)+"、"+content.strip().replace("&amp;hellip;",""))


if __name__ == "__main__":

	nei_han_spider = NeihanSpider()
	nei_han_spider.start_work()



