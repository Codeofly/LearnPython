# KTV 4个房子
import time
import random
from multiprocessing import Process,Semaphore
# def ktv(i,sem):
#     sem.acquire()
#     print('person %s 进来唱歌了'%i)
#     time.sleep(random.randint(1,5))
#     print('person %s 从ktv出去了'%i)
#     sem.release()
#
# if __name__ == '__main__':
#     sem = Semaphore(4)
#     for i in range(10):
#         Process(target=ktv,args=(i,sem)).start()

# 锁+计数器
# .acquire() 计数器-1
# 计数器减为0 = 阻塞
# .release() 计数器+1