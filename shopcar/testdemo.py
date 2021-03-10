# 测试
from shopcar.operation import Operation

def main():
    op = Operation()
    print("欢迎进入xxx购物系统".center(40,"*"))
    print("""本系统提供了如下功能：
    0.用户注册
    1.用户登录
    2.添加商品
    3.删除商品
    4.结算购物车
    5.注销登录
    6.退出系统""")

    while True:
        select = input("请输入你需要进行的操作：")
        if select == "0":
            op.register()
        elif select == "1":
            op.login()
        elif select == "2":
            op.add_shopcar()
        elif select == "3":
            op.del_shopcar()
        elif select == "4":
            op.total()
        elif select == "5":
            op.logoff()
        elif select == "6":
            print("欢迎再次光临~~~~")
            break
if __name__ == '__main__':
    main()