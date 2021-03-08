#csv: Comma Separated Values  逗号分隔值
#.csv是一种特殊的文本格式
#作用：主要采用来不同程序间进行数据交换，在爬虫中应用较多
#特点：可以用Excel打开，csv文件读写需要借助csv模块
import csv

#读取
def read_csv():
    f = open(r"csv文件.csv",'r',encoding='utf-8')
    data = csv.reader(f) #data是一个可迭代对象,其中元素是列表
    print(data)
    #如果要打印，需要遍历
    for info in data:
        print(info)
    f.close()
read_csv()

#写入
def write_csv():
    with open(r"csv2.csv",'w',encoding='utf-8',newline='') as csv2:  #newline默认为/n，换行
        r1 = csv.writer(csv2)#得到一个空的可迭代对象
        #写入字符串，每个字符串会用逗号隔开
        #r1.writerow("hello")
        row_list = [['ads','fef','gtgt'], ['ads','fef','gtgt'], ['ads','fef','gtgt']]
        for line in row_list:
           r1.writerow(line)

write_csv()

