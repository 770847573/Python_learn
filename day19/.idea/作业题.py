#创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数，思路提示：要找到对象创建的方法 在该方法中统计对象的个数

class Person1(object):
    __object_num = 0
    def __init__(self):
       print("对象初始化")
    def __new__(cls, *args, **kwargs):
        print("创建了一个对象")
        cls.__object_num += 1
    @classmethod
    def get_object_num(cls):
        return cls.__object_num

p1 = Person1()
p2 = Person1()
print(Person1.get_object_num())


#2.
"""
3.小明爱跑步，爱吃东西。

1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤

**从上面的语境中提取对象的属性，方法 ，进而声明成类 完成需求对应的操作**
"""
class Person(object):
    def __init__(self,name,weight):
        self.weight = weight
        self.name = name
    def run(self):
        self.weight -=0.5
        print(f"{self.name}的体重现在为{self.weight}")
    def eat(self):
        self.weight += 1
        print(f"{self.name}的体重现在为{self.weight}")
    def __str__(self):
        return fr"姓名：{self.name},体重：{self.weight}"

person1 = Person("小明",70)
person1.run()
person1.eat()
print(person1)

#3.

"""
图书管理系统的编写
图书类Book：
属性：书名name	作者author	是否借出isborrow   书籍位置index 
**注意：书籍的位置不能重复**

图书管理系统BookManager类
存放图书的工具使用列表
方法：
	1.添加图书
	2.借书 （根据图书名字借书）要检验图书是否存在、图书是否已经借出			
	3.还书
	4.查询书籍 （根据名字查询）

"""
class Book(object):
    book_list = []
    def __init__(self,name,author,index):
        self.name = name
        self.author = author
        self.isborrow = False#默认为False
        self.index = index

class BookManager(object):
    def add_book(self,book):
        index_list = [ book.index for book in Book.book_list]
        whlie True:

            Book.book_list.append()
