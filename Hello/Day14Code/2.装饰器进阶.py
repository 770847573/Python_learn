# 1.一个装饰器装饰多个函数
# 使用场景：给多个不同的函数增加同样的新的功能,为了函数参数的匹配，一般在inner中设置不定长参数
def wrapper(func):
    def inner(*args,**kwargs):
        # 调用原函数,一定要注意和原函数的参数匹配
        func(*args,**kwargs)
        # 增加新的功能
        print("new~~~~~")
    return inner
# 注意：同一个装饰器同时装饰多个函数，必须在每个函数的前面使用@xxx进行声明
@wrapper
def show():
    print("show")
@wrapper
def func1(a):
    print(a)
@wrapper
def func2(a,b,c):
    print("%s-%s-%d" % (a,b,c))

show()
func1(4)
func2("aaaa",34,35)

# 练习：书写一个装饰器，将一个指定函数的返回值加100之后返回
def add_hundred(fun):
    def inner(*args,**kwargs):
        # 调用原函数
        r = fun(*args,**kwargs)
        # 增加新的功能
        return r + 100
    return inner
@add_hundred
def add(a,b):
    return a + b
print(add(3,5))

# 练习：书写一个装饰器，可以统计任意一个函数的执行时间
import  time
def get_time(func):
    def inner(*args,**kwargs):
        # 开始时间
        start_time = time.time()
        # 调用原函数
        func(*args,**kwargs)
        # 结束时间
        end_time = time.time()
        return end_time - start_time
    return inner

print("*" * 30)

# 2.多个装饰器装饰同一个函数
# 使用场景：给同一个函数同时增加多个新的功能
def outter1(func1):
    print("1111")
    def inner1(*args,**kwargs):
        func1(*args,**kwargs)   # 调用的是inner2
        print("第一个装饰器~~~~~111")
    return inner1
def outter2(func2):
    print("2222")
    def inner2(*args,**kwargs):
        func2(*args,**kwargs)    # 调用的是inner3
        print("第二个装饰器~~~~~222")
    return inner2
def outter3(func3):
    print("3333")
    def inner3(*args,**kwargs):
        func3(*args,**kwargs)    # 调用的是show原函数
        print("第三个装饰器~~~~~333")
    return inner3
@outter1
@outter2
@outter3
def show():
    print("show函数被调用了~~~~~")

show()   # 调用的是inner1()

"""
工作原理：
传参：就近原则【从下往上】
    @outter1
    @outter2
    @outter3
    
    show原---》func3      show----》inner3
    show【inner3】----》func2      show-----》inner2
    show【inner2】----》func1      show------》inner1

执行：按照传参的顺序倒着执行
"""

print("*" * 30)

# 练习
def outter1(func1):
    print("1111")
    def inner1(*args,**kwargs):
        func1(*args,**kwargs)    # inner3
        print("第一个装饰器~~~~~111")
    return inner1
def outter2(func2):
    print("2222")
    def inner2(*args,**kwargs):
        func2(*args,**kwargs)     # show
        print("第二个装饰器~~~~~222")
    return inner2
def outter3(func3):
    print("3333")
    def inner3(*args,**kwargs):
        print("第三个装饰器~~~~~333")
        func3(*args,**kwargs)        # inner2
    return inner3
@outter1
@outter3
@outter2
def show():
    print("show函数被调用了~~~~~")
show()

"""
2 3 1
3 show 2 1
"""
