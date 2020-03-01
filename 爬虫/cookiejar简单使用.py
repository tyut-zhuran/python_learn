import urllib.request

import http.cookiejar

#创建一个cookiejar对象来保存cookie
cookiejar = http.cookiejar.CookieJar()


#创建一个处理器对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)

#用handler创建opener对象
opener = urllib.request.build_opener(handler)

url = "http://www.baidu.com/"

opener.open(url)


#cookiejar类似于字典
print(cookiejar)

cookie_str = ""
for item in cookiejar:
	cookie_str = cookie_str+item.name+"="+item.value +";"

print(cookie_str[:-1])



