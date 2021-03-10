"""
购物车类：
	商品列表：程序初始时，商品列表为空
"""
class Shopcar(object):
    #将购物车中的商品容器定义为字典，key为商品对象，数量为value
    __slots__ = ("goods_dic",)
    def __init__(self):
        self.goods_dic = {}
    def __str__(self):
        return f"商品列表：{self.goods_dic}"
    __repr__ = __str__