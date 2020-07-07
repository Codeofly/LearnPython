import socket
from threading import Thread
def socket_client():
    sk = socket.socket()
    sk.connect(('127.0.0.1',9000))
    while True:
        print(sk.recv(1024))
        sk.send(b'bye')
    sk.close()
for i in range(500):
    Thread(target=socket_client).start()

# 进程5 线程20 协程500个 —— 通用的组合  —— 50000

# 进程 线程 协程
# 并发编程的设计
# 进程 线程 协程 都用
#