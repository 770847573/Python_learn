from multiprocessing import Process,Pool
import time,os

"""
进程池需要创建多个进程进行同一管理
方式一：
      通过Pross类创建多个进程对象
方法二：
      通过Pool类创建进程池对象，管理多个进程
"""

# 让多个子进程执行同一个函数
def run(name):
    print(f"子进程{name}启动了，进程号{os.getpid()}")
    time.sleep(1)
    print(f"子进程{name}结束了————，进程号{os.getpid()}")

if __name__ == "__main__":
    print("父进程启动了")
    # 创建进程池对象  Pool(num):num表示可以同时进行的进程的数量，如果num省略，则默认表示当前操作系统的cpu核心数量
    p = Pool()

    # 通过循环创建多个子进程,执行同一个子任务，通过进程池统一管理
    for i in range(10):
        p.apply_async(run,args=(i,))
    # 不允许再向进程池中添加进程对象
    p.close()
    # 将进程池中的所有子进程对象合并
    p.join()

    print("父进程结束")