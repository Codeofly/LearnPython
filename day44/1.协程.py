# 协程 实际上 是一个线程
# 执行了多个任务 遇到IO就切换

from gevent import monkey;monkey.patch_all()
# 切换   yield greenlet
# 遇到IO gevent ：检测到IO，能够使用greenlet实现自动切换
import time
import gevent

def func():
    print('eating')  # 执行
    time.sleep(0.1)   # 遇到IO
    print('eating2')
    time.sleep(0.1)
    print('eating3')
g = gevent.spawn(func)  # 协程任务开启
# time.sleep(0)           # 阻塞 遇到IO
g.join()                  # 阻塞 遇到IO
# 如果你开启一个协程，你的主线程中没有足够的时间让你执行协程的任务
# 内部执行switch的行文，能够保证你的协程不结束之前，主线程不结束