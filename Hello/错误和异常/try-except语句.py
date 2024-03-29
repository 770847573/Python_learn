"""
根据具体需求，try-except-else/finally
    a.try-except
    b.try-except-except……
    c.try-except-esle
    d.try-except-finally
    e.try-finally
注意事项：
a.将可能存在异常的代码写在try中，检测起来，try代码块称为检测区
b.如果try中的代码出现异常，会执行except代码块；
如果try中没有异常，则会跳过except代码块。
c.不管try中是否存在异常，finally中的代码都会被执行
d.工作原理：当try中的代码出现异常，会从上往下依次比较except中的类型
，直到遇到匹配的类型，才执行相应的except中的代码，后面的except不会再执行
"""

#1.try-except-except：设定一种或多种异常
try:
    list1 = [45, 54, 7]
    index = int(input("请输入下标"))
    print(list1[index])
# e是个变量，类型是ValueError，指向的是由具体的代码产生的异常对象
except ValueError as e: # >> as >>invalid literal for int() with base 10: 'as'
    # 直接打印异常对象，得到的是字符串，说明系统的异常类已经重写了__str__
    print(e)
except IndexError as ie: # >>4 >>>list index out of range
    print("下标溢出了")
    print(ie)
print("over")

# 2. try-except-else:在try中没有任何异常时，else会被执行
try:
    list2 = [45, 54, 7]
    index = int(input("请输入下标"))
    print(list2[index])
except ValueError as e:
    print(e)
else:
    print("代码没问题啊")

#3.try-except-finally : 无论try中是否有异常，finally都会执行
#例如代码执行之后的清理工作，关闭文件等
#4.【面试题】在函数中使用try-except-finally,期间出现return，函数会结束，但finally语句会继续执行完成
def test():
    try:
        num_list = [2,3,3,4]
        num1 = int(input("请输入数子："))
        print(num_list[num1])
    except ValueError as e:
        print(e)
        return
    except IndexError as e:
        return 1
        print(e)
    finally:
        print("finally被执行了")

test()