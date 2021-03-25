from socket import *


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCLISock = socket(AF_INET,SOCK_STREAM)
tcpCLISock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCLISock.send(bytes(data,'utf-8'))
    server_data = tcpCLISock.recv(BUFSIZ)
    if not server_data:
        break
    print(server_data.decode('utf-8'))
tcpCLISock.close()