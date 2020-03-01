import urllib.request

import urllib
headers = {"User-Agent":"Mozilla/5.0"}
#
html = urllib.request.urlopen("http://www.baidu.com/").read()
with open ("baidu.html","wb") as f:
	f.write(html)

#构建请求对象

request = urllib.request.Request("http://www.baidu.com/",headers = headers)

#返回一个类文件的响应对象
response = urllib.request.urlopen(request)

#返回状态码
print(response.getcode())

#返回响应对应的url
print(response.geturl())

#返回响应的http报头
print(response.info())

#urllib中文需要编码
kv = {"name":"朱冉"}
#必须传入字典
print(urllib.parse.urlencode(kv))
