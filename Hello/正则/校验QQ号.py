"""
1.全是数字
2.位数为5-11
3.不能0开头
"""
def chekqq():
    resalut = True
    qqnum = input("请输入QQ号")
    if qqnum.isdigit():
        if len(qqnum) >= 5 and len(qqnum) <= 11:
            if qqnum[0] == "0":
                resalut = "首位不能为0"
        else:
            resalut = "QQ号必须为5-11位"
    else:
        resalut = "QQ号必须全为数字"

    return resalut


import re
# 使用正则判断
def checkQQ():
    QQnum = input("输入QQ号")
    r = re.match(r"^[1-9][0-9]{4,10}$", QQnum)
    print(r)

def checkphone():
    phonenum = input("请输入手机号：")
    r = re.match(r"^[1][3-9][0-9]{9}$",phonenum)
    if  not r:
        print("手机号格式不正确")

checkphone()


