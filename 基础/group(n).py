import re

url = "http://www.baidu.com/start=100?phpzhuran100.html"

pattern = re.compile("(\d+).*(\d+)")


# group(0)表示所有匹配的结果，group(1)表示的是第一个括号的匹配结果
page = int(pattern.search(url).group(1))
print(pattern.search(url).group(1))
url = pattern.sub(str(page+10),url)
print(url)