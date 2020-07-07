from socket import *
ip_port=('127.0.0.1',9000)
bufsize=4096

udp_client=socket(AF_INET,SOCK_DGRAM)

while True:
    msg=input('>>: ').strip()
    udp_client.sendto(msg.encode('utf-8'),ip_port)
    err,addr=udp_client.recvfrom(bufsize)
    out,addr=udp_client.recvfrom(bufsize)
    if err:
        print('error : %s'%err.decode('gbk'),end='')
    if out:
        print(out.decode('gbk'), end='')