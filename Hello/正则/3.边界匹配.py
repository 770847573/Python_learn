"""
--------------锚字符(边界字符)-------------

^     行首匹配，和在[]里的^不是一个意思    [^xxxxx]
$     行尾匹配

\A    匹配字符串开始，它和^的区别是,\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首
\Z    匹配字符串结束，它和$的区别是,\Z只匹配整个字符串的结束，即使在re.M模式下也不会匹配它行的行尾

\b    匹配一个单词的边界，也就是值单词和空格间的位置
\B    匹配非单词边界
"""
import re

# search():使用指定的正则在指定的字符串中从左往右依次进行搜索，只要找到一个符合条件的子字符串，则立即停止查找，返回一个对象
#          search函数的底层调用的是match
# findall():使用指定的正则在指定的字符串中匹配所有符合条件的子字符串，返回一个列表

print(re.search(r"^this","this is a text"))   # startswith()
print(re.search(r"text$","this is a text"))   # endswith()

print("this is a text\nthis is a text\nthis is a text\nthis is a text")

# 默认情况下，即使字符串有多行，使用^和$进行行首和行尾的匹配，都将字符串当做一行处理
print(re.findall(r"^this","this is a text\nthis is a text\nthis is a text\nthis is a text"))  # ['this']
print(re.findall(r"text$","this is a text\nthis is a text\nthis is a text\nthis is a text"))  # ['text']

# 如果需要匹配每个行的行首和行尾，需要设置flags=re.M,表示多行模式
print(re.findall(r"^this","this is a text\nthis is a text\nthis is a text\nthis is a text",flags=re.M)) # ['this', 'this', 'this', 'this']
print(re.findall(r"text$","this is a text\nthis is a text\nthis is a text\nthis is a text",flags=re.M)) # ['text', 'text', 'text', 'text']

# \A和\Z即使在re.M模式下也不会匹配它行的行首和行尾
print(re.findall(r"\Athis","this is a text\nthis is a text\nthis is a text\nthis is a text",flags=re.M))# ['this']
print(re.findall(r"text\Z","this is a text\nthis is a text\nthis is a text\nthis is a text",flags=re.M))# ['text']


