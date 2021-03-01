"""
2.设计两个类：
	a. 一个点Pointer类，属性包括x，y坐标。
	b. 一个Rectangle类（矩形）,属性有左上角坐标，宽，高
		方法：1. 计算矩形的面积；2. 判断点是否在矩形内
 	c.实例化一个点对象，一个正方形对象，输出矩形的面积，输出点是否在矩形内
"""
class Pointer(object):
    __slots__ = ("x","y")
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Rectangle(object):
    __slots__ =   ("left_top_point","width","height")
    def __init__(self,left_top_point,width,height):
        # left_top_point表示左上角的点的对象
        self.left_top_point = left_top_point
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    def isinner(self,other):
        # other是一个点的对象
        # x轴
        r0 = self.left_top_point.x <= other.x <= self.left_top_point.x + self.width
        # y轴
        r1 = self.left_top_point.y - self.height <= other.y <= self.left_top_point.y
        # x轴和y轴的条件都满足时，才表示指定点在矩形范围内
        return r0 and r1

# 创建左上角点的对象
left_top_point = Pointer(34,6)
# 创建矩形的对象
rectangle = Rectangle(left_top_point,40,10)
# 执行矩形的行为
print(rectangle.area())
# 创建一个任意的点
other_point = Pointer(-34,56)
print(rectangle.isinner(other_point))   # True:表示点在矩形内或者矩形上

"""
3.家具类(HouseItem) 有 名字 和 占地面积属性，其中
- 席梦思(bed) 占地 4 平米
- 衣柜(chest) 占地 2 平米
- 餐桌(table) 占地 1.5 平米

房子类(House) 有 户型、总面积 、剩余面积 和 家具名称列表 属性
- 新房子没有任何的家具
- 将 家具的名称 追加到 家具名称列表 中
- 判断 家具的面积 是否 超过剩余面积，如果超过，提示不能添加这件家具

a.将以上三件 家具对象 添加 到 房子对象 中
b.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
使用面向对象思想，编码完成上述功能。
"""
class HouseItem(object):
    def __init__(self,name,space):
        self.name = name
        self.space = space
class House(object):
    def __init__(self,type,total_area,free_area,itemlist=None):
        self.type = type
        self.total_area = total_area
        self.free_area = free_area

        if itemlist is None:
            itemlist = []
        self.itemlist = itemlist

    def add_item(self,item):
        # item表示家具的对象
        # 当家具的占地面积小于房子的剩余面积时，才能添加家具
        if item.space <= self.free_area:
            self.itemlist.append(item)

            # 重新计算房子的剩余面积
            self.free_area -= item.space

            # 输出信息
            print(f"家具{item.name}添加成功，户型为{self.type}的房子总面积为{self.total_area}，此时剩余面积为{self.free_area}，家具列表为{self.itemlist}")
        else:
            print("剩余面积不足，无法添加家具")

# 创建家具的对象
bed = HouseItem("席梦思床",2)
table = HouseItem("餐桌",1.5)

# 创建房子的对象
house = House("四室两厅两卫",130,100)
house.add_item(bed)
house.add_item(table)

print("*" * 30)

"""
学生类：姓名、年龄、学号、成绩
班级类：班级名称、学生列表
	显示所有学生
	根据学号查找学生
	添加一个学生
	删除一个学生（学生对象、学号）
	根据学号升序排序
"""
class Student(object):
    def __init__(self,name,age,stuid,score):
        self.name = name
        self.age = age
        self.stuid = stuid
        self.score = score
    def __str__(self):
        return f"姓名：{self.name},年龄：{self.age},学号：{self.stuid}，成绩：{self.score}"
    __repr__ = __str__

class Grade(object):
    def __init__(self, name,stulist):
        self.name = name
        # 将学生对象添加到stulist中
        self.stulist = stulist

    def show_all_stu(self):
        for stu in self.stulist:
            print(stu)

    def search_stu(self,stuid):
        for stu in self.stulist:
            if stu.stuid == stuid:
                print(stu)

    def add_stu(self,stu):
        if stu not in self.stulist:
            self.stulist.append(stu)

    def del_stu(self,stu):
        if stu in self.stulist:
            self.stulist.remove(stu)

    def sort_by_stuid(self):
        return sorted(self.stulist,key=lambda stu:stu.stuid)


# 创建学生的对象
s1 = Student("aaa",34,1001,99)
s2 = Student("aaa",45,1003,60)
s3 = Student("aaa",34,1002,100)

stu_list = [s1,s2,s3]

# 创建班级的对象
grade = Grade("二年一班",stu_list)
grade.show_all_stu()
grade.search_stu(1002)
# grade.add_stu(s2)

# s4 = Student("bbb",34,1006,100)
# grade.add_stu(s4)

print(grade.sort_by_stuid())