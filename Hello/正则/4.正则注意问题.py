import  re

# 1.flags的注意事项
# split(pattern,string,maxsplit,flags)
str2 = "zhangsan&&&&&lisi$$$$$$$$$$hanmeimei@@@Jack#############Tom%%Jerry"
print(re.split(r"[^a-z]+",str2,re.I))  # ['zhangsan', 'lisi', 'hanmeimei@@@Jack#############Tom%%Jerry']

# 注意：如果要设置flags，则尽量使用关键字参数传参，否则容易传错
print(re.split(r"[^a-z]+",str2,flags=re.I))  # ['zhangsan', 'lisi', 'hanmeimei', 'Jack', 'Tom', 'Jerry']

# 练习
print(re.split(r"a","1A2a3a4A5a",re.I))  # ['1A2', '3', '4A5a']
print(re.split(r"a","1A2a3a4A5a",flags=re.I))  # ['1', '2', '3', '4', '5', '']

# 2.match()/search()/findall()
a = re.match(r'\d',"abc3")     # 从左往右进行依次匹配
print(a)    # None
a = re.search(r'\d',"abc3")    # 查找，只要知道一个符合条件的则停止查找
print(a)   # <re.Match object; span=(3, 4), match='3'>
a = re.findall(r'\d',"abc3")   # 查找，查找所有符合条件的子字符串，返回一个列表
print(a)   # ['3']

# 3.空格:在正则表达式不要轻易添加空格，一个空格也属于一个正则字符
r = re.search(r" \d","5265 5274 cvb287528")
print(r)
r = re.search(r"\d","5265 5274 cvb287528")
print(r)