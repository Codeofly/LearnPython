# python中启动子进程
# 并发编程
# 并发 ：多段程序看起来是同时运行的
# ftp 网盘
# 不支持并发
# socketserver 多进程 并发
# 异步
    # 两个进程 分别做不同的事情
# 复习：
# 创建新进程
# join ：阻塞 直到 子进程结束
# 守护进程 daemon ：子(守护)进程随着主进程代码的技术而结束
# 进程之间数据隔离
# 使用类来开启一个进程 ：自定义类 继承Process 重写run方法 传参数需要重写init
# 属性 pid name
# 方法 terminate is_alive