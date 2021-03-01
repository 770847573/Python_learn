# 一、import  模块名
# 模块名的组成：包1.包2........py文件名

# 1.import  xxx
# 注意1：import表示将指定的py文件在允许的情况下加载一遍
import aaa.textDemo
import bbb.textDemo

# 访问变量
# 注意2：使用import xxx的方式访问模块中的变量或者函数，一定要在变量名或者函数名的前面指明模块【路径】，
# 当然，这种用法非常麻烦，每次都需要添加路径

# 注意3：在不同的模块中定义了相同的变量或者函数，相互之间没有影响
print(aaa.textDemo.num)
print(bbb.textDemo.num)

# 调用函数
aaa.textDemo.func()
bbb.textDemo.func()

# 2.import xxxx  as  别名：给xxx模块起别名，为了简化模块中变量或者函数的调用
# import  ccc.ddd.eee.text
# ccc.ddd.eee.text.func()
# ccc.ddd.eee.text.func1()
# ccc.ddd.eee.text.func2()
# ccc.ddd.eee.text.func3()

# 简化：起别名
import  ccc.ddd.eee.text  as t
t.func()
t.func1()
t.func2()
t.func3()