# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:25:52 2017

@author: zhuran
"""

import requests
import re

def getHtmlText(url):
    try:
        r = requests.get(url,headers = {"user-agent":"Mozilla/5.0"})
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
        
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(":")[1])
            title = eval(tlt[i].split(":")[1])
            ilt.append([price,title])
    except:
        print('')
    
def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for good in ilt:
        count += 1
        print(tplt.format(count,good[0],good[1]))
        
        
def main():
    good = "书包"
    depth = 3
    start_url = "https://s.taobao.com/search?q="+good
    info_list = []
    
    for i in range(depth):
        try:
            url= start_url + "&s=" + str(44*i)
            html = getHtmlText(url)
            parsePage(info_list,html)
        except:
            continue
    printGoodList(info_list)
    
if __name__ == "__main__":
    main()

        
        
        