# 1.概念：如果一个函数调用自身，则该函数被称为递归函数
# def a():
#     print("hello")
#     a()
# a()

# 2.递归使用
# a.需求：封装函数，报一个数，返回在该数位置处的斐波那契数列中对应的值,如：9---》34,11----》89
"""
1   2   3    4     5   6     7   8     9    10  11
1   1   2    3     5    8   13   21   34    55  89.....

例如：
f(5) = f(4) + f(3) = 3 + 2 = 5
f(4) = f(3) + f(2) = 2 + 1
f(3) = f(2) + f(1) = 1 + 1
f(3) = f(2) + f(1) = 1 + 1

f(n) = f(n - 1) + f(n - 2)

规律：
    a.临界值：当n为1和2时，结果为1
    b.公式：f(n) = f(n - 1) + f(n - 2)
"""
count = 0
def f(n):
    global  count
    count += 1
    if n == 1 or n == 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)

print(f(10))
print("次数:",count)


# b.需求：使用递归，求1~某个数之间所有整数的和
# 方式一
def add1(n):
    total1 = 0
    for i in range(1,n + 1):
        total1 += i
    return total1
print(add1(100))

# 方式二
def add(n):
    if n == 1:
        return 1
    else:
        return add(n - 1) + n

print(add(100))

"""
add(100)---->add(99) + 100
add(n)---->add(n- 1) + 100
"""
