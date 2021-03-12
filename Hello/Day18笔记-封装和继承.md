### 面向对象回顾

> ```Python
> # 1.概念
> """
> 面向对象
> 类
> 对象
> """
> 
> # 2.类以及类中成员的定义
> class Person():
>     # 限制属性的动态绑定
>     __slots__ = ("name","age")
> 
>     # 类属性【类的字段】
>     place = "地球"
>     # 构造函数
>     def __init__(self,name,age):
>         # 实例属性/对象属性【对象的字段】
>         self.name = name
>         self.age = age
> 
>     # 实例函数
>     def show(self):
>         print(f"姓名：{self.name},年龄：{self.age}")
> 
>     # 析构函数
>     def __del__(self):
>         pass
> 
> # 3.对象的创建以及类中成员的访问
> 
> # 类的实例化【对象的创建】
> p = Person("李正正",18)
> 
> # 类中成员的访问
> print(Person.place)
> print(p.place)
> 
> print(p.name,p.age)
> 
> p.show()
> ```

> 【面试题】面向对象语言的特征是什么？是什么？怎么使用？有什么作用？

### 一、封装

#### 1.概念

> 广义的封装：函数的定义和类的提取，都是封装的体现
>
> 狭义的封装:在面向对象编程中，一个类的某些属性，在使用的过程中，如果不希望被外界【直接】访问，就可以将该属性封装【将不希望被外界直接访问的属性私有化private，该属性只能被当前类持有，此时可以给外界暴露一个访问的函数即可】
>
> 封装的本质：就是属性私有化的过程
>
> 封装的好处：提高了数据的安全性，提高了数据的复用性
>
> 举例：插排，不需要关心属性在类的内部被做了什么样的操作，只需要关心可以将值传进去，也可以将值获取出来
>

#### 2.私有属性

##### 2.1基本使用

> 公开属性【public】：可以在类以外的任何地方直接访问的属性
>
> 私有属性【private】：只能在当前类的内部被直接访问的属性
>
> ```Python
> # 1.属性未被私有化
> class Animal1():
>     def __init__(self,name,age):
>         # 公开属性
>         self.name = name
>         self.age = age
>     def show(self):
>         print(self.name,self.age)
> a1 = Animal1("大黄",4)
> print(a1.name,a1.age)
> a1.name = "旺财"
> a1.age = 2
> print(a1.name,a1.age)
> 
> print("*" * 30)
> 
> # 2.属性被私有化
> class Animal2():
>     num1 = 10
>     __num2 = 20
>     def __init__(self,name,age):
>         # 私有属性:在属性名的前面添加两个下划线
>         self.__name = name
>         self.__age = age
>     def show(self):
>         print(self.__name,self.__age)
> 
> a2 = Animal2("大黄",4)
> # 注意：如果一个属性【类属性和实例属性】被私有化，则在类的外面无法通过  对象.属性  的方式直接访问
> # print(a2.name,a2.age)   # AttributeError: 'Animal2' object has no attribute 'name'
> # print(a2.__name,a2.__age) # AttributeError: 'Animal2' object has no attribute '__name'
> 
> a2.show()
> 
> # 扩展：私有属性的工作原理
> # 私有属性在底层的存储方式：_类名__属性名
> """
> 一个属性一旦被私有化，在底层形成对应的属性名，为_类名__属性名,但是不建议使用
> 原因：Python是跨平台的，私有化属性在不同的操作系统中会形成不同的形式
> """
> # print("访问私有属性",a2._Animal2__name,a2._Animal2__age)
> 
> # 注意：类属性和实例属性相同，只要在变量名前面他添加两个下划线，则都表示被私有化
> print(a2.num1)
> # print(a2.__num2)   # AttributeError: 'Animal2' object has no attribute '__num2'
> 
> print("*" * 30)
> 
> # 3.暴露给外界一个访问的函数
> class Animal3():
>     def __init__(self,name,age):
>         # 私有属性:在属性名的前面添加两个下划线
>         self.__name = name
>         self.__age = age
> 
>     # 定义实例函数，该函数的作用可以给私有化属性进行赋值，也可以直接获取值
>     # 获取值
>     def get_name(self):
>         return self.__name
>     # 修改值
>     def set_name(self,name):
>         self.__name = name
> 
>     def get_age(self):
>         return self.__age
>     def set_age(self,age):
>         # 数据的校验
>         if age < 0:
>             age = -age
>         self.__age = age
> 
> a3 = Animal3("大黄",4)
> print(a3.get_name())    # 大黄
> a3.set_name("旺财")
> print(a3.get_name())   # 旺财
> 
> print(a3.get_age())
> a3.set_age(-18)
> print(a3.get_age())
> 
> 
> print("*" * 30)
> 
> # 4.使用装饰器@property实现私有化属性的访问
> class Animal4():
>     def __init__(self,name,age):
>         # 私有属性:在属性名的前面添加两个下划线
>         self.__name = name
>         self.__age = age
> 
>     """
>     @property修饰的函数相当于get_xxx,用于获取私有属性的值
>     @xxx.setter修饰的函数相当于set_xxx,用于修改私有属性的值
>     
>     在Python中，为了和私有属性进行匹配，对于命名有建议：
>         a.被@property修饰的函数名命名为私有属性的变量名，如：__name---->name
>         b.@xxx.setter中的xxx必须和被@property修饰的函数名同名
>         c.被@xxx.setter修饰的函数的函数名也命名为私有属性的变量名，如：__name---->name
>     """
>     # 获取值
>     @property     # @property是将一个函数转化为属性使用
>     def name(self):
>         return self.__name
>     # 修改值
>     @name.setter
>     def name(self,name):
>         self.__name = name
> 
>     @property
>     def age(self):
>         return self.__age
>     @age.setter
>     def age(self,age):
>         if age < 0:
>             age = -age
>         self.__age = age
> 
> a4 = Animal4("大黄",4)
> print(a4.name)    # 此处访问的是被@property修饰的函数
> a4.name = "旺财"   # 此处访问的是被@name.setter修饰的函数
> print(a4.name)   # 旺财
> 
> print(a4.age)
> a4.age = -6
> print(a4.age)
> 
> # 面试题1:阅读下面的代码，写出代码运行的结果
> # 结论：@property可以单独使用，并不一定非要和@xxx.setter使用
> class Person():
>     @property
>     def show(self):
>         return 10
> p = Person()
> # print(p.show())   # TypeError: 'str' object is not callable
> print(p.show)
> ```

##### 2.2不同形式的属性

> ```Python
> 
> # 面试题2：解释下面不同书写形式的属性的含义
> """
> a:普通属性/公开属性，在类的内部或者外部都可以直接访问
> _a:一般被称为保护属性，在类的内部或者外部都可以直接访问，但是，一般不建议使用
> __a:私有属性，只能在类的内部被直接访问，在类的外部不可以直接访问，在类的外部一般借助于函数访问
> __a__:自定义的函数不建议使用该种命名方式，一般体现为系统属性或者系统函数的命名
> """
> 
> class Animal():
>     def __init__(self,name,age,height,score):
>         self.name = name    # 常用
>         self._age = age
>         self.__height = height   # 常用
>         self.__score__ = score
> 
> a = Animal("aaa",4,173,99)
> print(a.name)
> print(a._age)
> print(a.__score__)
> ```

#### 3.私有函数

> ```Python
> # 1.函数未被私有化
> class Person():
>     def func1(self):
>         print("11111")
> 
>         # 注意：在类的内部，实例函数之间相互调用，必须通过  self.函数()
>         self.func2()
> 
>     def func2(self):
>         print("2222")
> p1 = Person()
> p1.func1()
> p1.func2()
> 
> # 2.函数被私有化
> class Person():
>     # 公开函数
>     def func1(self):
>         print("11111")
> 
>         # 注意：在类的内部，实例函数之间相互调用，必须通过  self.函数()
>         self.__func2()
> 
>     # 私有函数
>     def __func2(self):
>         print("2222")
> 
> p1 = Person()
> p1.func1()
> # p1.__func2()
> 
> ```

> 封装的作用：
>
> ​	a.提高了数据的安全性
>
> ​	b.提高了数据的复用性

### 二、继承

#### 1.概念

> 如果两个或者两个以上的类具有相同的属性和方法，我们可以抽取一个类出来，在抽取出来的类中声明各个类公共的部分
>
> ​	被抽取出来的类——父类【father class】  超类【super class】  基类【base class】
>
> ​	两个或两个以上的类——子类  派生类
>
> ​	他们之间的关系——子类 继承自 父类   或者   父类  派生了 子类

#### 2.单继承

##### 2.1基本使用

> 简单来说，一个子类只能有一个父类，被称为单继承
>
> 语法：
>
> class 子类类名(父类类名):
>
> ​	类体
>
> 注意：object是Python中所有类的根类
>
> 默认情况下，如果一个类没有指明继承的父类，则默认继承自object
>
> ```Python
> # 父类
> class Person(object):
>     # 公共的特征
>     def __init__(self, name, age):
>         self.name = name
>         self.age = age
>     # 公共的行为
>     def eat(self):
>         print("eating")
> 
> # 子类
> # 需要继承父类中的属性和函数，同时也具有特有的属性和函数
> class Student(Person):
>     def __init__(self,name,age,subject):
>         Person.__init__(self,name,age)
>         self.subject = subject
>     def study(self):
>         print("studing")
> # 需要继承父类中的属性和函数
> class Doctor(Person):
>     def __init__(self, name, age):
>         # 在子类的构造函数调用父类中的构造函数【目的是为了定义需要的实例属性】
>         # 方式一：super(当前类，self).__init__(参数列表)
>         # super(Doctor,self).__init__(name,age)
>         # 方式二：super().__init__(参数列表)
>         # super().__init__(name,age)
>         # 方式三：父类类名.__init__(self,参数列表)
>         Person.__init__(self,name,age)
> 
> # 需要继承父类中的函数
> class Teacher(Person):
>     def __init__(self,num):
>         self.num = num
> # 需要继承父类中的属性和函数
> class Worker(Person):
>     pass
> 
> # 1.当子类中未定义构造函数，则创建子类对象的时候会默认调用父类的构造函数,同时继承了父类中的属性和未被私有化的函数
> w = Worker("王师傅",30)
> print(w.name,w.age)
> w.eat()
> 
> # 2.当子类中定义了构造函数，但是未定义父类中的实例属性
> # 特点：默认调用子类中的构造函数
> t = Teacher(20)
> print(t.num)
> # print(t.name,t.age)   # AttributeError: 'Teacher' object has no attribute 'name'
> t.eat()
> 
> # 3.当子类中定义了构造函数，而且定义了父类中的实例属性
> # 特点：需要在子类的构造函数中调用父类的构造函数
> d = Doctor("张医生",19)
> print(d.name,d.age)
> 
> # 4.
> s = Student("小明",18,"语文")
> print(s.subject)
> print(s.name,s.age)
> ```

##### 2.2继承中的slots

> ```Python
> class Animal(object):
>     __slots__ = ("name","age")
> 
> class Cat(Animal):
>     pass
> 
> a = Animal()
> # a.num = 23
> 
> c = Cat()
> c.num = 10
> print(c.num)
> 
> 
> # 结论：在父类中定义的属性的限制绑定，无法继承到子类中，如果子类需要同样的限制绑定，则需要重新定义
> ```

##### 2.3继承中的类属性

> ```Python
> # 【面试题】
> class MyClass1(object):
>   x = 10
> class MyClass2(MyClass1):
>   pass
> class MyClass3(MyClass1):
>   pass
> 
> print(MyClass1.x,MyClass2.x,MyClass3.x)   # 10 10 10
> # 修改子类值
> MyClass2.x = 20
> print(MyClass1.x,MyClass2.x,MyClass3.x)   # 10 20 10
> # 修改父类值
> MyClass1.x = 30
> print(MyClass1.x,MyClass2.x,MyClass3.x)   # 30 20 30   ******
> ```
