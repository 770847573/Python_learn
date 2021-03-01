#需求：封装一个函数，将指定目录【文件夹】下所有的py文件打印出来
# 注意：需要获取指定目录以及子目录下的所有的py文件
import os

def get_py_file(path):
    if not os.path.exists(path):
        print('目录不存在')
        return
    #如果路径是个文件
    if os.path.isfile(path):
        print('目录是文件，无法查找')
        if path.endswith('py'):
            print('py文件：',path)
        return

    #路径是文件夹，可以继续查找
    #把该路径下的所有内容列出
    all_list = os.listdir(path)
    #遍历所有文件夹或文件
    for file_name in all_list:
    #拼接路径
        sub_path = os.path.join(path,file_name)
    #如果是文件夹，则继续执行递归函数
        if os.path.isdir(sub_path):
            get_py_file(sub_path)
        else:
            if sub_path.endswith('py'):
              print('py文件：',sub_path)

if __name__ == '__main__':
    path = r'E:\Python study\Hello'
    get_py_file(path)