# 注意：py文件的文件名尽量不要和系统模块名重名，否则无法使用

from time import  *

# 1.time():获取当前时间的时间戳      ******
# 每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
# 时间表示形式一：时间戳
t1 = time()
print(t1)

# 2.gmtime():获取UTC的元组形式
# 时间表示形式二：时间的元组
t2 = gmtime()
print(t2)
# time.struct_time(tm_year=2021, tm_mon=1, tm_mday=30, tm_hour=13, tm_min=28, tm_sec=38, tm_wday=5, tm_yday=30, tm_isdst=0)

# 3.localtime():获取北京时间的元组形式      ******
t3 = localtime()
print(t3)

# 4.mktime():获取指定时间的时间戳
# 将时间的元组形式转化为时间戳
t4 = mktime(t3)
print(t4)

# 5.ctime():将时间戳转换为格式化字符串,结果为默认格式
t5 = ctime(t4)
print(t5)  # Sat Jan 30 21:35:20 2021

# 6.asctime():将时间元组形式转换为格式化字符串,结果为默认格式
t6 = asctime(t3)
print(t6)

# 7.strftime():将时间的元组形式转化为格式化字符串，格式可以自定义     ******
t7 = strftime("%Y/%m/%d %H:%M:%S",t3)
print(t7)   # 2021/01/30 21:42:21

# 8.strptime():将时间的格式化字符串转换为时间元组形式             *****
# 注意：解析时间的字符串时，给定的format一定要和原字符串匹配
time_str = "2021/01/30 21:42:21"
t8 = strptime(time_str,"%Y/%m/%d %H:%M:%S")
print(t8)

# 9.sleep():休眠
# 使用在多线程和多进程中比较多
print("start")
sleep(4)

print("over")
