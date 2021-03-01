import  os

# os模块：可以操作系统磁盘，包括文件和文件夹

# 1.listdir():列出指定目录下所有的内容,返回一个列表，列表中的元素是文件或者文件夹的名称
path = r"C:\Users\Administrator\Desktop\侯\工作文件\移动端开发资料"
list1 = os.listdir(path)
print(list1)

# 2.join():拼接路径，
# F:\coding11\Day11
# path1 = path + "\\" + "Day11"
# print(path1)

# 好处：可以自动识别操作系统，使用相应的拼接方式
path1 = os.path.join(path,"Day11")
print(path1)

# 3.exists():判断一个路径在当前磁盘中是否存在
print(os.path.exists(path1))
print(os.path.exists("F:\coding12"))

# 4.isfile():判断一个路径是否是文件，如果是文件则返回True
# isdir():判断一个路劲是否是文件夹,如果是文件夹则返回True
print(os.path.isfile(path))
print(os.path.isdir(path))
