# 1.自定义函数
class Animal(object):
    # func实现的是动物的运动方式：跑，飞，游
    def func(self):
        print("跑")

class Cat(Animal):
    pass
class Dog(Animal):
    pass
# 当父类中实现的函数满足不了子类的使用，则需要在子类中进行 函数的重写
# 注意：重写只需要在子类中定义一个和父类重名的函数即可，建议函数的声明和父类中的声明尽量相同
class Bird(Animal):
    def func(self):
        print("飞")
class Fish(Animal):
    def func(self):
        print("游")
b = Bird()


# 2.系统函数
# __str__和__repr__

# a.直接打印一个对象，默认结果是对象的地址
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"姓名：{self.name},年龄：{self.age}")

p = Person("张三",18)
print(p)    # <__main__.Person object at 0x000001BE1AB612E8>
print(p.__str__())  # <__main__.Person object at 0x000001BE1AB612E8>
# __str__是父类object中的一个函数，默认会被子类直接继承，__str__默认返回的是当前对象的地址

print("*" * 30)

# b.当打印一个对象的时候，希望打印的是该对象的属性值
class Person1(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"姓名：{self.name},年龄：{self.age}")

    # 当父类中函数的实现满足不了子类的需求，则在子类中重写
    def __str__(self):
        # 注意：重写__str__的时候，返回值一定是str，TypeError: __str__ returned non-string (type NoneType)
        return f"姓名：{self.name},年龄：{self.age}"

    # 如果将对象添加到列表中，直接打印列表，希望列表中的元素也是和对象相关的属性，则需要重写__repr__
    # def __repr__(self):
    #     return f"姓名：{self.name},年龄：{self.age}"

    # 简写
    __repr__ = __str__

p1 = Person1("张三",18)
print(p1)
print(p1.__str__())

p2 = Person1("李四",18)
print(p2)

per_list = [p1,p2]
for per in per_list:
    print(per)

print(per_list)  # [姓名：张三,年龄：18,姓名：李四,年龄：18]