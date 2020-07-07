import struct
import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
while True:
    ret = conn.recv(4)
    length = struct.unpack('i',ret)[0]
    msg = conn.recv(length)
    print(msg.decode('utf-8'))
conn.close()
# ret = struct.pack('i',1920000)
# print(ret)
#
# ret = struct.unpack('i',ret)
# print(ret[0])

# 能够把范围内一个任意的整数转换成一个固定长度的字节
# 还能转换回来

# 发送数据的时候
# xxxxtttttttttttttttttttttttttttttt
# 自定义了一个协议