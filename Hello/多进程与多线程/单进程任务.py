import multiprocessing
import time
def sing():
    for i in range(3):
      print('sing')
      time.sleep(0.5)
def dance():
    for i in range(3):
        print('dance')
        time.sleep(0.5)
if __name__ == '__main__':
    start_time = time.time()
    sing()
    dance()
    end_time = time.time()
    print(end_time - start_time,'秒')