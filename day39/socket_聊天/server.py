import socket
from multiprocessing import Process
def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        conn.send((msg + '_sb').encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1',9000))
    sk.listen()
    while True:
        conn,addr = sk.accept()
        Process(target=chat,args=[conn,]).start()   # 异步
    sk.close()
