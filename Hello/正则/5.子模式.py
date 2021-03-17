# 子模式其实是关于()的用法

import  re


# 1.依次书写正则表达式
s1 = "<abc123><fjfa>hello<fjfa><abc123>"
print(re.search(r"<[a-zA-Z]{1,}\d+><[a-zA-Z]+>\w+<[a-zA-Z]+><[a-zA-Z]{1,}\d+>",s1))

# 2.使用子模式
# <1><2><3><4>，使用子模式的前提条件:1和4的内容完全相同，2和3完全相同
s1 = "<abc123><fjfa>hello<fjfa><abc123>"
print(re.search(r"<([a-zA-Z]{1,}\d+)><([a-zA-Z]+)>\w+<\2><\1>",s1))


s1 = "<abc123><fjfa>hello<fjfa><abc124>"
print(re.search(r"<([a-zA-Z]{1,}\d+)><([a-zA-Z]+)>\w+<\2><\1>",s1))   # None

s1 = "<abc123><fjfa>hello<fjfa><abc123>"
print(re.search(r"<([a-zA-Z]{1,}\d+)><([a-zA-Z]+)>\w+<\1><\2>",s1))   # None


"""
如果原字符串中出现了重复的内容，可以考虑使用子模式
在正则中，对于重复出现的内容，可以从左往右使用()表示，系统会自动给()从左往右从1开始编号，1,2，。。。
如果后面的内容中有相同的子字符串，则可以使用\1,\2.。。。表示
"""
