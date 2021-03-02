import multiprocessing
import os
import os.path

def copy_file(file_name,source_dir,target_dir):
    #1.拼接源文件路径和目标文件路径
    source_path = source_dir+'/'+file_name
    target_path = target_dir + '/'+file_name
    #2.打开源文件和目标文件
    with open(source_path,'rb') as source_file:
        with open(target_path,'wb') as target_file:
            #3.循环读取源文件并拷贝到目标文件
            while True:

                data = source_file.read(1024)
                if data:
                   target_file.write(data)
                else:
                   break

if __name__ == "__main__":
    #1.定义源文件夹和目标文件夹
    source_dir = "Class"
    target_dir = "test"
    #2.创建目标文件夹
    try:
        os.mkdir(target_dir)
    except:
        print("目标文件夹已存在")
    #3.读取源文件夹文件列表
    file_list = os.listdir(source_dir)
    #4.循环文件列表中的文件进行拷贝
    for file_name in file_list:
        if not os.path.exists(target_dir+'/'+file_name):
          sub_process = multiprocessing.Process(target=copy_file,args=(file_name,source_dir,target_dir))
          sub_process.start()
        else:
            print(f"{file_name}文件已存在")