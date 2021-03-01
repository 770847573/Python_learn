# 实现方式
# 1.将列表推导式中的[]---->()
list1 = [i ** 2 for i in range(10)]
print(list1)
print(type(list1))   # <class 'list'>
print(list1[1])
print(list1[6])

ge1 = (i ** 2 for i in range(10))
print(ge1)
print(type(ge1))    # <class 'generator'>

# 生成器中的元素使用到谁，则生成谁
# 方式一：next()
# print(next(ge1))
# print(next(ge1))
# print(next(ge1))

# for _ in range(10):
#     print(next(ge1))

# 注意：当一个生成器中的元素全部获取完毕，再次获取，则会报错StopIteration
# print(next(ge1))

# 方式二：for循环
# for num in ge1:
#     print(num)

# 2.函数生成器：函数结合yield实现
# a
def func1():
    return 88   # 函数结束，将88返回
r1 = func1()
print(r1,type(r1))

# b
# 注意1：如果一个函数中出现了yield关键字，将表示生成器，简单理解：调用函数，函数的返回值为一个生成器
def func2():
    yield 88   #
r2 = func2()
print(r2,type(r2))   # <class 'generator'>

# 注意2：一般情况下，yield后面的值会成为生成器的预定义元素
print(next(r2))

# c.
# 如果想要预定义多个元素，则在函数中yield出现多次即可
def func3():
    yield 24
    yield 67
    yield 10
r3 = func3()
print(next(r3))
print(next(r3))
print(next(r3))

# d.
# 如果想要预定义多个元素，则在函数中yield出现多次即可，可以借助于循环实现
def func4():
    for i in range(10):
        yield i ** 2
r4 = func4()
print(r4)
# 从同一个生成器中获取三个元素
print(next(r4))
print(next(r4))
print(next(r4))

print("*" * 30)

# 补充：
# 问题一：带有yield关键字的函数，每调用一次，将生成一个生成器
def func4():
    for i in range(10):
        yield i ** 2
# 分别从三个生成器中获取一个元素
print(next(func4()))
print(next(func4()))
print(next(func4()))

# 问题二：通过循环结合next获取生成器中的所有元素
# 生成器的工作原理：当生成器中的元素全部获取完毕，则代码自动会进入except语句，则结束循环
def func4():
    for i in range(10):
        yield i ** 2
r5 = func4()
while True:
    try:
        print(next(r5))
    except:
        break