#解决业务中的问题，而这些问题系统异常无法处理，则需要根据实际要求自定义异常
#【面试题】自定义一个异常类
#a.自定义一个类，继承自系统异常父类
class MyException(BaseException):
    #b.定义构造函数，定义实例属性，该属性表示出现异常的描述
    def __init__(self,message):
        #c.调用父类的构造函数
        BaseException.__init__(self)
        self.message = message
    #d.重写__str__，返回错误信息描述
    def __str__(self):
        return self.message
    def handle(self):
        print("解决了异常")

# raise MyException("奥术大师多")
"""
Traceback (most recent call last):
  File "E:/Python study/Python_learn/Hello/错误和异常/自定义异常.py", line 14, in <module>
    raise MyException("奥术大师多")
__main__.MyException: 奥术大师多
"""
try:
    raise MyException("出现异常")
except MyException as e:
    print(e)
    e.handle()

# 练习：定义一个异常类，表示上班迟到，如果8点以后起床，一定会迟到；如果8点之前起床，不会迟到
class LateException(BaseException):
    def __init__(self,message):
        BaseException.__init__(self)
        self.message = message
    def __str__(self):
        return self.message
    def handle(self):
        print("加班")
time = int(input("请输入起床时间"))
try:
    if time > 8:
        raise LateException("迟到了")
    print("没有迟到")
except LateException as e:
    print(e)
    e.handle()