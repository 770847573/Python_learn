class Person(object):
    # 属性的限制绑定
    __slots__ = ("name","age")
    # 类属性
    num = 0
    # 构造函数
    def __init__(self,name,age):
        # 实例属性
        self.name = name
        self.age = age

    # 实例函数：形参列表的第一个参数为self，代表当前对象，调用函数的时候不需要手动传参
    def show(self):
        print("实例函数：" + "showing")

    # 类函数:被@classmethod装饰器修饰的函数被称为类函数，形参列表的第一个参数为cls，代表当前类，调用函数的时候也不需要手动传参
    @classmethod
    def check(cls):
        print("类函数：" + "checking")

        # 在类函数中可以创建当前类的对象,使用cls相当于使用Person
        per = cls("张三",18)   # Person()
        per.show()

    # 静态函数:被@staticmethod装饰器修饰的函数被称为静态函数，对形参没有任何要求
    @staticmethod
    def func():
        print("静态函数：" + "func~~~~~~")

# 调用方式不同
# 类函数和静态函数都可以通过类名或者对象调用
Person.check()
Person.func()

# 实例函数只能通过对象调用
p = Person("abc",19)
p.show()

"""
【面试题】简述实例函数，类函数和静态函数之间的区别
相同点：
        本质都是函数，所以默认参数，关键字参数，不定长参数都可以使用，也可以设置返回值
不同点：
    a.是否有系统装饰器
    b.参数列表不同
    c.调用方式不同
    d.使用场景不同：
        如果需要在函数的内部创建当前类的对象，则使用类函数
        如果需要封装一个工具类，为了简化函数的调用，则使用类函数或者静态函数
        如果在函数内部需要获取实例属性，则使用实例函数
"""

# 1.写一个计算器工具类Calculator，可以进行加、减、乘、除计算
class Calculator(object):
    @staticmethod
    def add(num1,num2):
        return num1 + num2

    @staticmethod
    def sub(num1, num2):
        return num1 - num2

    @staticmethod
    def mul(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return num1 / num2

Calculator.add(4,5)