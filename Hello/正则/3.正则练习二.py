import  re
# 1，替换敏感词从控制台输入一段文本，将其中可能会出现的敏感词替换为*
text = input("请输入一段文本：")
# 傻逼 煞笔  shit  fuck  艹草操
new_text = re.sub(r"[艹草操]|傻逼|煞笔|shit|fuck","*",text)
print(new_text)

# 2.拆分长字符串
s2 = "zhangsan%%%%%lisi@@@@@@@@@@Tom#BOB&&&xiaoMing%%%%%"
name_list = re.split(r"[%@#&]{1,}",s2)
print(name_list)
# 如果分割完字符串之后，列表中出现了空字符串，则需要手动操作
for name in name_list:
    if name == "":
        name_list.remove("")
print(name_list)

# 问题：
name_list = ['zhangsan', '', 'lisi', '', '','','Tom', 'BOB', 'xiaoMing', '']
for name in name_list[:]:
    if name == "":
        name_list.remove("")
print(name_list)
