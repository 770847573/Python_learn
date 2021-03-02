#id():获取一个对象在内存中的地址
print(id(454))

#2.type()
#a.获取一个对象的数据类型
#如果是系统类，结果是<class,类名>
print(type(4))
#如果是自定义类型，结果是<class,__main__,类名>

#b.比较类型  *****
print(type(20) == int)

#c.types模块来判定对象的数据类型
import types
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(4))) == types.GeneratorType)

#3.isinstance():判断对象是否是指定类型
print(isinstance(10,int))
print("*" * 30)
#4.issubclass():判断两个类是否是继承关系
class Person(object):
    pass
class Father(Person):
    pass
class Son(Father):
    pass
print(issubclass(Son,Father))
print(issubclass(Son,object))
print(issubclass(Son,Person))

