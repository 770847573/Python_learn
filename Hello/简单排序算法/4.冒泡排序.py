list1 = [34,3,6,3,73,7,3,100,346,3643,5,28]

# 冒泡升序排序

# 外层循环：控制比较的轮数
for i in range(len(list1) - 1):
    # 内层循环：控制的是每一轮比较的次数，以及参与比较的下标
    for j in range(len(list1) - 1 - i):
        # 比较：如果符合条件则交换位置
        # 如果下标小的元素  > 下标大的元素，则交换位置
        if list1[j] > list1[j + 1]:
            list1[j],list1[j + 1] = list1[j + 1],list1[j]
print(list1)
