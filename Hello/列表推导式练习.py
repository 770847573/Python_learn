#利用列表推导式将列表中的整数提取出来：
#方法一：isdigit() 将内容是数字的字符串提取成数字，字符串的功能
list1 = [True,11,'dsa',78,98]
list2 = [ele for ele in list1 if str(ele).isdigit()]
print(list2)

#方法二：type()
list1 = [True,11,'dsa',78,98]
list2 = [ele for ele in list1 if type(ele) == int]
print(list2)

#方法三：isinstance(变量，类型)
list1 = [True,11,'dsa',78,98]
list2 = [ele for ele in list1 if isinstance(ele,int) and not isinstance(ele,bool)]
print(list2)

#利用列表推导式将列表中的所有字符串长度列出来
list1 = ['sad','dwdqd','ddsa ','fgrg']
list2 = [len(word) for word in list1]
print(list2)