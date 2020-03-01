import requests
from lxml import etree
import json

class QiushiSpider():
	def __init__(self):
		self.url = "https://www.qiushibaike.com/"
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
		self.file = "qiushi.json"
	def load_page(self):
		r=  requests.get(self.url,headers = self.headers)
		return r.text.replace("<br>","")
	def start_work(self):
		html = self.load_page()
		selector = etree.HTML(html)
		self.select_info(selector)
	def select_info(self,selector):
		info_dict = {}
		#模糊搜索语法
		info = selector.xpath("//div[contains(@class,'article block')]")
		f = open(self.file,"wb")
		for item in info:
			info_dict["content"] = item.xpath(".//div[@class ='content']/span/text()")
			info_dict["content"] = "".join(info_dict["content"]).strip()
			info_dict["vote"] = item.xpath(".//div[@class = 'stats']/span[1]/i/text()")[0]
			self.write_to_file(info_dict,f)
		f.close()

	def write_to_file(self,info_dict,f):
		info_json = json.dumps(info_dict,ensure_ascii =False)
		f.write((info_json+"\n").encode("utf-8"))




if __name__ == "__main__":
	spider = QiushiSpider()
	spider.start_work()
