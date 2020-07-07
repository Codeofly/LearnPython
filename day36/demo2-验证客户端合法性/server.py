# 秘钥
# hashlib
# md5
# hashlib.md5('秘钥')
import os
import socket
import hmac
secret_key = '老衲洗头用飘柔'.encode('utf-8')
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()
while True:
    try:
        conn,addr = sk.accept()
        random_bytes = os.urandom(32)
        conn.send(random_bytes)
        obj = hmac.new(key =secret_key,msg =random_bytes)
        ret = obj.hexdigest()
        msg = conn.recv(1024).decode('utf-8')
        if msg == ret:print('是合法的客户端')
        else:conn.close()
    finally:
        sk.close()
        break
# 秘钥
# 加密方法














