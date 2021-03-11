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

	添加商品到购物车 ——》验证用户是否登录，没有登录提示登录
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
import  os,pickle,random
from shopcar1.shopcar import ShopCar
from shopcar1.user import User
from shopcar1.storage import Storage
from shopcar1.goods import Goods

path = r"userlist.txt"

class Operation(object):
    # 定义实例属性user_dict，key是用户id，value是用户对象
    __slots__ =  ("user_dict",)

    # 当程序启动时，需要判断保存用户的文件是否存在
    def __init__(self):
        self.__load_users()

    def __load_users(self):
        # 判断保存用户的文件是否存在，根据是否存在决定进行序列化还是反序列化
        # 假设：保存用户的文件名为userlist.txt
        if os.path.exists(path):
            # 存在
            with open(path,"rb") as f:
                self.user_dict = pickle.load(f)
        else:
            # 不存在
            # 注意：如果文件不存在，则定义一个空字典，当用户注册完毕，将用户对象添加到字典中，最后序列化到本地
            self.user_dict = {}

    # 生成用户随机id，该操作只在当前类中进行，所以私有化
    def __get_uid(self):
        # 问题：用户id一般是惟一的，但是获取随机数有可能重复，所以应该先判断
        while True:
            uid = str(random.randint(10000, 99999))
            if uid not in self.user_dict:
                print(f"当前获取的用户id为{uid}")
                return uid

    # 序列化用户，一旦用户的信息发生改变，则需要将数据和本地文件中的数据进行同步
    def save_user(self):
        with open(path,"wb") as f:
            pickle.dump(self.user_dict,f)

    # 用户注册
    def user_register(self):
        # 获取uid
        uid = self.__get_uid()
        # 引导用户输入自己的用户名和密码
        username = input("请输入你的用户名：")
        pwd = input("请输入你的密码：")
        # 创建购物车对象
        sp = ShopCar()

        # 根据上述信息创建一个用户对象
        user = User(uid=uid,uname=username,pwd=pwd,shopcar=sp)

        # 将用户添加到字典中
        self.user_dict[uid] = user

        # 将用户信息和本地磁盘进行同步
        self.save_user()

        print("注册成功！！！")

    # 用户登录
    def user_login(self):
        uid = input("请输入你的用户id：")
        if uid not in self.user_dict:
            print("对不起，你还未注册账号，请先注册")
            return

        # 判断用户的登录状态【第二次第三次....运行程序需要做的操作】
        user = self.user_dict[uid]
        if user.islogin:
            print("已经在登录状态，无需再次登录")
            return user

        # 说明未登录过【第一次登录】
        count = 0
        while True:
            count += 1
            if count > 3:
                print("已经错误三次,禁止登录")
                break
            name = input("请输入你的用户名：")
            pwd = input("请输入你的密码：")
            # 校验
            if name == user.uname and pwd == user.pwd:
                print("登录成功")
                # 更新用户的登录状态
                user.islogin = True
                return user
            else:
                print("用户名或密码错误，请重新输入")

    # 添加商品到购物车
    def add_goods(self):
        # 操作购物车之前，一定要检测用户是否则登录状态
        user = self.user_login()
        if not user:
            print("还未登录，请先登录")
            return

        # 下面商品的编号尽量和仓库中的商品的保存顺序相同，方便获取
        print("""仓库中的商品如下：
        0：Mac电脑,
        1：food,
        2：book,
        3：kindle""")

        # 获取仓库对象
        storage = Storage()

        index = input("请输入需要购买的商品编号：")
        if index.isdigit() and index in [str(x) for x in range(4)]:
            # index需要作为商品在仓库中的下标，所以转化为整型
            index = int(index)
            # 从仓库中获取指定编号的商品对象
            sto_goods = storage.goods_list[index]
            # 引导用户输入需要购买的商品的数量
            num = int(input(f"请输入需要购买的商品{sto_goods.gname}的数量："))
            if num < 0:
                print("输入有误")
            else:
                while num > sto_goods.free_num:
                    num = int(input(f"{sto_goods.gname}的剩余量为{sto_goods.free_num},请重新输入数量："))
                else:
                    # 重新创建一个商品对象，用于添加到当前用户的购物车中
                    ugoods = Goods(sto_goods.gname,sto_goods.price,num)
                    # 将商品对象添加到当前用户的购物车中
                    user.shopcar.goods_dict[ugoods] = num   # 让商品对象作为key，数量作为value

                    # 仓库中的商品数量需要减少
                    sto_goods.free_num -= num

                    # 数据的同步：商品和用户
                    self.save_user()
                    storage.save_goods()

                    print(f"商品{sto_goods.gname}添加购物车成功！！！")
                    print(user.shopcar)
        else:
            print("商品编号输入有误")

    # 从购物车中删除商品
    def del_goods(self):
        user = self.user_login()
        if not user:
            print("还未登录，请先登录")
            return

        gname = input("请输入需要删除的商品名称：")

        # 定义一个变量，用于记录需要删除的购物车中的对象
        ugoods = None
        # 定义一个变量，用于记录需要删除的商品在仓库中的商品对象
        sto_goods = None
        # 用于标记商品在购物车中是否存在
        flag = False

        # 寻找购物车中的商品对象
        for goods in user.shopcar.goods_dict:
            if goods.gname == gname:
                ugoods = goods
                flag = True

        if not flag:
            print(f"商品{gname}不存在")
            return

        # 寻找仓库中对应的商品对象
        storage = Storage()
        for goods in storage.goods_list:
            if goods.gname == gname:
                sto_goods = goods

        num = int(input(f"请输入需要删除的商品{gname}的数量:"))

        if num >= user.shopcar.goods_dict[ugoods]:
            # 全部删除
            # 删除购物车中的键值对
            user.shopcar.goods_dict.pop(ugoods)
            # 添加到仓库中
            sto_goods.free_num  += ugoods.free_num
        else:
            # 部分删除
            # 减少部分
            ugoods.free_num -= num
            # 更新字典
            user.shopcar.goods_dict[ugoods] = ugoods.free_num
            # 添加到仓库中
            sto_goods.free_num += num

        # 同步数据
        self.save_user()
        storage.save_goods()

        print("购物车中的商品删除成功！！！")

    # 购物车结算
    def get_total(self):
        user = self.user_login()
        if not user:
            print("还未登录，请先登录")
            return

        # 计算总价格
        total = 0
        for goods, num in user.shopcar.goods_dict.items():
            total += goods.price * num
        print(f"结算成功，所有商品总计为：{total}")

        # 清空购物车
        user.shopcar.goods_dict.clear()

        # 同步数据
        self.save_user()

    # 退出登录
    def quit_login(self):
        user = self.user_login()
        if user:   # user为真，则表示已经在登录状态，为None，则表示没有登录
            user.islogin = False
            self.save_user()

        print("用户注销成功！！！")


