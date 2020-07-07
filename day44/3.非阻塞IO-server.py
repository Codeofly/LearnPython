import socket

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.setblocking(False)
sk.listen()
conn_lst = []
del_lst = []
while True:
    try:
        conn,addr = sk.accept()   # 非阻塞的模型
        print(conn,addr)
        conn_lst.append(conn)
    except BlockingIOError as e:
        for conn in conn_lst:  #[conn1,conn2,conn3]
            try:
                msg= conn.recv(1024)  # 非阻塞
                if not msg:  # msg = b''
                    conn.close()
                    del_lst.append(conn)
                    continue
                print(msg)
                msg = msg.decode('utf-8').upper()
                conn.send(msg.encode('utf-8'))
            except BlockingIOError:pass
        for conn in del_lst:
            conn_lst.remove(conn)
        del_lst.clear()

# conn1 conn2
# conn1 -->recv
# conn2 <--

# 非阻塞IO —— 占用CPU利用率

