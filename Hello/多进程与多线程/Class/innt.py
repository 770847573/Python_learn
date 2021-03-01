class Person:
    def __init__(self,name):
        self.name = name
    def say_Hi(self):
        print('Hello,my name is',self.name)
p = Person('侯钰相')
p.say_Hi()