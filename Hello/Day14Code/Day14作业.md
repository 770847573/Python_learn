一、封装函数，显示指定路径下所有视频格式文件，如mp4，avi，rmvb等，并将找到的路径保存到列表中

二、复习之前的内容，重点复习简单算法、深浅拷贝、列表切片、列表、字典和字符串的系统功能，装饰器，

三、总结之前提到的面试题

四、完成下面的线下周测试题

1.简述Python中列表，元组，字典以及集合各自的特点


2.简述Python中深拷贝和浅拷贝的区别并举例说明

3.简述值传递和引用传递的区别


4.写出下面代码的输出结果并说明原因

```Python
list1 = ['a', 'b', 'c', 'd', 'e']
print(list1[10:])   
```

5.写出下面代码的输出结果并说明原因

```Python
str1 = ‘hello python’
str1.title()
print(str1)       
```

6.写出下面代码的输出结果并说明原因

```Python
def text(l):
	l[1] = 10
list1 = [1,2,3,4]
text(list1)
print(list1)  
```

7.写出下面代码执行的结果并说明原因

```Python
list1=[5,3,1,9,12] 
func = (x for x in list1 if x%3==0) 
func()
print(type(func))  <class 'generator'>
```

8.写出下面代码执行的结果并说明原因

```Python
def fun(li=[]):    
  li.append("abc")
  return li 
print(fun()) 
print(fun())  
```

9.已知函数： 

```Python
def func(a=1,**kwargs):
  if len(kwargs)>0:
      for value in kwargs.values():
           a += value
      print(“a=”,a)      # a= 8
```

调用函数func(n1=3,n2=4)打印的结果是

10.采用至少三种方式实现两个变量的值交换
x = 2
y = 3


11.封装函数，将一个字符串倒序，并返回结果【至少采用两种方式】

12.编写程序，找到下面字典中年龄最大的人，并输出
persons = {“li":18,"wang":50,"zhang":20,"sun":22}

13.封装函数，对某个列表进行排序，用冒泡实现降序排序，用选择实现升序排序

14.封装函数，统计某个字符串中出现频率最高的字符(单个符号)及其出现次数


15.封装函数，生成指定长度的验证码，要求全部由数字组成