#开房查询，从控制台输入名字，查询在kaifanglist.txt文件中的开房记录，如果没有，是一个单纯哥们，如果有的话，将其所有开房信息写入到以这哥们命名的文件中
import json
def check_kaifang():
    with open(r"kaifanglist.txt","r",encoding='utf-8') as kaifang_file:
        kaifang_list = kaifang_file.readlines()
    name = input("请输入人名：")

    for line in kaifang_list:
        if name == line.split(",")[0]:
            print(f"{name}被查到了，并记录")
            return write_data(line)
            break
    else:
         print(f"{name}是个单纯的大兄弟")



def write_data(info):
    name = info.split(',')[0]
    with open(f"开房记录/{name}.txt",'w',encoding='utf-8') as name_file:
        name_file.write(info)

check_kaifang()