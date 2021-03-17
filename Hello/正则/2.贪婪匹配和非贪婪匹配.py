"""
非贪婪匹配：最多只能匹配1个，如：?
贪婪匹配：尽可能多的匹配，没有上限,如：*和+

?:0个或1个
*:0个或多个
+:1个或多个
"""
import  re

# a.区别
print(re.findall(r"\d?","xyz6575725ghgh-675365gnajke")) # ['','','','6','5'.....'5',.....]
print(re.findall(r"\d*","xyz6575725ghgh-675365gnajke")) # ['','','',"6575725",''...."675365",''.....]
print(re.findall(r"\d+","xyz6575725ghgh-675365gnajke")) # ["6575725","675365"]

# b.*和+:尽可能多的匹配
# 结论：在+或者*的后面使用?,可以将贪婪匹配转换为飞贪婪匹配，但是，只能在正则表达式开头有限制条件的时候才能起作用
# 情况一：正则开头添加限制条件
print(re.findall(r"z\d*","xyz6575725ghgh-675365gnajke"))   # ["z6575725"]
print(re.findall(r"z\d+","xyz6575725ghgh-675365gnajke"))    # ["z6575725"]
# 尽可能少的匹配
print(re.findall(r"z\d*?","xyz6575725ghgh-675365gnajke"))  # ['z']
print(re.findall(r"z\d+?","xyz6575725ghgh-675365gnajke"))  # ['z6']

# 情况二：正则结尾添加限制条件
print(re.findall(r"\d*g","xyz6575725ghgh-675365gnajke"))   # ['6575725g', 'g', '675365g']
print(re.findall(r"\d+g","xyz6575725ghgh-675365gnajke"))   # ['6575725g', '675365g']
print(re.findall(r"\d*?g","xyz6575725ghgh-675365gnajke"))   # ['6575725g', 'g', '675365g']
print(re.findall(r"\d+?g","xyz6575725ghgh-675365gnajke"))   # ['6575725g', '675365g']

# 情况三：正则开头和结尾添加限制条件
print(re.findall(r"z\d*g","xyz6575725ghgh-675365gnajke"))  # ['z6575725g']
print(re.findall(r"z\d+g","xyz6575725ghgh-675365gnajke"))  # ['z6575725g']
print(re.findall(r"z\d*?g","xyz6575725ghgh-675365gnajke")) # ['z6575725g']
print(re.findall(r"z\d+?g","xyz6575725ghgh-675365gnajke")) # ['z6575725g']