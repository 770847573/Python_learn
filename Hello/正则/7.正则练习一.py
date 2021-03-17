# 1.要求从控制台输入用户名和密码，如果用户名和密码都输入合法，则注册成功
"""
要求：
    用户名：只能由数字或字母组成，长度为6~12位
    密码：只能由数字组成，长度必须为6位
"""
import  re
username = input("请输入用户名：")
pwd = input("请输入密码：")

# 匹配上，返回一个对象，匹配不上，返回None
r1 = re.match(r"^[0-9a-zA-Z]{6,12}$",username)
r2 = re.match(r"^\d{6}$",pwd)

if r1 and r2:
    print("注册成功")
else:
    print("注册失败")




