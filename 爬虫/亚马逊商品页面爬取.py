# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:34:33 2017

@author: zhuran
"""

import requests

url = "https://www.amazon.cn/gp/product/B0186FESGW"
kv = {"user-agent":"Mozilla/5.0"}
try:
    r = requests.get(url,headers = kv)
    print(r.status_code)
    r.raise_for_status()
    r.encoding= r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败！")