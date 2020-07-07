import socket
import struct

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    msg = 'hello world'
    length = struct.pack('i',len(msg))
    sk.send(length)
    sk.send(msg.encode('utf-8'))
sk.close()