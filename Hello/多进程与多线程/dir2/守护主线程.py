import threading
import time
def sing():
    for i in range(10):
        print('啦啦啦')
        time.sleep(0.2)

if __name__ == "__main__":
    sing_thread = threading.Thread(target=sing)
   # sing_thread.daemon = True
   # sing_thread = threading.Thread(target=sing,daemon=True)
    sing_thread.setDaemon(True)
    sing_thread.start()
    # 主线程顺延1秒
    time.sleep(1)
    print('主线程结束了')