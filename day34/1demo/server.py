import socket

sk = socket.socket()
sk.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sk.bind(('127.0.0.1',9000))
sk.listen()   # 参数n表示同一时间可以有n个链接等待与server端通信

while True:
    conn,addr = sk.accept()
    while True:
        ret = conn.recv(1024).decode('utf-8')
        if ret == 'q':break
        print(ret)
        inp = input('>>>')
        conn.send(inp.encode('utf-8'))
        if inp == 'q':break
    conn.close()

sk.close()

# tcp协议适用于 文件的上传和下载 发送邮件 发送重要的文件
# 每和一个客户端建立链接 都会在自己的操作系统上占用一个资源
# 同一时间 只能 和一个客户端通信

