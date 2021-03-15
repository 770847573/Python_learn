
# try-except
def div(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print(e)
print(div(10, 0))
print("*" * 30)

#assert断言，也可以理解为预测,语法：assert 条件语句，“错误描述“
# 如果其不是真的，就抛出一个错误，后面的代码不会执行
# def div1(x, y):
#     assert y  != 0,"除数不能为0"
#     r = x/y
#     print(r)
# print(div1(12,0))

#可以用来判断
num = 11
assert num % 2 == 0 , "不是偶数不要继续运行了"
print('num是偶数')
# 应用场景：爬虫【如果网络请求成功，则解析数据，如果请求失败，则不做任何操作】