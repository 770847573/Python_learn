# 1.多态的概念
# a.
class Animal(object):
    pass
class Cat(Animal):
    pass

# 在继承的前提下，一个子类对象的类型可以是当前类，也可以是父类，也可以是祖先类
c = Cat()
# isinstance(对象，类型)判断对象是否是指定的类型
print(isinstance(c,object))  # True
print(isinstance(c,Animal))  # True
print(isinstance(c,Cat))     # True

a = Animal()
print(isinstance(a,Cat))  # False

# b.
class Animal(object):
    def show(self):
        print("父类")
class Cat(Animal):
    def show(self):
        print("cat")
class Dog(Animal):
    def show(self):
        print("dog")
class Pig(Animal):
    def show(self):
        print("pig")

# 定义a的时候不确定a的类型，所以不能确定a.show()调用的是哪个类中的函数
def func(a):
    a.show()

c = Cat()
d = Dog()
p = Pig()

# 当运行程序的时候，才能确定a的类型
func(c)
func(d)
func(p)

# 2.多态的应用
# 好处：简化代码

# 需求：人喂养动物
class Animal(object):
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("eating")
class Cat(Animal):
    pass
class Dog(Animal):
    pass
class Pig(Animal):
    pass

class Person(object):
    """
    def feed_cat(self,cat):
        cat.eat()
    def feed_dog(self,dog):
        dog.eat()
    def feed_pig(self,pig):
        pig.eat()
    """
    # 定义的时候ani的类型并不确定，只有当函数被调用，传参之后才能确定他的类型
    def feed_animal(self,ani):
        ani.eat()

per = Person()

c = Cat("小白")
d = Dog("旺财")
p = Pig("小黑")

per.feed_animal(c)
per.feed_animal(d)
per.feed_animal(p)
