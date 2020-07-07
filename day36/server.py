import os
import json
import socket
import struct
filepath = r'D:\python11期视频笔记\python11期day35\视频.zip'

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

conn,addr = sk.accept()
filename = os.path.basename(filepath)
filesize = os.path.getsize(filepath)
dic = {'filename':filename,'filesize':filesize}
str_dic = json.dumps(dic).encode('utf-8')
len_dic = len(str_dic)
length = struct.pack('i',len_dic)
conn.send(length)   # dic的长度
conn.send(str_dic)  # dic
with open(filepath,'rb') as f:  # 文件
    while filesize:
        content = f.read(4096)
        conn.send(content)
        filesize -= len(content)
conn.close()
sk.close()