# ()
# |

import  re

# 1.
print(re.findall(r"\d*","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"\d+","xyz6575725ghgh-675365gnajke"))
"""
['', '', '', '6575725', '', '', '', '', '', '675365', '', '', '', '', '', '', '']
['6575725', '675365']
"""

# 2.
"""
?:0个或1个
*:0个或多个
+:1个或多个
"""
print(re.findall(r"\d*|[a-z]+","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"\d+|[a-z]+","xyz6575725ghgh-675365gnajke"))
"""
['', 'xyz', '6575725', '', 'ghgh', '', '675365', '', 'gnajke', '']
['xyz', '6575725', 'ghgh', '675365', 'gnajke']
"""

print("*" * 30)

# 3.注意：使用findall进行搜索，如果正则中使用了()，则最终匹配到的结果只会输出（）中的结果,其他匹配不到的使用""代替
print(re.findall(r"\d*|([a-z]+)","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"\d+|([a-z]+)","xyz6575725ghgh-675365gnajke"))
"""
['', 'xyz', '', '', 'ghgh', '', '', '', 'gnajke', '']
['xyz', '', 'ghgh', '', 'gnajke']
"""
print(re.findall(r"(\d*)|[a-z]+","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"(\d+)|[a-z]+","xyz6575725ghgh-675365gnajke"))
"""
['', '', '6575725', '', '', '', '675365', '', '', '']
['', '6575725', '', '675365', '']
"""
print("*" * 30)


print(re.findall(r"(\d*)","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"(\d+)","xyz6575725ghgh-675365gnajke"))


# 注意：使用findall进行搜索，如果正则中使用了()，当（）的数量大于1个，结果[(),().......]
print(re.findall(r"(\d*)|([a-z]+)","xyz6575725ghgh-675365gnajke"))
print(re.findall(r"(\d+)|([a-z]+)","xyz6575725ghgh-675365gnajke"))
"""
[('', ''), ('', 'xyz'), ('6575725', ''), ('', ''), ('', 'ghgh'), ('', ''), ('675365', ''), ('', ''), ('', 'gnajke'), ('', '')]
[('', 'xyz'), ('6575725', ''), ('', 'ghgh'), ('675365', ''), ('', 'gnajke')]
"""

# print(re.findall(r"((\d*)|([a-z]+))","xyz6575725ghgh-675365gnajke"))  # ((),())
# print(re.findall(r"((\d+)|([a-z]+))","xyz6575725ghgh-675365gnajke"))
"""
[('', '', ''), ('xyz', '', 'xyz'), ('6575725', '6575725', ''), ('', '', ''), ('ghgh', '', 'ghgh'), ('', '', ''), ('675365', '675365', ''), ('', '', ''), ('gnajke', '', 'gnajke'), ('', '', '')]
[('xyz', '', 'xyz'), ('6575725', '6575725', ''), ('ghgh', '', 'ghgh'), ('675365', '675365', ''), ('gnajke', '', 'gnajke')]
"""

# (((a)|(b)|(c)))   ----->[(外层的括号1，外层的括号2，a,b,c).......]
