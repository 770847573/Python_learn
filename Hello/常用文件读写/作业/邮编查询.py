#需求：邮编查询，读取 youbian.txt 文件中的数据， 完成邮编查询的操作，从控制台输入邮编号，如果有此邮编，请输出对应的城市，否则提示无此邮编
#方式一：切片
def get_city1():
    with open(r"youbian.txt", "r", encoding="utf-8") as postcode_file:
        postcode_list = postcode_file.readlines()
        #print(postcode_list) #'[110100,"北京市市辖区"],\n'……………………
    postcode_input = input("请输入邮编：")

    for part in postcode_list:
        if postcode_input == part[1:7]:
           print(f"邮编{postcode_input}存在，地址为{part[9:-4]}")
           break
    else:
        print("邮编不存在")
#get_city1()

#方式二：eval()，可以将一个字符串中有效的python代码识别出来，并执行

def get_city2():
    with open(r"youbian.txt", "r", encoding="utf-8") as postcode_file:
        postcode_list = postcode_file.readlines()
        #print(postcode_list)
    postcode_input = input("请输入邮编：")
    for data in postcode_list:

        real_data = data.rstrip(",\n")#'[110100,"北京市市辖区"],\n'----->[110100,"北京市市辖区"])
        real_data_list = eval(real_data)
        if postcode_input == str(real_data_list[0]):
           print(f"邮编{postcode_input}存在，地址为{real_data_list[1]}")
           break
    else:
        print("邮编不存在")


get_city2()