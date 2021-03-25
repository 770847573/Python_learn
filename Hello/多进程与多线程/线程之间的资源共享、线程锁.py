import threading
import time
"""
在多进程中，同一个变量，在不同的进程中各自有一份拷贝在其中，互不影响；而在多线程中，所有的变量都由所有线程共享，所以变量可以被任意一个线程修改。
容易发生数据错乱
解决方法：在线程访问临界资源时，给当前资源上锁，其他线程只能等待，直到锁被释放之后才能进入
"""
balance = 0
# 创建一个锁对象
lock = threading.Lock()

def change(n):
    global balance
    balance = balance + n
    balance = balance - n

def run(n):
    for i in range(1000001):
        # change函数是共享资源【临界资源】

        # 方式一：
        # 获取锁
        # lock.acquire()
        # try:
        #     change(n)
        # finally:
        #     # 释放锁
        #     lock.release()
        # 方式二：
        with lock:
            change(n)

# 在线程t1执行过程中，可能会被t2抢到时间片，从而打断t1执行的顺序，改变了balance的值的顺序
if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=(5,))
    t2 = threading.Thread(target=run,args=(8,))
    t1.start()
    t2.start()

    print(balance)