# 1. NameError 使用一个还未被赋予对象的变量
# print(a) # NameError: name 'a' is not defined

# 2. ValueError 传入一个调用者不期望的值，即使值的类型是正确的
# num = int(input("请输入一个数字")) # >>as >> ValueError: invalid literal for int() with base 10: 'as'

# 3. TypeError 传入对象类型与要求的不符合
# print(1 + "as") # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print("as" + 1) # TypeError: can only concatenate str (not "int") to str

# 4. IndexError IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]

# 5. AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
# "sds".append("s")  # AttributeError: 'str' object has no attribute 'append'
class Person(object):
    __slots__ = ("name",)
p = Person()
p.age # AttributeError: 'Person' object has no attribute 'age'




# 6.UnBoundLocalError: 试图访问一个当前作用域未设置的变量，通常在其他作用域存在同名变量
# 情况一：在嵌套函数局部作用域中修改了外层函数作用域的变量
def singleton(cls):
    instance = None
    def inner():
        nonlocal instance
        if not instance:
            instance = cls()
        return instance
    return inner

@singleton
class Animal(object):
    def __init__(self):
        print("pig")
a = Animal()
# 情况二：
b = 1
def func1():
    global b
    b =2
func1()
print(b) # 没加global b 之前打印1,加了之后打印2

# SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）