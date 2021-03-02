"""
2.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数
思路提示：要找到对象创建的方法 在该方法中统计对象的个数
"""
# 类字段：类属性
# 对象字段：实例属性/对象属性

# 方式一:__new__
class Person(object):
    # 类属性【当没有对象存在的时候，需要通过类名访问，】
    per_count = 0
    def __new__(cls, *args, **kwargs):
        # cls代表的就是当前类
        # print("new~~~~~")
        cls.per_count += 1
        # return super(Person,cls).__new__(cls)
        return object.__new__(cls)

p1 = Person()
p2 = Person()
print(Person.per_count)
print(p1.per_count)
p3 = Person()
p4 = Person()
p5 = Person()
p6 = Person()
print(Person.per_count)

print("*" * 30)

# 方式二：__init__
"""
class Person1(object):
    per_count = 0    # 类属性
    def __init__(self):
        self.per_count += 1   # 实例属性
p1 = Person1()
p2 = Person1()
p3 = Person1()
p4 = Person1()
print(Person1.per_count)
"""

# 优化
"""
class Person1(object):
    per_count = 0    # 类属性
    def __init__(self):
        Person1.per_count += 1   # 实例属性
p1 = Person1()
p2 = Person1()
p3 = Person1()
p4 = Person1()
print(Person1.per_count)
"""

# 再次优化
class Person1(object):
    per_count = 0    # 类属性
    @classmethod   # 被@classmethod修饰的函数被称为类函数
    def __init__(cls):
        cls.per_count += 1  # 实例属性
        # 类属性
        cls.name = "abc"
        cls.age = 0
p1 = Person1()
p2 = Person1()
p3 = Person1()
p4 = Person1()
print(Person1.per_count)

