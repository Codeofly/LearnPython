# 原理
# 黏包现象的成因
    # 你不知道在哪儿断句
# 解决问题
    # 在发送数据的时候，先告诉对方要发送的大小就可以了
        # 在发送的时候 先发送数据的大小 在发送内容
        # 在接受的时候 先接受大小 再根据大小接受内容
# 自定义协议


#_*_coding:utf-8_*_
from socket import *
ip_port=('127.0.0.1',8080)

tcp_socket_server=socket(AF_INET,SOCK_STREAM)
tcp_socket_server.bind(ip_port)
tcp_socket_server.listen(5)

conn,addr=tcp_socket_server.accept()
lenth = conn.recv(1)
print(lenth)
lenth = int(lenth.decode('utf-8'))
data1=conn.recv(lenth)
lenth2 = conn.recv(1)
lenth2 = int(lenth2.decode('utf-8'))
data2=conn.recv(lenth2)

print('----->',data1.decode('utf-8'))
print('----->',data2.decode('utf-8'))

conn.close()
tcp_socket_server.close()