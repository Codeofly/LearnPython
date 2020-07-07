from mysocket import Mysocket

sk = Mysocket()
while True:
    inp = input('>>>')
    sk.my_send(inp,('127.0.0.1',9090))
    msg,addr = sk.myrecv(1024)
    print(msg)

sk.close()

