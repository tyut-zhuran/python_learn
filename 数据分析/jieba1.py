import jieba


seg_list = jieba.cut("我叫朱冉,我是一名编程初学者,我来自太原理工大学",cut_all = True)#全模式，尽可能多的分词
print(seg_list)
print("全模式："+"/".join(seg_list))

#增加词语
jieba.add_word("朱冉")

seg_list2 = jieba.cut("我叫朱冉,我是一名编程初学者",cut_all = False)
print("精确模式："+"/".join(seg_list2))

seg_list3 = jieba.cut("我来自太原理工大学")
print("默认是精确模式："+"/".join(seg_list3))

seg_list4 = jieba.cut_for_search("我叫朱冉,我是一名编程初学者,我来自太原理工大学")
print("搜索引擎模式："+"/".join(seg_list4))