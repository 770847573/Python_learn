"""
购物车类：
	商品列表：程序初始时，商品列表为空
"""
class ShopCar(object):
    # 将购物车中的商品容器定义为字典，当添加商品的时候，让商品对象作为key，数量作为value
    __slots__ = ("goods_dict",)
    def __init__(self):
        # 程序初始时，商品列表为空
        self.goods_dict = {}

    def __str__(self):
        return f"【ShopCar】商品字典：{self.goods_dict}"
    __repr__ = __str__