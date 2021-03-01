class ShortInputException(Exception):
    def __init__(self,lenth,atleast):
        Exception.__init__(self)
        self.lenth = lenth
        self.atleast = atleast

try:
    lenth_limit = int(input('请规定字符串最小长度：'))
    text = input('请输入一些东西:')
    if len(text) <lenth_limit :
        raise ShortInputException(len(text),lenth_limit)
except EOFError:#Ctrl+D
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print('你输入的字符串长度为{0}，最小长度限制为{1}'.format(ex.lenth,ex.atleast))
else:
    print('No exception was raised.')
