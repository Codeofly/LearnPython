import socket
import subprocess

sk = socket.socket()
sk.connect(('127.0.0.1',9000))
while True:
    cmd = sk.recv(1024).decode('utf-8')
    print(cmd)
    if cmd == 'q':break
    ret = subprocess.Popen(cmd,shell=True,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)
    out = ret.stdout.read()
    err = ret.stderr.read()
    print(out,'*****\n',err)
    sk.send(b'out :'+out)
    sk.send(b'error :'+err)
sk.close()
# print('out :',ret.stdout.read().decode('gbk'))
# print('err :',ret.stderr.read().decode('gbk'))
