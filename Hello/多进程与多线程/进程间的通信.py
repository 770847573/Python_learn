# 虽然进程间资源不共享，但是只要找到一个中介就可以达到进程间的通信

# 需求：创建两个子进程，一个往队列queue中写入数据，一个王queue中读取数据，
# 注意：两个进程中的queue是同一个

from multiprocessing import Process,Queue
import os,time

# 写数据的进程任务函数
def write(q):

    print("写入进程%s启动了"%(os.getpid()))
    for value in ['A','B','C']:
        q.put(value)
        print(f"{value}被添加到队列")
        time.sleep(1)
    print("进程%s结束了"%(os.getpid()))


# 定义读取数据的进程任务函数

def read(q):
    print("读取进程%s启动了" % (os.getpid()))
    for i in range(3):
        try:
            value = q.get()
            print(f"从队列读取数据{value}")
        except BaseException as f:
            print(f)


    print("读取进程%s结束了" % (os.getpid()))

if __name__ == '__main__':
    print("父进程启动")
    # 创建一个Queue对象，Queue用于在两个进程之间传递数据
    q = Queue(3)

    # 创建子进程
    write_process = Process(target=write,args=(q,))
    read_process = Process(target=read,args=(q,))
    write_process.start()
    read_process.start()
    write_process.join()
    read_process.join()

    print("父进程结束")