"""
-------------------匹配多个字符------------------------

说明：下方的x、y、z均为假设的普通字符,n、m（非负整数），不是正则表达式的元字符
(xyz)    匹配小括号内的xyz(作为一个整体去匹配)
x?       匹配0个或者1个x
x*       匹配0个或者任意多个x（.* 表示匹配0个或者任意多个字符(换行符除外)）
x+       匹配至少一个x
x{n}     匹配确定的n个x（n是一个非负整数）
x{n,}    匹配至少n个x
x{n,m}   匹配至少n个最多m个x。注意：n <= m
x|y      |表示或，匹配的是x或y
"""

"""
()      表示分组，其中的内容可以当做一个整体处理
{}      数量匹配，限定指定的字符出现的次数
|       表示或，，语法：正则一|正则二，表示只要其中一个正则能够匹配上，则就可以得到结果

?       匹配0个或者1个,非贪婪匹配
*       匹配0个或者多个，贪婪匹配
+       匹配1个或者多个【匹配至少1个】，贪婪匹配
"""
import  re

# findall():使用指定的正则在指定的字符串中匹配所有符合条件的子字符串，返回一个列表

print(re.findall(r"a+","aaaaaaaaaaaaaaaaaaaaa"))    # ['aaaaaaaaa']，至少匹配1个，尽可能多的匹配
print(re.findall(r"a?","aaaaaaaaa"))    # ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', ''],优先匹配1个，最后必定有一个""
print(re.findall(r"a*","aaaaaaaaa"))    # ['aaaaaaaaa', ''],尽可能多的匹配,最后必定有一个""
print(re.findall(r"a{3}","aaaaaaaaaa"))    # ['aaa', 'aaa', 'aaa'],一次只能匹配3个
print(re.findall(r"a{3,}","aaaaaaaaa"))    # ['aaaaaaaaa'],尽可能多的匹配
print(re.findall(r"a{3,5}","aaaaaaaaa"))   # ['aaaaa', 'aaaa'],尽可能多的匹配

