# 1.导入进程包
import multiprocessing
import time
import os

def sing(num,name):
    #获取当前进程的编号
    print("sing进程的编号为：",os.getpid())
    print("sing进程的父进程编号为：",os.getppid())
    for i in range(num):
        print('{}唱歌'.format(name))
        #print('%s唱歌……'%name)
        time.sleep(0.5)


def dance(num,name):
    print("dance进程的编号为：", os.getpid())
    print("dance进程的父进程编号为：", os.getppid())
    for i in range(num):
        print('%s跳舞了'%name)
        time.sleep(0.5)


if __name__ == '__main__':
    print("主进程pid：",os.getpid())
    # 2.使用进程类创建进程对象
    #使用元祖方式传参
    sing_process = multiprocessing.Process(target=sing,args=(2,'小刘'))
    #使用字典方式给指定参数传参
    dance_process = multiprocessing.Process(target=dance,kwargs={'num':2,'name':'大王'})
    # 3.启动进程对象
    sing_process.start()
    dance_process.start()