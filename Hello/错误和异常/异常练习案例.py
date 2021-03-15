#读取文件内容，捕获可能出现的所有异常
file = None
try:
    with open("file1.txt", "r", encoding="utf-8") as file:
        r = file.readlines()
        for line in r:
            print(line)
except (FileNotFoundError, LookupError, ValueError) as e:# 文件找不到
    print(e)
finally:
    if not file:
        print("文件打开失败")
# ValueError: invalid mode: 'd'
# LookupError: unknown encoding: utf-3
