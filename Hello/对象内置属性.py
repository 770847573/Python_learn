#1.__slots__:限制对象属性的动态绑定

#2.__doc__:document表示类的描述信息，获取类中的文档注释
class Check(object):
    """
    该类用于数据的校验
    （这是Check的文档注释）
    """
    pass
print(Check.__doc__)

#3.__dict__:获取类或对象的所有信息【属性、函数】****,
class Person(object):
    def __init__(self,name,age):
        self.name= name
        self.age = age
    def show(self):
        pass
    @classmethod
    def func(cls):
        cls.pp = 1
    @staticmethod
    def staticfun():
        pass
print(Person.__dict__)
p = Person("老王",55)
print(p.__dict__)
#应用场景：查询系统类的属性和函数
print(str.__dict__)

#3.__moudle__:获取某个对象属于哪个模块，如果是当前模块则返回__main__，如果是其他模块，则返回模块名
print(p.__module__)

#4.__class__:类似于type(),获取对象的数据类型
print(p.__class__)
print(type(p))