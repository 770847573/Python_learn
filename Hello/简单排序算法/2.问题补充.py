# 1.深浅拷贝
"""
=:怎么都会改
列表.copy()和copy.copy()：只有修改一维列表中元素的时候，一个更改，另外一个不受影响
copy.deepcopy()：怎么都不会改

浅拷贝：只拷贝了列表的最外层
深拷贝：不管嵌套几层，都会被拷贝
"""
a = [1,2,3]
b = [4,5]
c = [a,b]   # c = [[1,2,3],[4,5]]
d = c       # d = [[1,2,3],[4,5]]
e = c.copy()  # e  = [[1,2,3],[4,5]]
a.append(20)
# 问：d和e的值分别为多少
print(c is d)   # True
print(c is e)   # False

print(c)   # c = [[1,2,3,20],[4,5]]
print(d)   # d = [[1,2,3,20],[4,5]]
print(e)   # e = [[1,2,3,20],[4,5]]

import copy
a  = [1,2,['a','b']]
b = a
c = copy.deepcopy(a)
a[-1].append(3)
# 问：b和c的值分别为多少
print(a)  # a = [1,2,['a','b',3]]
print(b)  # b = [1,2,['a','b',3]]
print(c)  # c = [1,2,['a','b']]

a  = [1,2,['a','b']]
b = a
c = copy.deepcopy(a)
a.append(3)
# 问：b和c的值分别为多少
print(a)  # a = [1,2,['a','b'],3]
print(b)  # b = [1,2,['a','b'],3]
print(c)  # c = [1,2,['a','b']]

# 2.嵌套列表
list1 = [[23,54],[3,4,5]]
# 元素的访问
sublist1 = list1[0]
sublist2 = list1[1]
print(sublist1)
print(sublist2)

num1 = sublist1[0]
num2 = sublist2[2]
print(num1,num2)

# 直接访问
print(list1[0][1])

# 多维列表元素的遍历
for sublist in list1:
    print(sublist)
    for num in sublist:
        print(num)

for i in range(len(list1)):
    print(list1[i])
    for j in range(len(list1[i])):
        print(list1[i][j])

for i,sublist in enumerate(list1):
    for j,num in enumerate(sublist):
        print(num)