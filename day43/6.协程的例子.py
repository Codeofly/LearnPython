# 异步和同步的测试
from gevent import monkey;monkey.patch_all()
import gevent
import time
def task(i):
    time.sleep(0.5)
    print(i)

def sync():      # 同步
    for i in range(10):
        task(i)

def async():    # 异步
    #gevent.joinall([gevent.spawn(task, i) for i in range(10)])
    g_lst = []
    for i in range(10):
        g = gevent.spawn(task, i)
        g_lst.append(g)
    # for g in g_lst:g.join()
    gevent.joinall(g_lst)
async()
print('-'*20)
sync()
