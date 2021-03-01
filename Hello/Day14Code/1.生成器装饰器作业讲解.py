# 1.书写一个装饰器，将一个指定函数的返回值加100之后返回
def add_hundred(fun):
    def inner(x,y):
        # 调用原函数
        r = fun(x,y)
        # 增加新的功能
        return r + 100
    return inner
@add_hundred
def add(a,b):
    return a + b
print(add(3,5))

# 2.写一个生成器能够产生1-10中所有半径是偶数的圆的面积
import math
# 方式一
ge1 = (math.pi * i ** 2 for i in range(1,11) if i % 2 == 0)
# 方式二
def get_area():
    for i in range(1,11):
        if i % 2 == 0:
            yield  math.pi * i ** 2
ge2 = get_area()

# 4.写一个可以产生学号的生成器, 生成的时候可以自定制学号数字位的宽度和学号的开头
"""
例如:
   study_id_creater('py',5) -> 依次产生: 'py00001', 'py00002', 'py00003',..py00100..'py99999'
   study_id_creater('test',3) -> 依次产生: 'test001', 'test002', 'test003',...,'test999'
"""
"""
def  xxx():
    yield  元素的规律
"""

# 方式一
def create_stuid1(prefix,width):
    for m in range(1,10 ** width):
        # 注意：使用+进行字符串的拼接，只能是字符串和字符串进行拼接
        yield prefix + "0" * (width - len(str(m))) + str(m)

ge1 = create_stuid1("py",5)
print(next(ge1))
create_stuid1("test",3)

# 方式二
def create_stuid2(prefix,width):
    for m in range(1,10 ** width):
        # zfill()填充，原字符串居右显示，前面用0字符填充
        # rjust()
        yield  prefix + str(m).zfill(width)
ge2 = create_stuid2("py",5)
print(next(ge2))
print(next(ge2))
print(next(ge2))
print(next(ge2))

