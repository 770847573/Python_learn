"""
程序
	因为一个程序可能有很多用户，则需要将用户保存在本地
			将注册的用户添加在字典中
				key：用户id 【用户id随机产生即可，从10000~99999中随机产生一个】
				value：对应的用户对象

	行为：
	用户注册——》根据下面信息生成一个用户，并将用户保存在本地
		随机产生 id
		输入姓名和密码
		创建一个购物车对象


	登录 ——》 登录成功返回为 True  否则返回为 False
		输入用户id 检测是否有该用户  没有的话提示注册
		有的话检测用户登录状态 若为 True  提示已登录
		否则 再输入密码进行登录
			不要忘记修改用户的登录状态

	购买商品 ——》验证用户是否登录，没有登录提示登录
		否则
			列出仓库中商品名单
				1. Mac电脑
				2.PthonBook
				3.草莓键盘
				4.iPhone
			用户输入对应的编号 在仓库中获得对应的商品
			用户输入数量 — 与该商品的的剩余量对比
				> 剩余量
					让用户重新输入并提示该商品的剩余量
				<=剩余量
					将该商品添加在该用户的购物车中
					并将仓库中的数据量做出相应的减少
				注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性

	删除购物车的商品——》验证用户是否登录，没有登录提示登录
		否则
			请用户输入商品名字 查看该用户的购物车中是否有该商品
			如果没有，提示购物车中没有该商品
			否则：
				先选择要删除的商品
				请用户设置删除的数量
					数量  >=   购物车中商品数量
						购物车清单中删除该商品
					否则：
						购物车清单中做出相应的减少
			注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性


	结算——》验证用户是否登录 没有登录提示登录
		否则
			获取该用户的购物车中商品清单，计算总额
		注意： 结算完成 购物车清空
			  将修改之后的结果同步在本地文件中，时刻保持数据的正确性


	退出登录———》验证用户是否登录 没有登录提示登录
		否则
			修改用户登录状态
		注意：将修改之后的结果同步在本地文件中，时刻保持数据的正确性

"""
import random,os,pickle
from user import User
from shop_car import Shopcar
from storage import Storage
from goods import Goods

path = f"userlist.txt"


class Operation(object):

    __slots__ = ("user_dict", "current_id")

    def __init__(self):
        self.__load_user()

    # 加载用户信息
    def __load_user(self):
        if os.path.exists(path):
            with open(path,'rb') as f:
                self.user_dict = pickle.load(f)
        else:
            # 第一次启动程序，还未登陆过
            self.user_dict = {}
        self.current_id = None

    # 获取新的id
    def get_new_id(self):
        while True:
            user_id = random.randint(10000,99999)
            if user_id not in self.user_dict: # 说明此id没有生成过
                return user_id
    # 同步本地用户数据

    def save_user(self):
        with open(path,'wb') as user_file_w:
            pickle.dump(self.user_dict, user_file_w)

    # 注册
    def register(self):
        new_id = self.get_new_id()
        print(f"用户id为{new_id}")
        uname = input("请输入用户名：")
        pwd = input("请输入密码：")
        shopcar = Shopcar()
        user = User(uname=uname, id=new_id, password=pwd, car=shopcar)
        # 将用户对象添加到字典
        self.user_dict[new_id] = user
        self.save_user()

    # 检测登录状态
    def check_login(self):
        if self.current_id:
            return self.user_dict[self.current_id]
        else:
            print("还未登录")
            return False

    def login(self):
        uid = int(input("请输入用户id："))
        if uid not in self.user_dict:
            print("用户id未注册，请注册")
            return
        # 获取该用户对象
        user = self.user_dict[uid]
        # 判断是否已经登录
        # 已经是登录状态
        if user.islogin :
            self.current_id = uid
            print("已经登录，无需输入密码")
            return user
        else:  # 还未登录
            count = 0
            while True:
                count += 1
                if count == 3:
                    print("还有两次错误机会")
                if count > 5:
                    print("错误次数过多，禁止登录")
                    break

                uname = input("请输入用户名：")
                pwd = input("请输入密码：")
                if uname == user.uname and pwd == user.password:
                    print("登录成功！！！")
                    self.current_id = uid
                    user.islogin = True
                    self.save_user()
                    return user
                else:
                    print("用户名或密码错误，请重新输入")

    def add_shopcar(self):
        user = self.check_login()
        if not user:
            print("还未登录，请先登录")
            return
        print("""
         仓库中还有以下商品：
         0.Mac电脑
         1.PthonBook
         2.草莓键盘
         3.iPhone
         """)
        choice = int(input("请输入你要买的商品相应的编号"))
        storage = Storage()
        # 获取仓库中的商品对象
        sto_goods = storage.goods_list[choice]
        buy_num = int(input("请输入购买的数量："))
        if buy_num < 0:
            print("输入有误")
        else:
            while buy_num > sto_goods.free_num:
                buy_num = int(input(f"{sto_goods.gname}还剩{sto_goods.free_num}件，请重新输入"))
            else:
                # 购物车已经有了同款商品，只需修改数量即可
                for goods in user.car.goods_dic:
                    if sto_goods.gname == goods.gname:
                        goods.free_num += buy_num
                        user.car.goods_dic[goods]= goods.free_num
                        sto_goods.free_num -= buy_num
                        print(f"{sto_goods.gname}{buy_num}件添加购物车成功！！")
                        print(user.car)
                        break


                else:
                    # 添加的商品在购物车里没有同款
                    # 创建一个新的商品对象添加到购物车中
                    shopcar_goods = Goods(sto_goods.gname, sto_goods.price, buy_num)
                    user.car.goods_dic[shopcar_goods] = buy_num
                    sto_goods.free_num -= buy_num
                    print(f"{sto_goods.gname}{buy_num}件添加购物车成功！！")
                    print(user.car)
                # 同步本地数据
                self.save_user()
                storage.save_goods()

    def del_shopcar(self):
        user = self.check_login()
        if not user:
            print("还未登录，请先登录")
            return
        goods_name = input("请输入要删除的商品名称")
        # 定义一个变量，记录需要删除的购物车中的商品对象
        ugoods = None
        # 定义变量，记录仓库中的商品对象
        sto_goods = None
        # 定义变量，记录购物车中商品是否存在
        flag = False

        # 寻找购物车中的商品
        for goods in user.car.goods_dic:
            if goods_name == goods.gname:
                ugoods = goods
                flag = True
        if not flag:
            print("商品不存在")
            return
        # 寻找仓库中的商品
        storage = Storage()
        for sgoods in storage.goods_list:
            if sgoods.gname == goods_name:
                sto_goods = sgoods

        del_num = int(input("请输入删除的数量"))
        if del_num >= user.car.goods_dic[ugoods]:
            print(f"清空购物车中的{goods_name}")
            user.car.goods_dic.pop(ugoods)
            sto_goods.free_num += ugoods.free_num
        else:
            # 减少部分
            ugoods.free_num -= del_num
            user.car.goods_dic[ugoods] = ugoods.free_num
            sto_goods.free_num += del_num
            print(f"{ugoods.gname}删除{del_num}成功")

        self.save_user()
        storage.save_goods()

    def total(self):
        user = self.check_login()
        if not user:
            print("还未登录，请先登录")
            return
        total_price = 0
        for goods,num in user.car.goods_dic.items():
            total_price += goods.price * num
        print(f"结算成功，总价格为{total_price}元")
        # 清空购物车
        user.car.goods_dic.clear()
        self.save_user()

    def logoff(self):
        user = self.check_login()
        if not user:
            print("还未登录")
            return
        else:
            user.islogin = False
            self.current_id = None
            print("注销成功")
        self.save_user()








