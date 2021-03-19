import re
"""
1.用户名匹配 

			要求:	1.用户名只能包含数字 字母 下划线

					2.不能以数字开头 

					3.⻓度在 6 到 16 位范围内

"""
def check_username():
    try:
        username = input("请输入用户名：")
        r = re.match(r"^[a-zA-Z_][0-9a-zA-Z_]{5,15}$", username)
        print(r.group())
    except BaseException as e:
        print(e)


"""
2.密码匹配 

			要求:	1.不能包含!@#¥%^&*这些特殊符号

					2.必须以字母开头 

					3.⻓度在 6 到 12 位范围内

"""
def check_pwd():
    try:
        pwd = input("请输入密码：")
        r = re.match(r"^[a-zA-Z][^%^&*]{5,11}$", pwd)
        print(r.group())
    except BaseException as e:
        print(e)

"""
3.已知有文件test.txt里面的内容如下，查找文件中以1000phone开头的语句，并保存到列表中

    1000phone hello python
    1000phone
    mobiletrain 大数据
    1000phone java
    mobiletrain html5
    mobiletrain 云计算
"""

def findword():
    with open("test.txt",'r',encoding="utf-8") as test:
        f = test.read()
        word = re.findall(r'^1000phone.*',f,flags=re.M)
        print(word)

"""
4.提取用户输入数据中的数值 (数值包括正负数 还包括整数和小数在内) 并求和 

    例如:“-3.14good87nice19bye000255.565” =====> -3.14 + 87 + 19 = 102.86
"""

def extract_digital():
    words = input('请输入一串字符：')
    digial_list = re.findall(r'[-]?(?:0|[1-9]\d*)(?:\.\d*)?',words)
    print(digial_list)
    k = 0
    for item in digial_list:
        k += float(item)
    print(k)
extract_digital()
