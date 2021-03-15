### 一、异常

#### 1.raise抛出

> ```Python
> """
> 异常的处理方式：
>     a.try-except捕获【重点掌握】
>     b.raise抛出【了解】
>     c.assert断言【掌握】
> """
> 
> # raise
> # 在程序中异常出现的形式
> # 1.根据具体的问题出现【异常对象】
> # e是一个引用，指向由具体的代码所产生的异常对象，该异常对象的类型为IndexError
> 
> # import random
> # list1 = [34,45,454,4,5,656]
> # index = random.randint(0,20)
> # print(list1[index])    # 此处的异常只是一种可能性
> """
> Traceback (most recent call last):
>   File "F:/coding11/Day26Code/1.异常处理方式-raise抛出.py", line 14, in <module>
>     print(list1[30])
> IndexError: list index out of range
> """
> 
> # try:
> #     list1 = [34,45,454,4,5,656]
> #     print(list1[30])
> # except IndexError as e:
> #     print(e)
> 
> # 2.直接通过异常类创建异常对象
> # raise 异常类(异常描述) 表示在程序中抛出一个异常对象,常用于自定义异常
> try:
>     raise IndexError("列表索引越界")  # 此处的异常对象会100%出现
> except IndexError as e:
>     print(e)
> """
> Traceback (most recent call last):
>   File "F:/coding11/Day26Code/1.异常处理方式-raise抛出.py", line 30, in <module>
>     raise IndexError("列表索引越界")
> IndexError: 列表索引越界
> """
> 
> print("over")
> ```

#### 2.assert断言

> ```Python
> # assert【面试题】
> 
> # 1.try-except
> # 问题：y不能为0
> def div(x,y):
>     try:
>         r = x / y
>         return r
>     except ZeroDivisionError as e:
>         print(e)
> 
> print(div(10,2))
> print(div(10,0))
> """
> Traceback (most recent call last):
>   File "F:/coding11/Day26Code/2.异常处理方式-assert断言.py", line 9, in <module>
>     print(div(10,0))
>   File "F:/coding11/Day26Code/2.异常处理方式-assert断言.py", line 6, in div
>     return x / y
> ZeroDivisionError: division by zero
> """
> 
> # 2.assert
> # assert表示断言，也可以理解为预测，语法：assert 条件表达式,如果条件不成立时的错误描述
> def div(x,y):
>     # 工作原理：预测指定的表达式是否成立，如果成立，则代码继续向下执行，
>     # 如果条件不成立，则会抛出一个新的异常AssertionError，则后面的代码没有执行的机会
>     assert  y != 0,"在除法运算中，除数不能为0"
>     r = x / y
>     return r
> 
> print(div(10,2))
> # print(div(10,0))
> """
> Traceback (most recent call last):
>   File "F:/coding11/Day26Code/2.异常处理方式-assert断言.py", line 31, in <module>
>     print(div(10,0))
>   File "F:/coding11/Day26Code/2.异常处理方式-assert断言.py", line 26, in div
>     assert  y != 0,"在除法运算中，除数不能为0"
> AssertionError: 在除法运算中，除数不能为0
> """
> 
> # 练习
> # a.在程序中出现判断，可以使用if
> num = 13
> # if num % 2 == 0:
> #     print(f"{num}是一个偶数")
> # print("over")
> 
> # b
> assert  num % 2 == 0
> print("over")
> 
> # 应用场景:爬虫【如果网络请求成功，则解析网页数据，如果请求失败，则不做任何操作】
> ```

#### 3.嵌套定义

> ```Python
> # 注意：在try-except语句中，一般情况下，在finally中还可以嵌套定义try-except
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
>     try:
>         f.close()
>     except AttributeError as e:
>         print("文件打开失败，文件对象未被定义，无需close",e)
> 
> print("over")
> 
> 
> # 总结：程序中哪里有异常，如果需要代码继续向下执行，则都可以使用try-except
> ```

#### 4.自定义异常

> ```Python
> # 如果解决生活中的问题，而这些问题系统异常无法处理，则需要根据具体的需求自定义异常
> # 【面试题】自定义一个异常类
> # a.自定义类，继承自系统的异常父类
> class MyException(BaseException):
>     # b.定义构造函数，在其中定义实例属性，该实例属性表示异常信息描述
>     def __init__(self,message):
>         # c.调用异常父类的构造函数
>         super().__init__()
>         self.message = message
> 
>     # d.重写__str__,返回异常的信息描述
>     def __str__(self):
>         return self.message
> 
>     # e.定义一个实例函数，用于解决问题
>     def handle(self):
>         print("解决了问题~~~~")
> 
> try:
>     raise MyException("出现了异常")
> except MyException as e:
>     print(e)
>     e.handle()
> 
> # 练习：定义一个异常类，表示上班迟到的异常，如果8点之后起床，一定会迟到，如果8点之前起床，则不会迟到
> class LateException(BaseException):
>     def __init__(self,message):
>         super().__init__()
>         self.message = message
>     def __str__(self):
>         return self.message
>     def handle(self):
>         print("延迟下班时间")
> 
> time = float(input("请输入闹钟的时间："))
> if time > 8:
>     try:
>         raise LateException("闹铃在8:00之后才响，迟到了~~~")
>     except LateException as e:
>         # 迟到的原因
>         print(e)
>         # 解决办法
>         e.handle()
>     print("正常上班")
> else:
>     print("早早到达公司，等待搬砖~~~~~")
> ```

### 二、正则表达式

#### 1.案例

##### 1.1校验手机号

> ```Python
> import  re    # regular expression有规律的语句
> 
> """
> 合法qq号的要求：
>     a.全数字
>     b.不能为0开头
>     c.范围为5~11
> """
> def checkqq(qq):
>     """
>     判断qq号是否合法
>     :param qq: qq是一个字符串
>     :return: 是否合法的结果
>     """
>     # 假设是合法的
>     result = True
> 
>     # 寻找不合法的条件
>     if qq.isdigit():
>         if qq[0] != "0":
>             if len(qq) < 5 or len(qq) > 11:
>                 result = False
>         else:
>             result = False
>     else:
>         result = False
>     return result
> 
> def checkqq1(qq):
>     # 假设是合法的
>     result = True
>     # 寻找不合法的条件
>     try:
>         int(qq)
>         if not qq.startswith("0"):
>             if len(qq) < 5 or len(qq) > 11:
>                 result = False
>         else:
>             result = False
>     except BaseException as e:
>         result = False
> 
>     return result
> 
> if __name__ == '__main__':
>     qq = "46357265792652675"
>     print(checkqq(qq))
> 
>     # 使用正则判断
>     # match:如果匹配上，则返回一个正则对象，如果匹配不上，则返回None
>     r1 = re.match(r"^[1-9][0-9]{4,10}$",qq)
>     print(r1)
>     r2 = re.match(r"^[1-9]\d{4,10}$", qq)
>     print(r2)
> ```

##### 1.2校验手机号

> ```Python
> import  re
> 
> """
> 合法手机号的要求：
>     a.全数字
>     b.位数为11位
>     c.开头只能是1
>     d.第二位：3 4  5  6   7  8  9
> """
> def checkphonenum(phonenum):
>     # 假设是合法的
>     result = True
> 
>     # 寻找不合法的条件
>     if phonenum.isdigit():
>         if phonenum[0] == "1":
>             if len(phonenum) == 11:
>                 if phonenum[1] in [str(i) for i in range(0,3)]:
>                     result = False
>             else:
>                 result = False
>         else:
>             result = False
>     else:
>         result = False
>     return result
> 
> if __name__ == '__main__':
>     phonenum = "185019707955462"
>     print(checkphonenum(phonenum))
> 
>     r1 = re.match(r"^[1][3-9][0-9]{9}$",phonenum)
>     print(r1)
>     r2 = re.match(r"^[1][3-9]\d{9}$", phonenum)
>     print(r2)
> ```

#### 2.概念

> 正则表达式（英语：Regular Expression，在代码中常简写为regex、regexp或RE）使用单个字符串来描述、匹配一系列符合某个句法规则的字符串搜索模式。
>
> - 搜索模式可用于文本搜索和文本替换。
> - 正则表达式是由一个字符序列形成的搜索模式。
> - 当你在文本中搜索数据时，你可以用搜索模式来描述你要查询的内容。
> - 正则表达式可以是一个简单的字符，或一个更复杂的模式。
> - 正则表达式可用于所有文本搜索和文本替换的操作
>
> 使用场景：
>
> - 用于验证邮箱格式 手机号格式 密码格式等
> - 爬虫时，使用正则抓取网页中指定内容
>
> 而在python中，通过内嵌集成re模块，程序媛们可以直接调用来实现正则匹配。正则表达式模式被编译成一系列的字节码，然后由用C编写的匹配引擎执行
>
> Python 自1.5版本起增加了re 模块，它提供 Perl 风格的正则表达式模式。
>
> re 模块使 Python 语言拥有全部的正则表达式功能
>
> re 模块也提供了与这些方法功能完全一致的函数，这些函数使用一个模式字符串做为它们的第一个参数

#### 3.单字符匹配

> ----------匹配单个字符与数字---------
> .                匹配除换行符以外的任意字符
> [0123456789]     []是字符集合，表示匹配方括号中所包含的任意一个字符
> [good]           匹配good中任意一个字符
> [a-z]            匹配任意小写字母
> [A-Z]            匹配任意大写字母
> [0-9]            匹配任意数字，类似[0123456789]
> [0-9a-zA-Z]      匹配任意的数字和字母
> [0-9a-zA-Z_]     匹配任意的数字、字母和下划线
> [^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
> [^0-9]           匹配所有的非数字字符
> \d               匹配数字，效果同[0-9]
> \D               匹配非数字字符，效果同[^0-9]
> \w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
> \W               匹配非数字，字母和下划线，效果同[^0-9a-zA-Z_]
> \s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
> \S               匹配任意的非空白符，效果同[^ \f\n\r\t]
>
> ```Python
> # 1.概念
> """
> 1.正则表达式的作用：
>     a.匹配
>     b.查找/搜索
>     c.分割
>     d.替换
>     
> 2.使用场景：
>     a.用于验证邮箱格式,手机号格式,密码格式,用户名，银行卡，身份证号等
>     b.爬虫时，使用正则抓取网页中指定内容
>     
> 3.常用的函数
>     a.match():匹配
>     b.findall()/search()：查找/搜索
>     c.split()：分割
>     d.sub()/subn():替换
> """
> 
> # 2.单字符匹配
> """
> ----------匹配单个字符与数字---------
> 
> .                匹配除换行符以外的任意字符
> 0123456789是字符集合，表示匹配方括号中所包含的任意一个字符
> [good]           匹配good中任意一个字符
> [a-z]            匹配任意小写字母
> [A-Z]            匹配任意大写字母
> 
> [0-9]            匹配任意数字，类似[0123456789]
> \d               匹配数字，效果同[0-9]
> 
> [^0-9]          匹配非数字字符，效果同0-9
> \D               匹配非数字字符，效果同0-9
> 
> [0-9a-zA-Z]      匹配任意的数字和字母
> 
> [0-9a-zA-Z_]     匹配任意的数字、字母和下划线
> \w               匹配数字，字母和下划线,效果同[0-9a-zA-Z_]
> 
> [^0-9a-zA-Z_]    匹配非数字，字母和下划线
> \W               匹配非数字，字母和下划线，效果同0-9a-zA-Z_
> 
> [^good]          匹配除了good这几个字母以外的所有字符，中括号里的^称为脱字符，表示不匹配集合中的字符
> 
> \s               匹配任意的空白符(空格，回车，换行，制表，换页)，效果同[ \r\n\t\f]
> \S               匹配任意的非空白符，效果同 \f\n\r\t
> """
> 
> """
> []      不管其中书写了多少字符，都只能匹配其中的一个字符
> -       连接符，用于表示连续的数据，一般用于表示数字或者字母
> .       匹配除换行符\n以外的任意字符,注意：如果也需要匹配换行符，则需要设置flags=re.DOTALL
> ^       ^使用在[]中被称为脱字符，表示否定
> \d,\w,\s   也表示单字符匹配，一个只能匹配单个的字符
> """
> 
> import  re
> 
> # 1.正则表达式中函数的调用方式
> # 方式一
> # 将正则表达式字符串编译为正则对象
> pattern = re.compile(r"[0-9]")
> # 用正则对象匹配指定的字符串，如果匹配成功则返回对象，否则返回None
> r = pattern.match("6")
> print(r)
> # 如果匹配上，则可以通过group函数获取匹配到的内容,如果匹配不上，则代码会报错
> # print(r.group())
> 
> # 方式二
> r = re.match(r"[0-9]","6")
> print(r)
> 
> # 2.演示单字符匹配
> # a
> r = re.match(r"[0-9]","6")
> print(r)
> 
> # b
> r = re.match(r"[d-x]","f")
> print(r)
> 
> # c
> r = re.match(r"[^a-z]","a")
> print(r)
> 
> # d
> r = re.match(r"\d","5")
> print(r)
> 
> # e
> r = re.match(r"[0-9a-zA-Z]","H")
> print(r)
> 
> # f
> r = re.match(r"\w","_")
> print(r)
> 
> # g
> r = re.match(r"\s","\n")
> print(r)
> 
> # h
> r = re.match(r".","\n")
> print(r)
> 
> r = re.match(r".","\n",flags=re.DOTALL)
> print(r)
> ```

