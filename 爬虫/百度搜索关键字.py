# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:50:01 2017

@author: zhuran
"""

import requests

keyword = "python"
kv = {"wd":keyword}
try:
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
    print(r.text[:1000])
except:
    print("爬取失败！")