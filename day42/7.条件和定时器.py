# from threading import Condition,Thread
# # acquire release
# # notify -- wait的行为
# # 10线程 wait
# # notify(1)
# def func(i,con):
#     con.acquire()
#     con.wait()
#     print(i*'*')
#     con.release()
#
# con = Condition()
# for i in range(10):
#     Thread(target=func,args=(i,con)).start()
# while True:
#     n = int(input('>>>'))
#     con.acquire()
#     con.notify(n)
#     con.release()
#
# con.acquire()
# con.notify_all()
# con.release()

# semaphore  允许统一是个n个线程执行这段代码
# event      有一个内部的事件来控制wait的行为
             #控制的是所有的线程
# condition  有一个内部的条件来控制wait的行为
            #可以逐个或者分批次的控制线程的走向

# from threading import Timer
# def func():
#     print('*'*20)
#
# t = Timer(5,func)   # 要开启一个线程，等到5秒钟之后才开启并且执行
# t.start()
# print('-'*10)
# print('^'*10)
