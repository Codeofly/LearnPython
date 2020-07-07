# 进程
# multiprocess
# Process —— 进程 在python中创建一个进程的模块
    # start
    # daemon 守护进程
    # join 等待子进程执行结束

# 锁 Lock
# acquire release
# 锁是一个同步控制的工具
# 如果同一时刻有多个进程同时执行一段代码，
# 那么在内存中的数据是不会发生冲突的
# 但是，如果涉及到文件，数据库就会发生资源冲突的问题
# 我们就需要用锁来把这段代码锁起来
# 任意一个进程执行了acquire之后，
# 其他所有的进程都会在这里阻塞，等待一个release

# 信号量 semaphore
# 锁 + 计数器
# 同一时间只能有指定个数的进程执行同一段代码

# 事件 Event
# set clear is_set   控制对象的状态
# wait  根据状态不同执行效果也不同
    # 状态是True ---> pass
    # 状态是False --> 阻塞
# 一般wait是和set clear放在不同的进程中
# set/clear负责控制状态
# wait负责感知状态
# 我可以在一个进程中控制另外一个或多个进程的运行情况

# IPC通信
# 队列 Queue
# 管道 PIPE



