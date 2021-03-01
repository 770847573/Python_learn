### 作业讲解

> ```Python
> # 将属于列表list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]，但不属于列表list2 = ["Sun","Mon","Thu","Fri","Sat"]的所有元素定义为一个新列表list3
> list1 = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
> list2 = ["Sun","Mon","Thu","Fri","Sat"]
> list3 = []
> # 注意：如果要获取列表中的所有元素，则一般都需要遍历列表
> for day in list1:
>     # 判断，判断一个数据是否存在于列表中，使用成员运算符
>     if day not in  list2:
>         list3.append(day)
> print(list3)
> 
> 
> # 已知一个列表中保存的是学生的姓名，要求去掉重复的名字，例如：names = ['张三', '李四', '大黄', '张三']  ->  names = ['张三', '李四', '大黄']
> # 思路：定义一个新的空的列表，遍历原列表，判断每个元素在新列表中是否存在，如果不存在则添加，如果存在则不添加
> # 方式一：append
> names = ['张三', '李四', '大黄', '张三']
> new_names = []
> for name in names:
>     if name not in new_names:
>         new_names.append(name)
> name = new_names
> print(name)
> 
> # 方式二：remove
> # names = ['张三', '李四', '大黄', '张三']
> # for i in range(1,len(names)):
> #     if names[i] == "张三":
> #         names.remove(names[i])
> # print(names)
> 
> # 扩展：删除全部的张三
> # 注意：遍历列表的时候，每当remove一个元素，列表变短了，但是下标还是按照原来的下标在执行
> names = ['张三', '张三','张三','张三','李四', '大黄', '张三',"张三","张三"]
> for name in names[:]:
>     if name == "张三":
>         names.remove(name)
> print(names)
> ```

### 一、列表【重点掌握】

> |               函数                |                             说明                             |
> | :-------------------------------: | :----------------------------------------------------------: |
> |             len(list)             |                       获取列表元素个数                       |
> |             max(list)             |                      返回列表元素最大值                      |
> |             min(list)             |                      返回列表元素最小值                      |
> |             list(seq)             |                       将元组转换为列表                       |
> |         list.append(obj)          |                    在列表末尾添加新的对象                    |
> |          list.count(obj)          |                统计某个元素在列表中出现的次数                |
> |         list.extend(seq)          | 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
> |          list.index(seq)          |           从列表中找出某个值第一个匹配项的索引位置           |
> |      list.insert(index,obj)       |                        将对象插入列表                        |
> |          list.pop(index)          | 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
> |         list.remove(obj)          |                移除列表中某个值的第一个匹配项                |
> |          list.reverse()           |                        反向列表中元素                        |
> | list.sort(key=None,reverse=False) |                       对原列表进行排序                       |
> |            list.copy()            |                           复制列表                           |
> |           list.clear()            |                           清空列表                           |

> 需要重点掌握的系统功能：
>
> ​	增：append()   insert()
>
> ​	删：remove()   pop()
>
> ​	改：reverse()    sort()
>
> ​	查：len()    count()    index()   list()

#### 1.列表切片

> ```Python
> # 切片：通过指定的区间和步长，截取列表的一部分元素，形成一个新的列表
> # 语法：列表[start:end:step]
> """
> 说明：
>     a.可以根据具体的需求，对start,end,step进行选择性的省略
>     b.如果省略start，则默认从列表的开头【0/-1】开始
>     c.如果省略end，则默认在列表的末尾【0/-1】结束
>     d.如果省略step,则默认值为1
> 
> 注意：
>     a.列表，字符串，元组都可以实现切片
>     b.无论切片怎么书写，结果都不会报错，区别在于其中有无元素
>     c.如果end未被省略，则不包含在内【包头不包尾】
> """
> list1 = [11,22,33,44,55,66,77,88,99]
> # 一、一般情况
> # 1.省略step
> print(list1[1:4])  # [22, 33, 44]
> print(list1[1:4:1])  # [22, 33, 44]
> 
> # 2.省略start
> print(list1[:4])   #  [11,22, 33, 44]
> print(list1[:4:1])
> 
> # 3.省略end
> print(list1[3:])
> print(list1[3::1])  # [44, 55, 66, 77, 88, 99]
> print(list1[3:8])   # [44, 55, 66, 77, 88]
> 
> print("*" * 30)
> 
> list1 = [11,22,33,44,55,66,77,88,99]
> 
> # 4.start和end都是正数
> """
> 用start + step的和判断是否在[start,end]区间内，如果不存在，则直接结果为[]
> """
> print(list1[1:7])
> print(list1[1:7:1])
> print(list1[1:7:-1])   # []
> 
> print(list1[7:1])     # []
> print(list1[7:1:-1])   # [88,77,66,55...33]  倒序
> 
> # 5.start和end都是负数
> print(list1[-1:-7])   # []
> print(list1[-1:-7:-1])  # [99,88,.....44]   倒序
> 
> print(list1[-7:-1])     # [33,44,55...88]
> print(list1[-7:-1:-1])   # []
> 
> print("*" * 30)
> 
> list1 = [11,22,33,44,55,66,77,88,99]
> 
> # 6.start和end一个为正数，一个为负数
> """
> 索引有两种取值方式：
> 0     1    2     3    4    5    6    7    8
> -9   -8   -7    -6   -5   -4   -3   -2   -1
> 
> 规律：
>     如果start和end一个为正，一个为负，则参考start的正负性
> """
> print(list1[-1:6:1])   # [-1:-3:1]    []
> print(list1[-1:6:-1])  # [-1:-3:-1]   [99,88]
> print(list1[-6:1:1])   # [-6:-8:1]     []
> print(list1[-6:1:-1])  # [-6:-8:-1]    [44,33]
> """
> []
> [99, 88]
> []
> [44, 33]
> """
> print(list1[1:-6:1])   # [1:3:1]      [22,22]
> print(list1[1:6:-1])  #  [1:3:-1]    []
> print(list1[6:-1:1])   # [6:8:1]     [77,88]
> print(list1[6:-1:-1])  # [6:8:-1]     []
> """
> [22, 33]
> []
> [77, 88]
> []
> """
> 
> list1 = [11,22,33,44,55,66,77,88,99]
> 
> # 二、特殊情况
> # 1
> # print(list1[100])   # 下标越界
> print(list1[100:])   # []
> 
> # 2.
> print(list1[0:-1])   # [11, 22, 33, 44, 55, 66, 77, 88]
> print(list1[0:8])   # [11, 22, 33, 44, 55, 66, 77, 88]
> 
> # 3.
> print(list1[2:100])   # [33, 44, 55, 66, 77, 88, 99]
> print(list1[2:])     # [33, 44, 55, 66, 77, 88, 99]
> 
> # 4.
> print(list1[::])  # 等价于list[:],获取全部元素
> print(list1[::-1])  # 倒序       *****
> 
> # 5.
> print(list1[-1:0])   # [-1:-9:1]   []
> print(list1[-1:0:-1])  # [-1:-9:-1]  [99,88,......22]
> 
> # 6
> print(list1[-6::1])
> print(list1[-6::-1])
> """
> [44, 55, 66, 77, 88, 99]
> [44, 33, 22, 11]
> """
> ```

#### 2.列表拷贝

> ```Python
> """
> 注意：
>     a.列表中实际上存储的是元素的地址
> """
> 
> # 一、=
> # a.一维列表
> list1= [44,55,66]
> list2 = list1
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[1] = 100
> print(list2)
> print(list1 is list2)
> 
> print("*" * 30)
> 
> # b.二维列表
> list1= [44,55,[77,88]]
> list2 = list1
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[2][1] = 100
> print(list2)
> print(list1 is list2)
> 
> # 结论：列表是可变的数据类型，当用=赋值时，不管列表是一维列表还是多维列表，
> # 如果用其中一个变量名修改其中的元素，另一个会随着更改
> 
> print("*" * 30)
> 
> # 二、列表.copy()，其实属于浅拷贝
> # a.一维列表
> list1= [44,55,66]
> list2 = list1.copy()
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[1] = 100
> print(list2)
> print(list1 is list2)
> 
> print("*" * 30)
> 
> # b.二维列表
> # 修改最里层的元素
> list1= [44,55,[77,88]]
> list2 = list1.copy()
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[2][1] = 100
> print(list2)
> print(list1 is list2)
> # 修改外层的元素
> list1= [44,55,[77,88]]
> list2 = list1.copy()
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[2] = 100
> print(list2)
> print(list1 is list2)
> 
> """
> 结论：
>     a.一维列表，一个列表修改了其中的元素，对另一个列表没有影响
>     b.多维列表，一个列表修改了最里层的元素，另一个列表会随着更改 
> """
> 
> print("*" * 30)
> 
> # 三、浅拷贝：copy.copy()
> # 导入模块
> import  copy
> # a.一维列表
> list1= [44,55,66]
> list2 = copy.copy(list1)
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[1] = 100
> print(list2)
> print(list1 is list2)
> 
> print("*" * 30)
> 
> # b.二维列表
> # 修改最里层的元素
> list1= [44,55,[77,88]]
> list2 = copy.copy(list1)
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[2][1] = 100
> print(list2)
> print(list1 is list2)
> 
> """
> copy.copy()结论：
>     a.一维列表，一个列表修改了其中的元素，对另一个列表没有影响
>     b.多维列表，一个列表修改了最里层的元素，另一个列表会随着更改 
> """
> 
> print("*" * 30)
> 
> # 四、深拷贝:copy.deepcopy()
> # a.一维列表
> list1= [44,55,66]
> list2 = copy.deepcopy(list1)
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[1] = 100
> print(list2)
> print(list1 is list2)
> 
> print("*" * 30)
> 
> # b.二维列表
> # 修改最里层的元素
> list1= [44,55,[77,88]]
> list2 = copy.deepcopy(list1)
> print(list1)
> print(list2)
> print(list1 is list2)
> list1[2][1] = 100
> print(list2)
> print(list1 is list2)
> 
> # 结论：不管是几维列表，一个列表修改其中的元素，对另一个列表没有任何影响
> 
> # 注意：修改列表元素的情况
> """
> a.list1[索引] = 值
> b.list1.append(值)
> c.list1.insert(0,值)
> d.list1.remove(值)
> e.list1.remove(1)
> """
> ```

#### 3.其他系统功能

> ```Python
> # 1.增
> # append()
> # insert()
> # extend()
> 
> list1 = [34,65]
> # r = list1.append(100)
> # print(r)  # None   函数的返回值为None
> list1.append(100)
> print(list1)
> 
> # 2.删
> # remove()
> # pop()
> # clear()
> list1 = [34,65,3,7,838]
> # list1.remove(100)   # ValueError: list.remove(x): x not in list
> # r1 = list1.remove(34)
> # print(r1)   # None
> 
> # 注意：通过pop删除指定位置处的元素，返回元素本身
> r2 = list1.pop(1)
> print(r2)
> 
> # 3.改
> list1 = [34,65,3,7,838]
> # 倒序/反转
> list1.reverse()  # 在列表内部倒序
> print(list1)
> # list1[::-1]   # 生成一个新的列表
> 
> # 排序
> list1 = [34,65,3,7,838]
> # 默认升序
> list1.sort()
> print(list1)
> 
> # 降序
> list1 = [34,65,3,7,838]
> list1.sort(reverse=True)
> print(list1)
> 
> # key:自定义排序规则
> # key后面一定要跟函数，作用：将列表中的每个元素作用于该函数，函数的运算结果作为排序的依据
> list1 = ["fagagag","af","fafg","gagwahahahh","agaga"]
> list1.sort(key=len,reverse=True)
> print(list1)
> 
> # 4.查
> list1 = [34,4,7,547,45,745,7]
> # 获取长度
> print(len(list1))
> 
> # 统计一个元素在列表中出现的次数
> print(list1.count(7))
> 
> # 求最值
> print(max(list1))
> print(min(list1))
> 
> # 求一个元素在列表中第一次出现的索引
> print(list1.index(7))
> # print(list1.index(100))   # ValueError: 100 is not in list
> 
> 
> # 注意：排序和求最值得依据是ASCII表，其中包含了常用的字母，数字字符，常用的符号，a--->97,A---->65,"0"--->48
> 
> # list()
> print(list("hello"))
> print(list(("hello",345,665)))
> ```

#### 4.列表推导式

> ```Python
> # 列表推导式又被称为列表生成式，是Python提供给我们的用来生成列表的一个强大又方便的工具
> 
> # 语法：[新的列表元素的规律   for循环   if语句]
> 
> # 1.需求：已知一个数字列表nums = [1, 2, 5, 9]，根据该列表生成一个新的列表，其中的元素是nums中每个元素的2倍，例如：nums = [1, 2, 5, 9]   ->  nums = [2, 4, 10, 18]
> nums = [1, 2, 5, 9]
> nums1 = []
> for n1 in nums:
>     nums1.append(n1 * 2)
> print(nums1)
> 
> nums2 = [n2 * 2  for n2 in nums]
> print(nums2)
> 
> # 2.需求：生成一个列表[1,4,9,16,25]
> list1 = []
> for i in range(1,6):
>     list1.append(i ** 2)
> print(list1)
> 
> list2 = [i ** 2 for i in range(1,6)]
> print(list2)
> 
> # 3.需求：生成一个列表[1,9,25,49,81]
> list1 = []
> for i in range(1,10):
>     if i % 2 == 1:
>         list1.append(i ** 2)
> print(list1)
> 
> list2 = [i ** 2 for i in range(1,10) if i % 2 == 1]
> print(list2)
> 
> # 4.嵌套循环
> list1 = []
> for x in "abc":
>     for y in "xyz":
>         list1.append(x + y)
> print(list1)
> 
> list2 = [x + y for x in "abc" for y in "xyz"]
> print(list2)
> ```