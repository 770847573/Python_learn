# 函数中捕获异常的两种方式
# 方式一：在函数调用时捕获
def test():
    list1 = [12,3,43,34]
    num = int(input("输入数字："))
    print(list1[num])
try:
    test()
except BaseException as e:
    print(e)

#方式二：在函数内捕获
def test1():
    try:
        list1 = [12, 3, 43, 34]
        num = int(input("输入数字："))
        print(list1[num])
    except BaseException as e:
        print(e)
test1()