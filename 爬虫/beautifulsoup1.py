# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 18:36:11 2017

@author: zhuran
"""

#beautifulsoup

import requests
from bs4 import BeautifulSoup

def getHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "something wrong!!"
        

html = getHtmlText("http://www.baidu.com")
soup = BeautifulSoup(html,"html.parser")
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p["id"])
print(soup.find_all("title"))
print(soup.get_text())#获取所有text内容

        