"""
异常的特点：
1.代码执行的过程中出现的错误，称之为异常【exception】
2.代码从上往下运行过程中，如果遇到了异常，而且异常未被处理，程序会立即停止，后面的代码不会运行
3.异常一般用类表示，如IndexError表示下表越界异常
4.异常的父类是BaseException或Exception或者Object
5.异常在代码中出现是一种可能性
6.在python中，处理异常的思想：暂时跳过可能出现异常的代码，执行后面的代码
"""

print("start")

try:
    list1 = [45, 54, 7]
    index = int(input("请输入下标"))
    print(list1[index])
except:
    print("someting wrong!!!")
print("over")