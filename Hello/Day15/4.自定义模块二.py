# 二、from   模块名  import  变量，函数，类

# 1.from   xxx  import   x1,x2.....
from  aaa.textDemo import func as fa,num  as a
from  bbb.textDemo import func as fb,num  as b
# from  ccc.ddd.eee.text import func as fc,func1,func2,func3

# 访问变量
# 注意1：使用from xxx import xx方式，则访问变量和调用函数的时候，不需要指明路径【模块名】
# 注意2：使用from xxx import xx方式，如果不同模块中出现了重名的变量或者函数，则后出现的会覆盖掉先出现的
#        谁最后出现则使用谁

# 注意3：但是，为了保证每个模块中重名的函数或者变量都能被访问，可以借助于as给每个变量或者函数分别器别名
print(a)
print(b)

# 调用函数
# fc()
# func1()

# 注意4：使用from xxx import xx方式，如果需要将一个模块中的所有的内容全部导入，则需要挨个书写
# 但是，一般情况下使用from xxx import *简写

# 2.from xxx import *
# 注意5：*代表全部
from  ccc.ddd.eee.text import *
func()
func1()
func2()

# 注意6：from xxx import *使用比较方便，但是，如果一个模块中定义了无数个变量或者函数，但是，实际只需要使用其中的几个
# 则会占用过多的内存空间