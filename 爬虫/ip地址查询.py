# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:29:16 2017

@author: zhuran
"""

import requests

url = "http://www.ip138.com/ips138.asp?ip="
ip = "123.174.49.103"
try:
    r = requests.get(url+ip)
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-2000:-1500])
except:
    print("查询失败！")