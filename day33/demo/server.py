import socket
# 基于tcp协议的一次通信
sk = socket.socket()   # 买手机
# sk.bind(('192.168.11.53',9999))    # 装一张电话卡
sk.bind(('192.168.11.89',9000))    # 装一张电话卡
# 8000 - 10000
sk.listen()   # 开机

conn,addr = sk.accept()   # 等着 接电话  我们两个的连接，对方的地址
print(addr)
conn.send('你好'.encode('utf-8'))
ret = conn.recv(1024)   #1024  表示接受1024个字节
print(ret.decode('utf-8'))

conn.close()   # 挂电话
sk.close()     # 关手机

# 计算机的回环地址  127.0.0.1