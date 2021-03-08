"""
对象的序列化和反序列化

序列化：将python中的对象持久化到磁盘上（写入）
反序列化：将磁盘上的内容读取出来，转化为python对象（读取）
"""
import pickle
#1.基本语法
#写入
f1 = open("p1.txt",'wb')
pickle.dump("hello",f1)
f1.close()

#读取
f2 = open("p1.txt",'rb')
r2 = pickle.load(f2)
print(r2)
f2.close()

#2.python中任意的对象都可以被序列化和反序列化
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(fr"姓名：{self.name}")

p = Person("Tom",12)
#将实例对象写入文本文件
f3 = open(r"person1.txt","wb")
pickle.dump(p,f3)
f3.close()
#读取
f4 = open(r"person1.txt","rb")
r4 = pickle.load(f4)
print(r4)
r4.show()
f4.close()