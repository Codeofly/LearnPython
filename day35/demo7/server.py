import os
import json
import struct
import socket

# D:\python11\day35\1.复习.py
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
print(addr)
dic = {'filename':'1.复习.py',
       'filesize':os.path.getsize(r'D:\python11\day35\1.复习.py')}
str_dic = json.dumps(dic).encode('utf-8')
dic_len = struct.pack('i',len(str_dic))
conn.send(dic_len)
conn.send(str_dic)
with open(r'D:\python11\day35\1.复习.py','rb') as f:
    content = f.read()
conn.send(content)
conn.close()
sk.close()

# 大文件的传输
    # 不能一次性读到内存里