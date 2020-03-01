list1 = [2,3,4,6,1,-2,-3,-5,-1]
print(sorted(list1,key = lambda x:x))
print(sorted(list1,key = lambda x:x , reverse = True))
print(sorted(list1,key = lambda x:(x<0,abs(x))))
#按照（x<0,abs(x)）排序 先false 后true
print((sorted("abcABCsdF6G5A23",key = lambda x:(x.isdigit(),x.isdigit() and int(x)%2 == 0,x.isupper(),x))))
print(''.join(sorted("abcABCsdF6G5A23",key = lambda x:(x.isdigit(),x.isdigit() and int(x)%2 == 0,x.isupper(),x))))
#.join()可以变列表为字符串