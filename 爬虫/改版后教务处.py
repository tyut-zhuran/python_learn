# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:47:04 2017

@author: zhuran
"""

import requests
import json
import matplotlib.pyplot as plt
from PIL import Image

tplt = "{0:{5}^5}{6:^10}{1:^15}{2:^5}{3:^8}{4:>10}"

class Stu():
    def __init__(self,name,num,gpa,paiming1,paiming2,banjirenshu,zhuanyerenshu,bm):
        self.name = name
        self.num = num 
        self.gpa = gpa
        self.paiming1 = paiming1
        self.paiming2 = paiming2
        self.banjirenshu = banjirenshu
        self.zhuanyerenshu = zhuanyerenshu
        self.bm = bm
    def __str__(self):
        return tplt.format(self.name,self.num,self.gpa,
                           self.paiming1+'/'+self.banjirenshu,
                           self.paiming2+'/'+self.zhuanyerenshu,
                           chr(12288),
                              self.bm) 
        
        
def getValidateCode(r):
    
    with open("validateCode.jpg","wb") as f:
        f.write(r.content)
    img = Image.open("validateCode.jpg")
    plt.imshow(img)
    plt.show()
    code = input("输入验证码：")
    return code


def getInfo(Info_list,Info_dict_list):
    url = "http://202.207.247.60/"
    headers = {"User-Agent":"Mozilla/5.0"}
    s = requests.Session()
    r = s.get(url,headers = headers)
    r = s.get("http://202.207.247.60/ValidateCode.aspx")
    txt_code = getValidateCode(r)
    data = {
    'txt_username':'2015001624',
    'txt_password':'120337',
    'txt_code':txt_code,
    '__VIEWSTATE':'/wEPDwULLTE5NTY4Njk4MjVkGAEFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYBBQ1jaGtSZW1lbWJlcm1l26Whon9CYPcGA7yTlPba2kRhH/v5plTTvgh0xjpr1cQ=',
    '__VIEWSTATEGENERATOR':'C2EE9ABB',
    '__EVENTVALIDATION':'/wEdAAYRLRZamXLLryo+bO6A5DQEs6cJ10LSoiuCyULvHjRPuC/yb/VVqFmvGO/9JabxfEtOvQSZUnBfbYku/hJfuKmgdDlmqzbR2b7nqJgQp10tGqtMpb9R/PAHkWF0A31JJ0NqcMNcBtNbEg/KRP0a1yv6kKezyiLG5KIyfX5o5sdIfQ==',
    'btn_login':'登录'}
    s.post(url,data = data,headers = headers)
    s.get("http://202.207.247.60/Default.aspx")
    for num in range(1596,1626):
        info  = {
                'limit':'40',
                'offset':'0',
                'order':'asc',
                'sort':'jqzypm,xh',
                'do':'xsgrcj',
                'xh':'201500'+str(num)}
        r  = s.post("http://202.207.247.60/Hander/Cj/CjAjax.ashx?rnd%20=%200.8340838591890283",
                    data = info,headers = headers)
        info_string = r.text.replace("[",'').replace("]",'')
        info_json = json.loads(info_string)
        Info_dict_list.append({"name":info_json["xm"],
                               "gpa":info_json["pjxfjd"]})
        Info_list.append(Stu(info_json['xm'],info_json['xh'],info_json['pjxfjd'],
                             info_json['gpabjpm'],info_json['gpazypm'],
                             info_json['bjrs'],info_json['zyrs'],info_json['bm']))
        
    
    
def main():
    Info_list = []
    Info_dict_list = []
    getInfo(Info_list,Info_dict_list)
    for info in Info_list:
        print(info)#输出所有信息！！！！！
    temp = sorted(Info_dict_list,key=lambda x: x["gpa"])
    temp.reverse()
    for it in temp:
        print(it)#按序输出！！！
    
    
if (__name__== "__main__"):
    main()
    
    