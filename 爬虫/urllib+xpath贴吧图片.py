
import urllib.request
import urllib.parse
from lxml import etree
class ImageSpider():
	def __init__(self,name,start_page,end_page):
		self.start_page = start_page
		self.end_page = end_page
		self.name = name
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
		self.num = 0
	def start_work(self):
		"""
		开始工作！
		"""
		kw = {"kw":self.name}
		
		for page in range(self.start_page,self.end_page+1):
			url = "http://tieba.baidu.com/f?"+"&"+urllib.parse.urlencode(kw)+"&pn=" +str((page-1)*50)
			html = self.load_page(url).decode("utf-8")
			self.parse_page(html)

	def load_page(self,url):
		"""
		加载页面得到HTML文本
		"""
		#加headers有问题？？？？？？
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		html = response.read()
		#self.parse_page(html)
		return html

	def parse_page(self,html):
		"""
		解析页面，得到各帖子的链接
		"""
		selector = etree.HTML(html)
		link_list = selector.xpath('//li[@class=" j_thread_list clearfix"]//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
		for link in link_list:
			fullurl = "https://tieba.baidu.com"+link
			self.find_img(fullurl)

	def find_img(self,fullurl):
		html = self.load_page(fullurl).decode("utf-8")
		selector = etree.HTML(html)
		img_link_list = selector.xpath('//img[@class="BDE_Image"]/@src')
		for img_link in img_link_list:
			self.write_img(img_link)

	def write_img(self,img_link):
		html = self.load_page(img_link)
		print(img_link)
		content = html
		with open("D://201707/python/爬虫/图片/"+img_link[-10:],"wb") as f:
			self.num+=1
			print("正在下载第%d张图片......"%self.num)
			f.write(content)

if __name__ == "__main__":
	img_spider = ImageSpider("美女",1,1)
	img_spider.start_work()

