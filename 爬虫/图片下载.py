# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:03:00 2017

@author: zhuran
"""

import requests
import os

url = "http://imgsrc.baidu.com/image/c0%3Dshijue%2C0%2C0%2C245%2C40/sign=626e96b8c711728b24208461a095a9bb/0eb30f2442a7d9337bfbfd5aa74bd11373f00143.jpg"

root = "C://Users//zhuran//Desktop//201707//python//爬虫//图片//"

path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        print(r.status_code)
        #r.raise_for_status()
        #r.encoding = r.apparent_encoding
        with open (path,"wb") as f:#以写入二进制方式打开
            f.write(r.content)#content二进制
            print("保存成功！")
    else:
            print("文件已存在！")
except:
    print("下载失败！")