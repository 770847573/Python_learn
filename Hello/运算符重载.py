#1.__add__
class Person(object):
    def __init__(self,age):
        self.age = age
    def __add__(self, other):
        return self.age + other.age
    def __str__(self):
        return str(self.age)
    __repr__ = __str__
p1 = Person(12)
p2 = Person(14)
print(p1)
print(p1+p2)


#2.__lt__  less than小于
#__gt__  greater than 大于
#__le__ less equal 小于等于
#__ge__ greater equal 大于等于
#__eq__ equal 等于
#__ne__ not equal 不等于
#a.以上函数只能应用在指定的数据类型之间
print("abc" < "xyz")
print("abc".__lt__("xyz"))

#b.
class Person1(object):
    def __init__(self,age):
        self.age = age
    def __lt__(self, other):
        return self.age < other.age

p1 = Person1(40)
p2 = Person1(15)
print(p1 < p2)   #要求比较两个人的年龄