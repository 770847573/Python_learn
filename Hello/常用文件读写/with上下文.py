#1.基本语法
"""
with open() as 变量:
  读取内容
注意：不需要close
任何格式的文件都可以采用with上下文来读写
"""

with open("LINUX操作.txt",'r',encoding='gbk') as f:
    with open("file1.txt",'w',encoding='gbk') as file1:
        content = f.read()
        print(content)
        file1.write(content)
        file1.flush()


#2.工作原理：
#with语句的作用：通过内部机制简化代码，还可以处理代码在执行过程中可能会遇到的异常（exception）
"""
with是管理上下文的关键字，也被称为上下文的管理器，当一个对象使用with的时候
当对象进入上下文的时候，会自动调用__enter__()函数，
当对象退出上下文时，会调用__exit__()函数；
as：通过as关键字接收with关键字的对象，as后面是一个变量，指向的是被打开的文件对象
"""

class Check(object):
    def __enter__(self):
        #当对象进入上下文时，主要是为了初始化相应的资源，如：打开文件
        print("对象进入了with上下文~~~~~~~")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        :param exc_type:异常类型，NameError
        :param exc_val:异常值，
        :param exc_tb:
        :return:
        """
        print("退出wtih上下文")
        return True

with Check() as check1:
    print('hahhaha')