#方式一：__new__
class Person(object):
    __instance = None
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

p1 = Person("Hou",24) #会执行__init__,会进入if判断，给__instance赋值一个对象
p2 = Person("Zhu",24)  #会执行__init__，但不会进入if判断，直接返回__instance，此时如果有参数传进来，则会被__init__改变
print(p1)
print(p2)

print("*"*30)
#方式二：装饰器
def singleton(cls):
    instance = None
    def get_instance(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args,**kwargs)
        return instance
    return get_instance

@singleton
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = Student('Tom',15)#会进入get_intance,也会进入if判断，所以会创建一个对象赋值给instance
s2 = Student('Jerry',5)#会进入get_instance,但是不会进入if，不会创建新的对象，直接返回instance，就算类有参数，也不会改变
print(s1.name,s1.age)
print(s2.name,s2.age)
print(s1)
print(s2)

