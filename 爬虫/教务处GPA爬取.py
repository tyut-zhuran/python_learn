# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 15:02:34 2017

@author: zhuran
"""

import requests
tplt = "{0:{5}^5}{1:^15}{2:^5}{3:^8}{4:^10}"
students = []
class Stu():
    def __init__(self,name,num,gpa,paiming1,paiming2):
        self.name = name
        self.num = num
        self.gpa = gpa
        self.paiming1 = paiming1
        self.paiming2 = paiming2
    def __str__(self):
        return (tplt.format(self.name,self.num,self.gpa,self.paiming1,self.paiming2,chr(12288)))
s = requests.Session()

s.post("http://202.207.247.60/",data = {"txt_username":"2015001614","txt_password":"120337"})

url = "http://202.207.247.60/Hander/Cj/CjAjax.ashx?rnd%20=%200.8083452519723235"
#data = {"limit":"40","offset":"0","order":"asc",
#"sort":"jqzypm","do":"xsgrcj","xh":"2015001619"}
for xuehao in range(1596,1626):#1596-1626
    data = {"limit":"40","offset":"0","order":"asc",
            "sort":"jqzypm","do":"xsgrcj","xh":"201500"+str(xuehao)}
    r = s.post(url,data)
    info = r.text.split("[{")[-1].split("}]")[0]
    info_list = list(info.replace('"','').split(","))
    #print(info_list)
    #print("姓名："+info_list[1].split(":")[-1])
    #print("学号："+info_list[0].split(":")[-1])
    #print("绩点："+info_list[15].split(":")[-1])
    #print("绩点班级排名："+info_list[16].split(":")[-1]+"/"+info_list[-2].split(":")[-1])
    #print("绩点专业排名："+info_list[17].split(":")[-1]+"/"+info_list[-1].split(":")[-1])
    name = info_list[1].split(":")[-1]
    num = info_list[0].split(":")[-1]
    gpa = info_list[15].split(":")[-1]
    paiming1 = info_list[16].split(":")[-1]+"/"+info_list[-2].split(":")[-1]
    paiming2 = info_list[17].split(":")[-1]+"/"+info_list[-1].split(":")[-1]
    students.append(Stu(name,num,gpa,paiming1,paiming2))
    
for student in students:
    print(student)
    
    