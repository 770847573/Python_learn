import math
#1.书写一个装饰器，将一个指定函数的返回值加100之后返回
#方法1
def Dec1(func):
    def inner1(n):
        r1 = func(n)
        return r1 + 100
    return inner1

def func1(x):
    print('原函数的返回值为',x)
    return x
r1 = Dec1(func1)(1)
print('使用装饰器后为',r1)

#方法2
@Dec1
def func2(x):
    print('原函数的返回值为', x)
    return x
r2 = func2(1)
print('使用装饰器后为',r2)
print('*'*40)
#2.写一个生成器能够产生1-10中所有半径是偶数的圆的面积
def sqa():
    for i in range(1,11):
        if i % 2 == 0:
            yield i**2*math.pi
        else:continue
resault2 = sqa()
while True:
    try:print(format(next(resault2),'.2f'))
    except:break
print('*'*40)
#3.书写一个递归函数，求指定数的阶乘
def Factorial(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return (x*Factorial(x-1))
print(Factorial(5))
print('*'*40)
#4.写一个可以产生学号的生成器, 生成的时候可以自定制学号数字位的宽度和学号的开头
def study_id_creater(name,num):
    for i in range(1,10**num-1):
        # yield (name+str(i).rjust(num,'0'))
        yield (name + str(i).zfill(num))
student = study_id_creater('student',2)
print(next(student))
