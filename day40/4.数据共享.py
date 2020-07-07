from multiprocessing import Manager,Process,Lock
def func(dic,lock):
    # lock.acquire()
    # dic['count'] = dic['count']-1
    # lock.release()    with lock:    # 上下文管理 ：必须有一个开始动作 和 一个结束动作的时候
        dic['count'] = dic['count'] - 1

if __name__ == '__main__':
    m = Manager()
    lock = Lock()
    dic = m.dict({'count':100})
    p_lst = []
    for i in range(100):
        p = Process(target=func,args=[dic,lock])
        p_lst.append(p)
        p.start()
    for p in p_lst:p.join()
    print(dic)

# 同一台机器上 ： Queue
# 在不同台机器上 ：消息中间件











