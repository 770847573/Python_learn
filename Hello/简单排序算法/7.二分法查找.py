# 已知列表list1 = [34,55,67,88,99,100],使用二分法查找67在列表中的位置

# 注意：二分法的前提：列表必须是有序的
list1 = [34,55,67,88,99,100]
list1.sort()

key = 60

# 定义最大下标和最小下标
left = 0
right = len(list1) - 1

# 循环计算中间的下标，并且通过比较数的大小，重置left和right的值
while left <= right:
    # 计算中间的下标
    middle = (left + right) // 2
    # 用待查找元素和中间下标对应的元素进行比较
    # 以升序为例
    if  key > list1[middle]:
        # 重置left的值
        left = middle + 1
    elif key < list1[middle]:
        # 重置right的值
        right = middle - 1
    else:
        # 找到了
        print("待查找元素%d在列表中的位置为：%d" % (key,middle))
        # 如果拿到结果，则可以提前结束循环
        break
else:
    print("待查找元素%d在列表中不存在" % (key))