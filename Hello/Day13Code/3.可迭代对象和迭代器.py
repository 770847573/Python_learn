"""
【面试题】可迭代对象和迭代器之间的区别和联系
区别
    可迭代对象：Iterable,可以直接作用于for循环的数据，如：list,tuple,dict,set,str,生成器等
    迭代器：Iterator，可以直接作用于for循环，而且可以使用next()获取元素的数据，如：生成器
联系：
    迭代器一定是可迭代对象，但是可迭代对象不一定是迭代器
    但是，可以通过系统功能iter()将不是迭代器的可迭代对象转换为迭代器
"""

from collections import Iterable,Iterator

# 1.可迭代对象
# isinstance(变量，类型)
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance("fafa",Iterable))
print(isinstance((i * 2 for i in range(5)),Iterable))

print("*" * 30)

# 2.迭代器
# isinstance(变量，类型)
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance("fafa",Iterator))
print(isinstance((i * 2 for i in range(5)),Iterator))

print(isinstance(iter([]),Iterator))
print(isinstance(iter(()),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter("fafa"),Iterator))