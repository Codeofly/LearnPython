import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
name = input('name :')
while True:
    inp = input('>>>')
    sk.sendto(('%s : %s'%(name,inp)).encode('utf-8'),('127.0.0.1',9090))
    msg,addr = sk.recvfrom(1024)
    print(msg.decode('utf-8'))

sk.close()


