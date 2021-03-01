import  datetime

# 1.now()
d1 = datetime.datetime.now()
print(d1)
print(type(d1))

# 2.两个datetime对象之间可以进行减法运算,不能进行加法运算    ******
d2 = datetime.datetime(2020,4,3,10,10,10,100)
d3 = datetime.datetime(2020,4,5,11,15,10,100)
d11 = d3 - d2
print(d11)
print(d11.days)   # 获取整天数
print(d11.seconds)  # 获取除了整天数之外的所有秒数

# 3.datetime类型和字符串之间可以相互转换
d1 = datetime.datetime.now()
s1 = d1.strftime("%Y.%m.%d")
print(s1)   # 2021.01.30

d2 = datetime.datetime.strptime(s1,"%Y.%m.%d")
print(d2)