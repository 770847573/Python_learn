# 1.id():获取一个对象在内存中的地址
print(id(3434))

# 2.type()
# a.获取一个对象的数据类型,
# 如果是系统类，结果为：<class 类型>
# 如果是自定义类，结果为：<class "__main__.类名">
print(type("fafa"))

# b.比较类型    ********
print(type(20) == type(34.5))
print(type(20) == int)

# c.借助于types模块，获取函数的类型
import  types
print(type(lambda  x:x) == types.LambdaType)
print(type(abs) == types.BuiltinFunctionType)

def show():
    pass
print(type(show) == types.BuiltinFunctionType)

print(type((x for x in range(5))) == types.GeneratorType)

# 3.isinstance() :判断一个对象是否是指定的类型    ********
print(isinstance(10,int))   # 一般结合if语句使用
print(type(10) == int)

# 4.issubclass(类1，类2):判断类1和类2之间是否具有继承关系
class Animal(object):
    pass
class Cat(Animal):
    pass
class SmallCat(Cat):
    pass
print(issubclass(SmallCat,Cat))
print(issubclass(SmallCat,Animal))
print(issubclass(SmallCat,object))