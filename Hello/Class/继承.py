class schoolmember():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('初始化学校成员{}'.format(self.name))
    def tell(self):
        print("姓名：{},年龄：{}".format(self.name,self.age),end=' ')
class student(schoolmember):
    def __init__(self,name,age,mark):
        schoolmember.__init__(self,name,age)
        self.mark = mark
        print('初始化学生{}'.format(self.name))
    def tell(self):
        schoolmember.tell(self)
        print('分数：{}'.format(self.mark))
class teacher(schoolmember):
    def __init__(self,name,age,salary):
        schoolmember.__init__(self,name,age)
        self.salary = salary
        print('初始化老师{}'.format(self.name))
    def tell(self):
        schoolmember.tell(self)
        print('学科:{}'.format(self.salary))

t = teacher('王老师',47,'语文')
s = student('大刘',16,99)
t.tell()
s.tell()