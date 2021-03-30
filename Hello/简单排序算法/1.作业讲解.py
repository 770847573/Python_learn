# 需求：利用列表推导式将已知列表中的整数提取出来
list1 = [True, 17, "hello", "bye", 98, 34, 21]
# 注意：isdigit()是字符串的功能，其他类型的变量无法使用
# 方式一:str()
list2 = [ele for ele in list1 if str(ele).isdigit()]
print(list2)
# 方式二:type()  # [17, 98, 34, 21]
list2 = [ele for ele in list1 if type(ele) == int]
print(list2)
# 方式三:isinstance(变量，类型)判断一个变量是否是指定的数据类型
list2 = [ele for ele in list1 if isinstance(ele,int) and not isinstance(ele,bool)]
print(list2)  # [17, 98, 34, 21]

# 需求：利用列表推导式存放指定列表中字符串的长度
# 注意：列表，元组，字符串，字典和集合都可以使用len()统计元素的个数或者计算容器的长度
list1 = ["good", "nice", "see you", "bye"]
# print(len("good"))
list2 = [len(word) for word in list1]
print(list2)