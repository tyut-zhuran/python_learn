# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 09:57:21 2017

@author: zhuran
"""

# 隐藏对象的属性

class Dog:
    def __init__(self):
        pass
    def set_age(self,new_age):
        if new_age>0 and new_age<100:
            self.age = new_age
        else:
            self.age = 0
    def get_age(self):
        return self.age
    
dog = Dog()
dog.set_age(10)
print(dog.get_age())

