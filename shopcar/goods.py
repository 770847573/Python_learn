"""
商品类：
	商品名称   商品价格   商品剩余量
"""
class Goods(object):
    __slots__ = ("gname","price","free_num")
    def __init__(self,gname,price,free_num):
        self.gname = gname
        self.price = price
        self.free_num = free_num
    def __str__(self):
        return f"商品名称：{self.gname},价格为：{self.price},剩余量：{self.free_num}"
    __repr__ = __str__