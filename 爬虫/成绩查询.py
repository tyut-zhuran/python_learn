# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:10:45 2017

prbowc7y@author: zhuran
"""

import requests 
from bs4 import BeautifulSoup
from PIL import Image
import matplotlib.pyplot as plt

#plt.figure("dog")



def validateCode(r):
    with open ("validateCode.jpg","wb") as f:
        f.write(r.content)
    img=Image.open('D:/201707/python/爬虫/validateCode.jpg')
    plt.imshow(img)
    plt.show()
    v_yzm = input("输入验证码：")
    return v_yzm

headers = {"user-agent":"Mozilla/5.0"}
s = requests.Session()
url = "http://202.207.247.44:8089/"
s.get(url)
r = s.get("http://202.207.247.44:8089/validateCodeAction.do")
v_yzm = validateCode(r)

data = {"zjh":"2015001624","mm":"120337","v_yzm":v_yzm}

r = s.post("http://202.207.247.44:8089/loginAction.do",headers = headers,data = data)
r = s.get("http://202.207.247.44:8089/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=5333")
'''with open ("my.html","wb") as f:
    f.write(r.content)'''
# r = s.get("http://202.207.247.44:8089/bxqcjcxAction.do")
html = r.text
soup= BeautifulSoup(html,"lxml")
gradeInfo = []
for tr in soup.find_all("tr",{"class":"odd"}):
    gradeInfo.append(tr.find_all("td")[2].get_text().replace('\r\n','').replace(' ','') + 
    "----" +tr.find_all("td")[6].p.get_text().replace('\xa0',''))
if (len(gradeInfo)==0):
    print("验证码错误！！")
else:
    for i in range(len(gradeInfo)):
        print(gradeInfo[i])
    print("\n\n共%d科！"%(len(gradeInfo)))
    
