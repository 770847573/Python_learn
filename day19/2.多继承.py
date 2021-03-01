# 1.在子类中未定义构造函数
class Father1(object):
    def __init__(self,n1):
        self.n1 = n1

class Father2(object):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

class Child(Father2,Father1):
    pass

# 创建子类的对象
# 注意：如果一个子类有多个父类，子类未定义构造函数，则创建子类对象的时候默认调用父类列表中第一个父类中的构造函数
c = Child(3,4)

# 2.在子类中定义构造函数
class Father1(object):
    def __init__(self,n1):
        self.n1 = n1
    def show(self):
        print("11111")
class Father2(object):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def show(self):
        print("2222")

class Child(Father2,Father1):
    def __init__(self,n1,num1,num2,kind):
        # 注意：在多继承中，在子类构造函数中调用父类的构造函数，只能使用 父类类名.__init__(self,参数列表)
        Father1.__init__(self,n1)
        Father2.__init__(self,num1,num2)
        self.kind = kind

# 注意：如果子类中定义了构造函数，创建子类对象调用的是子类自身的构造函数
c1 = Child(3,534,5,23)
# 注意：如果多个父类中出现重名的函数，子类对象默认调用的是父类列表中第一个父类中的函数
c1.show()

print("*" * 30)

# 3.在子类的实例函数中也可以调用父类中重名的实例函数
class Father1(object):
    def __init__(self,n1):
        self.n1 = n1
    def show(self):
        print("11111")
class Father2(object):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def show(self):
        print("2222")
class Child(Father2,Father1):
    def __init__(self,n1,num1,num2,kind):
        Father1.__init__(self,n1)
        Father2.__init__(self,num1,num2)
        self.kind = kind
    def show(self):
        # 在子类的实例函数中调用父类中重名的实例函数，和构造函数的调用相似
        super().show()   # super和父类有关，self和当前对象有关
        print("子类")

c2 = Child(3,534,5,23)
c2.show()