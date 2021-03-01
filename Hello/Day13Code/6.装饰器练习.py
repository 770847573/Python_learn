import  time

# 【面试题】需求：书写一个装饰器，可以统计一个函数的执行时间
# a.
def show():
    for i in range(100000):
        pass

def get_time(func):
    def inner():
        # 开始时间
        start_time = time.time()
        # 调用原函数
        func()
        # 结束时间
        end_time = time.time()

        return end_time - start_time
    return inner

f = get_time(show)
r = f()
print("该函数的执行时间：%.4f" % (r))

# b
def get_time1(func):
    def inner1():
        # 开始时间
        start_time = time.time()
        # 调用原函数
        func()
        # 结束时间
        end_time = time.time()

        return end_time - start_time
    return inner1
@get_time1
def show1():
    print("原函数被调用了")
    for i in range(100000):
        pass

r = show1()
print("该函数的执行时间：%.4f" % (r))