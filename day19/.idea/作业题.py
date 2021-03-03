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

    def __init__(self,name,author,index):
        self.name = name
        self.author = author
        self.isborrow = False#默认为False
        self.index = index
    def __str__(self):
        return f"书名：《{self.name}》,作者：{self.author}"
    __repr__ = __str__
class BookManager(object):
    book_list = []
    def start(self):
        book1 = Book('Python','tom','a1')
        book2 = Book('Java','Jerry','a2')
        self.book_list.append(book1)
        self.book_list.append(book2)
        print(self.book_list)
    def menu(self):
        self.start()
        print("欢迎进入图书馆管理系统")
        while True:
            print("""
                                   图书管理系统
                               1. 添加图书
                               2. 借书 (根据图书名借书)
                               3. 还书
                               4. 查询数据(根据图书名查询)
                               5. 退出

                        """)
            choice = input("请输入相应的数字办理业务")
            if choice == '1':
                self.add_book()
            if choice == '2':
                self.borrow_book()
            if choice == '3':
                self.back_book()
            if choice == '4':
                name = input("请输入图书名字")
                isexist = self.check_book(name)
                if isexist != None:
                    print(f"{name}书籍存在")
                else:
                    print(f"{name}书籍不存在")
            if choice == '5':
                break

    def add_book(self):
        name = input("请输入图书名字：")
        author = input("请输入作者：")
        index_list = [ book.index for book in self.book_list]
        while True:
            index = input("请输入存放位置：")
            if index not in index_list:
                break
            else:
                print("该位置已有图书，请重新输入位置")
        book = Book(name, author, index)
        self.book_list.append(book)
        print(f"{name}添加完成")

    def borrow_book(self):
        name = input("请输入想借的图书名字：")

        book = self.check_book(name)
        if book != None:
                if book.isborrow == False:
                   book.isborrow = True
                   print(f"{name}已借阅成功")
                else:
                    print(f"{name}图书已借出")
        else:
                print(f"{name}图书不存在")

    def back_book(self):
        name = input("请输入归还书籍名字：")
        book = self.check_book(name)
        if book != None:
            book.isborrow = False
            print(f"{name}已经成功归还")
        else:
            print(f"{name}这本书不是这里的")


    def check_book(self,name):
        for book in self.book_list:
            if book.name == name:
                print(book.isborrow)
                return book
        return None

manager = BookManager()
manager.menu()