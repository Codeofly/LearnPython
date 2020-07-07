import socket
lst = {'egon':'\033[1;31m','yuan':'\033[1;34m'}
sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9090))
while True:
    msg,client_addr= sk.recvfrom(1024)   # udp协议不用建立链接
    name,mesg = msg.decode('utf-8').split(':')
    color = lst.get(name.strip(),'')
    print('%s%s\033[0m'%(color,msg.decode('utf-8')))
    inp = input('>>>')
    sk.sendto(inp.encode('utf-8'),client_addr)

sk.close()

