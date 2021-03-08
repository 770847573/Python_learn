#1.读取
#f1 = open("建档和开户出错.png",'r',encoding='utf-8')  #UnicodeDecodeError: 'utf-8' codec can't decode byte 0x89 in position 0: invalid start byte
"""
如果打开的文件类型是图片、音视频、压缩包等，打开方式使用rb 或wb，后面没有encoding参数，因为二进制字节不需要编码格式
普通文本文件读取的结果是字符串，而二进制文件读取的结果是字节
"""
f1 = open("建档和开户出错.png",'rb')
r1 = f1.read()
f1.close()

#写入
f2 = open("图1.png",'wb')
f2.write(r1)
f2.flush()
f2.close()