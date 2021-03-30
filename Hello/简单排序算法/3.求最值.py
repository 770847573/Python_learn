# 自定义一个数字列表，找出列表中最大数连同下标一起输出
num_list = [45,45,7,57,568,56,2,19]
# 方式一:假设法
max_value = num_list[0]
for num in num_list:
    if num > max_value:
        max_value = num
print(max_value)

# 优化
max_value = num_list[0]
max_index = 0
for i in range(1,len(num_list)):
    if num_list[i] > max_value:
        max_value = num_list[i]
        max_index = i
print(max_index,max_value)

# 方式二：排序
# 冒泡排序和选择排序
