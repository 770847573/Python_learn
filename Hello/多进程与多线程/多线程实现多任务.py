# 1.导入线程模块threading
import threading
import time

def sing(name,num):
    for i in range(num):
        print(f"{name}sing^^^")
        time.sleep(1)

def dance(name,num):
    for i in range(num):
        print(f"{name}dance^^^")
        time.sleep(1)

# 2.创建线程对象
sing_thread = threading.Thread(target=sing,args=("Tom",3))
dance_thread = threading.Thread(target=dance,kwargs={'name':"Jerry",'num':3})

if __name__ == "__main__":
    # 3.启动多线程
    sing_thread.start()
    dance_thread.start()