age = 20
name = 'Swaroop'
print('{}今年{}岁了'.format(name,age))
print('{}正在学python'.format(name))
# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:*^11}'.format('hello'))
# 使用print是避免换行
print('a',end='')
print('b',end='')
print('c')
print('What\'s your name?' )
print('This is the first line\nThis is the second line')
print('This is the first line.\
This is the second line')
#原始字符串前加r
#在处理正则表达式时应全程使用原始字符串
print(r'新的一行使用\n')

