### **一、单选题**

**关于面向过程和面向对象，下列说法错误的是（B）。**

```
A. 面向过程和面向对象都是解决问题的一种思路

B. 面向过程是基于面向对象的

C. 面向过程强调的是解决问题的步骤

D. 面向对象强调的是解决问题的对象
```

**2. 关于类和对象的关系，下列描述正确的是（D）。**

```
A. 类和面向对象的核心

B. 类是现实中事物的个体

C. 对象是根据类创建的，并且一个类只能对应一个对象

D. 对象描述的是现实的个体，它是类的实例
```

**3.构造方法的作用是（C）。**

```
A. 一般成员方法 B. 类的初始化

C.对象的初始化 D.对象的建立
```

**4. 构造方法是类的一个特殊方法，Python中它的名称为（C）。**

```A. 与类同名 B. _construct C. _init_ D. init```

**5. Python类中包含一个特殊的变量（A），它表示当前对象自身，可以访问类的成员**

```
A. self B. me C.this D.与类同名
```

**6. 下列选项中，符合类的命名规范的是（A）。**

```
A. HolidayResort B. Holiday Resort C. hoildayResort D.hoilidayresort
```

**7. Python中用于释放类占用资源的方法是（B）。**

```
A. __init__ B. __del__ C. _del D. delete
```

### **二、判断题**

```
面向对象是基于面向过程的。（F）

通过类可以创建对象，有且只有一个对象实例。（F）

方法和函数的格式是完全一样的。（T）

创建类的对象时，系统会自动调用构造方法进行初始化。（T）

创建完对象后，其属性的初始值是固定的，外界无法进行修改。（F）

使用del语句删除对象，可以手动释放它所占用的资源。（F）
```

### **三、填空题**

```
1.在Python中，可以使用___class________关键字来声明一个类。
2.面向对象需要把问题划分多个独立的________对象___，然后调用其方法解决问题。
3.类的方法中必须有一个____cls_____参数，位于参数列表的开头。
4.Python提供了名称为_____(__init__)____的构造方法，实现让类的对象完成初始化。
5.如果想修改属性的默认值，可以在构造方法中使用____self_______设置。
```

### **四、简答题**

请简述self在类中的意义。

```
用于接受调用方法的当前类的对象， 哪个对象调用就表示对应的对象
```

简述封装、继承和多态的含义和作用

```
封装：将不希望被外界访问的属性私有化，在定义属性的时候在属性的前面添加两个下划线，
      为了保证数据的安全性，提高了数据的复用性，
      封装是定义类的准则【根据多个对象的特点，将相同的属性和行为抽取出来一个类，还可以进行属性的私有化】
继承：将多个相似的类中的共同的属性或者函数提取出来，形成一个父类，
      子类将会继承父类中未被私有化的属性和函数，可以提高代码的可扩展性，可复用性，可维护性
      继承是设计类的技巧【父类和子类，主要为了代码的重用】
多态：在继承的前提下，当代码运行的时候，根据传入的对象确定是哪个类，确定需要调用哪个函数
      多态是调用函数的技巧【不同的子类可能调用不同的函数，产生不同的执行结果，
      可以增加代码的灵活度，不会影响到类的内部设计】
```

请简书构造方法和析构方法的作用。

```
构造函数：创建对象的时候被自动调用的函数,创建对象并对对象做一些属性的初始化
析构函数：当对象被销毁的时候被自动调用的函数
```

### 五、编程题

1.写一个计算器工具类Calculator，可以进行加、减、乘、除计算

```python
"""
写一个计算器类Calculator，可以进行加、减、乘、除计算
分析：在这个类中 只有方法 没有属性，而且方法中操作的未知项与类也无关
    所以这些方法设置为静态方法即可
"""
class Calculator(object):
    @staticmethod
    def add(x, y):
        # 求和
        return x + y
    @staticmethod
    def sub(x, y):
        # 求差
        return x - y
    @staticmethod
    def mul(x, y):
        # 求乘
        return x * y
    @staticmethod
    def div(x, y):
        # 除
        return x / y
if __name__ == '__main__':
    value = Calculator.add(17, 28)
    print("求和：", value)
```

2.创建一个Person类，添加一个类字段用来统计Perosn类的对象的个数

思路提示：要找到对象创建的方法 在该方法中统计对象的个数

```Python
class Person(object):
    # 属性私有化 在变量前添加两个下划线
    __person_count = 0
    def __new__(cls, *args, **kwargs):
        print("对象被创建")
        # 对象创建一次 就调用这个新建的方法1次 所以次数+1
        # 类属性的值只能使用类修改  cls表示当前类
        cls.__person_count += 1
        return object.__new__(cls)

    def __init__(self):
        print("对象属性被初始化")

    # 私有属性 需要在类外获取值 所以提供一个对外获取的接口 操作的是类属性 所以我们使用类方法返回
    @classmethod
    def get_person_count(cls):
        # cls表示的是当前类
        return cls.__person_count
if __name__ == '__main__':
    # 创建对象
    p1 = Person()
    p2 = Person()
    p3 = Person()
    # 获取对象的个数
    print(p1.get_person_count())
    print(p2.get_person_count())
    print(p3.get_person_count())
```

3.小明爱跑步，爱吃东西。

1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤

**从上面的语境中提取对象的属性，方法 ，进而声明成类 完成需求对应的操作**

```python
"""
分析：
    小明是个人  是一个人的具体的实例
    从实例中分析 属性有：姓名  体重
                方法有 跑步 吃饭
"""
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    # 方法
    def run(self):
        # 会减肥0.5公斤
        self.weight -= 0.5
        print('跑步，哈哈 减重0.5公斤')

    def eat(self):
        # 会增加1公斤
        self.weight += 1
        print('吃了一顿饭，体重咋就涨了1公斤嘛')
    def __str__(self):
        return f'Person(name={self.name}, weight={self.weight})'

p = Person('小明', 75)
print(p)
p.run()
p.eat()
```

4.需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

**从上面的语境中提取对象的属性，方法 ，进而声明类完成需求对应的操作**

```python

```

5.图书管理系统的编写

图书类Book：

​		属性：书名name	作者author	是否借出isborrow   书籍位置index 

​		**注意：书籍的位置不能重复**

图书管理系统BookManager类

​		存放图书的工具使用列表

​		方法：

​				1.添加图书

​				2.借书 （根据图书名字借书）

​					要检验图书是否存在、图书是否已经借出			

​				3.还书

​				4.查询书籍 （根据名字查询）

```python
class Book(object):
    def __init__(self, name, author, bookIndex):
        self.name = name
        self.author = author
        # True:借出 Fale：未借出
        self.isborrow = False # 默认没有借出
        self.bookIndex = bookIndex
    def __str__(self):
        return "书名:《%s》 作者:<%s> 状态:<%s> 位置:<%s>" % (self.name, self.author, self.isborrow, self.bookIndex)
    __repr__ = __str__

class BookManage(object):
    books = [] # 存放图书的列表

    def start(self):
        """
        图书管理初始化
        起始状态存放着3本书
        """
        book1 = Book('python', 'Guido', "INS888")
        book2 = Book('java', 'hello',"IGS888")
        book3 = Book('c', 'westos', "INS880")
        book_list = [book1, book2, book3]
        self.books.extend(book_list)
        print(self.books)

    # 图书馆菜单
    def menu(self):
        self.start()
        while True:
            print("""
                        图书管理系统
                    1. 添加图书
                    2. 借书 (根据图书名借书)
                    3. 还书
                    4. 查询数据(根据图书名查询)
                    5. 退出

             """)

            choice = input("请输入您的选择Choice:")
            if choice == '1':
                # 添加书籍
                self.add_book()
            elif choice == '2':
                #借书
                self.borrow_book()
            elif choice == '3':
                # 还书
                self.return_book()
            elif choice == '4':
                # 查询书籍
                name = input("请输入书名：")
                book = self.check_book(name)
                print(book) if book else print('查无此书')
            elif choice == '5':
                break
            else:
                print("请输入正确的选择!")

    #1. 添加书籍
    def add_book(self):
        name = input("请输入书名：")
        author = input("请输入作者：")
        # 获取所有的图书的位置
        book_indexs = [book.bookIndex for book in self.books]
        while True:
            index = input("请输入存放书的位置：")
            # 筛查书籍位置
            if index not  in book_indexs:
                # 这是一个新的位置
                break
            else:
                print('该位置已有书籍 请重新设置位置')
        book = Book(name, author, index)
        self.books.append(book)
        print("添加图书%s成功!" % (book))

    #2. 借书
    def borrow_book(self):
        name = input("借阅书籍名称:")
        # 检查书籍是否存在
        book = self.check_book(name)
        if book != None: # 书籍存在
            # 检验书籍是否借出
            if not book.isborrow: # 未借出
                print("借阅《%s》成功" % (name))
                book.isborrow = True # 修改书籍借阅的状态
            else:
                print("书籍《%s》已经借出" % (name))
        else:
            print("书籍《%s》不存在!" % (name))
    # 还书
    def return_book(self):
        name = input("归还书籍名称:")
        # 检查书籍是否存在
        book = self.check_book(name)
        if book != None:  # 书籍存在
            print("归还《%s》成功" % (name))
            book.isborrow = False  # 修改书籍借阅的状态
        else:
            print("该书籍《%s》不是这个图书馆的!" % (name))

    #4. 根据书籍名称查询书籍
    def check_book(self, name):
        for book in self.books:
            if book.name == name:
                # 返回book对象
                return book
        return None

bookManage = BookManage()
bookManage.menu()
```

