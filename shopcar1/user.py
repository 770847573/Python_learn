"""
用户类：
	姓名  用户id【这个标识对于每个用户而言是唯一的]】    密码     拥有购物车  用户登录状态【默认为 False 表示没有登录】
"""
class User(object):
    __slots__ = ("uid","uname","pwd","shopcar","islogin")
    def __init__(self,uid,uname,pwd,shopcar):
        self.uid = uid
        self.uname = uname
        self.pwd = pwd
        self.shopcar = shopcar
        # 用户登录状态【默认为 False 表示没有登录】
        self.islogin = False

    def __str__(self):
        return f"【User】用户id：{self.uid},姓名：{self.uname},登录状态:{self.islogin}"
    __repr__ = __str__
