import socket
sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    sk.send(b'hello')
    print(sk.recv(1024))
sk.close()




