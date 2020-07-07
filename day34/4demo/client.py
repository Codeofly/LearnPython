import time
import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
while True:
    sk.sendto('%Y/%m/%d %H:%M:%S'.encode('utf-8'),('127.0.0.1',9090))
    ret,addr = sk.recvfrom(1024)
    print(ret.decode('utf-8'))
    time.sleep(1)
sk.close()