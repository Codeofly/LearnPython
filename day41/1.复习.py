# 队列
    # 队列 ： 先进先出、数据进程安全
    # 管道 + 锁
    # 生产者消费者模型 ： 解决数据供需不平衡
# 管道
    # 双向通信 数据进程不安全
    # EOFError：
        # 管道是由操作系统进行引用计数的，
        # 必须在所有进程中关闭管道后才能生成EOFError异常
# 数据共享（不常用）
    # Manager
    # list dict 数据进程不安全的
# 进程池
    # 存放进程的容器
    # 在进程创建之初，创建固定个数的进程
    # 会被多个任务循环利用
    # 节省了进程创建和销毁的时间开销
    # 降低了操作系统调度进程的压力
# 信号量和进程池的区别
    # 信号量 n个任务开启n个进程，
          # 但同一时间只能有固定个数的进程在执行
          # 进程在等待被执行
    # 进程池 n个任务开启固定个数的进程
          # 因此同一时间只能有固定个数的进程在执行
          # 任务在等待被执行
import time
from multiprocessing import Pool
def wahaha(i):
    time.sleep(1)
    print('*'*i)
if  __name__ == "__main__":
    p  =  Pool(5)
    p.map(func=wahaha,iterable=range(10))
    # 自带close和join
    # 但是参数必须是一个iterable
    # 不能获取返回值

    # res_l = []
    # for i in range(10):
    #     res= p.apply_async(func = wahaha,args=[i,])
    #     res_l.append(res)
    # for i in res_l:print(i.get())
    # p.close() # 不能再提交新的任务
    # p.join()  # 等待池中的任务都执行完
# 主进程默认等待子进程结束 —— 守护进程
# 普通的进程 ： 根据你调用的函数执行结束它就结束了
# 进程池里的进程
    # 没有返回值
        # 在提交任务之后：
        # p.close() # 不能再提交新的任务
        # p.join()  # 等待池中的任务都执行完
    # 有返回值的时候：
        # 在提交任务之后：
        # for i in res_l:print(i.get())
# 回调函数
    # 回调函数在什么时候执行
        # 子进程的任务执行完毕之后立即触发
    # 回调函数的参数
        # 子进程的返回值
    # 回调函数是由谁执行的
        # 主进程执行的
    # 在哪儿用？
        # 爬虫 ：
            # 如果要爬取多个格式相同的网页
            # 真正影响程序效率的是网络的延迟
            # 计算 分析 处理网页的时间是很快的

# 500
    # 有回调函数
    # 没有回调函数快







