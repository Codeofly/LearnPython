import socket
sk  = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    sk.send('heiheihei'.encode('utf-8'))
    import time
    time.sleep(0.1)
    sk.send('sayhahaha|我是heiheihei'.encode('utf-8'))
sk.close()