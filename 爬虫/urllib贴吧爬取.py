import urllib.request
import urllib.parse

def loadPage(url):
	"""
	传入url返回html
	"""
	return urllib.request.urlopen(url).read()
def writePage(html,filename):
	"""
	将传入的html写入文件
	"""
	print("*"*30)
	print("正在写入"+filename)
	with open(filename, "wb") as f:
		f.write(html)
	print("写入"+filename+"成功！")

def tiebaSpider(url,name, start_page, end_page):
	"""
	调度器
	"""
	for pn in range(start_page, end_page+1):
		page = (pn-1)*50

		kw = urllib.parse.urlencode({"kw":name})
		fullurl = url + "&" + kw +"&pn=" +str(page)
		html = loadPage(fullurl)
		filename = "第"+str(pn)+"页.html"
		writePage(html, filename)
#http://tieba.baidu.com/f?kw=python
def main():
	name = input("输入贴吧名：")
	start_page = int(input("输入起始页："))
	end_page = int(input("输入结束页："))
	url = "http://tieba.baidu.com/f?"
	tiebaSpider(url, name,start_page, end_page)


if __name__ == "__main__":
	main()