"""
用户类：
	姓名  用户id【这个标识对于每个用户而言是唯一的]】    密码     拥有购物车  用户登录状态【默认为 False 表示没有登录】
"""

class User(object):
    __slots__ = ("uname","id","password","car","islogin")
    def __init__(self,uname,id,password,car):
        self.uname = uname
        self.id = id
        self.password = password
        self.car = car
        self.islogin = False
    def __str__(self):
        return f"姓名{self.uname},id{self.id},购物车：{self.car},登录状态：{self.islogin}"
    __repr__ = __str__