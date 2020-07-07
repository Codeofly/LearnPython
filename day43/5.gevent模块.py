from gevent import monkey;monkey.patch_all()
# 它会把下面导入的所有的模块中的IO操作都打成一个包，gevent就能够认识这些IO了
import time
import gevent
# 使用gevent模块来执行多个函数，表示在这些函数遇到IO操作的时候可以在同一个线程中进行切花
# 利用其他任务的IO阻塞时间来切换到其他的任务继续执行
# spawn来发布协程任务
# join负责开启并等待任务执行结束
# gevent本身不认识其他模块中的IO操作，但是如果我们在导入其他模块之前执行from gevent import monkey;monkey.patch_all()
# gevent就能够认识在这句话之后导入的模块中的所有IO操作了
from threading import currentThread
def eat():
    print('eating1',currentThread())
    time.sleep(1)
    print('eating2')

def play():
    print('playing1',currentThread())
    time.sleep(1)
    print('playing2')
g1 = gevent.spawn(eat)
g2 = gevent.spawn(play)
g1.join()   # start 且等待g执行完毕
g2.join()

# 休息一会儿
# 协程——tcp 协议的socket并发server

