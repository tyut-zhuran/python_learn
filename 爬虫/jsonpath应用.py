'''
XPath	JSONPath	描述
/		$			根节点
.		@			现行节点
/		.or[]		取子节点
..		n/a			取父节点，Jsonpath未支持
//		..			就是不管位置，选择所有符合条件的条件
*		*			匹配所有元素节点
@		n/a			根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要。
[]		[]			迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等）
|		[,]			支持迭代器中做多选。
[]		?()			支持过滤操作.
n/a		()			支持表达式计算
()		n/a			分组，JsonPath不支持
'''

#jsonpath貌似不太好用还是正则大法好


import urllib.request
import json
from jsonpath_rw import jsonpath,parse


url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

html = (response.read().decode("utf-8"))


#将json格式的字符串转化为python对象
city_dict = json.loads(html)["content"]["data"]["allCitySearchLabels"]

pattern =parse("'*'[*].name")
pattern2 = parse("'*'[*].id")

city_name_info = pattern.find(city_dict)
city_id_info = pattern2.find(city_dict)

city_list = [{city.value:city2.value} for (city,city2) in zip(city_name_info,city_id_info)]

print(len(city_list))
print(city_list)