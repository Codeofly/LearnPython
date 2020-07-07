import json
import struct
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',9000))

dic_len = sk.recv(4)
dic_len = struct.unpack('i',dic_len)[0]
dic = sk.recv(dic_len)
str_dic = dic.decode('utf-8')
dic = json.loads(str_dic)
with open(dic['filename'],'wb') as f:
    while dic['filesize']:
        content = sk.recv(4096)
        dic['filesize'] -= len(content)
        f.write(content)
sk.close()








