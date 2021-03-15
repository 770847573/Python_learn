# 产生异常的形式
# 形式一：根据具体问题产生异常【异常对象】
try:
    list1 = [12, 3, 43, 34]
    print(list1[23])
except IndexError as e:
    print(e)

#形式2：直接通过异常类创建异常对象，
# raise异常类（异常描述）表示在程序中跑出一个异常对象
try:
    raise IndexError("下标越界~~~")
except IndexError as e:
    print(e)