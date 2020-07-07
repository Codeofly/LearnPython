# 黏包现象
# 粘包现象的成因 ：
    # tcp协议的特点 面向流的 为了保证可靠传输 所以有很多优化的机制
    # 无边界 所有在连接建立的基础上传递的数据之间没有界限
    # 收发消息很有可能不完全相等
    # 缓存机制，导致没发过去的消息会在发送端缓存
                    #没接收完的消息会在接收端缓存
# 解决：
    # 给应用层定制协议
#　解决方案一：只发送一条信息
# 先发送一个定长表示待发送数据长度的bytes     先接收一个固定长度
# 再发送要发送的数据                          再按照长度接收数据

# 解决方案二 ：发送的多条信息
# 先发送一个定长表示待发送字典长度的bytes     先接收一个固定长度
# 再发送要发送字典（字典中存储的是文件信息）  再按照长度接收字典
# 再发送文件                                 再根据字典中的信息接收相应的内容
