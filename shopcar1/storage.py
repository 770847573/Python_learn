"""
仓库类：【信息保存在本地磁盘：程序刚启动时把列表先存储到文件中，之后使用再读取出来】
	商品列表
	       商品名称    	价格        剩余量
		Mac电脑	   	20000    100
		PthonBook 	30	  	200
		草莓键盘         80      	60
		iPhone		7000		70
"""
import  os,pickle
from shopcar1.goods import Goods       # 注意：导入类和导入函数以及变量的方式相同

# 假设存储仓库中商品列表的文件名为goodslist.txt
path = r"goodslist.txt"

# 任何用户，任何一次访问到仓库的时候应该访问的都是同一个仓库，所以需要将仓库类定义为单例类
def singleton(cls):
    instance = None
    def getinstance(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args,**kwargs)
        return instance
    return getinstance

@singleton
class Storage(object):
    __slots__ = ("goods_list",)

    # 如果程序第一次启动：文件不存在，需要商品列表先存储到文件中
    # 如果程序第二次以上启动：文件存在，则需要将文件中的内容读取出来
    def __init__(self):
        # 注意：在实际项目开发中，建议早构造函数中的代码尽量简洁
        self.__load_goods()

    # 加载商品，对于其中的操作，只在当前类中可以进行
    def __load_goods(self):
        if os.path.exists(path):
            # 存在，说明程序不是第一次运行
            self.get_goods()
        else:
            # 不存在，说明程序是第一次运算
            # a.定义商品列表，用于存储仓库中的商品对象
            self.goods_list = []

            # b.模拟商品信息
            name_list = ["Mac电脑","food","book","kindle"]
            price_list = [130000,20,78,500]
            num_list = [100,100,100,100]

            # c.遍历上述三个列表，将对应的信息获取出来，然后创建商品对象并添加到商品列表中
            for i in range(len(name_list)):
                goods = Goods(name_list[i],price_list[i],num_list[i])
                self.goods_list.append(goods)

            # d.将商品列表存储到文件中【对象的序列化和反序列化】
            self.save_goods()

    def save_goods(self):
        with open(path, "wb") as f:
            pickle.dump(self.goods_list, f)

    def get_goods(self):
        with open(path, "rb") as f:
            self.goods_list = pickle.load(f)