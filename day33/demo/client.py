import socket

sk = socket.socket()   # 买个手机
sk.connect(('127.0.0.1',9999))   # 打电话

ret = sk.recv(1024)
print(ret.decode('utf-8'))
sk.send('你也好'.encode('utf-8'))

sk.close()    # 关机