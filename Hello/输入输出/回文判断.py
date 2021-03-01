import re
def reverse(text):
    return text[::-1]
def is_palindrome(text):
    forbidden = '[!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~" ]'
    # 如果文本中有标点符号呢？
    text = re.sub(forbidden,"",text)
    if text == reverse(text):
        print('是一个回文')
    else:print('不是回文')

something = input('输入一段文字：')
is_palindrome(something)



