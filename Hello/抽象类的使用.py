import abc
class MyClass(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def mymethod(self):
        pass
class My1(MyClass):
    def mymethod(self):
        print('Do something!!!')
my = My1()#如果一个类继承自抽象类，而未实现抽象方法，仍然是一个抽象类
my.mymethod()
#my1 = MyClass()  TypeError: Can't instantiate abstract class MyClass with abstract methods mymethod