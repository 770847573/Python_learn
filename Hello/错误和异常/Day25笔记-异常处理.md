### 一、异常和错误

#### 1.概念

> Python有两种错误很容易辨认：语法错误和异常
>
> ​	Python 的语法错误或者称之为解析错误，是初学者经常碰到的，比如缺少冒号等
>
> ​	在程序运行过程中，总会遇到各种各样的错误，有的错误是程序编写有问题造成的，这种错误我们通常称之为bug，bug是必须修复的；有的错误是用户输入造成的，这种错误可以通过检查用户输入来做相应的处理；还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了，这类错误被称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出
>
> ```Python
> print("start")
> try:
>     numlist = [34, 5, 5]
>     index = int(input("请输入上述列表的索引："))
>     num = numlist[index]
>     print(num)
> except:
>     print("出现了异常~~~~")
> 
> print("over")
> 
> 
> """
> 注意：
>     a.一般，在代码运行的过程中出现的错误被称为异常【exception】
>     b.代码从上往下执行的过程中，如果遇到了异常，而且异常未被处理，则程序会立即终止，后面的代码无法执行
>     c.异常一般使用类表示，如IndexError表示列表或者元组或者字符串的下标越界异常
>     d.异常的父类是BaseException或者Exception或者object
>     e.异常在代码中的出现是一种可能性
>     f.在Python中，处理异常的思想:让程序暂时跳过可能出现异常的代码，让后面的代码有执行的机会
> """
> ```

#### 2.常见异常【面试题】

> AttributeError 试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
> IOError 输入/输出异常；基本上是无法打开文件
> ImportError 无法引入模块或包；基本上是路径问题或名称错误
> IndentationError 语法错误（的子类） ；代码没有正确对齐
> IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
> KeyError 试图访问字典里不存在的键
> KeyboardInterrupt Ctrl+C被按下
> NameError 使用一个还未被赋予对象的变量
> SyntaxError Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
> TypeError 传入对象类型与要求的不符合
> UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
> 导致你以为正在访问它
> ValueError 传入一个调用者不期望的值，即使值的类型是正确的
>
> ```Python
> # 1.NameError:当使用了一个未定义的变量
> # print(num)  # NameError: name 'num' is not defined
> 
> # 2.ValueError:传入一个不期望的值，即使类型是正确的
> # num = int(input("请输入数字："))  # ValueError: invalid literal for int() with base 10: 'fahf'
> 
> # 3.TypeError:传入的数据类型不匹配
> # print(10 + "fahfa")   # TypeError: unsupported operand type(s) for +: 'int' and 'str'
> # print("faf" + 34)   # TypeError: can only concatenate str (not "int") to str
> 
> # 4.IndexError:当列表，元组或者字符串的索引越界
> 
> # 5.AttributeError:当一个对象访问了不存在的属性或者函数
> # "fafa".append("45")  # AttributeError: 'str' object has no attribute 'append'
> 
> class Person(object):
>     __slots__ = ("name",)
> p = Person()
> # p.age = 10    # AttributeError: 'Person' object has no attribute 'age'
> 
> # 6.UnboundLocalError:修改了其他作用域的变量:在函数内部修改了全局变量  或者  在局部作用域中修改了函数作用域中的变量
> # 情况一：gloabl
> a = 10
> def test():
>     global a
>     a += 2    # UnboundLocalError: local variable 'a' referenced before assignment
> test()
> 
> # 情况二:nonlocal
> def outter(cls):
>     instance = None
>     def inner():
>         nonlocal instance
>         if not instance:    # UnboundLocalError: local variable 'instance' referenced before assignment
>             instance = cls()
>         return instance
>     return inner
> @outter
> class Animal():
>     pass
> a = Animal()
> 
> # 7.FileNotFoundError:当读取文件的时候，文件不存在
> # f = open("file1.txt","r",encoding="utf-8")  # FileNotFoundError: [Errno 2] No such file or directory: 'file1.txt'
> 
> # 8.MoudleNotFoundError:模块导入错误，主要模块的路径有问题
> # import  aaa   # ModuleNotFoundError: No module named 'aaa'
> 
> # 9.ImportError
> # 10.SyntsaxError:Python代码非法，基本的语法错误
> ```

#### 3.异常处理方式

> 处理异常的本质：没有从根本上解决问题【修改代码】，只是将异常忽略，可以让后面的代码继续执行

##### 3.1try-except-finally/else捕获【常用】

> ```Python
> """
> 根据具体的需求，try-except-else/finally可能的形式：
>     a.try-except
>     b.try-except-except.....
>     c.try-except-else
>     d.try-except-finally
>     e.try-fianlly
> 
> 注意：
>     a.将可能存在异常的代码书写在try代码块中，监测起来，try代码块被称为监测区
>     b.如果try中的代码出现异常，肯定会执行相应的except代码块；如果try中的代码没有异常，则会跳过except代码块
>     c.不管try中的代码是否存在异常，finally代码块都会被执行
> """
> 
> # 1.try-except:只设定一种异常
> """
> try:
>     # 监测区
>     num = int(input("请输入数字："))
>     print(num)
> # e是一个变量，类型是ValueError，指向由具体的代码产生的异常对象
> # e可以自定义，但是为了和异常的概念吻合，一般使用e
> except ValueError as e:  # with open()  as f
>     print("出现了异常~~~~",type(e))
>     # 直接打印异常对象，得到的结果是一个字符串，说明系统的异常类中都已经重写了__str__,返回异常的信息描述
>     print(e)
> print("over")
> """
> 
> # 2.try-except-except....
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except ValueError as e:
>     print("数字格式输入有误~~~~")
>     print(e)
> except IndexError as e:
>     print("列表索引越界~~~~")
>     print(e)
> 
> print("over")
> """
> 
> """
> 注意：
>     a.如果try中可能存在多处异常，每次都只会处理其中的一个异常【原因：try中的代码在某个地方一旦遇到异常，try中后面的代码将没有执行的机会】
>     b.try中的代码在某处遇到了异常，则会自动根据异常的类型执行相应的except代码块
>     c.工作原理：当try中的代码遇到了异常，会从上往下依次比较except中的类型，直到遇到匹配的类型，才执行相应的代码块
> """
> 
> # 3.try-except:使用异常父类
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except BaseException as e:   # 多态  isinstance(子类的对象，父类)--->True
>     print("出现了异常",e)
> except ValueError as e:
>     print("数字格式输入有误~~~~")
>     print(e)
> except IndexError as e:
>     print("列表索引越界~~~~")
>     print(e)
> 
> print("over")
> """
> 
> # 如果要使用父类，则可以直接简化书写
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except BaseException as e:  
>     print("出现了异常",e)
> 
> print("over")
> """
> 
> # 注意：当except中使用了异常的父类BaseException,当BaseException出现在第一个except中，会捕获所有的异常类型
> 
> # 4.try-except:不声明类型【了解】
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except:
>     print("出现了异常")
> """
> 
> # 注意：好处是可以捕获所有类型的异常，但是缺点是不明确异常的类型，无法定位异常
> 
> # 5.try-except:给定指定的类型【了解】
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except (IndexError,ValueError,NameError,AttributeError):
>     print("出现了异常")
> """
> 
> # 注意：只能匹配给定类型的异常，同样缺点是无法定位异常
> 
> # 6.try-except-else
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except ValueError as e:
>     print(e)
> except IndexError as e:
>     print(e)
> else:
>     print("else被执行了")
> """
> 
> # 注意：只有当try中的代码没有任何异常的时候，else才有执行的机会
> 
> # 7.try-except-finally
> """
> try:
>     numlist = [34,4,6]
>     index = int(input("请输入数字："))
>     num = numlist[index]
>     print(num)
> except ValueError as e:
>     print(e)
> except IndexError as e:
>     print(e)
> finally:
>     print("finally被执行了")
> """
> 
> 
> # 注意：不管try中的代码是否由异常，finally都会执行，所以适用于代码执行完毕之后，最后的清理行为，如：关闭文件，关闭数据库等
> 
> # 8.【面试题】在函数中使用try-except-finally语句，如果出现return
> """
> def test():
>     try:
>         numlist = [34, 4, 6]
>         index = int(input("请输入数字："))
>         num = numlist[index]
>         return
>         print(num)
>     except ValueError as e:
>         print(e)
>         return
>     except IndexError as e:
>         return
>         print(e)
>     finally:
>         print("finally被执行了")
> 
>     print("over")
> 
> test()
> """
> 
> 
> # 注意：如果try-except-finally语句使用在函数中，在try和except任意的地方使用了return，finally都会被执行
> # 但是，try-except-finally语句后面的代码没有执行的机会
> 
> 
> # 练习：读取文件内容，捕获所有可能存在的异常
> # FileNotFoundError
> # ValueError:invalid mode: 'd'
> # LookupError: unknown encoding: utf-3
> f = None
> try:
>     f = open(r"file1.txt", "r", encoding="utf-8")
>     content = f.read()
>     print(content)
> except FileNotFoundError as e:
>     print("文件路径不存在",e)
> except ValueError as e:
>     print("打开文件的方式错误",e)
> except LookupError as e:
>     print("编码格式书写错误",e)
> finally:
>     if f:
>         f.close()
>     else:
>         print("文件打开失败")
> ```

##### 3.2问题补充

> ```Python
> # 函数中出现异常，有两种捕获方式
> 
> # 方式一：捕获函数调用
> # def test():
> #     numlist = [34, 4, 6]
> #     index = int(input("请输入数字："))
> #     num = numlist[index]
> #     print(num)
> #
> # try:
> #     test()
> # except BaseException as e:
> #     print(e)
> #
> 
> # 方式二：在函数内部捕获
> def test():
>     try:
>         numlist = [34, 4, 6]
>         index = int(input("请输入数字："))
>         num = numlist[index]
>         print(num)
>     except BaseException as e:
>         print(e)
> 
> test()
> ```