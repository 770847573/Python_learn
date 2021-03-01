import sys
import time

f = None
try:
    f = open("test.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end=' ')
        sys.stdout.flush()
    print("\n Press ctrl+c in 5 secs")
    time.sleep(5)
except IOError:
    print("没有找到文件")
except KeyboardInterrupt:
    print("你取消了阅读")
finally:
    if f:
        f.close()
    print("文件已关闭")
