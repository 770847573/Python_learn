"""
仓库类：【信息保存在本地磁盘：程序刚启动时把列表先存储到文件中，之后使用再读取出来】
	商品列表
	       商品名称    	价格        剩余量
		Mac电脑	   	20000    100
		PthonBook 	30	  	200
		草莓键盘         80      	60
		iPhone		7000		70
"""
import os,pickle

from goods import Goods
path = f"goods.txt"
name_list = ["Mac电脑","PthonBook","草莓键盘","iPhone"]
price_list = [2000,30,80,7000]
num_list = [100,200,60,70]

def singleton(cls):
    instance = None
    def get_instance(*args,**kwargs):
        nonlocal instance
        if not instance:
            instance = cls(*args,**kwargs)
        return instance
    return get_instance

@singleton
class Storage(object):
      __slots__ = ("goods_list",)
      def __init__(self):
          self.load_goods()

      def load_goods(self):
          if os.path.exists(path):
             self.read_file()
      # 程序第一次启动时，本地没有文件，将预设商品列表存储到本地文件
          else:
              self.goods_list = []
              for i in name_list:
                  goods = Goods(name_list[i],price_list[i],num_list[i])
                  self.goods_list.append(goods)
              self.write_file()

      def read_file(self):
          with open(path, "rb") as goods_file_r:
              file_list = pickle.load(goods_file_r)
              self.goods_list = file_list

      def write_file(self):
          with open(path, "wb") as goods_file_w:
              pickle.dump(self.goods_list, goods_file_w)


