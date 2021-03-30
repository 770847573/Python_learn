# 1.定义
list1 = [34,465]
print(type(list1))
tuple1 = (34,456)
print(type(tuple1))

# 注意:如果元组中只有一个元素，则需要在元素的后面添加逗号，为了消除歧义
list2 = [34]
print(list2)
print(type(list2))
tuple2 = (34,)
print(tuple2)
print(type(tuple2))

# 2.列表是可变的，元组是不可变的,所以元组一旦定义完成之后，将不能随意更改其中的元素
list1 = [45,5,7]
print(list1)
list1[0] = 100
print(list1)

tuple1 = (45,5,7)
print(tuple1)
# tuple1[0] = 100    # TypeError: 'tuple' object does not support item assignment

# 思考题
t1 = (34,64,6,[45,57])
t1[-1][0] = 100
print(t1)

# 3.因为元组不可变，所以和修改元素相关的功能都无法使用，其余的功能都可以使用，使用方式和列表相同
tuple1 = (45,5,7)
print(len(tuple1))
print(tuple1.count(5))
print(max(tuple1))
print(min(tuple1))
print(tuple1.index(5))




