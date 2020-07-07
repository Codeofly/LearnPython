import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    inp = input('>>>').encode('utf-8')
    sk.send(inp)
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
sk.close()