import  re
# 3.已知有文件test.txt里面的内容如下，查找文件中以1000phone开头的语句，并保存到列表中
# 封装函数，校验开头
def check_start(src_str):
    """
    校验字符串是否是以1000phone开头的
    :param src_str: 指定的字符串
    :return: 返回是否合法
    """
    result = re.match("1000phone",src_str)
    return False if result is None else True

if __name__ == '__main__':
    # 读取文件内容
    with open("test.txt","r",encoding="utf-8") as f:
        info_list = f.readlines()
        print(info_list)
        data_list = [line for line in info_list if check_start(line)]
    print(data_list)

# 4.提取用户输入数据中的数值 (数值包括正负数 还包括整数和小数在内) 并求和
# 例如:“-3.14good87nice19bye” =====> -3.14 + 87 + 19 = 102.86
"""
分析：
    整数：
        1位数         [0-9]
        2位数以上     [1-9][0-9]*
    
    小数：
        整数部分有1位            [0-9].[0-9]*
        整数部分有2位及以上      [1-9][0-9]*.[0-9]*
        
    -表示负数，可有可无，如果有表示负数，如果没有则表示正数
"""
def get_total(src_str):
    # 负号 整数部分  小数部分
    # [-]?(0|[1-9]\d*)(\.\d*)?

    match_list = re.finditer(r"[-]?(0|[1-9]\d*)(\.\d*)?",src_str)
    print(match_list)   # <callable_iterator object at 0x0000019F9AC30400>
    value_list = [ele.group() for ele in match_list]
    print(value_list)   # ['-3.14', '87', '19']
    return sum([float(value) for value in value_list])

def get_total1(src_str):
    match_list = re.findall(r"[-]?(?:0|[1-9]\d*)(?:\.\d*)?", src_str)
    print(match_list)  # ['-3.14', '87', '19']
    # 使用+拼接
    total_str = "+".join(match_list)   # -3.14+87+19
    return eval(total_str)

if __name__ == '__main__':
    # value = input("请输入一段文本：")
    value = "-3.14good87nice19bye"
    print(get_total(value))
    print(get_total1(value))


