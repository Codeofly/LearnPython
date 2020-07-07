# from threading import Lock
#
# lock= Lock()    # 在同一个线程中
#                 # 能够被一个锁的多个acquire阻塞住了
#                 # 这种锁就叫做互斥锁
# lock.acquire()
# lock.acquire()

# 科学家吃面问题
# 要完成一件事情 需要两个必要因素
# 要想吃到面 叉子 面
# 资源的互相抢占的问题  —— 死锁
# import time
# from threading import Thread,Lock
# def eat1(noodle_lock,fork_lock,name):
#     noodle_lock.acquire()
#     print('%s抢到了面'%name)
#     fork_lock.acquire()
#     print('%s抢到了叉子'%name)
#     print('%s正在吃面'%name)
#     fork_lock.release()
#     print('%s归还了叉子' % name)
#     noodle_lock.release()
#     print('%s归还了面' % name)
#
# def eat2(noodle_lock,fork_lock,name):
#     fork_lock.acquire()
#     print('%s抢到了叉子' % name)
#     time.sleep(0.5)
#     noodle_lock.acquire()
#     print('%s抢到了面'%name)
#     print('%s正在吃面'%name)
#     noodle_lock.release()
#     print('%s归还了面' % name)
#     fork_lock.release()
#     print('%s归还了叉子' % name)
#
# if __name__ == '__main__':
#     noodle_lock = Lock()
#     fork_lock = Lock()
#     Thread(target=eat1,args=(noodle_lock,fork_lock,'yuan')).start()
#     Thread(target=eat2,args=(noodle_lock,fork_lock,'egon')).start()
#     Thread(target=eat1,args=(noodle_lock,fork_lock,'nezha')).start()
#     Thread(target=eat2,args=(noodle_lock,fork_lock,'alex')).start()

# 递归锁
# from threading import Thread,RLock
# # 在同一个线程中对同一个锁多次acquire不会产生阻塞
# # 递归锁
# def func(rlock,flag):
#     rlock.acquire()
#     print(flag*10)
#     rlock.acquire()
#     print(flag * 10)
#     rlock.acquire()
#     print(flag * 10)
#     rlock.acquire()
#     print(flag * 10)
#     rlock.release()
#     rlock.release()
#     rlock.release()
#     rlock.release()
# rlock = RLock()
# Thread(target=func,args=(rlock,'*')).start()
# Thread(target=func,args=(rlock,'-')).start()



# import time
# from threading import Thread,RLock
# def eat1(noodle_lock,fork_lock,name):
#     noodle_lock.acquire()
#     print('%s抢到了面'%name)
#     fork_lock.acquire()
#     print('%s抢到了叉子'%name)
#     print('%s正在吃面'%name)
#     fork_lock.release()
#     print('%s归还了叉子' % name)
#     noodle_lock.release()
#     print('%s归还了面' % name)
#
# def eat2(noodle_lock,fork_lock,name):
#     fork_lock.acquire()
#     print('%s抢到了叉子' % name)
#     time.sleep(0.5)
#     noodle_lock.acquire()
#     print('%s抢到了面'%name)
#     print('%s正在吃面'%name)
#     noodle_lock.release()
#     print('%s归还了面' % name)
#     fork_lock.release()
#     print('%s归还了叉子' % name)
#
# if __name__ == '__main__':
#     fork_lock = noodle_lock = RLock()
#     Thread(target=eat1,args=(noodle_lock,fork_lock,'yuan')).start()
#     Thread(target=eat2,args=(noodle_lock,fork_lock,'egon')).start()
#     Thread(target=eat1,args=(noodle_lock,fork_lock,'nezha')).start()
#     Thread(target=eat2,args=(noodle_lock,fork_lock,'alex')).start()

# 有超过一个资源需要锁的时候 —— 递归锁
# 递归锁的应用场景
# 互斥锁和递归锁的区别


