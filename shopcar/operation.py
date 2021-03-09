
import random
from user import User

id_list = []
def signup():
    id = random.randint(10000, 99999)
    check_id(id)
    id_list.append(id)
    uname = input("请输入用户名：")
    pwd = input("请输入密码：")
    user = User(uname,id,pwd)

def check_id(id):
    for d in id_list:
        if d == id:
            id = random.randint(10000, 99999)
            check_id(id)
        else:
            return id

