from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

# 创建套接字对象
tcpSerSoc = socket(AF_INET,SOCK_STREAM)
tcpSerSoc.bind(ADDR)
tcpSerSoc.listen(5)

while True:
    print('等待连接…………')
    tcpCLISock , addr = tcpSerSoc.accept()
    print('链接来自',addr)

    while True:
        data = tcpCLISock.recv(BUFSIZ)
        print('收到来自%s的消息：%s'%(addr,data.decode('utf-8')))
        if not data:
            break
        data = f'[{ctime()}]' + data.decode('utf-8')

        tcpCLISock.send(bytes(data,encoding='utf-8'))

    tcpCLISock.close()
tcpSerSoc.close()