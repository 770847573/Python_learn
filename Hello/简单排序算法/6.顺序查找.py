
# 顺序查找不是算法，只是最简单的用来查询元素的方式，主要核心思想是遍历列表
# 查找所有指定的元素的位置
# list1 = [34,347,3,73,74,34,87,9,10,9,9,239]
# key = 9
# for i in range(len(list1)):
#     if list1[i] == key:
#         print("待查找元素%s在列表中存在，对应的索引为：%d" % (key,i))

# 模拟index功能，只查找第一次出现的元素的位置
list1 = [34,347,3,73,74,34,87,9,10,9,9,239]
key = 9
for i in range(len(list1)):
    if list1[i] == key:
        print("待查找元素%s在列表中存在，对应的索引为：%d" % (key,i))
        break
else:
    print("待查找元素%s在列表中不存在" % (key))

# 练习：自定义一个数字列表，求列表中第二大数的下标
list1 = [34,347,3,73,74,347,347,34,87,9,347,347,10,9,9,239]
# a.备份列表
new_list = list1.copy()
# b.对备份列表进行排序
for i in range(len(new_list) - 1):
    for j in range(len(new_list) - 1 - i):
        if new_list[j] > new_list[j + 1]:
            new_list[j],new_list[j + 1] = new_list[j + 1],new_list[j]
print(new_list)
# c.获取最大值
max_value = new_list[-1]
# d.统计最大值出现的次数
max_count = new_list.count(max_value)
# e.获取第二大值
second_value = new_list[-(max_count + 1)]
# f.回到原列表中进行顺序查找
for i in range(len(list1)):
    if list1[i] == second_value:
        print("第二大值为：%d,在列表中的位置为：%d" % (second_value,i))
