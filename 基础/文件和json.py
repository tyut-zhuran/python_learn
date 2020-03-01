import json 


f1 = open ("C:/aboutscrapy/douban250/movie.json","r",encoding = "utf-8")
f2 = open("C:/aboutscrapy/douban250/movie2.json","wb")
dic = {"paiming":1,"name":2,"score":3,"renshu":4,"quote":5,"people":6}

while(True):
	content = f1.readline()
	if content == "":
		break
	content_dict = json.loads(content)
	content_dict["people"] = content_dict["people"].replace("\n","").replace(" ","")
	content_dict = sorted(content_dict.items(),key = lambda x:dic[x[0]])
	f2.write((json.dumps(dict(content_dict),ensure_ascii = False)+'\n').encode())#字符串要编码才能以二进制写入
	
	
f1.close()
f2.close()
