#获取当前时间，判断是否是元旦，如果不是，计算和元旦差了多少天
import datetime
def get_time():
    time_now = datetime.datetime.now()
    time_now_day = time_now.strftime('%Y/%m/%d')
    if time_now_day == '2021/01/01':
        print('今天是是元旦')
    else:
        yuandan_date =datetime.datetime(2021,1,1,0,0,0)
        days1= time_now - yuandan_date
        days2 = days1.days
        print('今天不是元旦，距元旦相差了{}天'.format(days2))

get_time()