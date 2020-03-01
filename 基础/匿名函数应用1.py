












info_dict_list = [{"name":"zhuran","age":20},
					{"name":"sss","age":30},
					{"name":"www","age":28}]
print(info_dict_list)

info_dict_list.sort(key = lambda x:x["age"])

print(info_dict_list)

info_dict_list.reverse()

print(info_dict_list)

