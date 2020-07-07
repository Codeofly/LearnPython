import socket
BUFSIZE=1024
ip_port=('127.0.0.1',8080)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=s.connect_ex(ip_port)
lenth = str(len('hello')).encode('utf-8')
s.send(lenth)
s.send('hello'.encode('utf-8'))
lenth = str(len('egg')).encode('utf-8')
s.send(lenth)
s.send('egg'.encode('utf-8'))

s.close()