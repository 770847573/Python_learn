class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
      return f"姓名：{self.name},年龄：{self.age}"

    __repr__ = __str__

p1 = Person("老王",55)
print(p1)
p2 = Person("小王",22)
print([p1,p2])