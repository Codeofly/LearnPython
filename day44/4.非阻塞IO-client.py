import time
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
for i in range(20):
    sk.send(b'hello')
    print(sk.recv(1024))
    time.sleep(1)
sk.close()