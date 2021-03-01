# 4.写出下面代码的输出结果并说明原因
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[10:])

# []，原因：在切片中，不会保存，要么列表非空，要么列表为空

# 5.写出下面代码的输出结果并说明原因
str1 = "hello python"
str1.title()   # upper()/lower()/replace()
print(str1)

# hello python，原因：字符串是不可变的数据类型，但凡涉及到字符串的更改，都是生成了一个新的字符串

# 6.写出下面代码的输出结果并说明原因
def text(l):
	l[1] = 10
list1 = [1,2,3,4]
text(list1)
print(list1)

# [1,10,3,4] 原因：是引用传递【传递的数据是可变的数据类型】，如果形参做出了修改，则实参会随着修改

# 8.写出下面代码的输出结果并说明原因
def fun(li=[]):
    li.append("abc")
    return li

# 情况一
# print(fun())   # ['abc']
# print(fun())   # ['abc', 'abc']

# 情况二
print(fun())   # ['abc']
print(fun([1,2,3]))  # [1,2,3,'abc']
print(fun())   # ['abc', 'abc']
print(fun([1,2,3]))  # [1, 2, 3, 'abc']

# 注意：判断每次在操作的时候，针对的是不是同一个对象
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(id(list1) == id(list2))





