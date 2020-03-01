# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:25:49 2017

@author: zhuran
"""
import requests
'''
r = requests.get("http://www.baidu.com")
#print(r.text)
print (r.status_code)
print (r.headers)
print (r.encoding)
print (r.apparent_encoding)
#print (r.content)

r.encoding = r.apparent_encoding
print(r.content)
print (r.text)
'''


#requests库爬取通用框架
def getHtmlText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding  = r.apparent_encoding
        return r.text
    except:
        return "something wrong!"
        
print(getHtmlText("http://www.baidu.com"))
    