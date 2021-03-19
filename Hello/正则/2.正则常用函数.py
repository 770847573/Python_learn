import  re

# 注意：在正则常用的函数中，都有flags参数与，用于表示正则表达式的匹配方式，如：多行匹配，忽略大小写

# 1.compile(pattern，flags):将一个正则表达式字符串编译为正则对象，一般用于和其他函数结合使用，单独使用无意义
r1 = re.compile(r"\d+")
print(type(r1))  # <class 're.Pattern'>

# 2.match():用指定的正则表达式匹配指定的字符串,如果匹配上，则返回一个匹配对象，反之返回None    *****
r2 = re.match(r"^aaa","aaa is a text")
print(r2)   # <re.Match object; span=(0, 3), match='aaa'>
r2 = re.match(r"^aaa","bbb is a text")
print(r2)  # None

# 3.group():用来获取匹配到的内容
# r3 = r2.group()
# print(r3)

# 4.search():会在字符串中通过正则表达式进行查找，       ******
# 只要找到第一个匹配的结果则直接停止查找，返回对象，反之，则返回None
# search函数的底层调用的是match函数
r4 = re.search(r"\d+","aaa5245is62a6266226text")
print(r4)    # <re.Match object; span=(3, 7), match='5245'>
r4 = re.search(r"\s+","aaa5245is62a6266226text")
print(r4)   # None

# 5.findall():会在字符串中通过正则表达式进行查找,会查找出所有符合条件的子字符串，返回字符串的列表    ***********
# 如果查找到，列表非空，反之列表为空
r5 = re.findall(r"\d+","aaa5245is62a6266226text")
print(r5)  # ['5245', '62', '6266226']
r5 = re.findall(r"\s+","aaa5245is62a6266226text")
print(r5)  # []

# 注意：findall使用过程中的坑
# 如果正则表达式中出现()，则默认情况下只会输出()中匹配到的内容
s1 = "3453 3774   286292982 727"
print(re.findall(r"\w+\s+\w+",s1))   # ['3453 3774', '286292982 727']
print(re.findall(r"(\w+)\s+\w+",s1))  # ['3453', '286292982']
# 将捕获分组转换为非捕获分组，则使用(?:)
print(re.findall(r"(?:\w+)\s+\w+",s1))  # ['3453 3774', '286292982 727']

s2 = "a123ca456c"
print(re.findall(r"a(123|456)c",s2))   # ['123', '456']
print(re.findall(r"a(?:123|456)c",s2)) # ['a123c', 'a456c']

print("*" * 30)

# 6.finditer():会在字符串中通过正则表达式进行查找,会查找出所有符合条件的子字符串，返回一个迭代器,该迭代器中的元素是match对象
# Iterator：迭代器   Iterable:可迭代对象
r6 = re.finditer(r"\d+","aaa5245is62a6266226text")
print(type(r6))
for ele in r6:
    # 获取匹配到的值
    print(ele.group())
    # 获取下标
    print(ele.span())

r6 = re.finditer(r"\s+","aaa5245is62a6266226text")
print(r6)   # 如果匹配不到，仍然会返回一个迭代器，但是其中没有元素


# 7.sub()/subn()替换，用新的字符串替换通过正则表达式匹配出来的旧的字符串
s7 = "Bob is a handsome boy,he is cool,clever,and so on...."
# 需求：将其中的空格替换为-
s71 = s7.replace(" ","-")  # 缺点：replace只能替换有规律的字符串
print(s71)

s7 = "Bob is        a      handsome boy,he is     cool,clever,and    so on...."
s71 = s7.replace(" ","-")
print(s71)
s72 = re.sub(r"\s+","-",s7)   # 优点：可以替换没有规律的字符串
print(s72)

s72 = re.sub(r"\s+","-",s7,3)   # 可以限制替换的次数
print(s72)

# subn()返回一个元组，(替换之后的新的字符串，统计替换的次数)
s72 = re.subn(r"\s+","-",s7)  # ('Bob-is-a-handsome-boy,he-is-cool,clever,and-so-on....', 8)
print(s72)

# 8.split()    *****
# str.split():只能分割有规律的字符串,结果是一个列表
str1 = "one1two1three1four1five"
print(str1.split("1"))
print(re.split(r"1",str1))

# re.split()：可以分割没有规律的字符串,结果是一个列表
str1 = "one1two2three3four4five"
print(re.split(r"\d",str1))

str2 = "zhangsan     lisi  hanmeimei       jack      tom    jerry"
print(re.split(r"\s+",str2))

str2 = "zhangsan&&&&&lisi$$$$$$$$$$hanmeimei@@@Jack#############Tom%%Jerry"
print(re.split(r"[&$@#%]{2,}",str2))
print(re.split(r"[^a-zA-Z]+",str2))

