# C/S和B/S架构
# osi五层模型
    # 应用层
        # 自定义协议(struct) _ 解决黏包
        # 验证客户端合法性 _ hmac os.urandom
        # 解决TCP协议的server端并发问题 _socketserver
    #######socket#########
    # 传输层
        # 端口 在一台机器上唯一标识一个运行中的网络程序
        # tcp  三次握手 四次挥手 黏包问题
        # udp
        # 四层交换机 四层路由器
    # 网络层
        # ip协议
            # ip 网关ip 子网掩码
        # 路由器 三层交换机
    # 数据链路层
        # arp协议 ip-->mac  广播单播
        # 网卡
        # 交换机 广播 组播 单播
    # 物理层