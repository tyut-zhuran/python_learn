import urllib.request

import urllib.parse



headers = {
			"Accept":"application/json, text/javascript, */*; q=0.01",
			#"Accept-Encoding":"gzip, deflate",
			"Accept-Language":"zh-CN,zh;q=0.8",
			"Connection":"keep-alive",
			#"Content-Length":"219",
			"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
			"Cookie":"_ntes_nnid=fafef956df9d743e9246857e7173434b,1496657655375; OUTFOX_SEARCH_USER_ID_NCOO=819901213.6733047; JSESSIONID=aaaQBe5ifSvkmeLNSsT2v; SESSION_FROM_COOKIE=fanyiweb; OUTFOX_SEARCH_USER_ID=1508477959@10.169.0.27; ___rl__test__cookies=1501852700954",
			"Host":"fanyi.youdao.com",
			"Origin":"http://fanyi.youdao.com",
			"Referer":"http://fanyi.youdao.com/",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
			"X-Requested-With":"XMLHttpRequest"
				
}
word = input("输入翻译的关键字：")
#print(type(word))

data = {
			"i":word,
			"from":"AUTO",
			"to":"AUTO",
			"smartresult":"dict",
			"client":"fanyideskweb",
			#"salt":"1501850967820",
			#"sign":"cea84a20c6c52f83c96bbe70a9e69628",
			"doctype":"json",
			"version":"2.1",
			"keyfrom":"fanyi.web",
			"action":"action=FY_BY_CLlCKBUTTON",
			"typoResult":"true"
}
print("-----")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom="

#post的data也需要编码
data = urllib.parse.urlencode(data).encode()
print(data)
request = urllib.request.Request(url,data = data,headers = headers)
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))
