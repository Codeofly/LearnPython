import time
import random
from threading import Event,Thread

# wait()
# set clear isset

# 连接数据库
def connect_db(e):
    count = 1
    while count < 4:
        print('尝试第%s次检测连接'%count)
        e.wait(0.5)
        # 如果不传参数会一直等到事件为True为止
        # 如果传参数 传一个时间参数
        count += 1
        if e.is_set():
            print('连接成功')
            break
    else:
        print('连接失败')

def check_conn(e):
    '''检测数据库是否可以连接'''
    time.sleep(random.randint(1,2))
    e.set()

e = Event()
Thread(target=check_conn,args=(e,)).start()
Thread(target=connect_db,args=(e,)).start()

# 你要做一件事情 是有前提的
# 你就先去处理前提的问题 —— 前提处理好了 把状态设置成True
# 来控制即将要做的事情可以开始