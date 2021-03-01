# 1.列表推导式的使用
"""
列表推导式：list
通过列表推导式，使用一行代码可以实现一个简单的逻辑，从一定程度来说，可以简化代码

受到内存限制，列表容量肯定是有限的，而且创建一个包含100万个元素的列表，
不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
"""
list1 = [i * 2 for i in range(10)]
print(list1)

# 2.生成器：generator
"""
如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间，
在Python中，这种一边循环一边计算的机制，称为生成器：generator 
"""
ge1 = (i * 2 for i in range(10))
print(ge1)   # <generator object <genexpr> at 0x0000026D508DF570>

print(next(ge1))
print(next(ge1))
print(next(ge1))
