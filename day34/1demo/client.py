import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    inp = input('>>>')
    sk.send(inp.encode('utf-8'))
    if inp == 'q':break
    ret = sk.recv(1024).decode('utf-8')
    if ret == 'q':break
    print(ret)
sk.close()