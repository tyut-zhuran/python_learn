import urllib.request

import http.cookiejar

import urllib.parse


#创建cookiejar对象实例用来保存cookie
cookiejar = http.cookiejar.CookieJar()

#使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)
response1 = opener.open("https://www.zhihu.com/#signin")
_xsrf = response1.read().decode("utf-8")[-51:-19]
#opener的属性addhearder = [(name,value),(name,value)]
opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"),
						("Accept","*/*"),
						("Accept-Language","zh-CN,zh;q=0.8"),
						("Connection","keep-alive"),
						
						("Content-Type","application/x-www-form-urlencoded; charset=UTF-8"),
						("Host","www.zhihu.com"),
						("Origin","https//www.zhihu.com"),
						("Referer","https//www.zhihu.com/"),
						("X-Requested-With","XMLHttpRequest"),
						("X-Xsrftoken",_xsrf)]
data = {
		"_xsrf":_xsrf,
		"password":"13994972924z",
		"captcha_type":"cn",
		"phone_num":"15035917897"
}
# 发送的数据需要转码
data = urllib.parse.urlencode(data)
print(data)
print(data.encode())
url = "https://www.zhihu.com/login/phone_num"
request = urllib.request.Request(url,data = data.encode("utf-8"))
response2 = opener.open(request)
response3 = opener.open("https://www.zhihu.com/people/zhu-ran-97-41/activities")
with open("zhihu.html","wb") as f:
	f.write(response3.read())
print(response3.read().decode("utf-8"))



