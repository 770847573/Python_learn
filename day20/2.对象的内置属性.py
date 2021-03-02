# 1.__slots__:限制对象属性的动态绑定

# 2.__doc__:表示类的描述信息，获取类中的文档注释【直接书写在类中的多行注释】
class Check(object):
    """
    该类用于数据的校验
    """
    # 367252
    def show(self):
        pass
print(Check.__doc__)


# 3.__dict__：获取类或者对象的所有信息【属性和函数】,返回一个字典     *******
class Person(object):
    num = 10
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        pass

print(Person.__dict__)   # 获取类属性，实例函数，类方法和静态方法
p = Person("aaa",18)
print(p.__dict__)  # 获取实例属性

# 应用场景：查询系统类型的函数或者属性
print(str.__dict__)
print(list.__dict__)

# 4.__module__:获取指定对象属于哪个模块，如果是当前模块，则返回__main__,如果是其他模块，则返回模块名
print(p.__module__)

# 5.__class__:类似于type（xxx）,获取指定对象的数据类型
print(type(10))

print(type(p))
print(p.__class__)

print(type("hello"))
print("hello".__class__)
