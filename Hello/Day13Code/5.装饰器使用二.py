# 1.需求：书写一个装饰器，对年龄进行校验
def get_age(age):
    print("年龄：%d" % (age))

def check_age(func):
    def inner(n):
        # 新的功能：校验传进来的年龄是否是负数，如果是负数，则改为相反数
        if n < 0:
            n = -n
        # 调用原函数
        func(n)
    return inner

f = check_age(get_age)
f(-6)

# 使用场景：如果原函数有参数，而且在装饰器中需要对原函数中的参数做出操作，则在装饰器的内部函数中设置参数

print("*" * 30)

# 2.使用  @xxx 简化装饰器的使用
# 注意1：@xxx表示将一个指定的装饰器直接作用于需要装饰的函数，xxx表示装饰器的名称
# 注意2：使用@xxx装饰函数，则装饰器必须先存在，然后才能使用
def check_age1(func):
    print("外部函数被执行了~~~~~~")
    def inner1(n):
        print("内部函数被执行了~~~~~")
        if n < 0:
            n = -n
        # 调用原函数
        func(n)
    return inner1

# @xxx会调用装饰器的外部函数，同时将外部函数的返回值返回，原函数的函数名指向了内部函数的引用
@check_age1     # @xxx的作用相当于 check_age(get_age)
def get_age1(age):
    print("年龄：%d" % (age))

# get_age1(-18)调用的将不再是原函数，而是装饰器的内部函数
get_age1(-18)

"""
工作原理：
假设：
    原函数：a
    装饰器：wrapper(func)
    
@wrapper：func = a原    a------》inner
a() : inner()
"""


