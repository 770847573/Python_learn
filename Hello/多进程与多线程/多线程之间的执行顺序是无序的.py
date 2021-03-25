import time
import threading

def test():

        time.sleep(1)
        current_thread = threading.current_thread().name
        print(current_thread)

if __name__ == "__main__":
    for i in range(5):
        thread = threading.Thread(target=test)
        thread.start()