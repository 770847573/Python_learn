# Python package本质是一个文件夹【目录】，
# 但是特殊之处在于在该目录下有一个文件，名为__init__.py，代表初始化，
# 前期其中不写任何内容，后期会在其中书写项目的配置信息


# 包的好处：可以管理文件的命名【在不同的包下可以创建同名的文件】

"""
注意：
    a.关于包的使用，使用的都是相对路径，如：aaa\textDemo,bbb\textDemo
    b.使用包的时候，一般是结合py文件使用，整体代表的是一个模块，采用的是“点语法”，如：aaa.textDemo,bbb.textDemo
    c.使用模块名的时候，.代表的是路径的层级关系，一定不能省略,层级关系中，可以是包，也可以是目录
    d.相对路径是从工程的根目录开始，所以书写模块名的时候，要从工程的根目录开始书写
"""

# 需求：在当前文件中分别调用aaa,bbb,ccc包中的func函数

# 第一步：导入模块
import aaa.textDemo      # 注意：aaa被称为包，aaa.textDemo被称为模块名
import bbb.textDemo
import  ccc.ddd.eee.text
import  show
# 注意：在Python中，每个py文件都是一个模块，包只是为了管理py文件的路径，所以如果要自定义一个模块，一定要注意命名的规范

# 第二步：调用函数
aaa.textDemo.func()
bbb.textDemo.func()
ccc.ddd.eee.text.func()