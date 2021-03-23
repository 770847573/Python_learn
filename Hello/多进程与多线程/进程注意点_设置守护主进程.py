#注意点：主进程默认会等待所有子进程结束后再结束，除非给子进程设置主进程保护
# jion: 在子进程.start（）后，可以使主进程的代码等待子进程结束后再执行

import multiprocessing
import time

def show():
    for i in range(10):
        print("工作中,,,")
        time.sleep(0.2)

if __name__ == "__main__":
    show_process = multiprocessing.Process(target=show)
    #设置主进程保护，在主进程结束后，子进程自动销毁，不再执行下面代码
    show_process.daemon = True
    show_process.start()
    # show_process.join()
    time.sleep(1)
    print("主进程还有0.2秒结束")
    time.sleep(0.2)#后面会打印出一条"工作中,,,"，主进程结束
    print("主进程结束")