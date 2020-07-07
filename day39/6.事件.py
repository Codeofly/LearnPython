# 状态
# 子进程 如何 受到状态的影响？
# wait() 的方法 等待 ---> 信号
# 发送信号：通过事件来发送信号
    # True   set 把信号设置为True
    # False  clear 把信号设置位False

# 红绿灯 ：
    # 车     进程   wait() 等红灯
                # 根据状态变化 wait遇到True信号，就非阻塞
                #                  遇到False信号，就阻塞
    # 交通灯 进程   红灯 --> False
                #   绿灯 --> True


# 事件
# wait的方法 根据一个状态来决定自己是否要阻塞
# 状态相关的方法
    # set 将状态改为T
    # clear 将状态改为F
    # is_set 判断当前的状态是否为T

# from multiprocessing import Event

# # 创建一个事件的对象
# e = Event()
# print(e.is_set())  # 在事件的创世之初，状态为False
# e.set()
# e.wait()
# print(e.is_set())
# e.clear()
# print(e.is_set())
# e.wait()

import time
import random
from multiprocessing import Process,Event

def car(i,e):  # 感知状态的变化
    if not e.is_set():    # 当前这个事件的状态如果是False
        print('car%s正在等待'%i)  # 这辆车正在等待通过路口
    e.wait()    # 阻塞 直到有一个e.set行为  # 等红灯
    print('car%s通过路口'%i)

def traffic_light(e):  # 修改事件的状态
    print('\033[1;31m红灯亮\033[0m')
    # 事件在创立之初的状态是False，相当于我程序中的红灯
    time.sleep(2)  # 红灯亮2s
    while True:
        if not e.is_set():  # False
            print('\033[1;32m绿灯亮\033[0m')
            e.set()
        elif e.is_set():
            print('\033[1;31m红灯亮\033[0m')
            e.clear()
        time.sleep(5)

if __name__ == '__main__':
    e = Event()
    Process(target=traffic_light,args=[e,]).start()
    for i in range(50):
        time.sleep(random.randrange(0,5,2))
        Process(target=car,args=[i,e]).start()


















