### 作业讲解

> ```Python
> students = [
> {'name': '小花', 'age': 19, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '明明', 'age': 20, 'score': 40, 'gender': '男', 'tel':
> '15300022838'},
> {'name': '华仔', 'age': 18, 'score': 90, 'gender': '女', 'tel':
> '15300022839'},
> {'name': '静静', 'age': 16, 'score': 90, 'gender': '不明', 'tel':
> '15300022428'},
> {'name': 'Tom', 'age': 17, 'score': 59, 'gender': '不明', 'tel':
> '15300022839'},
> {'name': 'Bob', 'age': 18, 'score': 90, 'gender': '男', 'tel':
> '15300022839'}
> ]
> # a.统计不及格学生的个数
> count = 0
> for stu_dict in students:
>     if stu_dict["score"] < 60:
>         count += 1
> print("不及格学生的个数：%d" % (count))
> 
> # b.打印不及格学生的名字和对应的成绩
> for stu_dict in students:
>     if stu_dict["score"] < 60:
>         print("姓名：%s,成绩：%d" % (stu_dict['name'],stu_dict['score']))
> 
> # c.统计未成年学生的个数
> count = 0
> for stu_dict in students:
>     if stu_dict["age"] < 18:
>         count += 1
> print("未成年学生的个数：%d" % (count))
> 
> # d.打印手机尾号是8的学生的名字
> for stu_dict in students:
>     if stu_dict["tel"][-1] == "8":
>         print("姓名：%s" % (stu_dict['name']))
> 
> # e.打印最高分和对应的学生的名字
> # 方式一
> # max_score = students[0]['score']
> # for stu_dict in students:
> #     if stu_dict['score'] > max_score:
> #         max_score = stu_dict['score']
> 
> # 方式二
> max_score = max([stu_dict["score"] for stu_dict in students])
> print("最高成绩为：%d" % (max_score))
> for stu_dict in students:
>     if stu_dict['score'] == max_score:
>         print("姓名：%s,成绩：%d" % (stu_dict['name'],max_score))
> 
> # f.删除性别不明的所有学生
> # 方式一
> # new_students = []
> # for stu_dict in students:
> #     if stu_dict["gender"] != "不明":
> #         new_students.append(stu_dict)
> # print(new_students)
> 
> # 方式二
> # for stu_dict in students[:]:
> #     if stu_dict['gender'] == "不明":
> #         students.remove(stu_dict)
> # print(students)
> 
> # g.将列表按学生成绩从大到小排序
> # 方式一:冒泡排序
> # for i in range(len(students) - 1):
> #     for j in range(len(students) - i - 1):
> #         # 比较的是成绩，交换的是字典
> #         if students[j]["score"] < students[j + 1]['score']:
> #             students[j],students[j + 1] = students[j + 1],students[j]
> # print(students)
> 
> # 扩展：方式二:sort(key),key用于指定排序的规则,此处使用的是匿名函数
> students.sort(key=lambda stu_dict:stu_dict['score'],reverse=True)
> print(students)
> 
> # 1.dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]，
> # 按照字典中的成绩对列表进行降序排序 【使用排序算法】
> students = [{'科目':'政治', '成绩':98}, {'科目':'语文', '成绩':77}, {'科目':'数学', '成绩':99}, {'科目':'历史', '成绩':65}]
> for i in range(len(students) - 1):
>     for j in range(len(students) - i - 1):
>         # 比较的是成绩，交换的是字典
>         if students[j]["成绩"] < students[j + 1]['成绩']:
>             students[j],students[j + 1] = students[j + 1],students[j]
> print(students)
> 
> # 2.dict_list = [{“科目”:“政治”, “成绩”:98}, {“科目”:“语文”, “成绩”:77}, {“科目”:“数学”, “成绩”:99}, {“科目”:“历史”, “成绩”:65}]，
> # 去除列表中成绩小于70的字典 【列表推导式完成】
> new_students = [stu_dict for stu_dict in students if stu_dict['成绩'] >= 70]
> print(new_students)
> ```

### 一、数字类型【重点掌握】

#### 1.数学功能

> 内置功能
>
> - abs(x):返回数字的绝对值
> - (x>y)-(x<y):比较大小，
> - max(x1,x2,…):返回给定参数的最大值
> - min(x1,x2,…):返回给定参数的最小值
> - pow(x,y):求x的y次方的值
> - round(x,n):返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数
>
> 导入math模块  import math;
>
> - ceil(x):返回x的上入整数，不能直接访问，需要通过math访问，即math.ceil(18.1)	
>
> - floor(x):返回x的下入整数，同ceil的用法
>
> - modf(x):返回x的整数部分和小数部分，两部分的数值符号与x相同，整数部分以浮点型表示，同ceil的用法
>
> - sqrt(x):返回数字x的平方根，返回类型为浮点型
>
> 数学常量
>
>   math.pi ：圆周率
>   math.e ：自然常数
>
> ```Python
> # 一、内置函数
> # 【面试题】列举5个常用的内置函数并说明他们的作用
> # print()  input()
> 
> # 1.abs()：求绝对值
> print(abs(-18))
> 
> # 2.求最值
> print(max(45,4,7,74,76))
> print(min(34,6,6,4,654))
> 
> # 3.pow(x,y):求x的y次方
> print(pow(5,3))
> 
> # 4.sum(容器):求和
> print(sum([12,3]))
> print(sum((45,4,65)))
> print(sum({45,4,65}))
> print(sum((45,4,65),10))
> 
> # 5.round(x,y):求四舍五入
> # 如果省略y，则结果为四舍五入的整数，如果y未被省略，则表示需要保留的小数点后的位数
> print(round(8.23))
> print(round(8.73))
> 
> print(round(8.23,1))
> print(round(8.26,1))
> 
> print(round(8.233454,3))
> print(round(8.263854,3))
> 
> # 练习：求1~100之间所有整数的和
> print(sum(range(1,101)))
> print(sum(range(0,101,2)))
> 
> # 二、math模块中的功能，math.xxx()
> # 导入模块
> # 注意：创建py文件的时候，一定注意不要和系统的模块重名
> import  math
> # 1.ceil():向上取整
> print(math.ceil(16.9))
> print(math.ceil(16.1))
> 
> # 2.floor()：向下取整
> print(math.floor(16.9))
> print(math.floor(16.1))
> 
> # 3.sqrt():求算术平方根，结果为一个浮点型
> print(math.sqrt(9))   # 3.0
> 
> # 4.常量
> print(math.pi)   # 圆周率
> print(math.e)   # 自然常数
> ```

#### 2.随机数功能

> random模块中的相应函数
>
> ​	random.choice()
>
> ​	random.randint()
>
> ​	random.randrange()
>
> ​	random.random()
>
> ​	random.uniform()
>
> ```Python
> """
> random模块中的相应函数
> 	random.choice()                 ******
> 	random.randint()
> 	random.randrange()
> 	random.random()                 *****
> 	random.uniform()
>     random.sample()
> """
> # import  random
> from  random import  *     # 从random模块中导入所有内容
> 
> # 1.choice(seq),seq表示一个序列，可以是列表，字符串，元组等有序的集合，也可以是range()
> # 注意1：seq只能是有序的集合
> n1 = choice([34,3,65,6])
> print(n1)
> n2 = choice((34,3,65,6))
> print(n2)
> n3 =  choice("hfahfaf")
> print(n3)
> 
> # 注意2：如果序列存在，则直接使用，如果不存在，则通过range生成
> print(choice(range(1,100)))
> print(choice(range(0,100,2)))
> 
> # 2.randint(start,end):和range(start,end,step)的区别在于，randint是一个闭区间
> # 3.randrange(start,end,step),其中的start,end,step和range中的用法完全相同
> # 需求：在1~100之间产生一个随机数
> print(choice(range(1,101)))   # 包头不包尾
> print(randint(1,100))   # 闭区间
> print(randrange(1,101))     # 包头不包尾
> 
> # 注意：choice(range(start,end,step))、randint(start,end)、randrange(start,end,step)
> print(choice(range(1,101,2)))
> print(randint(1,100))
> print(randrange(1,101,2))
> 
> # 4.random():获取0~1之间的一个随时数
> print(random())
> print(round(random(),2))
> # 思考问题：生成20~100之间的随机数，包含整数和浮点数
> # [0,1]--->[0,80]---->[20,100]
> print(random() * 80 + 20)
> """
> 结论：
>     求n~m（m > n）之间的任意一个随机数，包含整数和浮点数
>     则随机数可以表示为：random() * (m - n) + n
> """
> 
> # 5.uniform(n,m)
> print(uniform(20,100))
> 
> # 6.sample()；根据指定的数量，随机抽样，结果为一个列表
> print(sample("5674562",3))
> print(sample([34,4,6,56,56,5],3))
> ```

### 二、集合【掌握】

#### 1.概念

> Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算
>
> set与dict类似，但是与dict的区别在于只是一组key的集合，不存储value
>
> 集合的本质：是一种无序的，可变的，不允许存储重复元素的集合
>
> 表示：{}，注意：如果直接使用{}则默认表示字典

####2.创建

> ```Python
> """
> 【面试题】说明列表，元组，字典和集合的区别
> 列表的本质：是一种有序的，可变的，允许存储重复元素的集合
> 元组的本质：是一种有序的，不可变的，允许存储重复元素的集合
> 字典的本质：是一种无序的，可变的，存储键值对的集合，但是，key不允许重复，而且key必须是不可变的数据类型
> 集合的本质：是一种无序的，可变的，不允许存储重复元素的集合
> 字符串的本质：是一种有序的，不可变的，可以存储重复字符的集合
> 
> 字典和集合之间的联系：集合相当于存储了字典中的一组key
> """
> 
> # 一、创建
> # 1.{}表示字典，而非集合
> set1 = {}
> print(set1)
> print(type(set1))
> # 空集合的表示
> set11 = set()
> print(set11)
> 
> # 2.{}不为空，其中的数据不是键值对
> set2 = {34,767,12,54}
> print(set2)
> print(type(set2))
> 
> # 3.创建非空集合
> set31 = {34,767,12,54}
> set32 = set([45,65,6])
> print(set32)
> set32 = set((45,65,6))
> print(set32)
> set32 = set({"a":10,"b":20})
> print(set32)
> 
> # 4.集合中不允许重复元素存在
> s1 = {45,5,65,65,65,65}
> print(s1)
> 
> # 需求：去除列表中的重复元素
> list1 = [34,63,6,3,63,3,3,3,6,6,6,6]
> # 方式一：remove
> # 方式二：append
> list2 = []
> for num in list1:
>     if num not in list2:
>         list2.append(num)
> print(list2)
> # 方式三：set()
> list3 = list(set(list1))
> print(list3)
> ```

#### 3.系统功能

> ```Python
> # 二、系统功能
> # 1.增
> # a.add(x)，x必须是不可变的数据类型                 ******
> set1 = {11,22,33,44,55}
> print(set1)
> set1.add(77)
> print(set1)
> set1.add("abc")
> print(set1)
> set1.add(True)
> print(set1)
> # set1.add([45,57,6])   # TypeError: unhashable type: 'list'
> # print(set1)
> # set1.add({"a":10,"b":20})  # # TypeError: unhashable type: dict
> set1.add((45,57,6))
> print(set1)
> 
> # b.update(x),和字典中的update的原理是一样的,x必须是可迭代对象【list,tuple,dict,set,str】，数据被打碎加入    ******
> set1 = {11,22,33,44,55}
> print(set1)
> # set1.update(77)  # TypeError: 'int' object is not iterable【可迭代对象：容器】
> set1.update([77])
> print(set1)
> set1.update({"a":10,"b":20})
> print(set1)
> 
> # 2.删
> # a.remove():删除指定的元素       *****
> set1 = {11,22,33,44,55}
> print(set1)
> set1.remove(33)
> print(set1)
> 
> # b.pop():随机删除一个元素
> set1.pop()
> print(set1)
> 
> # c.discard():删除指定的元素,和remove的功能相同，但是，如果被删除元素不存在，使用remove会报错，但是discard不会报错,返回None
> # set1.remove(100)   # KeyError: 100
> r = set1.discard(100)
> print(r)
> 
> # d.clear()
> set1.clear()
> print(set1)
> 
> # 3.查
> set1 = {11,22,33,44,55}
> print(len(set1))
> print(max(set1))
> print(min(set1))
> 
> set2 = set1.copy()
> ```

#### 4.基本运算

> ```Python
> # 三、集合之间的运算
> set1 = {1,2,3}
> set2 = {3,4,5}
> # 1.运算符
> # a.交集：&【按位与】
> print(set1 & set2)
> 
> # b.并集：|【按位或】
> print(set1 | set2)
> 
> # c.差集:-
> print(set1 - set2)
> 
> # d.并集 - 交集：^【按位异或】
> print(set1 ^ set2)
> 
> # 2.系统功能
> # a.交集
> print(set1.intersection(set2))
> 
> # b.并集
> print(set1.union(set2))
> 
> # c.差集
> print(set1.difference(set2))
> ```

###三、字符串【重点掌握】

> 由若干个字符组成的一个序列被称为字符串，其中的字符可以是字母，数字，符号，中文等
>
> 注意：字符串属于不可变的数据类型，可以作为字典的key
>
> 字符串的本质：是一种有序的，不可变的，可以存储重复字符的集合

#### 1.创建

> ```Python
> # 创建
> 
> # 1.''
> # 注意：变量命名的时候不要直接使用str
> s1 = '342gwsgr中文'
> print(s1)
> 
> # 2.""
> s1 = "342gwsgr中文"
> print(s1)
> 
> # 3.""""""
> s3 = """fhaf
> 647325
> fahjgh
> fhajhg"""
> print(s3)
> # \n表示换行
> s31 = "fhaf\nhajefga\n236572365\nahjg"
> print(s31)
> ```

#### 2.操作

> ```Python
> # 注意：字符串是不可变的数据类型，但凡涉及到字符串的更改，都是生成了一个新的字符串
> 
> # 1.拼接：+
> str1 = "hello"
> str2 = "Python"
> print(str1 + str2)
> print(str1)
> print(str2)
> 
> # 2.*
> print("*" * 30)
> print("hello" * 3)
> 
> # 思考问题：
> str1 = "hello"
> str2 = str1.upper()
> print(str1)
> print(str2)
> 
> # 3.in和not in :判断一个字符是否存在于一个字符串中
> 
> # 4.切片：和列表，元组的切片的使用方式完全相同
> 
> # 5.访问
> str1 = 'fhajghajkgh'
> print(str1[0])
> print(str1[-1])
> print(str1[5])
> 
> ```