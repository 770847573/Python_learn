class Robert():
    population = 0
    def __init__(self,name):
        """初始化数据"""
        self.name = name
        print('初始化{}'.format(self.name))
        Robert.population += 1
    def die(self):
        """销毁"""
        Robert.population-=1
        print("{}已经被销毁，还剩下{}个机器人".format(self.name,Robert.population))


    def say_hi(self):
        print('你好啊，我是你创造的{}',format(self.name))

    @classmethod
    def how_many(cls):
        print('现在有{}个机器人'.format(cls.population))

R1 = Robert('小强')
R1.say_hi()
R1.how_many()
R2 = Robert('小李')
R2.how_many()

R1.die()