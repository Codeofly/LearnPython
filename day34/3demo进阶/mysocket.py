from socket import *
class Mysocket(socket):
    def __init__(self,coding='utf-8'):
        self.coding = coding
        super().__init__(type=SOCK_DGRAM)

    def my_recv(self,num):
        msg,addr = self.recvfrom(num)
        return msg.decode(self.coding),addr

    def my_send(self,msg,addr):
        return self.sendto(msg.encode(self.coding),addr)

