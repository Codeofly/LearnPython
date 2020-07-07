import time
import socketserver
# 并发编程
class MyServer(socketserver.BaseRequestHandler):
    clients = {}
    def handle(self):
        qq_id = self.request.recv(1024).decode('utf-8')
        MyServer.clients[qq_id] = self.request
        recv_msg = self.request.recv(1024).decode('utf-8')
        print(recv_msg)
        if recv_msg.startswith('say'):
            recv_msg = recv_msg.replace('say','')
            print(recv_msg)
            friend,msg = recv_msg.split('|')
            time.sleep(5)
            print(MyServer.clients)
            print(friend)
            print('---',MyServer.clients.get(friend))
            if MyServer.clients.get(friend):
                MyServer.clients[friend].send(('%s|%s'%(qq_id,msg)).encode('utf-8'))
        # while True:
        #     print(self.client_address)
        #     print(self.request)   # conn
        #     self.request.send(b'hello')
        #     print(self.request.recv(1024))

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()







