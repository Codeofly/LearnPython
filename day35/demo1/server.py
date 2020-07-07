import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
while True:
    cmd = input('>>>')
    conn.send(cmd.encode('utf-8'))
    if cmd == 'q': break
    ret1 = conn.recv(1024)
    print('stdout : ', ret1.decode('gbk'))
    ret2 = conn.recv(1024)
    print('stderr : ',ret2.decode('gbk'))
conn.close()
sk.close()

# 发送过来的一整条信息
# 由于server端没有及时接受
# 后来发送的数据和之前没有接收完的数据黏在了一起
# 著名的黏包现象

