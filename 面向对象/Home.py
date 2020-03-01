# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:31:10 2017

@author: zhuran
"""

class Home:
    def __init__ (self,new_area,new_info,new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []
    def __str__(self):
        msg=  "房子的总面积是%d，可用面积是%d，户型是%s，地址是%s。"%(self.area,self.left_area,self.info,self.addr)
        msg += "当前房子里的物品有%s"%(str(self.contain_items))
        return msg
    def add_item(self,item):
        self.left_area -= item.area
        self.contain_items.append(item.name)
    
class Bed:
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area = new_area
        
    def __str__(self):
        return "%s占用的面积是%d"%(self.name,self.area)
fangzi = Home(129,"三室一厅","北京长安街")
print(fangzi)

bed = Bed("席梦思",4)
print(bed)
bed2 = Bed("三人床",6)
fangzi.add_item(bed)
fangzi.add_item(bed2)
print(fangzi)