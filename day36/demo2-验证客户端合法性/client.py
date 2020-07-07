import socket
import hmac
secret_key = '老衲洗头用飘柔'.encode('utf-8')
sk = socket.socket()
sk.connect(('127.0.0.1',9000))

urandom = sk.recv(1024)
hmac_obj =  hmac.new(key = secret_key,msg =urandom)
sk.send(hmac_obj.hexdigest().encode('utf-8'))
sk.close()


