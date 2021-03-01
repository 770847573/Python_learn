list1 = [1,55,86,454,885]
list2 = [3,456,78]

print("list1一共有{}个数字".format(len(list1)))
print('分别是',end=' ')
for i in list1:
    print(i,end=' ')

#比较
print('\n',list1.count(55))
print(max(list1))
