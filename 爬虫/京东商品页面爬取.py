# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 15:29:17 2017

@author: zhuran
"""

import requests
url = "https://item.jd.com/3701781.html"
try:
    r = requests.get(url)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
    
except:
    print("爬取失败！")    
    