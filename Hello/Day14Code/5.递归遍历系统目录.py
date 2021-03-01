# 需求：封装一个函数，将指定目录【文件夹】下所有的py文件打印出来
# 注意：需要获取指定目录以及子目录下的所有的py文件
import  os
def get_py_file(path):
    # 判断path是否存在
    if not os.path.exists(path):
        print("路径不存在，无法查找")
        # 后面的操作将没有执行的必要，则结束函数
        return

    # 判断path是否是文件
    if os.path.isfile(path):
        print("路径是文件，无法查找")
        if path.endswith(".py"):
            print("py文件：",path)
        return

    # 说明path是一个文件夹，则可以继续查找
    # 思路：获取文件夹中的所有内容，然后依次判断是文件还是文件夹，
    # 如果是文件，继续判断是否是py文件
    # 如果是文件夹，则继续向里查找

    # 获取文件夹中的所有内容
    all_list = os.listdir(path)
    # print(all_list)

    # 遍历列表
    for file_name in all_list:
        # 拼接路径
        sub_path = os.path.join(path,file_name)
        # print(sub_path)

        # 判断是否是文件夹
        if os.path.isdir(sub_path):
            # 文件夹
            # 则重复前面的步骤：获取---》遍历---》拼接----》判断
            # 所以使用递归
            get_py_file(sub_path)
        else:
            # 文件
            if sub_path.endswith(".py"):
                print("py文件：", sub_path)

if __name__ == '__main__':
    path = r"E:\Python study\Hello\Day14Code"
    get_py_file(path)

