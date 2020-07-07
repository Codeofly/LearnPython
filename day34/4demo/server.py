# 时间同步服务
# udp协议完成的
# 4、5 台机器
# 00:00 从一个文件里 读一些数据 明天的搜索
# 在一个机房里 有一台标准时间的服务器
# 机房里所有的机器 都每隔一段时间 就去请求这台服务器 来获取一个标准时间

import time
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9090))
while True:
    msg,addr = sk.recvfrom(1024)
    sk.sendto(time.strftime(msg.decode('utf-8')).encode('utf-8'),addr)
sk.close()