import socket
sk  = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    sk.send(b'hahaha')
    import time
    time.sleep(0.1)
    sk.send(b'xxxx')
    print(sk.recv(1024).decode('utf-8'))
    time.sleep(1000)
sk.close()