import urllib.request


#构建一个handler处理器对象，支持http请求
http_handler = urllib.request.HTTPHandler()

#创建一个opener对象，支持处理http请求
opener = urllib.request.build_opener(http_handler)


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
url = "http://www.baidu.com"
request = urllib.request.Request(url)


response = opener.open(request)

print(response.read().decode("utf-8"))