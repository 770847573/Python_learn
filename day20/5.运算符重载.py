# 1.__add__()：和+有关
# a.+:使用+号在计算机的底层实际上调用的是__add__函数，但是，+号只针对指定的数据类型有效
print(3 + 6)     # int + int = int
print(3 + 4.6)   # float + float = float
print("hello" + "python")  # str + str = str
print([2,4] + [34,5])  # list + list = list
print((2,4) + (34,5))  # tuple + tuple = tuple

# __dict__
print("hello".__add__("Python"))
print([2,4].__add__([34.5]))

# print(3 + "abc")

# b.需求：使用+使得两个自定义的对象相加
class Person(object):
    def __init__(self,age):
        self.age = age

p1 = Person(10)
p2 = Person(6)
print(p1)
print(p2)
# print(p1 + p2)   # TypeError: unsupported operand type(s) for +: 'Person' and 'Person'
# print(p1.__add__(p2))

print("*" * 30)

class Person1(object):
    def __init__(self,age):
        self.age = age
    def __add__(self, other):
        # self表示当前对象，other表示其他对象
          return Person1(self.age + other.age)
    def __str__(self):
        return str(self.age)
    __repr__ = __str__

p1 = Person1(10)
p2 = Person1(6)
print(p1)
print(p2)
print(type(p1))
print(type(p2))
# print(p1 + p2)   # Person + Person = int 【Person】
# print(p1.__add__(p2))

p3 = p1 + p2
print(type(p3))
p4 = p1.__add__(p2)
print(type(p4))

print(p3)
print(p4)

# 2.下面的函数对应是关系运算符
# __lt__：less than小于   <
# __gt__:greater than大于  >
# __le__：less equal 小于等于  <=
# __ge__：greater than  大于等于  >=
# __eq__：equal 等于   ==
# __ne__:not equal 不等于  !=
# print(str.__dict__)

# a.以上函数只能应用在指定的数据类型之间
print("abc" < "xyz")
print("abc".__lt__("xyz"))

# b.
class Person2(object):
    def __init__(self,age):
        self.age = age

    def __gt__(self, other):
        # self和other两个对象age属性进行比较
        if self.age > other.age:
            return True
        elif self.age < other.age:
            return False
        else:
            return 0

    def __lt__(self, other):
        # self和other两个对象age属性进行比较
        if self.age > other.age:
            return False
        elif self.age < other.age:
            return True
        else:
            return 0

    def __eq__(self, other):
        # self和other两个对象age属性进行比较
        if self.age == other.age:
            return True

p1 = Person2(34)
p2 = Person2(10)
# 需求：比较两个人的年龄大小
print(p1 > p2)  # TypeError: '>' not supported between instances of 'Person2' and 'Person2'
print(p1.__gt__(p2))

print(p1 < p2)

print(p1 == p2)

# 注意：区分重写和重载
"""
【面试题】简述重写和重载的区别
重写：override,在继承的前提下，在子类中重新实现父类中的函数
重载：overload,一般是为了让一些常用的运算符支持执行的数据类型，如：__add__(+),__lt__(<)。。。。。，
     在自定义的类中重新实现指定运算符对应的函数
"""