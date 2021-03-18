import os
import threading
from os import path

def copy_file(file_name,source_dir,tar_dir):
    source_path = path.join(source_dir,file_name)
    tar_path = path.join(tar_dir,file_name)

    with open(source_path,'rb') as source_file:
        with open(tar_path,'wb') as tar_file:
            while True:
                data = source_file.read(1024)
                if data:
                    tar_file.write(data)
                else:
                    break

source_dir = 'dri1'
tar_dir = 'dir2'

try:
    os.mkdir(tar_dir)
except BaseException as e:
    print('文件夹已存在')
file_list = os.listdir(source_dir)
for file_name in file_list:
    thread = threading.Thread(target=copy_file,args=(file_name,source_dir,tar_dir))
    thread.start()