from mysocket import Mysocket

sk = Mysocket()
sk.bind(('127.0.0.1',9090))
while True:
    msg,client_addr= sk.my_recv(1024)   # udp协议不用建立链接
    print(msg)
    if msg == 'q':sk.close()
    inp = input('>>>')
    sk.my_send(inp,client_addr)
    if inp == 'q':sk.close()
sk.close()
