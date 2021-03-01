#一、封装函数，显示指定路径下所有视频格式文件，如mp4，avi，rmvb等，并将找到的路径保存到列表中
import os
suffix_list = ('avi','mov','rmvb','rm','flv','mp4','3gp')
def get_view_file(path):
    if not os.path.exists(path):
        print('目录不存在')
        return
    if os.path.isfile(path):
        print('目录是文件，无法查找')
        if path.endswith(suffix_list):
            print('视频文件：',path)
            return

    all_file_list = os.listdir(path)

    for file in all_file_list:
        sub_file = os.path.join(path,file)
        #如果是文件夹，则重新执行函数
        if os.path.isdir(sub_file):
            get_view_file(sub_file)

        else:
            if sub_file.endswith(suffix_list):
              print('视频文件：',sub_file)
              return

if __name__ == '__main__':
    path = r'C:\Users\Administrator\Documents\WXWork\1688850252369970\Cache\Video'
    get_view_file(path)


#1.简述Python中列表，元组，字典以及集合各自的特点
#列表：是一种用于保存一系列有序项目的集合，可以用索引去指定某一个元素，使用中括号“[]”括起来，可以有重复重复元素，元素可以被方法操作改变。
#元祖：类似于列表，但是不能提供一些方法来改变其中的对象，使用圆括号“（）”括起来。
#字典：由多个键值（key）和值（value）组成，形式为K = {key = value1,key2 = value2},key值不可变，value可以是变量
# ，可以用["key"]来指定某一个元素
#序列（集合）：列表、元组和字符串可以看作序列（Sequence）的某种表现形式，是无序的，不允许有重复元素，可以使用切片的方法操作