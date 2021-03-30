# 1.读取
# 注意：
# a.关于文件的读写，并不是真正意义生上的打开，而是在内存中开辟了一份空间，定义一个变量，表是需要被打开的文件，该变量呗成为文件描述符
# b.文件必须存在，才能读取，否则会报错
# c.encoding必须是打开文件的编码格式，否则会报错
# d.为了避免资源浪费，文件需要关闭
def read_file():
    # a.打开文件  open(path,mode,encoding)
    """
    path:需要打开的文件路径
    mode:文件打开的方式，读取方式：r,r+,rw,rb等
                      写入方式：w,w+,wb,a等
    encoding：表是文件对应的编码格式
    """
    f = open("LINUX操作.txt", "r", encoding="gbk")
    # b.读取文件内容
    # r = f.read()  一次性全部读取完，括号里表是读取得字节数，中文一个字占一个字节
    # r = f.readline()  #一次只能读取一行内容
    r = f.readlines()  # 一次性读取全部内容，但是返回一个列表，每行内容是列表的每个元素
    for lines in r:
        print(lines, end=" ")
    # c.关闭文件
    f.close()


read_file()


# 2.写入

def writer_file():
    # a.打开文件
    """
    注意：写入的文件可以不存在
    w：覆盖，a：追加到后面,二者都会自动创建文件
    """
    f2 = open("file1.txt", "a", encoding="gbk")
    # b.向文件中写入内容
    f2.write("今天是个好日期")
    # 为了提高写入的速度，可以进行刷新(写入量比较大的时候)
    f2.flush()
    # c.关闭文件
    f2.close()


writer_file()
