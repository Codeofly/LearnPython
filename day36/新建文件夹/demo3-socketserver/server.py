import socketserver
# 并发编程
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        self.request.send(b'hello')
        msg = self.recv(1024)
        print(msg)

if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9000),MyServer)
    server.serve_forever()







