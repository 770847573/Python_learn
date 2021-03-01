import pickle
shoplist_file = 'shoplist.data'
shoplist = ['apple','mango']
#以写入形式打开
#我们首先需要通过 open 以写入（write）二进制（binary）模式打开文件，
#然后调用 pickle 模块的 dump 函数。这一过程被称作封装（Pickling）。
f = open(shoplist_file,'wb')
pickle.dump(shoplist,f)
#清除shoplist变量
del shoplist
#已读取形式打开
#接着，我们通过 pickle 模块的 load 函数接收返回的对象。这个过程被称作拆封（Unpickling）
f = open(shoplist_file,'rb')
list = pickle.load(f)
print(list)