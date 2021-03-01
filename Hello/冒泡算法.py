#冒泡排序：
list = [12,23,3,43,5435,64654,22,3431]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):

        if list[j] > list[j + 1]:
            list[j] , list[j + 1] = list[j+1] , list[j]
print(list)
#选择排序：

list = [12,23,3,43,5435,64654,277,3431]
for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[i]<list[i+j+1]:
            list[i],list[i + j + 1] = list[i+j+1],list[i]
print(list)